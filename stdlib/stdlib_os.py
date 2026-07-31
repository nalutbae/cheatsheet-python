# os: operating system interfaces

import os
import sys

print("=" * 5, "Environment variables", "=" * 5)

# Get environment variables
home = os.getenv("HOME") or os.getenv("USERPROFILE")
print(f"Home: {home}")

path = os.getenv("PATH", "")
path_dirs = path.split(os.pathsep)[:5]
print(f"PATH (first 5): {path_dirs}")

user = os.getenv("USER", os.getenv("USERNAME", "unknown"))
print(f"User: {user}")

# Set environment variable (only for current process)
os.environ["MY_VAR"] = "hello"
print(f"MY_VAR via getenv: {os.getenv('MY_VAR')}")  # hello
print(f"MY_VAR via environ: {os.environ['MY_VAR']}")  # hello

# Delete environment variable
del os.environ["MY_VAR"]
print(f"MY_VAR after delete: {os.getenv('MY_VAR')}")  # None

# Expand variables in strings
expanded = os.path.expandvars("$HOME/documents")
print(f"Expanded $HOME: {expanded}")

# Expand user home directory
user_path = os.path.expanduser("~/documents")
print(f"Expand ~/documents: {user_path}")

print("=" * 5, "Current directory and path operations", "=" * 5)

# Current working directory
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# Change directory (save and restore)
original_cwd = os.getcwd()
os.chdir(os.path.expanduser("~"))
print(f"Home directory: {os.getcwd()}")
os.chdir(original_cwd)
print(f"Back to: {os.getcwd()}")

# Path joining (use os.path.join, not string concatenation)
data_path = os.path.join("data", "raw", "file.txt")
print(f"Joined path: {data_path}")  # data/raw/file.txt (or data\raw\file.txt on Windows)

# Path splitting
dir_name = os.path.dirname("/home/user/docs/file.txt")
base_name = os.path.basename("/home/user/docs/file.txt")
print(f"Dirname: {dir_name}")  # /home/user/docs
print(f"Basename: {base_name}")  # file.txt

# Split extension
root, ext = os.path.splitext("document.pdf")
print(f"Root: {root}, Extension: {ext}")  # Root: document, Extension: .pdf

# Absolute path
abs_path = os.path.abspath(".")
print(f"Absolute path: {abs_path}")

# Normalize path (remove . and ..)
normalized = os.path.normpath("/home/user/../user/./docs")
print(f"Normalized: {normalized}")  # /home/user/docs

# Common prefix and path
prefix = os.path.commonprefix(["/home/user/docs", "/home/user/data", "/home/user/pics"])
print(f"Common prefix: {prefix}")  # /home/user/

print("=" * 5, "File and directory existence", "=" * 5)

# Check existence
print(f"Current dir exists: {os.path.exists('.')}")  # True
print(f"Nonexistent exists: {os.path.exists('/nonexistent/path')}")  # False

# Check type
print(f"Is directory: {os.path.isdir('.')}")  # True
print(f"Is file: {os.path.isfile(__file__)}")  # True

# Check accessibility
print(f"Is readable: {os.access(__file__, os.R_OK)}")  # True
print(f"Is writable: {os.access(__file__, os.W_OK)}")  # True
print(f"Is executable: {os.access(__file__, os.X_OK)}")  # depends on OS

print("=" * 5, "File information (stat)", "=" * 5)

# Get file statistics
stat = os.stat(__file__)
print(f"Size: {stat.st_size} bytes")
print(f"Last modified: {stat.st_mtime}")
print(f"Mode: {oct(stat.st_mode)}")

# File size helper
file_size = os.path.getsize(__file__)
print(f"File size: {file_size} bytes")

# Modification time
mtime = os.path.getmtime(__file__)
print(f"Modification time: {mtime}")

print("=" * 5, "Directory operations", "=" * 5)

