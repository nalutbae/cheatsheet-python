# Command-line arguments with sys.argv and argparse

import os
EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "sys.argv: basic command-line arguments", "=" * 5)

import sys

# sys.argv is a list of command-line arguments
# sys.argv[0] is always the script name
# sys.argv[1:] are the arguments passed to the script

# For demonstration, we simulate sys.argv
original_argv = sys.argv
sys.argv = ["my_script.py", "input.txt", "--verbose", "100"]

print(f"Script name: {sys.argv[0]}")  # my_script.py
print(f"All arguments: {sys.argv}")  # ['my_script.py', 'input.txt', '--verbose', '100']
print(f"Arguments only: {sys.argv[1:]}")  # ['input.txt', '--verbose', '100']
print(f"Argument count: {len(sys.argv) - 1}")  # 3

# Simple manual argument parsing
# if len(sys.argv) < 2:
#     print("Usage: python script.py <filename>")
#     sys.exit(1)
# filename = sys.argv[1]

sys.argv = original_argv  # restore

print("=" * 5, "argparse: structured argument parsing", "=" * 5)

import argparse

# Basic argparse example
parser1 = argparse.ArgumentParser(description="A sample program")
parser1.add_argument("filename", help="Input file to process")
parser1.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
parser1.add_argument("-n", "--count", type=int, default=1, help="Number of iterations")

# Simulate command-line arguments
args1 = parser1.parse_args(["data.txt", "-v", "-n", "5"])
print(f"Filename: {args1.filename}")  # data.txt
print(f"Verbose: {args1.verbose}")  # True
print(f"Count: {args1.count}")  # 5

# Positional arguments (required)
parser2 = argparse.ArgumentParser()
parser2.add_argument("input", help="Input file path")
parser2.add_argument("output", help="Output file path")

args2 = parser2.parse_args(["in.txt", "out.txt"])
print(f"Input: {args2.input}")  # in.txt
print(f"Output: {args2.output}")  # out.txt

# Optional arguments with defaults
parser3 = argparse.ArgumentParser()
parser3.add_argument("--host", default="localhost", help="Server hostname")
parser3.add_argument("--port", type=int, default=8080, help="Server port")
parser3.add_argument("--debug", action="store_true", help="Enable debug mode")

args3 = parser3.parse_args(["--host", "example.com", "--port", "9090"])
print(f"Host: {args3.host}")  # example.com
print(f"Port: {args3.port}")  # 9090
print(f"Debug: {args3.debug}")  # False

# Choices: restrict argument values
parser4 = argparse.ArgumentParser()
parser4.add_argument("--mode", choices=["train", "test", "validate"], default="train")
parser4.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="INFO")

args4 = parser4.parse_args(["--mode", "test", "--log-level", "DEBUG"])
print(f"Mode: {args4.mode}")  # test
print(f"Log level: {args4.log_level}")  # DEBUG

# nargs: variable number of arguments
parser5 = argparse.ArgumentParser()
parser5.add_argument("files", nargs="+", help="One or more input files")  # 1 or more
parser5.add_argument("--tags", nargs="*", help="Zero or more tags")  # 0 or more
parser5.add_argument("--optional", nargs="?", const="default", help="Optional single arg")  # 0 or 1

args5 = parser5.parse_args(["file1.txt", "file2.txt", "file3.txt", "--tags", "a", "b", "c"])
print(f"Files: {args5.files}")  # ['file1.txt', 'file2.txt', 'file3.txt']
print(f"Tags: {args5.tags}")  # ['a', 'b', 'c']

# Mutual exclusion: only one of two options
parser6 = argparse.ArgumentParser()
group = parser6.add_mutually_exclusive_group()
group.add_argument("--verbose", action="store_true", help="Verbose output")
group.add_argument("--quiet", action="store_true", help="Quiet output")

args6 = parser6.parse_args(["--verbose"])
print(f"Verbose: {args6.verbose}")  # True
print(f"Quiet: {args6.quiet}")  # False

# Subcommands (like git: git add, git commit, etc.)
parser7 = argparse.ArgumentParser()
subparsers = subparsers = parser7.add_subparsers(dest="command", help="Available commands")

# 'add' subcommand
add_parser = subparsers.add_parser("add", help="Add a file")
add_parser.add_argument("file", help="File to add")
add_parser.add_argument("--force", action="store_true", help="Force add")

# 'commit' subcommand
commit_parser = subparsers.add_parser("commit", help="Commit changes")
commit_parser.add_argument("-m", "--message", required=True, help="Commit message")
commit_parser.add_argument("-a", "--all", action="store_true", help="Commit all changes")

args7 = parser7.parse_args(["add", "test.txt", "--force"])
print(f"Command: {args7.command}")  # add
print(f"File: {args7.file}")  # test.txt
print(f"Force: {args7.force}")  # True

args8 = parser7.parse_args(["commit", "-m", "Initial commit", "-a"])
print(f"Command: {args8.command}")  # commit
print(f"Message: {args8.message}")  # Initial commit
print(f"All: {args8.all}")  # True

# Boolean flags: store_true, store_false
parser9 = argparse.ArgumentParser()
parser9.add_argument("--enable-cache", action="store_true", help="Enable caching")
parser9.add_argument("--no-cache", action="store_false", dest="use_cache", help="Disable caching")

args9 = parser9.parse_args(["--enable-cache"])
print(f"Enable cache: {args9.enable_cache}")  # True

args10 = parser9.parse_args(["--no-cache"])
print(f"Use cache: {args10.use_cache}")  # False

print("=" * 5, "stdin/stdout/stderr redirection", "=" * 5)

# Redirecting stdout to a file
stdout_path = os.path.join(EXAMPLE_DIR, "stdout_output.txt")

original_stdout = sys.stdout
with open(stdout_path, "w") as f:
    sys.stdout = f
    print("This goes to the file")
    print("And this too")
sys.stdout = original_stdout

with open(stdout_path, "r") as f:
    print(f"File contents: {f.read().strip()}")  # File contents: This goes to the file\nAnd this too

# Redirecting stderr
stderr_path = os.path.join(EXAMPLE_DIR, "stderr_output.txt")

original_stderr = sys.stderr
with open(stderr_path, "w") as f:
    sys.stderr = f
    print("This is an error message", file=sys.stderr)
sys.stderr = original_stderr

# Using contextlib.redirect_stdout (cleaner approach)
from contextlib import redirect_stdout

redirect_path = os.path.join(EXAMPLE_DIR, "redirect_output.txt")

with open(redirect_path, "w") as f:
    with redirect_stdout(f):
        print("Captured output")
        print("Multiple lines")

with open(redirect_path, "r") as f:
    print(f"Captured: {f.read().strip()}")  # Captured output\nMultiple lines