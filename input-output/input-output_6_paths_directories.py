# Directory and file path operations

import os
import shutil
from pathlib import Path

# Create examples directory
EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "os.path operations", "=" * 5)

# Joining paths
path1 = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined: {path1}")  # folder/subfolder/file.txt (or folder\subfolder\file.txt on Windows)

# Splitting paths
full_path = os.path.join(EXAMPLE_DIR, "test.txt")
print(f"Basename: {os.path.basename(full_path)}")  # test.txt
print(f"Dirname: {os.path.dirname(full_path)}")  # .../examples

# Splitting extension
print(f"Splitext: {os.path.splitext('report.pdf')}")  # ('report', '.pdf')
print(f"Splitext: {os.path.splitext('archive.tar.gz')}")  # ('archive.tar', '.gz')

# Getting absolute path
abs_path = os.path.abspath(".")
print(f"Absolute: {abs_path}")

# Checking path existence
print(f"Example dir exists: {os.path.exists(EXAMPLE_DIR)}")  # True
print(f"Fake path exists: {os.path.exists('/nonexistent/path')}")  # False

# Checking file vs directory
print(f"Is dir: {os.path.isdir(EXAMPLE_DIR)}")  # True

# Create a test file to check isfile
test_file = os.path.join(EXAMPLE_DIR, "path_test.txt")
with open(test_file, "w") as f:
    f.write("test")
print(f"Is file: {os.path.isfile(test_file)}")  # True

# Getting file size and modification time
size = os.path.getsize(test_file)
mtime = os.path.getmtime(test_file)
print(f"Size: {size} bytes")  # 4 bytes
print(f"Modified: {mtime}")

# Listing directory contents
print(f"Listdir: {os.listdir(EXAMPLE_DIR)}")

# Walking directory tree
print("Walk results:")
for root, dirs, files in os.walk(EXAMPLE_DIR):
    for f in files[:3]:  # limit output
        print(f"  {os.path.join(root, f)}")

print("=" * 5, "pathlib (modern approach, Python 3.4+)", "=" * 5)

# Creating Path objects
p = Path(EXAMPLE_DIR)
print(f"Path: {p}")
print(f"Name: {p.name}")  # examples
print(f"Parent: {p.parent.name}")  # input-output (or cheatsheet directory name)
print(f"Exists: {p.exists()}")  # True
print(f"Is dir: {p.is_dir()}")  # True

# Path arithmetic with / operator
data_path = Path(EXAMPLE_DIR) / "data" / "raw"
print(f"Nested path: {data_path}")  # .../examples/data/raw

# Creating directories
data_path.mkdir(parents=True, exist_ok=True)

# Path parts
sample = Path("/home/user/documents/report.txt")
print(f"Parts: {sample.parts}")  # ('/', 'home', 'user', 'documents', 'report.txt')
print(f"Drive: {sample.drive}")  # '' (empty on Linux, 'C:' on Windows)
print(f"Root: {sample.root}")  # /
print(f"Stem: {sample.stem}")  # report
print(f"Suffix: {sample.suffix}")  # .txt
print(f"Suffixes: {sample.suffixes}")  # ['.txt']

# Multiple suffixes
archive = Path("backup.tar.gz")
print(f"Stem: {archive.stem}")  # backup.tar
print(f"Suffix: {archive.suffix}")  # .gz
print(f"Suffixes: {archive.suffixes}")  # ['.tar', '.gz']

# Path resolution
p = Path("folder/../file.txt")
print(f"Resolved: {p.resolve()}")

# Glob pattern matching
example_dir = Path(EXAMPLE_DIR)

# Create some test files for glob
for name in ["test_a.txt", "test_b.txt", "data.csv", "config.json"]:
    (example_dir / name).write_text(f"content of {name}")

# Find all .txt files
txt_files = list(example_dir.glob("*.txt"))
print(f"TXT files: {[f.name for f in txt_files]}")

# Find all files with recursive glob
all_files = list(example_dir.glob("**/*"))
print(f"Total files: {len(all_files)}")

# Reading and writing with Path
readme_path = example_dir / "readme_path_test.txt"
readme_path.write_text("Hello from pathlib!")
content = readme_path.read_text()
print(f"Read: {content}")  # Hello from pathlib!

# Appending with Path (read + write)
existing = readme_path.read_text()
readme_path.write_text(existing + "\nAppended line!")
print(readme_path.read_text())
# Hello from pathlib!
# Appended line!

# Renaming and moving
renamed_path = example_dir / "renamed_test.txt"
readme_path.rename(renamed_path)
print(f"Renamed exists: {renamed_path.exists()}")  # True
print(f"Original exists: {readme_path.exists()}")  # False

# Stat information
stat_info = renamed_path.stat()
print(f"Size: {stat_info.st_size} bytes")
print(f"Modified: {stat_info.st_mtime}")

print("=" * 5, "File operations (copy, move, delete)", "=" * 5)

# Copying files
src = os.path.join(EXAMPLE_DIR, "test_a.txt")
dst = os.path.join(EXAMPLE_DIR, "test_a_copy.txt")
shutil.copy2(src, dst)  # copy2 preserves metadata
print(f"Copy exists: {os.path.exists(dst)}")  # True

# Copying directories
src_dir = os.path.join(EXAMPLE_DIR, "data")
dst_dir = os.path.join(EXAMPLE_DIR, "data_backup")
if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
shutil.copytree(src_dir, dst_dir)
print(f"Backup dir exists: {os.path.exists(dst_dir)}")  # True

# Moving/renaming files
move_src = os.path.join(EXAMPLE_DIR, "test_b.txt")
move_dst = os.path.join(EXAMPLE_DIR, "moved_b.txt")
shutil.move(move_src, move_dst)
print(f"Moved file exists: {os.path.exists(move_dst)}")  # True

# Deleting files
delete_path = os.path.join(EXAMPLE_DIR, "to_delete.txt")
with open(delete_path, "w") as f:
    f.write("temporary")
os.remove(delete_path)
print(f"Deleted file exists: {os.path.exists(delete_path)}")  # False

# Deleting directories
del_dir = os.path.join(EXAMPLE_DIR, "to_delete_dir")
os.makedirs(del_dir, exist_ok=True)
shutil.rmtree(del_dir)
print(f"Deleted dir exists: {os.path.exists(del_dir)}")  # False

print("=" * 5, "Temporary files and directories", "=" * 5)

import tempfile

# Temporary file (auto-deleted when closed)
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=True) as tmp:
    tmp.write("Temporary content")
    tmp.flush()  # ensure data is written
    print(f"Temp file: {tmp.name}")
    print(f"Temp file exists: {os.path.exists(tmp.name)}")  # True

print(f"After close, exists: {os.path.exists(tmp.name)}")  # False (auto-deleted)

# Temporary file (kept after closing)
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
    tmp.write("Persistent temp content")
    tmp.flush()
    kept_path = tmp.name

print(f"Kept temp file exists: {os.path.exists(kept_path)}")  # True
os.remove(kept_path)  # manually clean up

# Temporary directory
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"Temp dir: {tmpdir}")
    temp_file = os.path.join(tmpdir, "test.txt")
    with open(temp_file, "w") as f:
        f.write("temp data")
    print(f"Temp dir contents: {os.listdir(tmpdir)}")  # ['test.txt']

print(f"After exit, temp dir exists: {os.path.exists(tmpdir)}")  # False

# gettempdir() — system temp directory location
print(f"System temp dir: {tempfile.gettempdir()}")