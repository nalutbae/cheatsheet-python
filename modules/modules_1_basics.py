# Module basics: creating, importing, and organizing modules

import os
import sys

# Ensure this module's directory is on the path for sibling imports
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 5, "What is a module?", "=" * 5)

# A module is simply a .py file containing Python code.
# Any .py file can be imported as a module.
# The file name (without .py) becomes the module name.

# Import an entire module
import math

print(f"math.pi: {math.pi}")  # 3.141592653589793
print(f"math.sqrt(16): {math.sqrt(16)}")  # 4.0
print(f"math.ceil(3.2): {math.ceil(3.2)}")  # 4
print(f"math.floor(3.8): {math.floor(3.8)}")  # 3

# Import specific names from a module
from math import factorial, gcd

print(f"factorial(5): {factorial(5)}")  # 120
print(f"gcd(12, 8): {gcd(12, 8)}")  # 4

# Import with an alias
import math as m

print(f"m.log(100): {m.log(100):.4f}")  # 4.6052

# Import multiple names
from math import sin, cos, tan

print(f"sin(0): {sin(0)}")  # 0.0
print(f"cos(0): {cos(0)}")  # 1.0

# Import all names (not recommended for production)
from math import pi, e

print(f"pi: {pi}")  # 3.141592653589793
print(f"e: {e}")  # 2.718281828459045

print("=" * 5, "Module attributes", "=" * 5)

# Every module has special attributes
import math

print(f"Module name: {math.__name__}")  # math
print(f"Module file: {math.__file__}")  # path to math module
print(f"Module doc: {math.__doc__[:50]}...")  # first 50 chars of docstring

# List all names in a module
print(f"Number of names in math: {len(dir(math))}")  # many
print(f"Some names: {dir(math)[:10]}")  # ['__doc__', '__loader__', ...]

# Check if a module has a specific attribute
print(f"hasattr(math, 'sqrt'): {hasattr(math, 'sqrt')}")  # True
print(f"hasattr(math, 'nonexistent'): {hasattr(math, 'nonexistent')}")  # False

# Get a function by name using getattr
func = getattr(math, "sqrt")
print(f"getattr(math, 'sqrt')(25): {func(25)}")  # 5.0

print("=" * 5, "Creating and importing a custom module", "=" * 5)

# Import our custom utility module (modules_9_util.py must exist)
from modules_9_util import add, multiply, greet, Calculator

print(f"add(3, 5): {add(3, 5)}")  # 8
print(f"multiply(4, 6): {multiply(4, 6)}")  # 24
print(f"greet('Alice'): {greet('Alice')}")  # Hello, Alice!

calc = Calculator(10)
print(f"calc.add(5): {calc.add(5)}")  # 15
print(f"calc.subtract(3): {calc.subtract(3)}")  # 12
print(f"calc.multiply(2): {calc.multiply(2)}")  # 24

# Import with alias
import modules_9_util as util

print(f"util.add(1, 2): {util.add(1, 2)}")  # 3
print(f"util.PI: {util.PI}")  # 3.14159

# Check module attributes
print(f"Custom module name: {util.__name__}")  # modules_9_util
print(f"Custom module doc (first 40): {util.__doc__[:40]}...")

print("=" * 5, "Conditional import with try-except", "=" * 5)

# Try importing a module, fall back if not available
try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # pip install tomli
    except ImportError:
        tomllib = None

if tomllib:
    print("TOML support available")
else:
    print("TOML support not available")

# Import with version check
import sys

if sys.version_info >= (3, 10):
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} supports match-case")
else:
    print("Python version does not support match-case")

print("=" * 5, "Reloading a module", "=" * 5)

# When developing a module, you may need to reload it after changes
import importlib

import modules_9_util as util

# Reload the module (useful during development)
importlib.reload(util)

print(f"After reload, util.add(2, 3): {util.add(2, 3)}")  # 5

print("=" * 5, "__all__: controlling 'from module import *'", "=" * 5)

# modules_9_util.py defines __all__ = ["add", "multiply", "greet"]
# Only names listed in __all__ will be imported with 'from module import *'

from modules_9_util import *

# These are available because they are in __all__
print(f"add(10, 20): {add(10, 20)}")  # 30
print(f"multiply(3, 4): {multiply(3, 4)}")  # 12
print(f"greet('Bob'): {greet('Bob')}")  # Hello, Bob!

# Calculator is NOT in __all__, so it is not imported by 'from module import *'
# Calculator would need explicit import: from modules_9_util import Calculator