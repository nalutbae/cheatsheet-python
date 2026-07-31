# argparse: command-line argument parsing

import argparse
import sys

print("=" * 5, "Basic argument parser", "=" * 5)

# Create a simple parser
parser = argparse.ArgumentParser(
    prog="myapp",
    description="A sample application demonstrating argparse",
    epilog="Thank you for using myapp!"
)

# Positional arguments (required)
parser.add_argument("input_file", help="Input file to process")
parser.add_argument("output_file", help="Output file to write")

# Optional arguments (flags)
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("-q", "--quiet", action="store_true", help="Suppress output")
parser.add_argument("-n", "--count", type=int, default=1, help="Number of iterations")
parser.add_argument("-o", "--output-format", choices=["json", "csv", "xml"], default="json",
                    help="Output format (default: json)")

# Parse demo arguments
demo_args = ["data.txt", "result.txt", "-v", "-n", "5", "-o", "csv"]
args = parser.parse_args(demo_args)

print(f"Input file: {args.input_file}")  # data.txt
print(f"Output file: {args.output_file}")  # result.txt
print(f"Verbose: {args.verbose}")  # True
print(f"Quiet: {args.quiet}")  # False
print(f"Count: {args.count}")  # 5
print(f"Output format: {args.output_format}")  # csv

print("=" * 5, "Advanced argument types", "=" * 5)

# Integer and float arguments
parser2 = argparse.ArgumentParser()
parser2.add_argument("--port", type=int, default=8080, help="Port number")
parser2.add_argument("--ratio", type=float, default=0.5, help="Ratio (0.0 to 1.0)")
parser2.add_argument("--name", type=str, default="world", help="Name to greet")

args2 = parser2.parse_args(["--port", "9090", "--ratio", "0.75", "--name", "Alice"])
print(f"Port: {args2.port}")  # 9090
print(f"Ratio: {args2.ratio}")  # 0.75
print(f"Name: {args2.name}")  # Alice

# Boolean flags
parser3 = argparse.ArgumentParser()
parser3.add_argument("--debug", action="store_true", help="Enable debug mode")
parser3.add_argument("--no-cache", action="store_true", help="Disable caching")
parser3.add_argument("--verbose", action="count", default=0, help="Increase verbosity (-v, -vv, -vvv)")

args3 = parser3.parse_args(["--debug", "-vv"])
print(f"Debug: {args3.debug}")  # True
print(f"No cache: {args3.no_cache}")  # False
print(f"Verbosity level: {args3.verbose}")  # 2

# store_const and store_true/store_false
parser4 = argparse.ArgumentParser()
parser4.add_argument("--enable", action="store_true", help="Enable feature")
parser4.add_argument("--disable", action="store_false", dest="enabled", help="Disable feature")
parser4.add_argument("--mode", action="store_const", const="fast", default="normal")

args4 = parser4.parse_args(["--enable", "--mode"])
print(f"Enable: {args4.enable}")  # True
print(f"Enabled: {args4.enabled}")  # True (default, --disable would set to False)
print(f"Mode: {args4.mode}")  # fast

print("=" * 5, "nargs: variable number of arguments", "=" * 5)

parser5 = argparse.ArgumentParser()

# nargs='?': 0 or 1 argument (uses const if not provided)
parser5.add_argument("--config", nargs="?", const="default.cfg", default=None, help="Config file")

# nargs='+': 1 or more arguments
parser5.add_argument("files", nargs="+", help="Input files")

# nargs='*': 0 or more arguments
parser5.add_argument("--tags", nargs="*", default=[], help="Tags")

# nargs=N: exactly N arguments
parser5.add_argument("--pos", nargs=2, type=float, help="Position (x y)")

args5 = parser5.parse_args(["file1.txt", "file2.txt", "--config", "--tags", "a", "b", "c"])
print(f"Config: {args5.config}")  # default.cfg (const value)
print(f"Files: {args5.files}")  # ['file1.txt', 'file2.txt']
print(f"Tags: {args5.tags}")  # ['a', 'b', 'c']

args5b = parser5.parse_args(["file1.txt", "--pos", "1.5", "2.5"])
print(f"Position: {args5b.pos}")  # [1.5, 2.5]

print("=" * 5, "Subcommands", "=" * 5)

parser6 = argparse.ArgumentParser(prog="git-demo")
subparsers = parser6.add_subparsers(dest="command", help="Available commands")

