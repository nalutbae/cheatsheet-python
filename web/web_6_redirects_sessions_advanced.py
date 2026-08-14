# requests: redirects, rate limiting, session management, and PreparedRequest

import requests
import os
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

BASE = "https://httpbin.org"

print("=" * 5, "Redirect handling", "=" * 5)

# Follow redirects (default behavior)
resp = requests.get(f"{BASE}/redirect/2")
print(f"Follow redirects: status={resp.status_code}, url={resp.url}")
print(f"Redirect history: {[r.status_code for r in resp.history]}")
print(f"History URLs: {[r.url for r in resp.history]}")

# Disable redirect following
resp = requests.get(f"{BASE}/redirect/2", allow_redirects=False)
print(f"\nNo follow: status={resp.status_code}")  # 302
print(f"Location header: {resp.headers.get('location')}")

# Limit number of redirects (session-level setting)
session_limited = requests.Session()
session_limited.max_redirects = 2
try:
    resp = session_limited.get(f"{BASE}/redirect/5", timeout=5)
except requests.TooManyRedirects as e:
    print(f"\nTooManyRedirects caught (max_redirects=2)")
finally:
    session_limited.close()

# Relative redirect
resp = requests.get(f"{BASE}/relative-redirect/1")
print(f"\nRelative redirect: status={resp.status_code}, url={resp.url}")

# Absolute redirect
resp = requests.get(f"{BASE}/absolute-redirect/1")
print(f"Absolute redirect: status={resp.status_code}, url={resp.url}")

# Inspect redirect chain
resp = requests.get(f"{BASE}/redirect/3")
print(f"\nFull redirect chain:")
for i, r in enumerate(resp.history):
    print(f"  Hop {i+1}: {r.status_code} -> {r.headers.get('location', 'N/A')[:60]}")
print(f"  Final: {resp.status_code} {resp.url}")

print("=" * 5, "Rate limiting and throttling", "=" * 5)

# Simple rate limiter class
class RateLimiter:
    """Limit requests to max_calls per period_seconds."""
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []

    def wait(self):
        now = time.time()
        self.calls = [c for c in self.calls if now - c < self.period]
        if len(self.calls) >= self.max_calls:
            sleep_time = self.period - (now - self.calls[0])
            print(f"  Rate limited — sleeping {sleep_time:.1f}s")
            time.sleep(sleep_time)
        self.calls.append(time.time())

limiter = RateLimiter(max_calls=3, period=1)  # 3 requests per second

for i in range(5):
    limiter.wait()
    resp = requests.get(f"{BASE}/get", timeout=5)
    print(f"  Request {i+1}: {resp.status_code}")

print("=" * 5, "Exponential backoff", "=" * 5)

# Custom backoff function
def request_with_backoff(url, max_retries=3, base_delay=1):
    """Make a request with exponential backoff on failure."""
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            return resp
        except requests.exceptions.RequestException as e:
            delay = base_delay * (2 ** attempt)  # 1, 2, 4 seconds
            print(f"  Attempt {attempt+1} failed: {type(e).__name__}")
            if attempt < max_retries - 1:
                print(f"  Retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"  All {max_retries} attempts failed")
                raise

# Successful request
resp = request_with_backoff(f"{BASE}/get")
print(f"  Success: {resp.status_code}")

# Failed request with backoff (demonstrates retry logic)
try:
    resp = request_with_backoff(f"{BASE}/status/500", max_retries=2, base_delay=0.1)
except requests.exceptions.HTTPError as e:
    print(f"  Final error: {e.response.status_code}")

print("=" * 5, "Session context manager", "=" * 5)

# Session as context manager (auto-closes connections)
with requests.Session() as session:
    session.headers.update({"X-App": "Demo"})
    resp = session.get(f"{BASE}/get")
    print(f"Session in context manager: {resp.status_code}")
    echoed = resp.json()["headers"]
    print(f"X-App: {echoed.get('X-App')}")
# Session is automatically closed here

print("=" * 5, "PreparedRequest (low-level control)", "=" * 5)

# Build a PreparedRequest manually for fine-grained control
req = requests.Request(
    "POST",
    f"{BASE}/post",
    data={"key": "value"},
    headers={"X-Custom": "prepared"},
)
prepared = session.prepare_request(req)
print(f"Prepared method: {prepared.method}")  # POST
print(f"Prepared URL: {prepared.url}")
print(f"Prepared body: {prepared.body}")
print(f"Prepared headers: {dict(list(prepared.headers.items())[:3])}")

# Send with a session
with requests.Session() as s:
    resp = s.send(prepared, timeout=5)
    print(f"Sent prepared request: {resp.status_code}")
    print(f"Response data: {resp.json()['form']}")

print("=" * 5, "Session configuration and defaults", "=" * 5)

# Global defaults via Session
session = requests.Session()

# Set default headers for all requests
session.headers.update({
    "Authorization": "Bearer global-token",
    "X-App-Version": "2.0",
})

# SSL verification (default: True)
session.verify = True
# session.verify = "/path/to/ca-bundle.crt"  # Custom CA

# Client certificate
# session.cert = ("/path/client.cert", "/path/client.key")

# Maximum redirects
session.max_redirects = 30  # default

# Connection pool settings
adapter = HTTPAdapter(
    pool_connections=10,  # number of connection pools
    pool_maxsize=10,       # max connections per pool
    max_retries=3,         # retry on connection errors
)
session.mount("https://", adapter)
session.mount("http://", adapter)

resp = session.get(f"{BASE}/get")
print(f"Session with defaults: {resp.status_code}")
echoed = resp.json()["headers"]
print(f"Authorization: {echoed.get('Authorization', 'none')[:20]}...")
print(f"X-App-Version: {echoed.get('X-App-Version')}")

session.close()

print("=" * 5, "Environment variables", "=" * 5)

# requests automatically uses these environment variables:
# HTTP_PROXY / HTTPS_PROXY — proxy configuration
# REQUESTS_CA_BUNDLE — custom CA certificate bundle
# CURL_CA_BUNDLE — alternative CA bundle path
# NO_PROXY — comma-separated list of hosts to bypass proxy

print("Environment variable proxy settings:")
print(f"  HTTP_PROXY: {os.environ.get('HTTP_PROXY', 'not set')}")
print(f"  HTTPS_PROXY: {os.environ.get('HTTPS_PROXY', 'not set')}")
print(f"  NO_PROXY: {os.environ.get('NO_PROXY', 'not set')}")

# Use .netrc for authentication (automatic)
# Create ~/.netrc with:
#   machine httpbin.org login alice password secret
# requests will automatically use these credentials

# Trust environment for proxy settings
session = requests.Session()
session.trust_env = True  # default: True — uses env vars for proxy/SSL
print(f"\ntrust_env: {session.trust_env}")

# Disable environment settings
session.trust_env = False  # Ignore HTTP_PROXY, .netrc, etc.
print(f"trust_env disabled: {session.trust_env}")
session.close()