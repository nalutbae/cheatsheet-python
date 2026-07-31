# with statement (context manager)
# Ensures proper acquisition and release of resources

# File handling with 'with' (automatic close)
# Writing a file
with open("/tmp/demo_with.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Using with statement\n")
# File is automatically closed here, even if an exception occurs

# Reading a file
with open("/tmp/demo_with.txt", "r") as f:
    content = f.read()
    print(content)
# Hello, World!
# Using with statement

# Multiple context managers in one with statement
with open("/tmp/demo_with.txt", "r") as src, open("/tmp/demo_copy.txt", "w") as dst:
    dst.write(src.read())

with open("/tmp/demo_copy.txt", "r") as f:
    print(f.read())
# Hello, World!
# Using with statement

# Custom context manager using a class
class Timer:
    """A simple timer context manager."""
    import time

    def __enter__(self):
        self.start = self.time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = self.time.time()
        self.duration = self.end - self.start
        print(f"Elapsed: {self.duration:.4f} seconds")
        return False  # do not suppress exceptions

with Timer():
    total = sum(range(1000000))
    print(f"Sum: {total}")
# Sum: 499999500000
# Elapsed: 0.XXXX seconds

# Custom context manager using contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def temp_value(value):
    """A context manager that yields a value."""
    print(f"Entering: {value}")
    try:
        yield value
    finally:
        print(f"Exiting: {value}")

with temp_value(42) as v:
    print(f"Inside: {v}")
# Entering: 42
# Inside: 42
# Exiting: 42

# contextlib.suppress: ignore specified exceptions
from contextlib import suppress

# Instead of:
# try:
#     os.remove("/tmp/nonexistent_file")
# except FileNotFoundError:
#     pass

# Use suppress:
import os
with suppress(FileNotFoundError):
    os.remove("/tmp/nonexistent_file")
print("No error raised for missing file")  # No error raised for missing file

# contextlib.redirect_stdout: capture print output
from contextlib import redirect_stdout
import io

output = io.StringIO()
with redirect_stdout(output):
    print("This goes to the buffer")
    print("And this too")

captured = output.getvalue()
print(f"Captured: {captured!r}")
# Captured: 'This goes to the buffer\nAnd this too\n'

# Lock simulation (thread-safe resource access)
class Lock:
    """A simple lock context manager for demonstration."""
    def __init__(self):
        self._locked = False

    def __enter__(self):
        if self._locked:
            raise RuntimeError("Lock is already held")
        self._locked = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._locked = False
        return False

lock = Lock()

with lock:
    print("Doing work with lock held")  # Doing work with lock held
    # lock is released automatically when leaving the block

print(f"Lock released: {not lock._locked}")  # Lock released: True

# Database-like transaction pattern
class Transaction:
    """A simple transaction context manager."""
    def __init__(self):
        self.committed = False

    def __enter__(self):
        print("Begin transaction")
        return self

    def commit(self):
        self.committed = True
        print("Transaction committed")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.committed:
            print("Transaction rolled back")
        return False

# Successful transaction
with Transaction() as tx:
    print("Performing operations...")
    tx.commit()
# Begin transaction
# Performing operations...
# Transaction committed

# Failed transaction (exception causes rollback)
try:
    with Transaction() as tx:
        print("Performing operations...")
        raise ValueError("Something went wrong")
except ValueError:
    pass
# Begin transaction
# Performing operations...
# Transaction rolled back