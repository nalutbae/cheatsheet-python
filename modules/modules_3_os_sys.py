# The os and sys modules

import os
import sys

print("=" * 5, "os module: environment and paths", "=" * 5)

# Environment variables
print(f"HOME: {os.getenv('HOME', os.getenv('USERPROFILE', 'unknown'))}")  # user home directory
print(f"PATH length: {len(os.getenv('PATH', ''))}")  # PATH variable length
print(f"OS: {os.name}")  # nt (Windows), posix (Linux/Mac)

# Current working directory
print(f"CWD: {os.getcwd()}")

# Change directory (use with caution)
original_dir = os.getcwd()
# os.chdir("/tmp")  # uncomment to change directory
# os.chdir(original_dir)  # change back

# List directory contents
print(f"CWD contents: {os.listdir('.')[:5]}...")  # first 5 items

# Path operations with os.path
path = os.path.join("folder", "subfolder", "file.txt")
print(f"Joined path: {path}")

print(f"Basename: {os.path.basename(path)}")  # file.txt
print(f"Dirname: {os.path.dirname(path)}")  # folder/subfolder
print(f"Splitext: {os.path.splitext('report.pdf')}")  # ('report', '.pdf')
print(f"Exists '.': {os.path.exists('.')}")  # True
print(f"Isdir '.': {os.path.isdir('.')}")  # True

# Create and remove directories
tmp_dir = os.path.join(os.path.dirname(__file__), "tmp_test_dir")
os.makedirs(tmp_dir, exist_ok=True)
print(f"Created dir: {os.path.exists(tmp_dir)}")  # True
os.rmdir(tmp_dir)
print(f"Removed dir: {not os.path.exists(tmp_dir)}")  # True

# Walk directory tree
for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = dirs[:2]  # limit depth for demo
    level = root.replace(".", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = " " * 2 * (level + 1)
    for f in files[:3]:
        print(f"{subindent}{f}")
    if len(files) > 3:
        print(f"{subindent}... and {len(files) - 3} more files")
    break  # only show top level for demo

print("=" * 5, "sys module: Python runtime", "=" * 5)

# Command line arguments
print(f"sys.argv: {sys.argv[:1]}")  # script name

# Python version
print(f"Python version: {sys.version}")
print(f"Python version info: {sys.version_info}")
print(f"Python major: {sys.version_info.major}")  # 3
print(f"Python minor: {sys.version_info.minor}")  # 11+

# Platform
print(f"Platform: {sys.platform}")  # win32, linux, darwin

# Module search path
print(f"sys.path entries (first 3):")
for p in sys.path[:3]:
    print(f"  {p}")

# sys.modules: currently loaded modules
loaded = list(sys.modules.keys())[:5]
print(f"Loaded modules (first 5): {loaded}")

# Maximum integer and float
print(f"Max int: {sys.maxsize}")  # platform-dependent
print(f"Float info: {sys.float_info.epsilon}")  # machine epsilon

# sys.exit() — terminates the program
# sys.exit(0)  # success
# sys.exit(1)  # failure

# Recursion limit
print(f"Recursion limit: {sys.getrecursionlimit()}")  # 1000

# Standard streams
print(f"stdin: {sys.stdin}")
print(f"stdout: {sys.stdout}")
print(f"stderr: {sys.stderr}")

print("=" * 5, "pathlib: modern path handling", "=" * 5)

from pathlib import Path

# Creating Path objects
p = Path(".")
print(f"Current path: {p.resolve()}")

# Path parts
file_path = Path("/home/user/documents/report.txt")
print(f"Parts: {file_path.parts}")  # ('/', 'home', 'user', 'documents', 'report.txt')
print(f"Name: {file_path.name}")  # report.txt
print(f"Stem: {file_path.stem}")  # report
print(f"Suffix: {file_path.suffix}")  # .txt
print(f"Parent: {file_path.parent}")  # /home/user/documents

# Path operations
new_path = Path("folder") / "subfolder" / "file.py"
print(f"Path with /: {new_path}")  # folder/subfolder/file.py

# Home directory
home = Path.home()
print(f"Home: {home}")

# Glob patterns
py_files = list(Path(".").glob("modules_*.py"))
print(f"Python files in modules/: {[f.name for f in py_files]}")

# Reading and writing
test_file = Path(__file__).parent / "tmp_pathlib_test.txt"
test_file.write_text("Hello from pathlib!\nSecond line\n")
content = test_file.read_text()
print(f"Read: {content.strip()}")
test_file.unlink()  # clean up

print("=" * 5, "os: file and process operations", "=" * 5)

# File size
this_file = os.path.getsize(__file__)
print(f"This file size: {this_file} bytes")

# File modification time
mtime = os.path.getmtime(__file__)
print(f"Modification time: {mtime}")

# Environment
print(f"Number of CPUs: {os.cpu_count()}")
print(f"Process ID: {os.getpid()}")
print(f"Current user: {os.getenv('USER', os.getenv('USERNAME', 'unknown'))}")

# Execute a command
result = os.system("echo 'Hello from os.system'")
print(f"Command exit code: {result}")