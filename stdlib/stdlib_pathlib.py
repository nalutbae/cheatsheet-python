# pathlib: modern path handling

from pathlib import Path
import os
import tempfile

EXAMPLE_DIR = Path(__file__).parent / "stdlib_examples"
EXAMPLE_DIR.mkdir(exist_ok=True)

print("=" * 5, "Creating Path objects", "=" * 5)

# From strings
p1 = Path("folder/subfolder/file.txt")
print(f"Path from string: {p1}")  # folder/subfolder/file.txt

# From home directory
home = Path.home()
print(f"Home directory: {home}")

# From current directory
cwd = Path.cwd()
print(f"Current directory: {cwd}")

# From this file
this_file = Path(__file__).resolve()
print(f"This file: {this_file}")

# Path arithmetic with / operator
data_dir = EXAMPLE_DIR / "data" / "raw"
print(f"Nested path: {data_dir}")  # .../stdlib_examples/data/raw

print("=" * 5, "Path properties", "=" * 5)

# Path parts
sample = Path("/home/user/documents/report.txt")
print(f"Parts: {sample.parts}")  # ('/', 'home', 'user', 'documents', 'report.txt')
print(f"Drive: {sample.drive}")  # '' on Linux, 'C:' on Windows
print(f"Root: {sample.root}")  # /
print(f"Anchor: {sample.anchor}")  # /
print(f"Parents: {list(sample.parents)}")  # [PosixPath('/home/user/documents'), ...]
print(f"Parent: {sample.parent}")  # /home/user/documents
print(f"Name: {sample.name}")  # report.txt
print(f"Stem: {sample.stem}")  # report
print(f"Suffix: {sample.suffix}")  # .txt
print(f"Suffixes: {sample.suffixes}")  # ['.txt']

# Multiple suffixes
archive = Path("backup.tar.gz")
print(f"Stem: {archive.stem}")  # backup.tar
print(f"Suffix: {archive.suffix}")  # .gz
print(f"Suffixes: {archive.suffixes}")  # ['.tar', '.gz']

# Changing parts
print(f"with_name: {sample.with_name('output.csv')}")  # /home/user/documents/output.csv
print(f"with_stem: {sample.with_stem('draft')}")  # /home/user/documents/draft.txt
print(f"with_suffix: {sample.with_suffix('.csv')}")  # /home/user/documents/report.csv

# Relative path
rel = Path("src/main.py")
print(f"Is absolute: {rel.is_absolute()}")  # False
abs_path = Path("/usr/local/bin/python")
print(f"Is absolute: {abs_path.is_absolute()}")  # True

print("=" * 5, "Path resolution and existence", "=" * 5)

# resolve(): absolute path, resolving symlinks
p = Path("folder/../file.txt")
print(f"Resolved: {p.resolve()}")  # /current/dir/file.txt

# Check existence
print(f"EXAMPLE_DIR exists: {EXAMPLE_DIR.exists()}")  # True
print(f"EXAMPLE_DIR is_dir: {EXAMPLE_DIR.is_dir()}")  # True

# Create a test file
test_file = EXAMPLE_DIR / "pathlib_test.txt"
test_file.write_text("Hello from pathlib!")
print(f"test_file exists: {test_file.exists()}")  # True
print(f"test_file is_file: {test_file.is_file()}")  # True

# File size and modification time
stat = test_file.stat()
print(f"Size: {stat.st_size} bytes")  # 20 bytes
print(f"Modified: {stat.st_mtime}")

print("=" * 5, "Reading and writing files", "=" * 5)

# Write text
write_path = EXAMPLE_DIR / "hello.txt"
write_path.write_text("Hello, World!\nSecond line\n")
print(f"Wrote: {write_path}")

# Read text
content = write_path.read_text()
print(f"Read: {content.strip()}")

# Write bytes
binary_path = EXAMPLE_DIR / "data.bin"
binary_path.write_bytes(b"\x00\x01\x02\xff\xfe\xfd")
print(f"Wrote binary: {binary_path}")

# Read bytes
data = binary_path.read_bytes()
print(f"Read binary: {list(data)}")  # [0, 1, 2, 255, 254, 253]

# Append text (read + write)
existing = write_path.read_text()
write_path.write_text(existing + "Third line\n")
print(f"After append: {write_path.read_text().strip()}")

