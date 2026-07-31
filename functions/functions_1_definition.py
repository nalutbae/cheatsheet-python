# Function definition and basic usage

# Simple function with no parameters
def greet():
    print("Hello, World!")

greet()  # Hello, World!

# Function with one parameter
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")  # Hello, Alice!

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Function with no explicit return (returns None)
def say_hello(name):
    print(f"Hello, {name}")

value = say_hello("Bob")  # Hello, Bob
print(value)  # None

# Function with multiple return values (tuple unpacking)
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(17, 5)
print(f"Quotient: {q}, Remainder: {r}")  # Quotient: 3, Remainder: 2

# Return multiple values as a dictionary
def get_user_info():
    return {"name": "Alice", "age": 30, "city": "Seoul"}

info = get_user_info()
print(info)  # {'name': 'Alice', 'age': 30, 'city': 'Seoul'}

# Function calling another function
def double(x):
    return x * 2

def square_then_double(x):
    return double(x ** 2)

print(square_then_double(3))  # 18

# Early return pattern
def is_even(number):
    if number % 2 != 0:
        return False
    return True

print(is_even(4))  # True
print(is_even(7))  # False

# Docstrings
def calculate_area(radius):
    """Calculate the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle as a float.
    """
    import math
    return math.pi * radius ** 2

print(calculate_area(5))  # 78.53981633974483
print(calculate_area.__doc__)  # Calculate the area of a circle. ...

# type hints (Python 3.5+)
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(4, 5))  # 20

# type hints with complex types
from typing import List, Dict, Optional, Union

def process_items(items: List[int]) -> Dict[str, int]:
    return {"count": len(items), "sum": sum(items)}

print(process_items([1, 2, 3]))  # {'count': 3, 'sum': 6}

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(find_user(1))  # Alice
print(find_user(3))  # None

def parse_value(value: Union[int, str]) -> str:
    return str(value).upper()

print(parse_value(42))  # 42
print(parse_value("hello"))  # HELLO

# Function as a first-class object
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet_with(style, name):
    return style(f"Hello, {name}")

print(greet_with(shout, "Alice"))  # HELLO, ALICE
print(greet_with(whisper, "Alice"))  # hello, alice

# Storing functions in a list
operations = [shout, whisper]
for op in operations:
    print(op("Hello"))  # HELLO / hello

# Passing a function as an argument to sorted
words = ["banana", "apple", "cherry", "date"]
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)  # ['date', 'apple', 'banana', 'cherry']

sorted_by_last = sorted(words, key=lambda w: w[-1])
print(sorted_by_last)  # ['banana', 'apple', 'date', 'cherry']

# Functions are objects with attributes
def my_func():
    """This is my function."""
    pass

print(my_func.__name__)  # my_func
print(my_func.__doc__)  # This is my function.
print(type(my_func))  # <class 'function'>