# urllib: URL handling, requests, and parsing

from urllib.parse import urlparse, urlunparse, parse_qs, urlencode, quote, unquote
from urllib.parse import urljoin, urlsplit, urldefrag
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import json

print("=" * 5, "URL parsing with urlparse", "=" * 5)

# Parse a complete URL
url = "https://www.example.com:8080/path/to/page?name=Alice&age=30&tags=python&tags=web#section1"
parsed = urlparse(url)

print(f"Full URL: {url}")
print(f"Scheme: {parsed.scheme}")    # https
print(f"Netloc: {parsed.netloc}")    # www.example.com:8080
print(f"Hostname: {parsed.hostname}")  # www.example.com
print(f"Port: {parsed.port}")        # 8080
print(f"Path: {parsed.path}")        # /path/to/page
print(f"Params: {parsed.params}")    # (empty)
print(f"Query: {parsed.query}")      # name=Alice&age=30&tags=python&tags=web
print(f"Fragment: {parsed.fragment}")  # section1
print(f"Username: {parsed.username}")  # None
print(f"Password: {parsed.password}")  # None

# URL with authentication
auth_url = "https://user:pass@api.example.com/v1/data?key=val"
auth_parsed = urlparse(auth_url)
print(f"Username: {auth_parsed.username}")  # user
print(f"Password: {auth_parsed.password}")  # pass
print(f"Hostname: {auth_parsed.hostname}")  # api.example.com

# Parse query string
query_string = "name=Alice&age=30&hobby=reading&hobby=coding"
params = parse_qs(query_string)
print(f"Parsed query: {params}")  # {'name': ['Alice'], 'age': ['30'], 'hobby': ['reading', 'coding']}

# Get single value from parsed query
single_vals = {k: v[0] for k, v in params.items()}
print(f"Single values: {single_vals}")  # {'name': 'Alice', 'age': '30', 'hobby': 'reading'}

# Parse query with keep_blank_values
blank_query = "key1=val&key2=&key3"
print(f"With blanks: {parse_qs(blank_query, keep_blank_values=True)}")
print(f"Without blanks: {parse_qs(blank_query)}")

print("=" * 5, "URL construction with urlencode", "=" * 5)

# Build query string from dictionary
params_dict = {"name": "Alice", "age": "30", "city": "Seoul"}
query = urlencode(params_dict)
print(f"Query string: {query}")  # name=Alice&age=30&city=Seoul

# Build query string with multiple values
multi_params = {"q": "python tutorial", "lang": ["en", "ko"], "page": "1"}
query = urlencode(multi_params, doseq=True)
print(f"Multi-value query: {query}")  # q=python+tutorial&lang=en&lang=ko&page=1

# Construct a full URL
base_url = "https://api.example.com/search"
full_url = f"{base_url}?{query}"
print(f"Full URL: {full_url}")

# Reconstruct URL from parts
parts = ("https", "www.example.com", "/path/to/page", "", "key=value", "section")
reconstructed = urlunparse(parts)
print(f"Reconstructed: {reconstructed}")

print("=" * 5, "URL encoding and decoding", "=" * 5)

# quote: encode special characters for URL
original = "Hello World! 파이썬 path/to/file"
encoded = quote(original)
print(f"Original: {original}")
print(f"Encoded: {encoded}")  # Hello%20World%21%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20path/to/file

# quote with safe characters
encoded_safe = quote(original, safe="/! ")
print(f"With safe chars: {encoded_safe}")  # Hello World! 파이썬 path/to/file

# unquote: decode URL-encoded string
encoded_url = "Hello%20World%21%20%ED%8C%8C%EC%9D%B4%EC%8D%AC"
decoded = unquote(encoded_url)
print(f"Decoded: {decoded}")  # Hello World! 파이썬

# Encoding query parameters
search_query = "Python 튜토리얼"
encoded_query = quote(search_query)
search_url = f"https://example.com/search?q={encoded_query}"
print(f"Search URL: {search_url}")

# Decoding percent-encoded URLs
complex_url = "https://example.com/path/%EC%8B%9C%EC%9E%91"
decoded_path = unquote(complex_url)
print(f"Decoded URL: {decoded_path}")

print("=" * 5, "URL joining and manipulation", "=" * 5)

# urljoin: join base URL and relative URL
base = "https://www.example.com/docs/"
print(f"Absolute: {urljoin(base, '/api/v1/data')}")  # https://www.example.com/api/v1/data
print(f"Relative: {urljoin(base, 'page2.html')}")  # https://www.example.com/docs/page2.html
print(f"Parent: {urljoin(base, '../index.html')}")  # https://www.example.com/index.html
print(f"Full URL: {urljoin(base, 'https://other.com/page')}")  # https://other.com/page

