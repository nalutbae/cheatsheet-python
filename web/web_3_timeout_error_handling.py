# requests: timeout, error handling, and robust patterns

import requests
from requests.exceptions import (
    Timeout, ConnectionError, HTTPError, RequestException, URLRequired,
)
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

BASE = "https://httpbin.org"

print("=" * 5, "Timeout configuration", "=" * 5)

# Single timeout value — applies to both connect and read
try:
    resp = requests.get(f"{BASE}/get", timeout=5)
    print(f"Request succeeded: {resp.status_code}")  # 200
except Timeout:
    print("Request timed out (5s)")

# Separate connect and read timeouts
try:
    # connect_timeout=3, read_timeout=10
    resp = requests.get(f"{BASE}/get", timeout=(3, 10))
    print(f"Separate timeouts: {resp.status_code}")  # 200
except Timeout:
    print("Request timed out")

# Timeout on POST
try:
    resp = requests.post(f"{BASE}/post", json={"key": "value"}, timeout=5)
    print(f"POST with timeout: {resp.status_code}")  # 200
except Timeout:
    print("POST timed out")

# No timeout — dangerous (blocks indefinitely)
# resp = requests.get(f"{BASE}/get")  # No timeout set!
# Always set a timeout in production code

print("=" * 5, "Exception hierarchy", "=" * 5)

# requests.exceptions hierarchy:
#   RequestException
#     ├── ConnectionError
#     │     ├── ConnectTimeout
#     │     └── MaxRetryError
#     ├── Timeout
#     │     ├── ConnectTimeout
#     │     └── ReadTimeout
#     ├── URLRequired
#     ├── TooManyRedirects
#     ├── HTTPError
#     │     └── raises from raise_for_status()
#     └── JSONDecodeError

print("=" * 5, "ConnectionError", "=" * 5)

# ConnectionError — DNS failure, refused connection, etc.
try:
    resp = requests.get("https://this-domain-does-not-exist-12345.com", timeout=5)
except ConnectionError as e:
    print(f"ConnectionError caught: {type(e).__name__}")
    print(f"  Message: {str(e)[:80]}...")

# Connection refused (no server on that port)
try:
    resp = requests.get("http://localhost:59999", timeout=2)
except (ConnectionError, requests.exceptions.InvalidURL) as e:
    print(f"Connection error: {type(e).__name__}")

print("=" * 5, "Timeout exceptions", "=" * 5)

# ReadTimeout — server too slow to respond
try:
    # httpbin /delay/10 responds after 10 seconds
    resp = requests.get(f"{BASE}/delay/10", timeout=3)
except Timeout as e:
    print(f"Timeout caught: {type(e).__name__}")
    print(f"  Read timeout after 3s waiting for 10s delay")

# ConnectTimeout — server not accepting connections in time
try:
    resp = requests.get("https://10.255.255.1", timeout=1)
except Timeout as e:
    print(f"ConnectTimeout caught: {type(e).__name__}")

print("=" * 5, "HTTPError with raise_for_status", "=" * 5)

# raise_for_status raises HTTPError for 4xx/5xx
for status_code in [200, 404, 500]:
    try:
        resp = requests.get(f"{BASE}/status/{status_code}", timeout=5)
        resp.raise_for_status()
        print(f"Status {status_code}: OK (no exception)")
    except HTTPError as e:
        print(f"Status {status_code}: HTTPError — {e}")

# Detailed error information
try:
    resp = requests.get(f"{BASE}/status/403", timeout=5)
    resp.raise_for_status()
except HTTPError as e:
    print(f"\nDetailed HTTPError info:")
    print(f"  URL: {e.response.url}")
    print(f"  Status code: {e.response.status_code}")
    print(f"  Reason: {e.response.reason}")
    print(f"  Headers: {dict(list(e.response.headers.items())[:3])}")

print("=" * 5, "Catching all request exceptions", "=" * 5)

# RequestException catches everything
url = f"{BASE}/status/404"
try:
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
except ConnectionError:
    print("Network problem (DNS, refused connection, etc.)")
