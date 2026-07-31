# glob: Unix-style pathname pattern expansion

import glob
import os
from pathlib import Path

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "stdlib_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

# Create test directory structure
test_dirs = ["src", "docs", "tests", "data/raw", "data/processed"]
for d in test_dirs:
    os.makedirs(os.path.join(EXAMPLE_DIR, d), exist_ok=True)

test_files = {
    "src/main.py": "# main module",
    "src/utils.py": "# utilities",
    "src/helpers.py": "# helper functions",
    "src/__init__.py": "",
    "src/config.json": '{"debug": false}',
    "docs/readme.md": "# Documentation",
    "docs/api.md": "# API Reference",
    "docs/changelog.md": "# Changelog",
    "tests/test_main.py": "# test main",
    "tests/test_utils.py": "# test utils",
    "tests/__init__.py": "",
    "data/raw/data1.csv": "a,b,c\n1,2,3",
    "data/raw/data2.csv": "d,e,f\n4,5,6",
    "data/processed/result.json": '{"result": true}',
    "notes.txt": "Project notes",
    "config.yaml": "key: value",
    "README.md": "# Project",
}
for filepath, content in test_files.items():
    full_path = os.path.join(EXAMPLE_DIR, filepath)
    with open(full_path, "w") as f:
        f.write(content)

print("=" * 5, "Basic glob patterns", "=" * 5)

# glob.glob: returns a list of matching paths

# * matches any sequence of characters
py_files = glob.glob(os.path.join(EXAMPLE_DIR, "src", "*.py"))
print(f"*.py in src:")
for f in sorted(py_files):
    print(f"  {os.path.basename(f)}")

# ? matches exactly one character
two_char_py = glob.glob(os.path.join(EXAMPLE_DIR, "src", "??.py"))
print(f"??.py in src: {[os.path.basename(f) for f in sorted(two_char_py)]}")

# Match all markdown files
md_files = glob.glob(os.path.join(EXAMPLE_DIR, "docs", "*.md"))
print(f"*.md in docs: {[os.path.basename(f) for f in sorted(md_files)]}")

# Match all CSV files
csv_files = glob.glob(os.path.join(EXAMPLE_DIR, "data", "raw", "*.csv"))
print(f"*.csv in data/raw: {[os.path.basename(f) for f in sorted(csv_files)]}")

print("=" * 5, "Recursive glob with **", "=" * 5)

# ** matches any number of directories (recursive=True required)

# Find all .py files recursively
all_py = glob.glob(os.path.join(EXAMPLE_DIR, "**", "*.py"), recursive=True)
print(f"All .py files (recursive):")
for f in sorted(all_py):
    print(f"  {os.path.relpath(f, EXAMPLE_DIR)}")

# Find all .md files recursively
all_md = glob.glob(os.path.join(EXAMPLE_DIR, "**", "*.md"), recursive=True)
print(f"All .md files (recursive):")
for f in sorted(all_md):
    print(f"  {os.path.relpath(f, EXAMPLE_DIR)}")

# Find all files in any directory named "raw"
raw_files = glob.glob(os.path.join(EXAMPLE_DIR, "**", "raw", "*"), recursive=True)
print(f"Files in 'raw' dirs:")
for f in sorted(raw_files):
    if os.path.isfile(f):
        print(f"  {os.path.relpath(f, EXAMPLE_DIR)}")

print("=" * 5, "glob.iglob: iterator version", "=" * 5)

# iglob returns an iterator instead of a list (more memory efficient)
print(f"iglob results (iterator):")
for f in sorted(glob.iglob(os.path.join(EXAMPLE_DIR, "src", "*.py"))):
    print(f"  {os.path.basename(f)}")

# Useful for processing files one at a time without loading all paths into memory
py_count = sum(1 for _ in glob.iglob(os.path.join(EXAMPLE_DIR, "**", "*.py"), recursive=True))
print(f"Total .py files: {py_count}")

print("=" * 5, "Character ranges and sets", "=" * 5)

# [abc] matches 'a', 'b', or 'c'
# Create test files with different extensions
for ext in ["a1.py", "b2.py", "c3.py"]:
    with open(os.path.join(EXAMPLE_DIR, "src", ext), "w") as f:
        f.write(f"# {ext}")

# Match files starting with a, b, or c
abc_files = glob.glob(os.path.join(EXAMPLE_DIR, "src", "[abc]*.py"))
print(f"[abc]*.py: {sorted([os.path.basename(f) for f in abc_files])}")

