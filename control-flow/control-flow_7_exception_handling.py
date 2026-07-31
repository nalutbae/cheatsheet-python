# Exception handling with try-except-else-finally

# Basic try-except
try:
    result = 10 / 2
    print(result)  # 5.0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catching specific exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: division by zero")  # Error: division by zero
except TypeError:
    print("Error: type mismatch")

# Multiple exceptions in one except clause
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")  # Conversion error: invalid literal for int() with base 10: 'abc'

# Catching any exception
try:
    lst = [1, 2, 3]
    print(lst[10])
except Exception as e:
    print(f"An error occurred: {e}")  # An error occurred: list index out of range

# try-except-else: else runs only if no exception occurs
try:
    num = int("42")
except ValueError:
    print("Not a valid number")
else:
    print(f"Valid number: {num}")  # Valid number: 42

# try-except-finally: finally always runs
try:
    f = open("/dev/null", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup code runs here")  # Cleanup code runs here

# Complete try-except-else-finally
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Division attempt completed")

print(safe_divide(10, 2))
# Result: 5.0
# Division attempt completed
# 5.0

print(safe_divide(10, 0))
# Cannot divide by zero
# Division attempt completed
# None

# Raising exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise ValueError("Must be 18 or older")
    return "Access granted"

try:
    print(check_age(25))  # Access granted
except ValueError as e:
    print(f"Error: {e}")

try:
    print(check_age(-5))
except ValueError as e:
    print(f"Error: {e}")  # Error: Age cannot be negative

# Re-raising exceptions
def process_data(data):
    try:
        if not data:
            raise ValueError("Empty data")
        return data.upper()
    except ValueError:
        print("Logging error in process_data")
        raise  # re-raise the same exception

try:
    process_data("")
except ValueError as e:
    print(f"Caught at outer level: {e}")
# Logging error in process_data
# Caught at outer level: Empty data

# Custom exception classes
class InvalidScoreError(Exception):
    """Exception raised for invalid test scores."""
    def __init__(self, score, message="Score must be between 0 and 100"):
        self.score = score
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (got {self.score})"

def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(score)
    return score

try:
    validate_score(150)
except InvalidScoreError as e:
    print(f"Error: {e}")  # Error: Score must be between 0 and 100 (got 150)

# Exception hierarchy
# BaseException
#   ├── SystemExit
#   ├── KeyboardInterrupt
#   ├── GeneratorExit
#   └── Exception
#       ├── StopIteration
#       ├── ArithmeticError
#       │   ├── FloatingPointError
#       │   ├── OverflowError
#       │   └── ZeroDivisionError
#       ├── LookupError
#       │   ├── IndexError
#       │   └── KeyError
#       ├── TypeError
#       ├── ValueError
#       ├── AttributeError
#       ├── FileNotFoundError
#       └── ...

# Common built-in exceptions
exceptions_demo = [
    (lambda: 1 / 0, ZeroDivisionError),
    (lambda: [1, 2][5], IndexError),
    (lambda: {"a": 1}["b"], KeyError),
    (lambda: int("abc"), ValueError),
    (lambda: None.value, AttributeError),
    (lambda: "2" + 2, TypeError),
]

for func, expected in exceptions_demo:
    try:
        func()
    except expected as e:
        print(f"Caught {expected.__name__}: {e}")
# Caught ZeroDivisionError: division by zero
# Caught IndexError: list index out of range
# Caught KeyError: 'b'
# Caught ValueError: invalid literal for int() with base 10: 'abc'
# Caught AttributeError: 'NoneType' object has no attribute 'value'
# Caught TypeError: can only concatenate str (not "int") to str

# assert statement
def calculate_average(numbers):
    assert len(numbers) > 0, "Cannot calculate average of empty list"
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))  # 20.0

try:
    calculate_average([])
except AssertionError as e:
    print(f"Assertion failed: {e}")  # Assertion failed: Cannot calculate average of empty list