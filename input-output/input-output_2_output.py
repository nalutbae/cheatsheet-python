# print() and output formatting

print("=" * 5, "Basic print()", "=" * 5)

# Basic output
print("Hello, World!")  # Hello, World!

# Multiple arguments (space-separated by default)
print("Name:", "Alice", "Age:", 30)  # Name: Alice Age: 30

# Custom separator with sep
print("2025", "07", "31", sep="-")  # 2025-07-31
print("a", "b", "c", sep=", ")  # a, b, c
print("a", "b", "c", sep="")  # abc

# Custom end character (default: newline)
print("Hello", end=" ")
print("World")  # Hello World (on same line)

print("Loading", end="...")
print("Done")  # Loading...Done

# Printing to a file-like object
from io import StringIO

buffer = StringIO()
print("Hello", "World", file=buffer)
print(buffer.getvalue())  # Hello World\n

# Suppressing newline
print("Line 1", end="")
print("Line 2")  # Line 1Line 2

print("=" * 5, "f-strings (Python 3.6+)", "=" * 5)

name = "Alice"
age = 30
height = 1.75

# Basic f-string
print(f"My name is {name}")  # My name is Alice
print(f"{name} is {age} years old")  # Alice is 30 years old

# Expressions inside f-strings
print(f"2 + 3 = {2 + 3}")  # 2 + 3 = 5
print(f"{'hello'.upper()}")  # HELLO
print(f"Length of '{name}': {len(name)}")  # Length of 'Alice': 5

# Format specifiers
pi = 3.14159265
print(f"Pi: {pi:.2f}")  # Pi: 3.14
print(f"Pi: {pi:.4f}")  # Pi: 3.1416
print(f"Pi: {pi:.0f}")  # Pi: 3

# Width and alignment
print(f"{'Left':<10}|")  # Left      |
print(f"{'Right':>10}|")  #      Right|
print(f"{'Center':^10}|")  #  Center  |

# Number formatting
num = 42
print(f"Binary: {num:b}")  # Binary: 101010
print(f"Octal: {num:o}")  # Octal: 52
print(f"Hex: {num:x}")  # Hex: 2a
print(f"Hex upper: {num:X}")  # Hex upper: 2A
print(f"Padded: {num:05d}")  # Padded: 00042

# Large number formatting
big = 1000000
print(f"Comma: {big:,}")  # Comma: 1,000,000
print(f"Percent: {0.856:.1%}")  # Percent: 85.6%

# Date formatting in f-strings
from datetime import datetime
now = datetime(2025, 7, 31, 14, 30, 0)
print(f"Date: {now:%Y-%m-%d}")  # Date: 2025-07-31
print(f"Time: {now:%H:%M:%S}")  # Time: 14:30:00
print(f"DateTime: {now:%Y-%m-%d %H:%M}")  # DateTime: 2025-07-31 14:30

# Nested f-strings (Python 3.12+)
width = 10
print(f"{'Value':>{width}}")  #      Value

# Debug f-strings (Python 3.8+)
x = 42
y = [1, 2, 3]
print(f"{x = }")  # x = 42
print(f"{x + 1 = }")  # x + 1 = 43
print(f"{len(y) = }")  # len(y) = 3

print("=" * 5, "str.format() method", "=" * 5)

# Positional arguments
print("{} + {} = {}".format(2, 3, 5))  # 2 + 3 = 5

# Index-based arguments
print("{0} and {1}".format("Alice", "Bob"))  # Alice and Bob
print("{1} and {0}".format("Alice", "Bob"))  # Bob and Alice

# Named arguments
print("{name} is {age} years old".format(name="Alice", age=30))  # Alice is 30 years old

# Mixing positional and named
print("{0} is {age}".format("Alice", age=30))  # Alice is 30

# Format specifiers
print("{:.2f}".format(3.14159))  # 3.14
print("{:>10}".format("right"))  #      right
print("{:<10}".format("left"))  # left      
print("{:^10}".format("center"))  #   center  
print("{:05d}".format(42))  # 00042
print("{:,}".format(1000000))  # 1,000,000
print("{:.1%}".format(0.856))  # 85.6%

# Accessing attributes and items
from collections import OrderedDict
point = (3, 4)
print("Point: ({0[0]}, {0[1]})".format(point))  # Point: (3, 4)

print("=" * 5, "printf-style % formatting", "=" * 5)

# Old-style formatting (still supported)
print("Name: %s" % "Alice")  # Name: Alice
print("Age: %d" % 30)  # Age: 30
print("Pi: %.2f" % 3.14159)  # Pi: 3.14
print("Hex: %#x" % 255)  # Hex: 0xff

# Multiple values with tuple
print("%s is %d years old" % ("Alice", 30))  # Alice is 30 years old

# Mapping with dict
data = {"name": "Bob", "age": 25}
print("%(name)s is %(age)d" % data)  # Bob is 25

print("=" * 5, "String alignment methods", "=" * 5)

text = "Python"

print(text.ljust(20))  # Python              
print(text.rjust(20))  #               Python
print(text.center(20))  #        Python       

print(text.ljust(20, "-"))  # Python--------------
print(text.rjust(20, "-"))  # --------------Python
print(text.center(20, "-"))  # -------Python-------

# zfill: pad with leading zeros
num_str = "42"
print(num_str.zfill(5))  # 00042
print("-42".zfill(5))  # -0042

print("=" * 5, "Printing collections", "=" * 5)

# Pretty printing with pprint
from pprint import pprint

data = {
    "users": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ],
    "settings": {"theme": "dark", "lang": "en"},
}
pprint(data)
# {'settings': {'lang': 'en', 'theme': 'dark'},
#  'users': [{'age': 30, 'name': 'Alice'}, {'age': 25, 'name': 'Bob'}]}

# pprint with width control
pprint(data, width=40)
# {'settings': {'lang': 'en',
#               'theme': 'dark'},
#  'users': [{'age': 30, 'name': 'Alice'},
#            {'age': 25, 'name': 'Bob'}]}

# Printing a table
headers = ["Name", "Age", "City"]
rows = [
    ["Alice", "30", "Seoul"],
    ["Bob", "25", "Tokyo"],
    ["Charlie", "35", "London"],
]

# Simple table with f-strings
for row in [headers] + rows:
    print(f"{row[0]:<10} {row[1]:>4} {row[2]:<10}")
# Name       Age City      
# Alice       30 Seoul     
# Bob         25 Tokyo     
# Charlie     35 London