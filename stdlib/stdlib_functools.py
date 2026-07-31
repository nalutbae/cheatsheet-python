# functools: higher-order functions and operations on callables

from functools import reduce, partial, wraps, lru_cache, total_ordering
from functools import singledispatch, cached_property
from typing import Any

print("=" * 5, "reduce: cumulative operations", "=" * 5)

# Sum all elements
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum via reduce: {total}")  # 15

# Product of all elements
product = reduce(lambda x, y: x * y, numbers)
print(f"Product via reduce: {product}")  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Max via reduce: {maximum}")  # 5

# With initializer
total_with_init = reduce(lambda x, y: x + y, numbers, 100)
print(f"Sum with init 100: {total_with_init}")  # 115

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda acc, lst: acc + lst, nested)
print(f"Flattened: {flattened}")  # [1, 2, 3, 4, 5, 6]

# Build a dictionary from key-value pairs
pairs = [("a", 1), ("b", 2), ("c", 3)]
result = reduce(lambda d, pair: {**d, pair[0]: pair[1]}, pairs, {})
print(f"Dict from pairs: {result}")  # {'a': 1, 'b': 2, 'c': 3}

# Empty list edge case (requires initializer)
empty_sum = reduce(lambda x, y: x + y, [], 0)
print(f"Sum of empty list: {empty_sum}")  # 0

print("=" * 5, "partial: fix some function arguments", "=" * 5)

# Basic partial: fix first argument
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(f"square(4): {square(4)}")  # 16
print(f"cube(3): {cube(3)}")  # 27

# Partial with positional arguments
def greet(greeting, name):
    return f"{greeting}, {name}!"

say_hello = partial(greet, "Hello")
say_hi = partial(greet, "Hi")
print(say_hello("Alice"))  # Hello, Alice!
print(say_hi("Bob"))  # Hi, Bob!

# Partial with built-in functions
import operator

double = partial(operator.mul, 2)
triple = partial(operator.mul, 3)
print(f"double(5): {double(5)}")  # 10
print(f"triple(5): {triple(5)}")  # 15

# Practical: configuring a logger
def log_message(level, prefix, message):
    return f"[{level}] {prefix}: {message}"

info_log = partial(log_message, "INFO", "App")
error_log = partial(log_message, "ERROR", "App")
print(info_log("Started"))  # [INFO] App: Started
print(error_log("Crashed"))  # [ERROR] App: Crashed

# Inspect partial attributes
print(f"Func: {square.func}")  # <function power>
print(f"Keywords: {square.keywords}")  # {'exponent': 2}

print("=" * 5, "lru_cache: memoization with least-recently-used cache", "=" * 5)

# Basic memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci(10): {fibonacci(10)}")  # 55
print(f"fibonacci(50): {fibonacci(50)}")  # very fast with cache

# Cache info
print(f"Cache info: {fibonacci.cache_info()}")

# Clear cache
fibonacci.cache_clear()
print(f"After clear: {fibonacci.cache_info()}")

# Expensive computation with cache
@lru_cache(maxsize=32)
def expensive_computation(n):
    """Simulate an expensive computation."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# First call: computes
result1 = expensive_computation(10000)
info1 = expensive_computation.cache_info()
print(f"First call - Hits: {info1.hits}, Misses: {info1.misses}")

# Second call: cached
result2 = expensive_computation(10000)
info2 = expensive_computation.cache_info()
print(f"Second call - Hits: {info2.hits}, Misses: {info2.misses}")

# Custom key function for unhashable types
def process_data(data_id, data_list):
    """Process data with caching by ID."""
    return sum(data_list)

# For unhashable arguments, convert to hashable key
@lru_cache(maxsize=128)
def process_sorted(data_id, data_tuple):
    """Process data with hashable key."""
    return sum(data_tuple)

result = process_sorted("batch1", tuple([1, 2, 3, 4, 5]))
print(f"Process result: {result}")  # 15

print("=" * 5, "wraps: preserving function metadata", "=" * 5)

# Without @wraps (metadata is lost)
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_function():
    """This is my function."""
    return 42

print(f"Name: {my_function.__name__}")  # wrapper (wrong!)
print(f"Doc: {my_function.__doc__}")  # None or wrapper's doc (wrong!)

# With @wraps (metadata is preserved)
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_function2():
    """This is my function."""
    return 42

print(f"Name: {my_function2.__name__}")  # my_function2 (correct!)
print(f"Doc: {my_function2.__doc__}")  # This is my function. (correct!)

# Practical: timing decorator with @wraps
import time

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"  {func.__name__} took {(end - start) * 1000:.3f}ms")
        return result
    return wrapper

@timed
def slow_add(a, b):
    """Add two numbers slowly."""
    return a + b

print(f"Name: {slow_add.__name__}")  # slow_add
print(f"Doc: {slow_add.__doc__}")  # Add two numbers slowly.
result = slow_add(1, 2)  # prints timing

print("=" * 5, "total_ordering: auto-fill comparison methods", "=" * 5)

# Without total_ordering: need to define __lt__, __le__, __gt__, __ge__
# With total_ordering: define __eq__ + one comparison, rest are auto-generated

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade == other.grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade < other.grade

    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

alice = Student("Alice", 90)
bob = Student("Bob", 85)
charlie = Student("Charlie", 90)

print(f"Alice > Bob: {alice > bob}")  # True
print(f"Alice >= Charlie: {alice >= charlie}")  # True
print(f"Bob < Alice: {bob < alice}")  # True
print(f"Bob <= Charlie: {bob <= charlie}")  # True

students = [alice, bob, charlie]
students_sorted = sorted(students)
print(f"Sorted: {students_sorted}")

print("=" * 5, "singledispatch: generic functions by type", "=" * 5)

@singledispatch
def process(value):
    """Default handler for unknown types."""
    return f"Unknown type: {type(value).__name__}"

@process.register(str)
def _(value):
    return f"String ({len(value)} chars): {value.upper()}"

@process.register(int)
def _(value):
    return f"Integer: {value:,} (hex: {value:#x})"

@process.register(float)
def _(value):
    return f"Float: {value:.4f}"

@process.register(list)
def _(value):
    return f"List ({len(value)} items): {value[:3]}..."

@process.register(dict)
def _(value):
    return f"Dict ({len(value)} keys): {list(value.keys())}"

print(process("hello"))  # String (5 chars): HELLO
print(process(42))  # Integer: 42 (hex: 0x2a)
print(process(3.14159))  # Float: 3.1416
print(process([1, 2, 3, 4, 5]))  # List (5 items): [1, 2, 3]...
print(process({"a": 1, "b": 2}))  # Dict (2 keys): ['a', 'b']
print(process(True))  # Unknown type: bool (falls through to default)

print("=" * 5, "cached_property: property cached on instance", "=" * 5)

class DataSet:
    def __init__(self, data):
        self.data = data

    @cached_property
    def sum(self):
        """Expensive computation, cached after first access."""
        print("  Computing sum...")
        return sum(self.data)

    @cached_property
    def mean(self):
        """Cached mean calculation."""
        print("  Computing mean...")
        return self.sum / len(self.data)

ds = DataSet([1, 2, 3, 4, 5])
print(f"First access to sum: {ds.sum}")  # Computing sum... 5
print(f"Second access to sum: {ds.sum}")  # 5 (cached, no recomputation)
print(f"Mean: {ds.mean}")  # Computing mean... 3.0

# cached_property can be invalidated by deleting the attribute
del ds.sum  # clear cache
print(f"After cache clear: {ds.sum}")  # Computing sum... 5