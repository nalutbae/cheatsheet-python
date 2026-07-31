# Utility module used by other modules_9 examples
# This file is imported by modules_1_basics.py

"""Custom utility module for demonstrating module imports.
This module provides basic math functions and a Calculator class.
"""

PI = 3.14159
VERSION = "1.0.0"

# __all__ controls what 'from modules_9_util import *' imports
__all__ = ["add", "multiply", "greet"]


def add(a, b):
    """Add two numbers."""
    return a + b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"


class Calculator:
    """A simple calculator class."""

    def __init__(self, initial=0):
        self.value = initial

    def add(self, x):
        self.value += x
        return self.value

    def subtract(self, x):
        self.value -= x
        return self.value

    def multiply(self, x):
        self.value *= x
        return self.value

    def divide(self, x):
        if x == 0:
            raise ValueError("Cannot divide by zero")
        self.value /= x
        return self.value

    def reset(self):
        self.value = 0
        return self.value

    def __repr__(self):
        return f"Calculator(value={self.value})"


def _private_helper(x):
    """A private function (convention: underscore prefix)."""
    return x * 2


# Code that runs when the module is executed directly
if __name__ == "__main__":
    print(f"modules_9_util version {VERSION}")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"multiply(4, 5) = {multiply(4, 5)}")
    print(f"greet('World') = {greet('World')}")
    calc = Calculator(10)
    print(f"Calculator: {calc.add(5)}")