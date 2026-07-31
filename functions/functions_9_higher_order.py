# Higher-order functions: functions that take other functions as arguments or return functions

print("=" * 5, "Functions as first-class citizens", "=" * 5)

# Assigning a function to a variable
def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # function assigned to a variable
print(say_hello("Alice"))  # Hello, Alice!

# Passing a function as an argument
def apply(func, value):
    return func(value)

print(apply(str.upper, "hello"))  # HELLO
print(apply(len, "hello"))  # 5

# Returning a function from another function
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
print(make_multiplier(10)(4))  # 40

print("=" * 5, "map, filter, reduce", "=" * 5)

# map() applies a function to every item
numbers = [1, 2, 3, 4, 5]

# Using lambda with map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Using named function with map
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

temps_c = [0, 10, 20, 30, 40]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
print(temps_f)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# map with multiple iterables
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
combined = list(map(lambda a, b: a + b, nums1, nums2))
print(combined)  # [11, 22, 33]

# map with None to zip-like behavior (Python 2 style, not in Python 3)
# Use zip() instead
pairs = list(zip(nums1, nums2))
print(pairs)  # [(1, 10), (2, 20), (3, 30)]

# filter() selects items that match a condition
numbers = range(1, 21)

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Filter positive numbers
mixed = [-5, -3, 0, 1, 4, -2, 7]
positives = list(filter(lambda x: x > 0, mixed))
print(positives)  # [1, 4, 7]

# filter with None removes falsy values
data = [0, "", None, 1, "hello", [], [1, 2], False, True]
truthy = list(filter(None, data))
print(truthy)  # [1, 'hello', [1, 2], True]

# reduce() from functools
from functools import reduce

# Sum using reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)  # 15

# Product using reduce
product = reduce(lambda a, b: a * b, numbers)
print(product)  # 120

# reduce with initial value
total_with_init = reduce(lambda a, b: a + b, numbers, 100)
print(total_with_init)  # 115

# Find maximum using reduce
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)  # 5

# Flatten a list of lists using reduce
lists = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, lists)
print(flat)  # [1, 2, 3, 4, 5, 6]

print("=" * 5, "sorted with key function", "=" * 5)

# Sort by key function
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95},
]

# Sort by grade (ascending)
by_grade = sorted(students, key=lambda s: s["grade"])
print([s["name"] for s in by_grade])  # ['Charlie', 'Alice', 'Bob', 'Diana']

# Sort by grade (descending)
by_grade_desc = sorted(students, key=lambda s: s["grade"], reverse=True)
print([s["name"] for s in by_grade_desc])  # ['Diana', 'Bob', 'Alice', 'Charlie']

# Sort by name length
by_name_len = sorted(students, key=lambda s: len(s["name"]))
print([s["name"] for s in by_name_len])  # ['Bob', 'Alice', 'Diana', 'Charlie']

print("=" * 5, "Function composition", "=" * 5)

# Composing functions together
def compose(*functions):
    """Compose multiple functions right-to-left."""
    def composed(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result
    return composed

add_one = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

# double(square(add_one(3))) = double(square(4)) = double(16) = 32
composed = compose(double, square, add_one)
print(composed(3))  # 32

# Pipe functions left-to-right
def pipe(*functions):
    """Pipe multiple functions left-to-right."""
    def piped(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    return piped

# add_one(3) = 4 → square(4) = 16 → double(16) = 32
piped = pipe(add_one, square, double)
print(piped(3))  # 32

print("=" * 5, "Partial application with functools.partial", "=" * 5)

from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a square function from power
square = partial(power, exponent=2)
print(square(5))  # 25

# Create a cube function from power
cube = partial(power, exponent=3)
print(cube(3))  # 27

# Partial with built-in functions
from decimal import Decimal, ROUND_HALF_UP

# Create a round_to function with fixed decimal places
round_to_2 = partial(round, ndigits=2)
print(round_to_2(3.14159))  # 3.14

# Partial for string formatting
greet_formal = partial("Good morning, {}!".format)
greet_casual = partial("Hey, {}!".format)

print(greet_formal("Alice"))  # Good morning, Alice!
print(greet_casual("Bob"))  # Hey, Bob!

print("=" * 5, "Currying", "=" * 5)

# Manual currying: transforming a multi-argument function into a chain of single-argument functions
def curry_add(a):
    def inner(b):
        return a + b
    return inner

add_5 = curry_add(5)
print(add_5(3))  # 8
print(add_5(10))  # 15

# Generic curry for two-argument functions
def curry(func):
    def curried(a):
        def inner(b):
            return func(a, b)
        return inner
    return curried

@curry
def multiply(a, b):
    return a * b

double = multiply(2)
triple = multiply(3)
print(double(5))  # 10
print(triple(5))  # 15