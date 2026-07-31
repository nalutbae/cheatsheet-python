# Standard input with input()

# Basic input: reads a line from stdin as a string
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# input() always returns a string — convert for other types
# age_str = input("Enter your age: ")
# age = int(age_str)
# print(f"You will be {age + 1} next year.")

# Reading a number directly
# height = float(input("Enter your height in cm: "))
# print(f"Your height is {height} cm.")

# Multiple values on one line (space-separated)
# line = input("Enter two numbers separated by space: ")
# a, b = map(int, line.split())
# print(f"Sum: {a + b}")

# Multiple values with specific delimiter
# line = input("Enter name,age,city (comma-separated): ")
# name, age, city = line.split(",")
# print(f"Name: {name}, Age: {age}, City: {city}")

# Reading a list of integers
# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# print(f"Numbers: {nums}, Sum: {sum(nums)}")

# Validating input with try-except
# while True:
#     try:
#         value = int(input("Enter a positive integer: "))
#         if value <= 0:
#             raise ValueError("Must be positive")
#         break
#     except ValueError as e:
#         print(f"Invalid input: {e}")
# print(f"You entered: {value}")

# Reading until a sentinel value
# lines = []
# while True:
#     line = input("Enter text (or 'quit' to finish): ")
#     if line == "quit":
#         break
#     lines.append(line)
# print(f"You entered {len(lines)} lines: {lines}")

# Password input (hidden characters) — use getpass module
# from getpass import getpass
# password = getpass("Enter password: ")
# print("Password received (length: {})".format(len(password)))

# Reading with a timeout hint
# import sys
# if sys.stdin.isatty():
#     answer = input("Continue? (y/n): ")
# else:
#     answer = "y"  # default when piped

print("=" * 5, "sys.stdin for bulk reading", "=" * 5)

import sys

# Read all input at once (useful for piped input)
# all_input = sys.stdin.read()

# Read line by line (useful for piped input)
# for line in sys.stdin:
#     print(line.strip())

# Read one line
# line = sys.stdin.readline().strip()

# Read N lines
# n = int(sys.stdin.readline())
# lines = [sys.stdin.readline().strip() for _ in range(n)]

# Demonstrating with in-memory string (for testing without real input)
from io import StringIO

test_input = StringIO("Hello\nWorld\nPython\n")
line1 = test_input.readline().strip()
line2 = test_input.readline().strip()
line3 = test_input.readline().strip()
print(line1)  # Hello
print(line2)  # World
print(line3)  # Python

print("=" * 5, "Interactive menu pattern", "=" * 5)

# Common pattern: interactive menu with input()
def show_menu():
    print("\n=== Menu ===")
    print("1. Add item")
    print("2. View items")
    print("3. Delete item")
    print("0. Exit")

# Uncomment to run interactively:
# items = []
# while True:
#     show_menu()
#     choice = input("Select: ").strip()
#     if choice == "1":
#         item = input("Enter item name: ")
#         items.append(item)
#         print(f"Added: {item}")
#     elif choice == "2":
#         for i, item in enumerate(items, 1):
#             print(f"  {i}. {item}")
#     elif choice == "3":
#         idx = int(input("Enter item number: ")) - 1
#         if 0 <= idx < len(items):
#             removed = items.pop(idx)
#             print(f"Removed: {removed}")
#     elif choice == "0":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice")