# shutil: file and directory operations

import shutil
import os
from pathlib import Path

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "stdlib_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "Copying files", "=" * 5)

# Create a source file for testing
src_file = os.path.join(EXAMPLE_DIR, "source.txt")
with open(src_file, "w") as f:
    f.write("Hello, this is the source file!\nLine 2\nLine 3\n")

# Copy a file (metadata preserved)
dst_file = os.path.join(EXAMPLE_DIR, "copy.txt")
result = shutil.copy(src_file, dst_file)
print(f"copy(): {result}")  # full path of destination

# Copy file content only (no metadata)
dst_file2 = os.path.join(EXAMPLE_DIR, "copy2.txt")
result = shutil.copyfile(src_file, dst_file2)
print(f"copyfile(): {result}")

# Copy with file object
src_obj = os.path.join(EXAMPLE_DIR, "copy_obj.txt")
shutil.copyfileobj(open(src_file, "rb"), open(src_obj, "wb"))
print(f"copyfileobj(): {src_obj}")

# Copy file mode and metadata only (not content)
dst_meta = os.path.join(EXAMPLE_DIR, "copy_meta.txt")
with open(dst_meta, "w") as f:
    f.write("Different content")
shutil.copystat(src_file, dst_meta)
print(f"copystat(): metadata copied to {dst_meta}")

print("=" * 5, "Copying directories", "=" * 5)

# Create a source directory structure
src_dir = os.path.join(EXAMPLE_DIR, "source_dir")
os.makedirs(src_dir, exist_ok=True)
os.makedirs(os.path.join(src_dir, "subdir"), exist_ok=True)
with open(os.path.join(src_dir, "file1.txt"), "w") as f:
    f.write("File 1 content")
with open(os.path.join(src_dir, "subdir", "file2.txt"), "w") as f:
    f.write("File 2 content")

# Copy entire directory tree
dst_dir = os.path.join(EXAMPLE_DIR, "dest_dir")
if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
result = shutil.copytree(src_dir, dst_dir)
print(f"copytree(): {result}")

# Verify the copy
for root, dirs, files in os.walk(dst_dir):
    for f in files:
        filepath = os.path.join(root, f)
        print(f"  Copied: {os.path.relpath(filepath, EXAMPLE_DIR)}")

# copytree with ignore pattern
dst_dir2 = os.path.join(EXAMPLE_DIR, "dest_dir2")
if os.path.exists(dst_dir2):
    shutil.rmtree(dst_dir2)
shutil.copytree(src_dir, dst_dir2, ignore=shutil.ignore_patterns("*.txt"))
print(f"copytree with ignore: {os.listdir(dst_dir2)}")  # only subdirectory remains

# copytree with dirs_exist_ok (Python 3.8+)
dst_dir3 = os.path.join(EXAMPLE_DIR, "dest_dir3")
os.makedirs(dst_dir3, exist_ok=True)
shutil.copytree(src_dir, dst_dir3, dirs_exist_ok=True)
print(f"copytree dirs_exist_ok: files copied into existing dir")

print("=" * 5, "Moving and renaming", "=" * 5)

# Move a file
move_src = os.path.join(EXAMPLE_DIR, "to_move.txt")
with open(move_src, "w") as f:
    f.write("I will be moved")
move_dst = os.path.join(EXAMPLE_DIR, "moved.txt")
result = shutil.move(move_src, move_dst)
print(f"move(): {result}")  # new path
print(f"Original exists: {os.path.exists(move_src)}")  # False
print(f"Moved exists: {os.path.exists(move_dst)}")  # True

# Move into a directory
move_src2 = os.path.join(EXAMPLE_DIR, "to_move2.txt")
with open(move_src2, "w") as f:
    f.write("I will be moved into a dir")
result = shutil.move(move_src2, dst_dir)
print(f"move into dir: {result}")

# Rename is same as move for files on same filesystem
rename_src = os.path.join(EXAMPLE_DIR, "to_rename.txt")
with open(rename_src, "w") as f:
    f.write("I will be renamed")
