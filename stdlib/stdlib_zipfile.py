# zipfile: ZIP archive creation, reading, and manipulation

import zipfile
import os
import io

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "stdlib_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "Creating ZIP archives", "=" * 5)

# Create test files to archive
for name, content in [
    ("hello.txt", "Hello, World!\n"),
    ("data.csv", "name,age\nAlice,30\nBob,25\n"),
    ("notes.md", "# Notes\n\nSome important notes.\n"),
]:
    with open(os.path.join(EXAMPLE_DIR, name), "w") as f:
        f.write(content)

# Create a ZIP file from individual files
zip_path = os.path.join(EXAMPLE_DIR, "archive.zip")

# Method 1: write files one by one
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for name in ["hello.txt", "data.csv", "notes.md"]:
        filepath = os.path.join(EXAMPLE_DIR, name)
        zf.write(filepath, arcname=name)  # arcname: name inside the ZIP

print(f"Created: {zip_path}")
print(f"Size: {os.path.getsize(zip_path)} bytes")

# Method 2: write from string data (no file needed)
zip_path2 = os.path.join(EXAMPLE_DIR, "from_string.zip")
with zipfile.ZipFile(zip_path2, "w") as zf:
    zf.writestr("greeting.txt", "Hello from string!\n")
    zf.writestr("config.json", '{"key": "value"}')
    zf.writestr("subdir/nested.txt", "Nested content\n")

print(f"Created from string: {zip_path2}")
print(f"Size: {os.path.getsize(zip_path2)} bytes")

print("=" * 5, "Reading ZIP archives", "=" * 5)

# List contents of a ZIP file
with zipfile.ZipFile(zip_path, "r") as zf:
    print(f"Archive contents:")
    for info in zf.infolist():
        print(f"  {info.filename}: {info.file_size} bytes (compressed: {info.compress_size})")

# namelist: get list of filenames
with zipfile.ZipFile(zip_path, "r") as zf:
    names = zf.namelist()
    print(f"Name list: {names}")

# Read a specific file from the archive
with zipfile.ZipFile(zip_path, "r") as zf:
    content = zf.read("hello.txt").decode("utf-8")
    print(f"Content of hello.txt: {content.strip()}")

# Read all files
with zipfile.ZipFile(zip_path, "r") as zf:
    for name in zf.namelist():
        content = zf.read(name).decode("utf-8")
        print(f"  {name}: {len(content)} chars")

print("=" * 5, "Extracting ZIP archives", "=" * 5)

# Extract a single file
extract_dir = os.path.join(EXAMPLE_DIR, "extracted")
os.makedirs(extract_dir, exist_ok=True)

with zipfile.ZipFile(zip_path, "r") as zf:
    zf.extract("hello.txt", extract_dir)
    print(f"Extracted: hello.txt")

# Extract all files
extract_all_dir = os.path.join(EXAMPLE_DIR, "extracted_all")
with zipfile.ZipFile(zip_path, "r") as zf:
    zf.extractall(extract_all_dir)
    print(f"Extracted all to: {extract_all_dir}")

# List extracted files
for root, dirs, files in os.walk(extract_all_dir):
    for f in files:
        filepath = os.path.join(root, f)
        print(f"  {os.path.relpath(filepath, extract_all_dir)}")

# Extract from string-based ZIP (with subdirectories)
with zipfile.ZipFile(zip_path2, "r") as zf:
    for name in zf.namelist():
        content = zf.read(name).decode("utf-8")
        print(f"  {name}: {content.strip()}")

print("=" * 5, "Appending to existing archives", "=" * 5)

# Append files to an existing ZIP
with zipfile.ZipFile(zip_path, "a") as zf:
    zf.writestr("extra.txt", "This file was added later.\n")
    zf.writestr("more_data/info.txt", "Information file.\n")

with zipfile.ZipFile(zip_path, "r") as zf:
    print(f"After appending:")
    for info in zf.infolist():
        print(f"  {info.filename}")

print("=" * 5, "Compression methods", "=" * 5)

# Compare compression methods
test_data = "A" * 10000  # highly compressible data

for method, name in [
    (zipfile.ZIP_STORED, "STORED (no compression)"),
    (zipfile.ZIP_DEFLATED, "DEFLATED (default)"),
    (zipfile.ZIP_BZIP2, "BZIP2"),
    (zipfile.ZIP_LZMA, "LZMA"),
]:
    test_zip = os.path.join(EXAMPLE_DIR, f"test_{name.split()[0].lower()}.zip")
    try:
        with zipfile.ZipFile(test_zip, "w", compression=method) as zf:
            zf.writestr("repeated.txt", test_data)
        size = os.path.getsize(test_zip)
        ratio = size / len(test_data) * 100
        print(f"  {name}: {size} bytes ({ratio:.1f}% of original)")
        os.remove(test_zip)
    except Exception as e:
        print(f"  {name}: not supported ({e})")