# Write with encoding
utf8_path = EXAMPLE_DIR / "korean.txt"
utf8_path.write_text("안녕하세요\n", encoding="utf-8")
print(f"Korean text: {utf8_path.read_text(encoding='utf-8').strip()}")

print("=" * 5, "Directory operations", "=" * 5)

# Create directories
new_dir = EXAMPLE_DIR / "new_folder" / "sub_folder"
new_dir.mkdir(parents=True, exist_ok=True)
print(f"Created: {new_dir}")  # exists

# Remove directory
new_dir.rmdir()  # remove sub_folder (must be empty)
EXAMPLE_DIR.joinpath("new_folder").rmdir()  # remove new_folder

# Create and iterate directories
for i in range(3):
    (EXAMPLE_DIR / f"dir_{i}").mkdir(exist_ok=True)
    (EXAMPLE_DIR / f"dir_{i}" / f"file_{i}.txt").write_text(f"Content {i}")

# List directory contents
print(f"Directory contents:")
for item in EXAMPLE_DIR.iterdir():
    print(f"  {'[DIR]' if item.is_dir() else '[FILE]'} {item.name}")

# Glob pattern matching
print(f"TXT files: {sorted(p.name for p in EXAMPLE_DIR.glob('*.txt'))}")
print(f"All files recursively: {len(list(EXAMPLE_DIR.rglob('*')))} items")

# Find files with pattern
py_files = list(Path.cwd().glob("**/*.py"))
print(f"Python files in cwd tree: {len(py_files)}")

# Clean up test directories
for i in range(3):
    dir_path = EXAMPLE_DIR / f"dir_{i}"
    for f in dir_path.iterdir():
        f.unlink()
    dir_path.rmdir()

print("=" * 5, "Path operations", "=" * 5)

# Join paths
data_path = EXAMPLE_DIR / "data" / "2025" / "07"
print(f"Joined: {data_path}")

# Get parent directory names
p = Path("/home/user/projects/myapp/src/main.py")
print(f"Path: {p}")
print(f"Parent: {p.parent}")  # /home/user/projects/myapp/src
print(f"Grandparent: {p.parent.parent}")  # /home/user/projects/myapp
print(f"Parent name: {p.parent.name}")  # src

# Relative to
try:
    rel = Path("/home/user/projects/myapp/src/main.py").relative_to("/home/user/projects")
    print(f"Relative: {rel}")  # myapp/src/main.py
except ValueError as e:
    print(f"Cannot make relative: {e}")

# is_relative_to (Python 3.9+)
p1 = Path("/home/user/file.txt")
p2 = Path("/home")
print(f"is_relative_to: {p1.is_relative_to(p2)}")  # True

print("=" * 5, "Temporary files with pathlib", "=" * 5)

# Create a temp file
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
    tmp.write("Temporary content")
    tmp_path = Path(tmp.name)

print(f"Temp file: {tmp_path}")
print(f"Exists: {tmp_path.exists()}")  # True
print(f"Content: {tmp_path.read_text()}")  # Temporary content
tmp_path.unlink()  # clean up
print(f"After unlink: {tmp_path.exists()}")  # False

# Create a temp directory
with tempfile.TemporaryDirectory() as tmpdir:
    tmp_path = Path(tmpdir)
    (tmp_path / "test.txt").write_text("Hello")
    print(f"Temp dir files: {list(tmp_path.iterdir())}")

print("=" * 5, "Path vs os.path comparison", "=" * 5)

# os.path (old way)
old_join = os.path.join("folder", "subfolder", "file.txt")
old_basename = os.path.basename(old_join)
old_dirname = os.path.dirname(old_join)
old_split = os.path.splitext(old_join)

# pathlib (new way)
new_path = Path("folder") / "subfolder" / "file.txt"
new_name = new_path.name
new_parent = new_path.parent
new_suffix = new_path.suffix

print(f"os.path.join:    {old_join}  →  pathlib: {new_path}")
print(f"os.path.basename: {old_basename}  →  pathlib: {new_name}")
print(f"os.path.dirname:  {old_dirname}  →  pathlib: {new_parent}")
print(f"os.path.splitext: {old_split}  →  pathlib: ({new_path.stem}, {new_suffix})")

# Clean up example files
for f in EXAMPLE_DIR.glob("*.txt"):
    f.unlink()
for f in EXAMPLE_DIR.glob("*.bin"):
    f.unlink()
EXAMPLE_DIR.rmdir()