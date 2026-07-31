# traceback: stack trace extraction and formatting

import traceback
import sys
import os

print("=" * 5, "Basic exception traceback", "=" * 5)

# Generate a traceback and capture it
def inner_function():
    x = 1 / 0  # ZeroDivisionError

def middle_function():
    return inner_function()

def outer_function():
    return middle_function()

try:
    outer_function()
except ZeroDivisionError:
    # Method 1: traceback.print_exc() prints to stderr
    print("Method 1: traceback.format_exc() returns string:")
    tb_str = traceback.format_exc()
    print(tb_str)

print("=" * 5, "Extracting traceback information", "=" * 5)

def risky_divide(a, b):
    return a / b

try:
    result = risky_divide(10, 0)
except ZeroDivisionError:
    # traceback.format_exc: get traceback as string
    formatted = traceback.format_exc()
    print(f"format_exc:\n{formatted}")

    # traceback.extract_tb: extract raw frame info
    exc_type, exc_value, exc_tb = sys.exc_info()
    if exc_tb is not None:
        extracted = traceback.extract_tb(exc_tb)
        print(f"extract_tb frames: {len(extracted)}")
        for frame in extracted:
            print(f"  File {frame.filename}, line {frame.lineno}, in {frame.name}")
            print(f"    {frame.line}")

    # traceback.format_exception: format all parts
    exc_type, exc_value, exc_tb = sys.exc_info()
    if exc_tb is not None:
        lines = traceback.format_exception(exc_type, exc_value, exc_tb)
        print(f"format_exception returns {len(lines)} sections")

print("=" * 5, "traceback.print_exc vs format_exc", "=" * 5)

def demonstrate_traceback_methods():
    try:
        values = [1, 2, 3]
        return values[10]  # IndexError
    except IndexError:
        # format_exc: returns traceback as string
        tb_string = traceback.format_exc()
        print("format_exc returns string:")
        print(tb_string)

        # format_exception: returns list of strings
        exc_type, exc_value, exc_tb = sys.exc_info()
        if exc_tb is not None:
            lines = traceback.format_exception(exc_type, exc_value, exc_tb)
            print(f"format_exception returns {len(lines)} lines")

        # extract_stack: get current stack without exception
        stack = traceback.extract_stack()
        print(f"extract_stack: {len(stack)} frames")

demonstrate_traceback_methods()

print("=" * 5, "Custom error formatting", "=" * 5)

