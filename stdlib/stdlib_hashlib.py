# hashlib: cryptographic hashing and message digests

import hashlib
import os

print("=" * 5, "Available algorithms", "=" * 5)

print(f"Available: {sorted(hashlib.algorithms_available)}")
print(f"Guaranteed: {sorted(hashlib.algorithms_guaranteed)}")
print(f"MD5 available: {'md5' in hashlib.algorithms_available}")
print(f"SHA256 available: {'sha256' in hashlib.algorithms_available}")

print("=" * 5, "Creating hashes", "=" * 5)

# SHA-256 hash (recommended for most uses)
text = "Hello, World!"
hash_obj = hashlib.sha256(text.encode("utf-8"))
print(f"SHA-256: {hash_obj.hexdigest()}")
# 7f83b1657ff5fc53b92dc...

# MD5 hash (fast but not cryptographically secure)
md5_hash = hashlib.md5(text.encode("utf-8"))
print(f"MD5: {md5_hash.hexdigest()}")

# SHA-1 hash (deprecated for security, still used for checksums)
sha1_hash = hashlib.sha1(text.encode("utf-8"))
print(f"SHA-1: {sha1_hash.hexdigest()}")

# SHA-512 hash
sha512_hash = hashlib.sha512(text.encode("utf-8"))
print(f"SHA-512: {sha512_hash.hexdigest()[:40]}...")  # truncated for display

# SHA-384 hash
sha384_hash = hashlib.sha384(text.encode("utf-8"))
print(f"SHA-384: {sha384_hash.hexdigest()[:40]}...")

# BLAKE2 (modern, fast, secure)
blake2b = hashlib.blake2b(text.encode("utf-8"))
print(f"BLAKE2b: {blake2b.hexdigest()[:40]}...")

blake2s = hashlib.blake2s(text.encode("utf-8"))
print(f"BLAKE2s: {blake2s.hexdigest()[:40]}...")

print("=" * 5, "Hash properties", "=" * 5)

# Hash length (in bytes and hex digits)
for algo in ["md5", "sha1", "sha256", "sha512"]:
    h = hashlib.new(algo)
    print(f"{algo}: {h.digest_size} bytes = {h.digest_size * 2} hex chars, block_size={h.block_size}")

# Deterministic: same input always gives same output
h1 = hashlib.sha256(b"hello")
h2 = hashlib.sha256(b"hello")
print(f"Same input, same hash: {h1.hexdigest() == h2.hexdigest()}")  # True

# Small change = completely different hash
h3 = hashlib.sha256(b"hello")
h4 = hashlib.sha256(b"hellp")  # one character difference
print(f"hello: {h3.hexdigest()[:20]}...")
print(f"hellp: {h4.hexdigest()[:20]}...")
print(f"Completely different: {h3.hexdigest() != h4.hexdigest()}")  # True

print("=" * 5, "Incremental hashing (large files)", "=" * 5)

# For large data, update the hash incrementally
data_parts = [b"Hello", b", ", b"World", b"!"]

# Method 1: hash all at once
full_hash = hashlib.sha256(b"Hello, World!")
print(f"Full hash: {full_hash.hexdigest()[:20]}...")

# Method 2: update incrementally
incremental = hashlib.sha256()
for part in data_parts:
    incremental.update(part)
print(f"Incremental hash: {incremental.hexdigest()[:20]}...")

# Both methods produce the same result
print(f"Same result: {full_hash.hexdigest() == incremental.hexdigest()}")  # True

# Practical: hash a file
file_content = b"This is the content of a file.\nLine 2.\nLine 3.\n"

def hash_bytes(data, algorithm="sha256"):
    """Hash bytes using the specified algorithm."""
    h = hashlib.new(algorithm)
    h.update(data)
    return h.hexdigest()

print(f"File hash (SHA-256): {hash_bytes(file_content)[:40]}...")
print(f"File hash (MD5): {hash_bytes(file_content, 'md5')}")

print("=" * 5, "HMAC: keyed hashing for message authentication", "=" * 5)

import hmac

secret_key = b"my-secret-key-12345"
message = b"Important message to verify"

# Create HMAC
mac = hmac.new(secret_key, message, hashlib.sha256)
print(f"HMAC-SHA256: {mac.hexdigest()[:40]}...")

# Verify HMAC (constant-time comparison to prevent timing attacks)
received_mac = mac.hexdigest()
new_mac = hmac.new(secret_key, message, hashlib.sha256)
is_valid = hmac.compare_digest(received_mac, new_mac.hexdigest())
print(f"HMAC valid: {is_valid}")  # True

# Wrong key produces different HMAC
wrong_key = b"wrong-key"
wrong_mac = hmac.new(wrong_key, message, hashlib.sha256)
is_valid = hmac.compare_digest(received_mac, wrong_mac.hexdigest())
print(f"HMAC with wrong key: {is_valid}")  # False

# Tampered message produces different HMAC
tampered = b"Important message to verify TAMPERED"
tampered_mac = hmac.new(secret_key, tampered, hashlib.sha256)
is_valid = hmac.compare_digest(received_mac, tampered_mac.hexdigest())
print(f"HMAC with tampered message: {is_valid}")  # False

print("=" * 5, "Practical: password hashing with salt", "=" * 5)

import secrets

def hash_password(password, salt=None):
    """Hash a password with a salt using SHA-256."""
    if salt is None:
        salt = secrets.token_hex(16)
    hashed = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return f"{salt}${hashed}"

def verify_password(password, stored_hash):
    """Verify a password against a stored hash."""
    salt, hashed = stored_hash.split("$")
    new_hash = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return hmac.compare_digest(hashed, new_hash)

# Hash and verify
original_password = "MySecurePassword123!"
stored = hash_password(original_password)
print(f"Stored hash: {stored[:40]}...")
print(f"Correct password: {verify_password(original_password, stored)}")  # True
print(f"Wrong password: {verify_password('wrongpassword', stored)}")  # False

# Note: For real applications, use bcrypt, argon2, or PBKDF2
# hashlib.pbkdf2_hmac is available for key derivation
salt = b"salt_value"
key = hashlib.pbkdf2_hmac("sha256", b"password", salt, 100000)
print(f"PBKDF2 key: {key.hex()[:40]}...")

print("=" * 5, "Practical: file integrity check", "=" * 5)

# Create example files
EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "stdlib_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

file_path = os.path.join(EXAMPLE_DIR, "integrity_test.txt")
with open(file_path, "w") as f:
    f.write("Original content\n")

def file_hash(filepath, algorithm="sha256"):
    """Calculate hash of a file."""
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

original_hash = file_hash(file_path)
print(f"Original hash: {original_hash[:40]}...")

# Verify file integrity
def verify_file_integrity(filepath, expected_hash, algorithm="sha256"):
    """Verify file integrity by comparing hashes."""
    actual_hash = file_hash(filepath, algorithm)
    if hmac.compare_digest(actual_hash, expected_hash):
        return True
    return False

print(f"Integrity check (original): {verify_file_integrity(file_path, original_hash)}")  # True

# Tamper with file
with open(file_path, "a") as f:
    f.write("Tampered!\n")

print(f"Integrity check (tampered): {verify_file_integrity(file_path, original_hash)}")  # False

# Clean up
os.remove(file_path)