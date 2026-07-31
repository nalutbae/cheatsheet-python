# File reading and writing

import os

# Use a project-relative directory for example files
EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "Writing files", "=" * 5)

# Basic file writing with open()
file_path = os.path.join(EXAMPLE_DIR, "basic.txt")

with open(file_path, "w") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")
    f.write("Third line\n")

# Read it back to verify
with open(file_path, "r") as f:
    print(f.read())
# Hello, World!
# Second line
# Third line

# Writing multiple lines with writelines()
file_path2 = os.path.join(EXAMPLE_DIR, "lines.txt")

with open(file_path2, "w") as f:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    f.writelines(lines)

with open(file_path2, "r") as f:
    print(f.read())
# Line 1
# Line 2
# Line 3

# Write modes: "w" (overwrite), "a" (append), "x" (exclusive create)
append_path = os.path.join(EXAMPLE_DIR, "append.txt")

with open(append_path, "w") as f:
    f.write("First line\n")

with open(append_path, "a") as f:
    f.write("Appended line\n")

with open(append_path, "r") as f:
    print(f.read())
# First line
# Appended line

# "x" mode: exclusive create — fails if file exists
exclusive_path = os.path.join(EXAMPLE_DIR, "exclusive.txt")

with open(exclusive_path, "x") as f:
    f.write("New file\n")
# with open(exclusive_path, "x") as f:  # FileExistsError if run again

print("=" * 5, "Reading files", "=" * 5)

# Read entire file with read()
with open(file_path, "r") as f:
    content = f.read()
    print(f"Full content:\n{content}")

# Read a specific number of characters
with open(file_path, "r") as f:
    first_5 = f.read(5)
    print(f"First 5 chars: {first_5!r}")  # First 5 chars: 'Hello'

# Read a single line with readline()
with open(file_path, "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"Line 1: {line1!r}")  # Line 1: 'Hello, World!\n'
    print(f"Line 2: {line2!r}")  # Line 2: 'Second line\n'

# Read all lines as a list with readlines()
with open(file_path, "r") as f:
    lines = f.readlines()
    print(f"Lines: {lines}")  # ['Hello, World!\n', 'Second line\n', 'Third line\n']

# Iterate over lines (most memory efficient for large files)
with open(file_path, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.rstrip()}")

# Stripping newlines when reading
with open(file_path, "r") as f:
    lines_stripped = [line.rstrip("\n") for line in f]
    print(lines_stripped)  # ['Hello, World!', 'Second line', 'Third line']

print("=" * 5, "File modes summary", "=" * 5)

# "r"  — read (default), file must exist
# "w"  — write, creates or overwrites
# "a"  — append, creates if not exists
# "x"  — exclusive create, fails if exists
# "r+" — read and write, file must exist
# "w+" — write and read, creates or overwrites
# "a+" — append and read, creates if not exists
# "b"  — binary mode (add to any mode: "rb", "wb", "ab")
# "t"  — text mode (default, add to any mode: "rt", "wt")

print("=" * 5, "Binary file I/O", "=" * 5)

binary_path = os.path.join(EXAMPLE_DIR, "data.bin")

# Writing binary data
with open(binary_path, "wb") as f:
    data = bytes([0, 1, 2, 255, 254, 253])
    f.write(data)

# Reading binary data
with open(binary_path, "rb") as f:
    content = f.read()
    print(f"Binary content: {content}")  # Binary content: b'\x00\x01\x02\xff\xfe\xfd'
    print(f"As list: {list(content)}")  # As list: [0, 1, 2, 255, 254, 253]

print("=" * 5, "File pointer operations", "=" * 5)

seek_path = os.path.join(EXAMPLE_DIR, "seek_test.txt")

with open(seek_path, "w") as f:
    f.write("ABCDEFGHIJ")

with open(seek_path, "r") as f:
    print(f"Position: {f.tell()}")  # 0
    f.read(3)
    print(f"After 3 chars: {f.tell()}")  # 3
    f.seek(0)
    print(f"After seek(0): {f.tell()}")  # 0
    print(f"Read from start: {f.read(5)}")  # ABCDE
    f.seek(5)
    print(f"Read from 5: {f.read()}")  # FGHIJ

print("=" * 5, "CSV file I/O", "=" * 5)

import csv

csv_path = os.path.join(EXAMPLE_DIR, "data.csv")

# Writing CSV
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 30, "Seoul"])
    writer.writerow(["Bob", 25, "Tokyo"])
    writer.writerow(["Charlie", 35, "London"])

# Reading CSV
with open(csv_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['name', 'age', 'city']
# ['Alice', '30', 'Seoul']
# ['Bob', '25', 'Tokyo']
# ['Charlie', '35', 'London']

# DictReader and DictWriter
csv_dict_path = os.path.join(EXAMPLE_DIR, "dict_data.csv")

with open(csv_dict_path, "w", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30, "city": "Seoul"})
    writer.writerow({"name": "Bob", "age": 25, "city": "Tokyo"})

with open(csv_dict_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} ({row['age']}) from {row['city']}")
# Alice (30) from Seoul
# Bob (25) from Tokyo

print("=" * 5, "JSON file I/O", "=" * 5)

import json

json_path = os.path.join(EXAMPLE_DIR, "data.json")

# Writing JSON
data = {
    "name": "Alice",
    "age": 30,
    "scores": [85, 92, 78],
    "address": {"city": "Seoul", "zip": "04500"},
}

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

# Reading JSON
with open(json_path, "r") as f:
    loaded = json.load(f)
    print(f"Name: {loaded['name']}")  # Name: Alice
    print(f"Scores: {loaded['scores']}")  # Scores: [85, 92, 78]

# JSON string conversion (not file I/O, but related)
json_string = json.dumps(data, indent=2)
print(json_string)

parsed = json.loads(json_string)
print(parsed["name"])  # Alice

print("=" * 5, "Path operations with os.path and pathlib", "=" * 5)

from pathlib import Path

# os.path operations
file_name = os.path.basename(file_path)
dir_name = os.path.dirname(file_path)
print(f"Basename: {file_name}")  # basic.txt
print(f"Dirname: {dir_name}")  # .../examples

# pathlib operations (recommended modern approach)
p = Path(file_path)
print(f"Name: {p.name}")  # basic.txt
print(f"Stem: {p.stem}")  # basic
print(f"Suffix: {p.suffix}")  # .txt
print(f"Parent: {p.parent.name}")  # examples
print(f"Exists: {p.exists()}")  # True
print(f"Is file: {p.is_file()}")  # True
print(f"Size: {p.stat().st_size} bytes")  # 34 bytes