# urljoin with different base paths
base2 = "https://www.example.com/docs/tutorial/index.html"
print(f"Same dir: {urljoin(base2, 'page2.html')}")  # .../docs/tutorial/page2.html
print(f"Parent dir: {urljoin(base2, '../advanced/')}")  # .../docs/advanced/
print(f"Root path: {urljoin(base2, '/')}")  # https://www.example.com/

# urlsplit: like urlparse but doesn't split params from path
url_complex = "https://example.com/path;param?query=val"
split_result = urlsplit(url_complex)
print(f"Split path: {split_result.path}")  # /path;param
print(f"Split query: {split_result.query}")  # query=val

# urldefrag: remove fragment from URL
url_with_frag = "https://example.com/page#section1"
defragged, fragment = urldefrag(url_with_frag)
print(f"URL without fragment: {defragged}")  # https://example.com/page
print(f"Fragment: {fragment}")  # section1

print("=" * 5, "Making HTTP requests", "=" * 5)

# Simple GET request (using a reliable public API)
try:
    response = urlopen("https://httpbin.org/get", timeout=10)
    print(f"Status: {response.status}")  # 200
    print(f"Reason: {response.reason}")  # OK
    print(f"Headers: {dict(list(response.headers.items())[:5])}")
    content = response.read().decode("utf-8")
    data = json.loads(content)
    print(f"Origin: {data.get('origin', 'N/A')}")
    print(f"URL: {data.get('url', 'N/A')}")
except (URLError, HTTPError) as e:
    print(f"Request error: {e}")

# GET request with custom headers
try:
    req = Request(
        "https://httpbin.org/headers",
        headers={
            "User-Agent": "PythonCheatSheet/1.0",
            "Accept": "application/json",
        }
    )
    response = urlopen(req, timeout=10)
    data = json.loads(response.read().decode("utf-8"))
    sent_headers = data.get("headers", {})
    print(f"User-Agent sent: {sent_headers.get('User-Agent', 'N/A')}")
except (URLError, HTTPError) as e:
    print(f"Request error: {e}")

# POST request with data
try:
    import urllib.parse as up
    post_data = up.urlencode({"name": "Alice", "age": "30"}).encode("utf-8")
    req = Request("https://httpbin.org/post", data=post_data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    response = urlopen(req, timeout=10)
    result = json.loads(response.read().decode("utf-8"))
    print(f"POST form data: {result.get('form', {})}")
except (URLError, HTTPError) as e:
    print(f"POST error: {e}")

print("=" * 5, "Error handling", "=" * 5)

# HTTP errors
try:
    urlopen("https://httpbin.org/status/404", timeout=10)
except HTTPError as e:
    print(f"HTTP Error: {e.code} {e.reason}")  # 404 Not Found
except URLError as e:
    print(f"URL Error: {e.reason}")

# Connection errors
try:
    urlopen("https://nonexistent.domain.example", timeout=5)
except URLError as e:
    print(f"Connection error: {type(e.reason).__name__}")

# Timeout errors
try:
    urlopen("https://httpbin.org/delay/10", timeout=2)
except URLError as e:
    print(f"Timeout error: {e}")

# Handling both HTTP and URL errors
def safe_request(url, timeout=10):
    """Make a request with comprehensive error handling."""
    try:
        response = urlopen(url, timeout=timeout)
        return response.read().decode("utf-8")
    except HTTPError as e:
        return f"HTTP Error {e.code}: {e.reason}"
    except URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"Error: {e}"

result = safe_request("https://httpbin.org/get")
print(f"Safe request result: {result[:80]}..." if len(result) > 80 else f"Safe request result: {result}")

print("=" * 5, "Practical: URL builder class", "=" * 5)

class URLBuilder:
    """Fluent URL builder using urllib.parse."""

    def __init__(self, base_url):
        self._scheme = "https"
        self._netloc = base_url
        self._path = ""
        self._params = {}
        self._fragment = ""

    def path(self, *parts):
        self._path = "/" + "/".join(str(p) for p in parts)
        return self

    def query(self, **kwargs):
        self._params.update(kwargs)
        return self

    def fragment(self, frag):
        self._fragment = frag
        return self

    def build(self):
        query = urlencode(self._params) if self._params else ""
        return urlunparse((self._scheme, self._netloc, self._path, "", query, self._fragment))

# Usage
builder = URLBuilder("api.example.com")
url = builder.path("v2", "users").query(name="Alice", page=1, limit=10).fragment("results")
print(f"Built URL: {url}")

builder2 = URLBuilder("search.example.com")
url2 = builder2.path("search").query(q="python tutorial", lang="en")
print(f"Built URL 2: {url2}")