# [0-9] matches any digit
digit_files = glob.glob(os.path.join(EXAMPLE_DIR, "src", "*[0-9]*.py"))
print(f"*[0-9]*.py: {sorted([os.path.basename(f) for f in digit_files])}")

# [!abc] matches characters NOT in the set
not_abc = glob.glob(os.path.join(EXAMPLE_DIR, "src", "[!abc]*.py"))
print(f"[!abc]*.py: {sorted([os.path.basename(f) for f in not_abc])}")

print("=" * 5, "escape: literal pattern matching", "=" * 5)

# glob.escape: escape special characters in a path
special_path = os.path.join(EXAMPLE_DIR, "src", "file[1].py")
escaped = glob.escape(special_path)
print(f"Original: {special_path}")
print(f"Escaped: {escaped}")

# Create a file with special characters in name
special_file = os.path.join(EXAMPLE_DIR, "file[1].txt")
with open(special_file, "w") as f:
    f.write("special content")

# Without escape, [1] would be treated as a character set
wrong_pattern = os.path.join(EXAMPLE_DIR, "file[1].txt")
wrong_matches = glob.glob(wrong_pattern)
print(f"Without escape: {wrong_matches}")  # might not match

# With escape, the brackets are treated literally
correct_pattern = glob.escape(os.path.join(EXAMPLE_DIR, "file[1].txt"))
correct_matches = glob.glob(correct_pattern)
print(f"With escape: {correct_matches}")

print("=" * 5, "Practical patterns", "=" * 5)

# Find all Python files (including __init__.py)
all_python = glob.glob(os.path.join(EXAMPLE_DIR, "**", "*.py"), recursive=True)
init_files = [f for f in all_python if os.path.basename(f) == "__init__.py"]
non_init = [f for f in all_python if os.path.basename(f) != "__init__.py"]
print(f"Init files: {len(init_files)}")
print(f"Non-init .py files: {len(non_init)}")

# Find all configuration files
config_patterns = ["*.json", "*.yaml", "*.yml", "*.toml", "*.ini", "*.cfg"]
config_files = []
for pattern in config_patterns:
    config_files.extend(glob.glob(os.path.join(EXAMPLE_DIR, "**", pattern), recursive=True))
print(f"Config files:")
for f in sorted(config_files):
    print(f"  {os.path.relpath(f, EXAMPLE_DIR)}")

# Find files by multiple extensions
extensions = ["*.py", "*.md", "*.csv"]
for ext in extensions:
    matches = glob.glob(os.path.join(EXAMPLE_DIR, "**", ext), recursive=True)
    print(f"  {ext}: {len(matches)} files")

# Find the deepest files (most nested)
all_files = glob.glob(os.path.join(EXAMPLE_DIR, "**", "*"), recursive=True)
all_files = [f for f in all_files if os.path.isfile(f)]
max_depth = max(len(Path(f).relative_to(EXAMPLE_DIR).parts) for f in all_files)
deep_files = [f for f in all_files if len(Path(f).relative_to(EXAMPLE_DIR).parts) == max_depth]
print(f"Deepest files (depth={max_depth}):")
for f in deep_files:
    print(f"  {os.path.relpath(f, EXAMPLE_DIR)}")

print("=" * 5, "glob vs pathlib.glob vs os.walk", "=" * 5)

# Method 1: glob module
glob_results = sorted(glob.glob(os.path.join(EXAMPLE_DIR, "**", "*.py"), recursive=True))
print(f"glob: {len(glob_results)} files")

# Method 2: pathlib.Path.glob
pathlib_results = sorted(str(p) for p in Path(EXAMPLE_DIR).rglob("*.py"))
print(f"pathlib.rglob: {len(pathlib_results)} files")

# Method 3: os.walk (more control)
walk_results = []
for root, dirs, files in os.walk(EXAMPLE_DIR):
    for f in files:
        if f.endswith(".py"):
            walk_results.append(os.path.join(root, f))
walk_results.sort()
print(f"os.walk: {len(walk_results)} files")

# All three find the same files
print(f"All methods agree: {glob_results == pathlib_results == walk_results}")

print("=" * 5, "Cleanup", "=" * 5)

shutil_import = __import__("shutil")
shutil_import.rmtree(EXAMPLE_DIR)
print(f"Cleaned up examples directory")