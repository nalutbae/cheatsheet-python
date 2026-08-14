# requests: file download, streaming, and progress tracking

import requests
import os
import tempfile

BASE = "https://httpbin.org"

print("=" * 5, "Download file to memory", "=" * 5)

# Small file — load entire response into memory
resp = requests.get(f"{BASE}/image/png", timeout=10)
print(f"Status: {resp.status_code}")  # 200
print(f"Content-Type: {resp.headers.get('content-type')}")  # image/png
print(f"Size: {len(resp.content)} bytes")

# Access content as bytes
print(f"First 20 bytes: {resp.content[:20]}")

# Check if response is binary
print(f"Is image: {resp.headers.get('content-type', '').startswith('image')}")

print("=" * 5, "Stream download to file (large files)", "=" * 5)

# Stream=True means the response body is not downloaded immediately
# Use iter_content() to download chunk by chunk
download_path = os.path.join(tempfile.gettempdir(), "test_image.png")
resp = requests.get(f"{BASE}/image/png", stream=True, timeout=10)

with open(download_path, "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192):
        if chunk:  # filter out keep-alive chunks
            f.write(chunk)

print(f"Downloaded to: {download_path}")
print(f"File size: {os.path.getsize(download_path)} bytes")
os.unlink(download_path)  # clean up

# Always close stream responses when done
resp.close()

print("=" * 5, "Download with progress tracking", "=" * 5)

# Track download progress using Content-Length header
resp = requests.get(f"{BASE}/image/jpeg", stream=True, timeout=10)
total_size = int(resp.headers.get("content-length", 0))
downloaded = 0
chunks_received = 0

for chunk in resp.iter_content(chunk_size=8192):
    downloaded += len(chunk)
    chunks_received += 1
    if total_size > 0:
        pct = (downloaded / total_size) * 100
        # Print progress at 25%, 50%, 75%, 100%
        if pct >= chunks_received * 25:
            print(f"  Progress: {pct:.0f}% ({downloaded}/{total_size} bytes)")

print(f"JPEG download complete: {downloaded} bytes in {chunks_received} chunks")
resp.close()

print("=" * 5, "Download with context manager", "=" * 5)

# Use context manager to ensure response is closed
download_path = os.path.join(tempfile.gettempdir(), "test_image2.png")

with requests.get(f"{BASE}/image/png", stream=True, timeout=10) as resp:
    resp.raise_for_status()
    with open(download_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

print(f"Downloaded with context manager: {os.path.getsize(download_path)} bytes")
os.unlink(download_path)

print("=" * 5, "Raw response stream", "=" * 5)

# .raw gives access to the underlying urllib3 response
# Must set stream=True before accessing .raw
resp = requests.get(f"{BASE}/stream/5", stream=True, timeout=10)

# Read raw bytes (socket level)
raw_data = resp.raw.read(200)
print(f"Raw bytes read: {len(raw_data)} bytes")
print(f"Raw data type: {type(raw_data)}")

# Decode raw data
decoded = raw_data.decode("utf-8", errors="replace")
print(f"Decoded preview: {decoded[:80]}...")
resp.close()

print("=" * 5, "Line-by-line streaming (SSE / NDJSON)", "=" * 5)

# iter_lines() — useful for Server-Sent Events, NDJSON, log streams
resp = requests.get(f"{BASE}/stream/5", stream=True, timeout=10)
lines = []
for line in resp.iter_lines(decode_unicode=True):
    if line:  # skip empty keep-alive lines
        lines.append(line)

print(f"Lines received: {len(lines)}")
if lines:
    print(f"First line preview: {lines[0][:80]}...")
resp.close()

# iter_lines with delimiter
resp = requests.get(f"{BASE}/stream/3", stream=True, timeout=10)
for i, line in enumerate(resp.iter_lines(decode_unicode=True)):
    if line and i < 2:  # Show first 2 non-empty lines
        print(f"  Line {i+1}: {line[:80]}...")
resp.close()

print("=" * 5, "Chunked transfer encoding", "=" * 5)

# iter_content with various chunk sizes
resp = requests.get(f"{BASE}/stream/3", stream=True, timeout=10)
small_chunks = []
for chunk in resp.iter_content(chunk_size=256):
    small_chunks.append(chunk)
print(f"Small chunks (256 bytes): {len(small_chunks)} chunks")
resp.close()

resp = requests.get(f"{BASE}/stream/3", stream=True, timeout=10)
large_chunks = []
for chunk in resp.iter_content(chunk_size=16384):
    large_chunks.append(chunk)
print(f"Large chunks (16KB): {len(large_chunks)} chunks")
resp.close()

print("=" * 5, "Download with retry on failure", "=" * 5)

from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

session = requests.Session()
retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)

# This will automatically retry if the server returns 5xx
resp = session.get(f"{BASE}/image/png", timeout=10)
print(f"Download with retry: {resp.status_code}")  # 200
print(f"Size: {len(resp.content)} bytes")
session.close()

print("=" * 5, "Download with content-type detection", "=" * 5)

# Detect content type and save with correct extension
resp = requests.get(f"{BASE}/image/png", timeout=10)
content_type = resp.headers.get("content-type", "")
extension_map = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/gif": ".gif",
    "application/json": ".json",
    "text/html": ".html",
    "text/plain": ".txt",
}
ext = extension_map.get(content_type.split(";")[0].strip(), ".bin")
print(f"Content-Type: {content_type}")
print(f"Detected extension: {ext}")

# Save with correct extension
download_path = os.path.join(tempfile.gettempdir(), f"downloaded{ext}")
with open(download_path, "wb") as f:
    f.write(resp.content)
print(f"Saved as: {download_path}")
os.unlink(download_path)

print("=" * 5, "Conditional download (Last-Modified / ETag)", "=" * 5)

# First request — get ETag and Last-Modified
resp = requests.get(f"{BASE}/get", timeout=10)
etag = resp.headers.get("ETag")
last_modified = resp.headers.get("Last-Modified")
print(f"ETag: {etag}")
print(f"Last-Modified: {last_modified}")

# Conditional request — only download if content changed
if etag:
    headers = {"If-None-Match": etag}
    resp2 = requests.get(f"{BASE}/get", headers=headers, timeout=10)
    if resp2.status_code == 304:
        print("Content not modified (304 Not Modified) — skip download")
    else:
        print(f"Content changed: {resp2.status_code}")

if last_modified:
    headers = {"If-Modified-Since": last_modified}
    resp3 = requests.get(f"{BASE}/get", headers=headers, timeout=10)
    if resp3.status_code == 304:
        print("Not modified since last download (304) — skip download")
    else:
        print(f"Modified: {resp3.status_code}")