except Timeout:
    print("Request timed out")
except HTTPError as e:
    print(f"HTTP error: {e.response.status_code} — {e.response.reason}")
except RequestException as e:
    print(f"Other request error: {e}")

print("=" * 5, "Robust request helper function", "=" * 5)

def safe_request(method, url, max_retries=3, timeout=10, **kwargs):
    """Make an HTTP request with retry, timeout, and error handling."""
    session = requests.Session()

    # Configure retry strategy
    retry = Retry(
        total=max_retries,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        resp = session.request(method, url, timeout=timeout, **kwargs)
        resp.raise_for_status()
        return {"success": True, "status": resp.status_code, "data": resp}
    except ConnectionError as e:
        return {"success": False, "error": "connection_error", "message": str(e)[:100]}
    except Timeout as e:
        return {"success": False, "error": "timeout", "message": str(e)[:100]}
    except HTTPError as e:
        return {"success": False, "error": "http_error", "status": e.response.status_code, "message": str(e)[:100]}
    except RequestException as e:
        return {"success": False, "error": "request_error", "message": str(e)[:100]}
    finally:
        session.close()

# Test with various URLs
result = safe_request("GET", f"{BASE}/get")
print(f"GET /get: success={result['success']}, status={result['status']}")

result = safe_request("GET", f"{BASE}/status/404")
print(f"GET /status/404: success={result['success']}, error={result['error']}")

result = safe_request("POST", f"{BASE}/post", json={"test": "data"})
print(f"POST /post: success={result['success']}, status={result['status']}")

result = safe_request("GET", "https://this-domain-does-not-exist-12345.com", max_retries=1, timeout=3)
print(f"GET bad domain: success={result['success']}, error={result['error']}")

print("=" * 5, "Working with response content", "=" * 5)

resp = requests.get(f"{BASE}/get", timeout=10)

# .text — decoded string
print(f"Type of .text: {type(resp.text)}")
print(f"Text preview: {resp.text[:80]}...")

# .content — raw bytes
print(f"Type of .content: {type(resp.content)}")
print(f"Content length: {len(resp.content)} bytes")

# .json() — parsed JSON
data = resp.json()
print(f"JSON keys: {list(data.keys())}")

# .encoding — detected or explicit encoding
print(f"Encoding: {resp.encoding}")

# .raw — raw socket response (requires stream=True)
resp_raw = requests.get(f"{BASE}/get", stream=True)
raw_data = resp_raw.raw.read(100)
print(f"Raw bytes (first 100): {len(raw_data)} bytes")
resp_raw.close()

# .iter_content — chunked reading
resp_chunked = requests.get(f"{BASE}/stream/3", stream=True)
chunks = []
for chunk in resp_chunked.iter_content(chunk_size=8192):
    chunks.append(chunk)
print(f"Chunks received: {len(chunks)}")
resp_chunked.close()

# .iter_lines — line-by-line reading (useful for streaming APIs)
resp_lines = requests.get(f"{BASE}/stream/3", stream=True)
line_count = 0
for line in resp_lines.iter_lines(decode_unicode=True):
    if line:
        line_count += 1
print(f"Non-empty lines: {line_count}")
resp_lines.close()

print("=" * 5, "URL manipulation", "=" * 5)

from urllib.parse import urlencode, urlparse, parse_qs

# Build URL with query parameters
base_url = "https://httpbin.org/get"
params = {"q": "python requests", "page": 2, "sort": "date"}
full_url = f"{base_url}?{urlencode(params)}"
print(f"Built URL: {full_url}")

# Parse URL
parsed = urlparse(full_url)
print(f"Scheme: {parsed.scheme}")  # https
print(f"Netloc: {parsed.netloc}")  # httpbin.org
print(f"Path: {parsed.path}")  # /get
print(f"Query: {parsed.query}")  # q=python+requests&page=2&sort=date
print(f"Query dict: {parse_qs(parsed.query)}")