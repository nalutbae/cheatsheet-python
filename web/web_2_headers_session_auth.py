# requests: headers, sessions, authentication, and cookies

import requests
import json
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

BASE = "https://httpbin.org"

print("=" * 5, "Custom headers", "=" * 5)

# Common headers
headers = {
    "User-Agent": "MyApp/2.0 (compatible; Python/3.11)",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "no-cache",
    "X-Custom-Header": "custom-value",
}
resp = requests.get(f"{BASE}/get", headers=headers)
echoed = resp.json()["headers"]
print(f"User-Agent: {echoed.get('User-Agent')}")
print(f"Accept: {echoed.get('Accept')}")
print(f"X-Custom-Header: {echoed.get('X-Custom-Header')}")

# Important: requests default User-Agent
resp = requests.get(f"{BASE}/get")
default_ua = resp.json()["headers"].get("User-Agent")
print(f"\nDefault User-Agent: {default_ua}")

print("=" * 5, "Basic authentication", "=" * 5)

# Basic auth — username:password in Authorization header
resp = requests.get(
    f"{BASE}/basic-auth/alice/secret",
    auth=HTTPBasicAuth("alice", "secret"),
)
print(f"Basic auth status: {resp.status_code}")  # 200
print(f"Authenticated: {resp.json()['authenticated']}")  # True
print(f"User: {resp.json()['user']}")  # alice

# Shorthand for basic auth
resp = requests.get(
    f"{BASE}/basic-auth/bob/password123",
    auth=("bob", "password123"),
)
print(f"Auth shorthand: {resp.json()['authenticated']}")  # True

# Failed auth
resp = requests.get(f"{BASE}/basic-auth/alice/secret", auth=("alice", "wrong"))
print(f"Failed auth status: {resp.status_code}")  # 401

print("=" * 5, "Digest authentication", "=" * 5)

# Digest auth — more secure than basic auth
resp = requests.get(
    f"{BASE}/digest-auth/auth/alice/secret",
    auth=HTTPDigestAuth("alice", "secret"),
)
print(f"Digest auth status: {resp.status_code}")  # 200

print("=" * 5, "Bearer token authentication", "=" * 5)

# Bearer token — commonly used with APIs
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example-token"
headers_bearer = {"Authorization": f"Bearer {token}"}
resp = requests.get(f"{BASE}/get", headers=headers_bearer)
echoed_auth = resp.json()["headers"].get("Authorization", "")
print(f"Bearer header sent: {echoed_auth[:30]}...")

print("=" * 5, "Cookies", "=" * 5)

# Send cookies with request
cookies = {"session_id": "abc123", "user_pref": "dark_mode"}
resp = requests.get(f"{BASE}/cookies", cookies=cookies)
print(f"Cookies echoed: {resp.json()['cookies']}")

# Set cookies via response
resp = requests.get(f"{BASE}/cookies/set?theme=light&lang=en")
print(f"Cookies after set: {resp.json()['cookies']}")

# Delete a cookie
resp = requests.get(f"{BASE}/cookies/delete?theme")
print(f"Cookies after delete: {resp.json()['cookies']}")

print("=" * 5, "Session with persistent cookies", "=" * 5)

# Session maintains cookies across requests
session = requests.Session()

# Set cookies via session
session.cookies.set("session_id", "xyz789", domain="httpbin.org")
session.cookies.set("user_pref", "dark_mode", domain="httpbin.org")

resp = session.get(f"{BASE}/cookies")
print(f"Session cookies: {resp.json()['cookies']}")

# Set more cookies through the server
resp = session.get(f"{BASE}/cookies/set?counter=1")
print(f"After server-set: {session.cookies.get_dict()}")

print("=" * 5, "Session object", "=" * 5)

# Session persists headers, cookies, auth, and config across requests
session = requests.Session()

# Set default headers and auth for all requests in this session
session.headers.update({"X-App-Version": "2.0", "X-Request-Source": "python-cli"})
session.auth = ("alice", "secret")

# First request — headers and auth are sent automatically
resp = session.get(f"{BASE}/basic-auth/alice/secret")
print(f"Session auth: {resp.json()['authenticated']}")  # True
echoed = resp.json()["user"]  # alice
print(f"Session user: {echoed}")

# Second request — same headers and auth applied
resp = session.get(f"{BASE}/get")
echoed_headers = resp.json()["headers"]
print(f"X-App-Version: {echoed_headers.get('X-App-Version')}")
print(f"X-Request-Source: {echoed_headers.get('X-Request-Source')}")

# Override session headers for a single request
resp = session.get(f"{BASE}/get", headers={"X-Override": "yes", "X-App-Version": "3.0"})
echoed = resp.json()["headers"]
print(f"Overridden X-App-Version: {echoed.get('X-App-Version')}")  # 3.0
print(f"Extra X-Override: {echoed.get('X-Override')}")  # yes

# Clean up
session.close()

print("=" * 5, "Session with retry configuration", "=" * 5)

# Mount custom adapter with retry logic on a session
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

session = requests.Session()

# Configure retry: total=3, backoff_factor=0.5, retry on 500/502/503/504
retry_strategy = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET", "POST"],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

resp = session.get(f"{BASE}/get")
print(f"Session with retry: {resp.status_code}")  # 200

session.close()

print("=" * 5, "HTTPS and SSL verification", "=" * 5)

# By default, requests verifies SSL certificates
resp = requests.get("https://httpbin.org/get")
print(f"HTTPS (verify=True): {resp.status_code}")  # 200

# Disable verification (not recommended for production)
# resp = requests.get("https://httpbin.org/get", verify=False)
# print(f"HTTPS (verify=False): {resp.status_code}")

# Use custom CA bundle
# resp = requests.get("https://example.com", verify="/path/to/ca-bundle.crt")

# Use client certificate
# resp = requests.get("https://example.com", cert=("/path/client.cert", "/path/client.key"))

print("=" * 5, "Proxy configuration", "=" * 5)

# Single proxy
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
# resp = requests.get("https://httpbin.org/ip", proxies=proxies)
# print(f"IP via proxy: {resp.json()['origin']}")

# Proxy with authentication
# proxies = {
#     "http": "http://user:pass@10.10.1.10:3128",
#     "https": "http://user:pass@10.10.1.10:1080",
# }
# resp = requests.get("https://httpbin.org/ip", proxies=proxies)

# Session-level proxy
# session = requests.Session()
# session.proxies.update(proxies)
# resp = session.get("https://httpbin.org/ip")
# session.close()

# Use environment variables (HTTP_PROXY, HTTPS_PROXY)
# resp = requests.get("https://httpbin.org/ip")  # auto-detects env vars

print("Proxy examples shown as comments (require actual proxy server)")