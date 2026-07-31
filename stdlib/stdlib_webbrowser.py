# webbrowser: open URLs in web browsers

import webbrowser
import os

print("=" * 5, "Browser detection and info", "=" * 5)

# Try to detect available browsers
browsers = {
    "Chrome": "chrome",
    "Firefox": "firefox",
    "Edge": "edge",
    "Safari": "safari",
    "Opera": "opera",
    "Default": None,
}

for name, browser_name in browsers.items():
    try:
        if browser_name:
            controller = webbrowser.get(browser_name)
        else:
            controller = webbrowser.get()
        print(f"  {name}: Available")
    except webbrowser.Error:
        print(f"  {name}: Not available")

# Get default browser name
default = webbrowser.get()
print(f"\nDefault browser: {default.__class__.__name__}")

# Get specific browser controller
try:
    chrome = webbrowser.get("chrome")
    print(f"Chrome controller: {chrome.__class__.__name__}")
except webbrowser.Error:
    print("Chrome: Not available")

try:
    firefox = webbrowser.get("firefox")
    print(f"Firefox controller: {firefox.__class__.__name__}")
except webbrowser.Error:
    print("Firefox: Not available")

print("=" * 5, "Opening URLs", "=" * 5)

# webbrowser.open() opens a URL in the default browser
# NOTE: These are commented out to avoid actually opening browsers
# during the cheat sheet demo. Uncomment to use.

# Open a URL in the default browser
# webbrowser.open("https://www.python.org")

# Open a URL with new=1 (new window if possible)
# webbrowser.open("https://docs.python.org", new=1)

# Open a URL with new=2 (new tab if possible)
# webbrowser.open("https://pypi.org", new=2)

# The 'new' parameter:
#   0 = same window/tab (default)
#   1 = new window
#   2 = new tab

print("webbrowser.open() examples (commented out):")
print('  webbrowser.open("https://www.python.org")')
print('  webbrowser.open("https://docs.python.org", new=1)')
print('  webbrowser.open("https://pypi.org", new=2)')

print("=" * 5, "Opening URLs in specific browsers", "=" * 5)

# Use a specific browser
# firefox = webbrowser.get("firefox")
# firefox.open("https://www.mozilla.org")

# chrome = webbrowser.get("chrome")
# chrome.open("https://www.google.com")

print("Specific browser examples (commented out):")
print('  firefox = webbrowser.get("firefox")')
print('  firefox.open("https://www.mozilla.org")')
print('  chrome = webbrowser.get("chrome")')
print('  chrome.open("https://www.google.com")')

print("=" * 5, "Opening local files", "=" * 5)

# Open a local HTML file
# html_path = os.path.abspath("index.html")
# webbrowser.open(f"file://{html_path}")

# Open a local file with a specific browser
# chrome = webbrowser.get("chrome")
# chrome.open(f"file://{html_path}")

print("Local file examples (commented out):")
print('  html_path = os.path.abspath("index.html")')
print('  webbrowser.open(f"file://{html_path}")')

print("=" * 5, "Registering custom browsers", "=" * 5)

# Register a custom browser path
# On Windows:
# webbrowser.register("mybrowser", None, webbrowser.GenericBrowser("C:/path/to/browser.exe"))

# On macOS:
# webbrowser.register("mybrowser", None, webbrowser.MacOSXBrowser("My Browser"))

# On Linux:
# webbrowser.register("mybrowser", None, webbrowser.GenericBrowser("/usr/bin/my-browser"))

print("Custom browser registration (commented out):")
print('  webbrowser.register("mybrowser", None, webbrowser.GenericBrowser("/path/to/browser"))')

# Using BackgroundBrowser (runs browser in background)
# browser = webbrowser.BackgroundBrowser("/usr/bin/firefox")
# webbrowser.register("firefox-bg", None, browser)

# Using GenericBrowser (waits for browser to exit)
# browser = webbrowser.GenericBrowser("/usr/bin/lynx")
# webbrowser.register("lynx", None, browser)

print("=" * 5, "Opening search queries", "=" * 5)

# Build a search URL and open it
from urllib.parse import quote_plus

def open_search(query, engine="google"):
    """Open a search query in the default browser."""
    engines = {
        "google": "https://www.google.com/search?q=",
        "bing": "https://www.bing.com/search?q=",
        "duckduckgo": "https://duckduckgo.com/?q=",
        "github": "https://github.com/search?q=",
        "stackoverflow": "https://stackoverflow.com/search?q=",
        "pypi": "https://pypi.org/search/?q=",
        "wikipedia": "https://en.wikipedia.org/w/index.php?search=",
    }
    base_url = engines.get(engine, engines["google"])
    url = base_url + quote_plus(query)
    print(f"  Search URL: {url}")
    # webbrowser.open(url)
    return url

# Example search URLs
print("Search URL examples:")
open_search("Python webbrowser module", "google")
open_search("Python webbrowser", "stackoverflow")
open_search("requests", "pypi")
open_search("webbrowser", "wikipedia")

print("=" * 5, "Practical: documentation opener", "=" * 5)

def open_python_docs(module_name, version="3"):
    """Open Python documentation for a module."""
    base_url = f"https://docs.python.org/{version}/library/{module_name}.html"
    print(f"  Docs URL: {base_url}")
    # webbrowser.open(base_url)
    return base_url

def open_github_repo(owner, repo):
    """Open a GitHub repository in the browser."""
    url = f"https://github.com/{owner}/{repo}"
    print(f"  GitHub URL: {url}")
    # webbrowser.open(url)
    return url

# Example usage
print("Documentation opener examples:")
open_python_docs("webbrowser")
open_python_docs("urllib.parse")
open_github_repo("python", "cpython")
open_github_repo("psf", "requests")

print("=" * 5, "webbrowser.open_new and open_new_tab", "=" * 5)

# open_new: try to open in a new window
# webbrowser.open_new("https://www.python.org")

# open_new_tab: try to open in a new tab
# webbrowser.open_new_tab("https://docs.python.org")

print("open_new / open_new_tab examples (commented out):")
print('  webbrowser.open_new("https://www.python.org")')
print('  webbrowser.open_new_tab("https://docs.python.org")')

print("=" * 5, "Return value and error handling", "=" * 5)

# open() returns True if the browser was launched successfully
# result = webbrowser.open("https://www.python.org")
# print(f"Browser launched: {result}")

# Handle cases where no browser is available
try:
    result = webbrowser.open("https://www.python.org")
    if result:
        print("  Browser opened successfully")
    else:
        print("  Could not open browser")
except webbrowser.Error as e:
    print(f"  Error: {e}")
    # Fallback: print URL for manual opening
    print("  Please open manually: https://www.python.org")

print("=" * 5, "Summary of webbrowser functions", "=" * 5)

functions = [
    ("webbrowser.open(url)", "Open URL in default browser"),
    ("webbrowser.open_new(url)", "Open URL in new window"),
    ("webbrowser.open_new_tab(url)", "Open URL in new tab"),
    ("webbrowser.get(name)", "Get browser controller by name"),
    ("webbrowser.register(name, ...)", "Register a custom browser"),
]
for func, desc in functions:
    print(f"  {func:<40} {desc}")