# Create directories
test_dir = os.path.join(os.path.dirname(__file__), "stdlib_examples", "os_test")
os.makedirs(test_dir, exist_ok=True)
print(f"Created: {test_dir}")
print(f"Exists: {os.path.exists(test_dir)}")  # True

# Create nested directories
nested = os.path.join(test_dir, "level1", "level2", "level3")
os.makedirs(nested, exist_ok=True)
print(f"Nested dir created: {os.path.exists(nested)}")

# List directory contents
entries = os.listdir(test_dir)
print(f"Entries in test_dir: {entries}")

# Create test files
for name in ["file1.txt", "file2.py", "file3.csv"]:
    open(os.path.join(test_dir, name), "w").close()

entries = os.listdir(test_dir)
print(f"After creating files: {sorted(entries)}")

# Remove a file
os.remove(os.path.join(test_dir, "file3.csv"))
print(f"After removing file3.csv: {sorted(os.listdir(test_dir))}")

# Remove empty directory
os.rmdir(nested)
print(f"After rmdir: {not os.path.exists(nested)}")

# Remove directory tree
import shutil
shutil.rmtree(os.path.join(os.path.dirname(__file__), "stdlib_examples"))
print(f"Cleaned up test directory")

print("=" * 5, "Walking directory trees", "=" * 5)

# os.walk: iterate over directory tree
walk_dir = os.path.dirname(__file__)
print(f"Walking {os.path.basename(walk_dir)}:")
for root, dirs, files in os.walk(walk_dir):
    level = root.replace(walk_dir, "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = "  " * (level + 1)
    for f in files[:3]:  # limit to first 3 files per directory
        print(f"{sub_indent}{f}")
    if len(files) > 3:
        print(f"{sub_indent}... and {len(files) - 3} more files")

print("=" * 5, "Process and system information", "=" * 5)

# Process ID
print(f"PID: {os.getpid()}")  # current process ID
print(f"PPID: {os.getppid()}")  # parent process ID

# User information
print(f"UID: {os.getuid() if hasattr(os, 'getuid') else 'N/A (Windows)'}")
print(f"GID: {os.getgid() if hasattr(os, 'getgid') else 'N/A (Windows)'}")

# System information
print(f"OS name: {os.name}")  # 'nt' on Windows, 'posix' on Unix
print(f"Platform: {sys.platform}")
print(f"CPU count: {os.cpu_count()}")
print(f"Page size: {os.sysconf('SC_PAGE_SIZE') if hasattr(os, 'sysconf') else 'N/A'}")

# Load average (Unix only)
if hasattr(os, 'getloadavg'):
    load = os.getloadavg()
    print(f"Load average: {load}")
else:
    print(f"Load average: N/A (Windows)")

print("=" * 5, "Path separator constants", "=" * 5)

print(f"os.sep: {os.sep!r}")  # '/' on Unix, '\\' on Windows
print(f"os.altsep: {os.altsep!r}")  # '/' on Windows, None on Unix
print(f"os.pathsep: {os.pathsep!r}")  # ':' on Unix, ';' on Windows
print(f"os.linesep: {os.linesep!r}")  # '\n' on Unix, '\r\n' on Windows
print(f"os.curdir: {os.curdir!r}")  # '.'
print(f"os.pardir: {os.pardir!r}")  # '..'

print("=" * 5, "Executing system commands", "=" * 5)

# os.system: run a command and return exit code
exit_code = os.system("echo 'Hello from os.system'")
print(f"Exit code: {exit_code}")

# os.popen: run a command and capture output
output = os.popen("echo 'Hello from os.popen'").read()
print(f"Output: {output.strip()}")

# Platform-specific examples
if os.name == "nt":  # Windows
    print(f"Platform: Windows")
    print(f"COMSPEC: {os.getenv('COMSPEC', 'N/A')}")
else:  # Unix
    print(f"Platform: Unix")
    print(f"Shell: {os.getenv('SHELL', 'N/A')}")