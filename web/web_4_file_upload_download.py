# requests: file uploads and multipart form data

import requests
import os
import tempfile

BASE = "https://httpbin.org"

print("=" * 5, "Upload a single file", "=" * 5)

# Create a temporary file to upload
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("Hello, this is a test file content!")
    temp_path = f.name

try:
    with open(temp_path, "rb") as f:
        resp = requests.post(f"{BASE}/post", files={"file": f})
    result = resp.json()
    print(f"Status: {resp.status_code}")  # 200
    print(f"File name echoed: {result['files']['file'][:30]}...")
    print(f"File field name: file")
finally:
    os.unlink(temp_path)

print("=" * 5, "Upload with custom filename and content type", "=" * 5)

with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
    f.write("name,age\nAlice,30\nBob,25\n")
    temp_path = f.name

try:
    with open(temp_path, "rb") as f:
        # Tuple: (filename, file_object, content_type)
        resp = requests.post(
            f"{BASE}/post",
            files={"file": ("data.csv", f, "text/csv")},
        )
    result = resp.json()
    print(f"Status: {resp.status_code}")  # 200
    print(f"Content type set: text/csv")
    print(f"File content echoed: {result['files']['file'][:40]}...")
finally:
    os.unlink(temp_path)

print("=" * 5, "Upload multiple files", "=" * 5)

with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f1, \
     tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f2:
    f1.write("Content of file 1")
    f2.write("Content of file 2")
    path1, path2 = f1.name, f2.name

try:
    with open(path1, "rb") as fp1, open(path2, "rb") as fp2:
        resp = requests.post(
            f"{BASE}/post",
            files=[
                ("files", ("file1.txt", fp1, "text/plain")),
                ("files", ("file2.txt", fp2, "text/plain")),
            ],
        )
    result = resp.json()
    print(f"Status: {resp.status_code}")  # 200
    print(f"Multiple files uploaded: {list(result['files'].keys())}")
finally:
    os.unlink(path1)
    os.unlink(path2)

print("=" * 5, "Upload from in-memory content (no temp file)", "=" * 5)

# Upload bytes directly without a file on disk
content = b"This is in-memory content, not from a file."
resp = requests.post(
    f"{BASE}/post",
    files={"file": ("memory.txt", content, "text/plain")},
)
result = resp.json()
print(f"Status: {resp.status_code}")  # 200
print(f"In-memory file echoed: {result['files']['file'][:40]}...")

# Upload string content
text_content = "Plain text content uploaded directly."
resp = requests.post(
    f"{BASE}/post",
    files={"file": ("notes.txt", text_content, "text/plain")},
)
result = resp.json()
print(f"String upload: {result['files']['file'][:30]}...")

print("=" * 5, "Multipart form data (files + fields)", "=" * 5)

with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("Resume content here...")
    temp_path = f.name

try:
    with open(temp_path, "rb") as fp:
        resp = requests.post(
            f"{BASE}/post",
            data={"applicant": "Alice", "position": "Engineer"},
            files={"resume": ("resume.txt", fp, "text/plain")},
        )
    result = resp.json()
    print(f"Status: {resp.status_code}")  # 200
    print(f"Form fields: {result['form']}")
    print(f"File uploaded: {list(result['files'].keys())}")
finally:
    os.unlink(temp_path)

print("=" * 5, "Multipart with mixed content types", "=" * 5)

# JSON + file in the same request
json_payload = {"name": "Bob", "role": "Developer"}
file_content = b"Cover letter content here."

# Note: cannot mix data= and json= in the same request.
# Use data for form fields, files for file uploads.
# For JSON body + files, send JSON as a form field:
resp = requests.post(
    f"{BASE}/post",
    data={"metadata": '{"name": "Bob", "role": "Developer"}'},
    files={"document": ("cover.txt", file_content, "text/plain")},
)
result = resp.json()
print(f"Mixed upload status: {resp.status_code}")  # 200
print(f"Form metadata: {result['form']['metadata'][:40]}...")
print(f"File: {list(result['files'].keys())}")

print("=" * 5, "Upload with explicit Content-Type header", "=" * 5)

with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
    import json
    json.dump({"key": "value", "items": [1, 2, 3]}, f)
    temp_path = f.name

try:
    with open(temp_path, "rb") as f:
        resp = requests.post(
            f"{BASE}/post",
            files={"file": ("data.json", f, "application/json")},
        )
    result = resp.json()
    print(f"JSON file upload: {result['files']['file'][:50]}...")
finally:
    os.unlink(temp_path)

print("=" * 5, "Upload with additional headers per file", "=" * 5)

file_content = b"Binary data content."
resp = requests.post(
    f"{BASE}/post",
    files={
        "file": (
            "report.pdf",     # filename
            file_content,     # content
            "application/pdf",  # content type
            {"X-Custom-Header": "custom-value"},  # extra headers
        ),
    },
)
print(f"Upload with custom headers: {resp.status_code}")  # 200