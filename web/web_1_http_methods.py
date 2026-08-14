# requests: HTTP methods — GET, POST, PUT, PATCH, DELETE

import requests
import json

# Use httpbin.org for testing — it echoes back what you send
BASE = "https://httpbin.org"

print("=" * 5, "GET request", "=" * 5)

# Simple GET
resp = requests.get(f"{BASE}/get")
print(f"Status: {resp.status_code}")  # 200
print(f"Content-Type: {resp.headers.get('content-type')}")  # application/json
print(f"Response URL: {resp.url}")

# GET with query parameters
params = {"q": "python requests", "page": 1, "sort": "relevance"}
resp = requests.get(f"{BASE}/get", params=params)
print(f"\nGET with params URL: {resp.url}")
data = resp.json()
print(f"Query params echoed: {data['args']}")

# GET with custom headers
headers = {"User-Agent": "MyApp/1.0", "Accept": "application/json"}
resp = requests.get(f"{BASE}/get", headers=headers)
print(f"Headers echoed: User-Agent={resp.json()['headers'].get('User-Agent')}")

print("=" * 5, "POST request", "=" * 5)

# POST with form data
form_data = {"username": "alice", "password": "secret123"}
resp = requests.post(f"{BASE}/post", data=form_data)
result = resp.json()
print(f"Form data echoed: {result['form']}")

# POST with JSON body
json_data = {"name": "Alice", "age": 30, "skills": ["Python", "SQL"]}
resp = requests.post(f"{BASE}/post", json=json_data)
result = resp.json()
print(f"JSON data echoed: {result['json']}")

# POST with explicit content-type
resp = requests.post(
    f"{BASE}/post",
    data=json.dumps(json_data),
    headers={"Content-Type": "application/json"},
)
print(f"Manual JSON post status: {resp.status_code}")  # 200

# POST with files will be covered in requests_3_advanced.py

print("=" * 5, "PUT request", "=" * 5)

# PUT — replace entire resource
updated_user = {"name": "Alice Smith", "age": 31, "skills": ["Python", "SQL", "Docker"]}
resp = requests.put(f"{BASE}/put", json=updated_user)
result = resp.json()
print(f"PUT data echoed: {result['json']}")

print("=" * 5, "PATCH request", "=" * 5)

# PATCH — partial update
patch_data = {"age": 32}
resp = requests.patch(f"{BASE}/patch", json=patch_data)
result = resp.json()
print(f"PATCH data echoed: {result['json']}")

print("=" * 5, "DELETE request", "=" * 5)

# DELETE — remove resource
resp = requests.delete(f"{BASE}/delete")
result = resp.json()
print(f"DELETE status: {resp.status_code}")  # 200

print("=" * 5, "Response object attributes", "=" * 5)

resp = requests.get(f"{BASE}/get")
print(f"Status code: {resp.status_code}")  # 200
print(f"Reason: {resp.reason}")  # OK
print(f"Encoding: {resp.encoding}")  # utf-8
print(f"URL: {resp.url}")
print(f"Content length: {len(resp.content)} bytes")
print(f"Text preview: {resp.text[:100]}...")
print(f"JSON keys: {list(resp.json().keys())}")

# Response headers
print(f"\nResponse headers:")
for key, value in resp.headers.items():
    print(f"  {key}: {value[:60]}{'...' if len(value) > 60 else ''}")

# Check status with raise_for_status
resp = requests.get(f"{BASE}/get")
resp.raise_for_status()  # Raises HTTPError if status >= 400
print(f"\nraise_for_status: OK (no exception)")

# ELIF-style status checking
resp = requests.get(f"{BASE}/get")
if resp.ok:  # True if status_code < 400
    print(f"Request succeeded: {resp.status_code}")
elif resp.status_code == 404:
    print("Not found")
elif resp.status_code == 500:
    print("Server error")

print("=" * 5, "Streaming large responses", "=" * 5)

# Stream response — process chunk by chunk without loading all into memory
resp = requests.get(f"{BASE}/stream/5", stream=True)
chunk_count = 0
for chunk in resp.iter_content(chunk_size=8192):
    chunk_count += 1
    if chunk_count > 3:  # Just demonstrate first few chunks
        break
print(f"Streamed {chunk_count} chunks (stopped early)")
resp.close()  # Important: close when streaming