def safe_execute(func, *args, **kwargs):
    """Execute a function with detailed error reporting."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        exc_type, exc_value, exc_tb = sys.exc_info()
        if exc_tb is not None:
            # Get the deepest frame (where the error occurred)
            tb_entries = traceback.extract_tb(exc_tb)
            if tb_entries:
                last_frame = tb_entries[-1]
                error_info = {
                    "type": exc_type.__name__,
                    "message": str(exc_value),
                    "file": os.path.basename(last_frame.filename),
                    "line": last_frame.lineno,
                    "function": last_frame.name,
                    "code": last_frame.line,
                }
                print(f"Error: {error_info['type']}: {error_info['message']}")
                print(f"  Location: {error_info['file']}:{error_info['line']} in {error_info['function']}")
                print(f"  Code: {error_info['code']}")
            return None

def faulty_function():
    data = {"key": "value"}
    return data["nonexistent_key"]  # KeyError

result = safe_execute(faulty_function)

print("=" * 5, "Stack trace without exception", "=" * 5)

def function_a():
    return function_b()

def function_b():
    return function_c()

def function_c():
    # Get current call stack (no exception needed)
    stack = traceback.extract_stack()
    print(f"Call stack depth: {len(stack)} frames")
    for i, frame in enumerate(stack):
        print(f"  {i}: {frame.name} at line {frame.lineno} in {os.path.basename(frame.filename)}")
    return stack

stack = function_a()

print("=" * 5, "Walking the traceback", "=" * 5)

def level_3():
    return 1 / 0

def level_2():
    return level_3()

def level_1():
    return level_2()

try:
    level_1()
except ZeroDivisionError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    if exc_tb is not None:
        print("Walking traceback frames:")
        tb = exc_tb
        depth = 0
        while tb is not None:
            frame = tb.tb_frame
            code = frame.f_code
            print(f"  Frame {depth}: {code.co_name} at {os.path.basename(code.co_filename)}:{tb.tb_lineno}")
            # Show local variables
            locals_snapshot = frame.f_locals
            if locals_snapshot:
                print(f"    Locals: {list(locals_snapshot.keys())}")
            tb = tb.tb_next
            depth += 1

print("=" * 5, "Logging exceptions", "=" * 5)

import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s', force=True)

def log_exception_example():
    try:
        result = int("not a number")
    except ValueError:
        # Log the full traceback
        logging.error("Failed to convert string to int", exc_info=True)

        # Or log just the error message
        logging.error(f"Error message only: {traceback.format_exc().splitlines()[-1]}")

log_exception_example()

print("=" * 5, "Chained exceptions", "=" * 5)

def parse_data(data):
    try:
        return int(data)
    except ValueError as e:
        raise TypeError(f"Invalid data type: {data!r}") from e

try:
    parse_data("abc")
except TypeError:
    tb_str = traceback.format_exc()
    print("Chained exception traceback:")
    print(tb_str)

# Explicitly suppressed context
def parse_data_suppressed(data):
    try:
        return int(data)
    except ValueError:
        raise TypeError(f"Invalid data: {data!r}") from None

try:
    parse_data_suppressed("abc")
except TypeError:
    tb_str = traceback.format_exc()
    print("Suppressed context:")
    print(tb_str)

print("=" * 5, "traceback utility functions", "=" * 5)

# print_list: format a list of FrameSummary objects
frames = [
    traceback.FrameSummary("file1.py", 10, "func_a", line="x = 1"),
    traceback.FrameSummary("file2.py", 20, "func_b", line="y = x + 1"),
    traceback.FrameSummary("file3.py", 30, "func_c", line="z = y / 0"),
]
formatted = traceback.format_list(frames)
print("format_list:")
for line in formatted:
    print(f"  {line.rstrip()}")

# print_tb: format a traceback object
try:
    raise ValueError("test error for print_tb")
except ValueError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    if exc_tb is not None:
        tb_lines = traceback.format_tb(exc_tb)
        print(f"format_tb: {len(tb_lines)} frame(s)")

# format_exception_only: format just the exception type and message
try:
    raise RuntimeError("Something went wrong")
except RuntimeError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    exc_only = traceback.format_exception_only(exc_type, exc_value)
    print(f"Exception only: {''.join(exc_only).strip()}")

print("=" * 5, "Practical: custom exception reporter", "=" * 5)

class ExceptionReporter:
    """Custom exception reporter with detailed formatting."""

    def __init__(self, max_depth=None, include_locals=False):
        self.max_depth = max_depth
        self.include_locals = include_locals

    def report(self, exc_type, exc_value, exc_tb):
        """Generate a detailed exception report."""
        lines = []
        lines.append("=" * 60)
        lines.append("EXCEPTION REPORT")
        lines.append("=" * 60)
        lines.append(f"Type: {exc_type.__name__}")
        lines.append(f"Message: {exc_value}")
        lines.append("")

        if exc_tb is not None:
            lines.append("Traceback (most recent call last):")
            tb = exc_tb
            depth = 0
            while tb is not None and (self.max_depth is None or depth < self.max_depth):
                frame = tb.tb_frame
                code = frame.f_code
                lines.append(f'  File "{code.co_filename}", line {tb.tb_lineno}, in {code.co_name}')
                lines.append(f"    {code.co_linecount} lines in function" if hasattr(code, 'co_linecount') else f"    {frame.f_locals.get('__name__', '???')}")
                if self.include_locals:
                    locals_dict = {k: repr(v) for k, v in frame.f_locals.items() if not k.startswith('__')}
                    if locals_dict:
                        lines.append(f"    Locals: {locals_dict}")
                tb = tb.tb_next
                depth += 1

        lines.append("=" * 60)
        return "\n".join(lines)

def deep_function(depth=0):
    if depth >= 3:
        return 1 / 0
    return deep_function(depth + 1)

try:
    deep_function()
except Exception:
    exc_type, exc_value, exc_tb = sys.exc_info()
    reporter = ExceptionReporter(max_depth=5, include_locals=False)
    report = reporter.report(exc_type, exc_value, exc_tb)
    print(report)