# 'add' subcommand
add_parser = subparsers.add_parser("add", help="Add files to staging")
add_parser.add_argument("files", nargs="+", help="Files to add")
add_parser.add_argument("--all", action="store_true", help="Add all files")

# 'commit' subcommand
commit_parser = subparsers.add_parser("commit", help="Commit changes")
commit_parser.add_argument("-m", "--message", required=True, help="Commit message")
commit_parser.add_argument("-a", "--all", action="store_true", help="Commit all changes")

# 'push' subcommand
push_parser = subparsers.add_parser("push", help="Push to remote")
push_parser.add_argument("remote", nargs="?", default="origin", help="Remote name")
push_parser.add_argument("branch", nargs="?", default="main", help="Branch name")

# Parse 'add' command
args_add = parser6.parse_args(["add", "file1.txt", "file2.txt"])
print(f"Command: {args_add.command}")  # add
print(f"Files: {args_add.files}")  # ['file1.txt', 'file2.txt']

# Parse 'commit' command
args_commit = parser6.parse_args(["commit", "-m", "Initial commit", "-a"])
print(f"Command: {args_commit.command}")  # commit
print(f"Message: {args_commit.message}")  # Initial commit
print(f"All: {args_commit.all}")  # True

# Parse 'push' command
args_push = parser6.parse_args(["push", "upstream", "develop"])
print(f"Command: {args_push.command}")  # push
print(f"Remote: {args_push.remote}")  # upstream
print(f"Branch: {args_push.branch}")  # develop

print("=" * 5, "Mutually exclusive arguments", "=" * 5)

parser7 = argparse.ArgumentParser()
group = parser7.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
group.add_argument("-q", "--quiet", action="store_true", help="Quiet output")

args7 = parser7.parse_args(["--verbose"])
print(f"Verbose: {args7.verbose}")  # True
print(f"Quiet: {args7.quiet}")  # False

# Both --verbose and --quiet would cause an error:
# args7b = parser7.parse_args(["--verbose", "--quiet"])  # error: not allowed with argument

print("=" * 5, "Custom type conversion", "=" * 5)

def positive_int(value):
    """Argparse type function: positive integer."""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

def port_number(value):
    """Argparse type function: valid port number (1-65535)."""
    ivalue = int(value)
    if not (1 <= ivalue <= 65535):
        raise argparse.ArgumentTypeError(f"{value} is not a valid port number (1-65535)")
    return ivalue

parser8 = argparse.ArgumentParser()
parser8.add_argument("--workers", type=positive_int, default=4, help="Number of workers")
parser8.add_argument("--port", type=port_number, default=8080, help="Port number")

args8 = parser8.parse_args(["--workers", "8", "--port", "3000"])
print(f"Workers: {args8.workers}")  # 8
print(f"Port: {args8.port}")  # 3000

# Invalid values would raise errors:
# args8b = parser8.parse_args(["--workers", "-1"])  # error: -1 is not a positive integer

print("=" * 5, "Complete application example", "=" * 5)

def main():
    """Example: a complete CLI application."""
    parser = argparse.ArgumentParser(
        prog="data_processor",
        description="Process and analyze data files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  data_processor input.csv -o output.json
  data_processor input.csv --format csv --verbose --rows 100
  data_processor input.csv --validate --stats
        """
    )

    # Required positional argument
    parser.add_argument("input_file", help="Input data file path")

    # Optional arguments
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("-f", "--format", choices=["json", "csv", "yaml"], default="json",
                        help="Output format (default: json)")
    parser.add_argument("-n", "--rows", type=int, default=0, help="Process only N rows")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--validate", action="store_true", help="Validate input data")
    parser.add_argument("--stats", action="store_true", help="Print statistics")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without writing")
    parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                        default="INFO", help="Logging level")

    args = parser.parse_args([
        "data.csv", "-o", "result.json", "--format", "json",
        "--verbose", "--stats", "--rows", "1000"
    ])

    print(f"Input: {args.input_file}")
    print(f"Output: {args.output}")
    print(f"Format: {args.format}")
    print(f"Rows: {args.rows}")
    print(f"Verbose: {args.verbose}")
    print(f"Stats: {args.stats}")
    print(f"Dry run: {args.dry_run}")
    print(f"Log level: {args.log_level}")

main()