rename_dst = os.path.join(EXAMPLE_DIR, "renamed.txt")
os.rename(rename_src, rename_dst)
print(f"rename(): {rename_dst}")

print("=" * 5, "Removing directories", "=" * 5)

# Remove a directory tree
rm_dir = os.path.join(EXAMPLE_DIR, "to_remove")
os.makedirs(os.path.join(rm_dir, "nested"), exist_ok=True)
with open(os.path.join(rm_dir, "nested", "file.txt"), "w") as f:
    f.write("content")
print(f"Before rmtree: {os.path.exists(rm_dir)}")  # True

shutil.rmtree(rm_dir)
print(f"After rmtree: {os.path.exists(rm_dir)}")  # False

# rmtree with ignore_errors
rm_dir2 = os.path.join(EXAMPLE_DIR, "to_remove2")
os.makedirs(rm_dir2, exist_ok=True)
shutil.rmtree(rm_dir2, ignore_errors=True)
print(f"rmtree with ignore_errors: {not os.path.exists(rm_dir2)}")  # True

# Remove single file (use os.remove, not shutil)
rm_file = os.path.join(EXAMPLE_DIR, "to_remove.txt")
with open(rm_file, "w") as f:
    f.write("bye")
os.remove(rm_file)
print(f"File removed: {not os.path.exists(rm_file)}")  # True

# Remove empty directory (use os.rmdir, not shutil)
rm_empty = os.path.join(EXAMPLE_DIR, "empty_dir")
os.makedirs(rm_empty, exist_ok=True)
os.rmdir(rm_empty)
print(f"Empty dir removed: {not os.path.exists(rm_empty)}")  # True

print("=" * 5, "Disk usage", "=" * 5)

# Get disk usage statistics
usage = shutil.disk_usage(EXAMPLE_DIR)
print(f"Total: {usage.total / (1024**3):.1f} GB")
print(f"Used: {usage.used / (1024**3):.1f} GB")
print(f"Free: {usage.free / (1024**3):.1f} GB")

print("=" * 5, "File permissions and ownership", "=" * 5)

# Get file mode bits
mode = os.stat(src_file).st_mode
print(f"File mode: {oct(mode)}")  # e.g., 0o100644

# Copy mode bits
shutil.copymode(src_file, dst_file)
print(f"Mode copied from source to destination")

# Get file size
size = os.path.getsize(src_file)
print(f"Source file size: {size} bytes")

print("=" * 5, "Which: finding executables", "=" * 5)

# Find executable in PATH
python_path = shutil.which("python")
print(f"python: {python_path}")

pip_path = shutil.which("pip")
print(f"pip: {pip_path}")

# Find with specific extension (Windows)
notepad = shutil.which("notepad")
print(f"notepad: {notepad}")

# Return None if not found
missing = shutil.which("nonexistent_program_xyz")
print(f"nonexistent: {missing}")  # None

print("=" * 5, "Archive operations", "=" * 5)

# Create a ZIP archive
archive_src = os.path.join(EXAMPLE_DIR, "source_dir")
archive_path = os.path.join(EXAMPLE_DIR, "archive")
result = shutil.make_archive(archive_path, "zip", root_dir=EXAMPLE_DIR, base_dir="source_dir")
print(f"Created archive: {result}")

# List supported archive formats
print(f"Archive formats: {shutil.get_archive_formats()}")

# List supported unpack formats
print(f"Unpack formats: {shutil.get_unpack_formats()}")

# Unpack an archive
unpack_dir = os.path.join(EXAMPLE_DIR, "unpacked")
os.makedirs(unpack_dir, exist_ok=True)
shutil.unpack_archive(result, unpack_dir)
print(f"Unpacked to: {unpack_dir}")

# Verify unpacked content
for root, dirs, files in os.walk(unpack_dir):
    for f in files:
        filepath = os.path.join(root, f)
        print(f"  Unpacked: {os.path.relpath(filepath, unpack_dir)}")

print("=" * 5, "Cleanup", "=" * 5)

# Remove the entire examples directory
shutil.rmtree(EXAMPLE_DIR)
print(f"Cleaned up: {not os.path.exists(EXAMPLE_DIR)}")  # True