print("=" * 5, "ZipInfo: detailed file information", "=" * 5)

with zipfile.ZipFile(zip_path, "r") as zf:
    for info in zf.infolist():
        print(f"  Filename: {info.filename}")
        print(f"  Size: {info.file_size} bytes")
        print(f"  Compressed: {info.compress_size} bytes")
        print(f"  Date: {info.date_time}")  # (year, month, day, hour, min, sec)
        print(f"  Compression type: {info.compress_type}")
        print(f"  Comment: {info.comment}")
        print()

print("=" * 5, "Password-protected archives", "=" * 5)

# Create a password-protected ZIP (note: ZIP encryption is weak!)
password = b"secret123"
pwd_zip = os.path.join(EXAMPLE_DIR, "password_protected.zip")

with zipfile.ZipFile(pwd_zip, "w") as zf:
    zf.writestr("confidential.txt", "This is top secret!\n")
    # Note: zipfile module's built-in encryption is weak (ZIP_CRYPTO)
    # For strong encryption, use the pyzipper library instead

print(f"Created password-protected archive")

# Read from a password-protected archive
with zipfile.ZipFile(pwd_zip, "r") as zf:
    try:
        content = zf.read("confidential.txt", pwd=password)
        print(f"Decrypted content: {content.decode('utf-8').strip()}")
    except RuntimeError as e:
        print(f"Encryption method not supported: {e}")
        print("Note: Use pyzipper for AES encryption support")

print("=" * 5, "In-memory ZIP archives", "=" * 5)

# Create a ZIP in memory (no file on disk)
buffer = io.BytesIO()

with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.writestr("in_memory_1.txt", "Created in memory\n")
    zf.writestr("in_memory_2.txt", "Also in memory\n")
    zf.writestr("data/report.csv", "id,value\n1,100\n2,200\n")

# Read from in-memory ZIP
buffer.seek(0)
with zipfile.ZipFile(buffer, "r") as zf:
    print(f"In-memory ZIP contents:")
    for name in zf.namelist():
        content = zf.read(name).decode("utf-8")
        print(f"  {name}: {content.strip()}")

# Send in-memory ZIP as bytes
zip_bytes = buffer.getvalue()
print(f"In-memory ZIP size: {len(zip_bytes)} bytes")

# Create another in-memory ZIP from bytes
buffer2 = io.BytesIO(zip_bytes)
with zipfile.ZipFile(buffer2, "r") as zf:
    names = zf.namelist()
    print(f"Names from bytes: {names}")

print("=" * 5, "Checking archive integrity", "=" * 5)

# Test if a ZIP file is valid
with zipfile.ZipFile(zip_path, "r") as zf:
    bad_file = zf.testzip()
    if bad_file is None:
        print(f"Archive integrity: OK (no corrupt files)")
    else:
        print(f"Corrupt file: {bad_file}")

# Check if a file is a ZIP file
print(f"Is ZIP (valid): {zipfile.is_zipfile(zip_path)}")  # True
print(f"Is ZIP (text file): {zipfile.is_zipfile(os.path.join(EXAMPLE_DIR, 'hello.txt'))}")  # False
print(f"Is ZIP (nonexistent): {zipfile.is_zipfile('/nonexistent.zip')}")  # False

print("=" * 5, "Practical: backup directory to ZIP", "=" * 5)

def backup_directory(src_dir, dest_zip):
    """Create a ZIP backup of a directory."""
    with zipfile.ZipFile(dest_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, src_dir)
                zf.write(filepath, arcname)
                print(f"  Added: {arcname}")

backup_zip = os.path.join(EXAMPLE_DIR, "backup.zip")
print(f"Creating backup:")
backup_directory(EXAMPLE_DIR, backup_zip)

# Verify backup
with zipfile.ZipFile(backup_zip, "r") as zf:
    print(f"\nBackup contains {len(zf.namelist())} files:")
    for name in zf.namelist():
        info = zf.getinfo(name)
        print(f"  {name}: {info.file_size} bytes")

print("=" * 5, "Cleanup", "=" * 5)

import shutil
shutil.rmtree(EXAMPLE_DIR)
print("Cleaned up examples directory")