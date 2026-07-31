# Ternary conditional expression (inline if-else)
# syntax: value_if_true if condition else value_if_false

# Basic ternary
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Ternary with numbers
x = 10
y = 20
max_val = x if x > y else y
print(max_val)  # 20

# Ternary with strings
score = 75
result = "Pass" if score >= 60 else "Fail"
print(result)  # Pass

# Nested ternary (use sparingly for readability)
grade = 85
letter = "A" if grade >= 90 else "B" if grade >= 80 else "C" if grade >= 70 else "D" if grade >= 60 else "F"
print(letter)  # B

# Ternary in list comprehension
numbers = range(10)
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# Ternary with function calls
def format_name(name):
    return name.upper() if name else "UNKNOWN"

print(format_name("hello"))  # HELLO
print(format_name(""))  # UNKNOWN

# Ternary with None check
value = None
result = value if value is not None else "default"
print(result)  # default

# Ternary for dictionary value selection
config = {"mode": "prod"}
mode_text = "Production" if config.get("mode") == "prod" else "Development"
print(mode_text)  # Production

# Walrus operator with ternary (Python 3.8+)
data = [1, 2, 3, 4, 5]
result = "long" if (length := len(data)) > 3 else "short"
print(f"Length: {length}, Result: {result}")  # Length: 5, Result: long

print("=" * 5, "Short-circuit evaluation", "=" * 5)

# and: returns the first falsy value or the last value
print(1 and 2 and 3)  # 3
print(0 and 2 and 3)  # 0
print("" and "hello")  # ""
print([] and "hello")  # []
print(None and 42)  # None

# or: returns the first truthy value or the last value
print(0 or 1 or 2)  # 1
print("" or "default")  # default
print(None or "fallback")  # fallback
print([] or [1, 2])  # [1, 2]
print(0 or "")  # ""

# Practical short-circuit patterns

# Default value using or
name = ""
display = name or "Anonymous"
print(display)  # Anonymous

# Conditional execution using and
count = 5
count > 0 and print("Positive count")  # Positive count

count = 0
count > 0 and print("This won't print")

# Safely accessing attributes
obj = None
result = obj and obj.value  # Returns None without error
print(result)  # None

# Chaining defaults with or
config_value = None
env_value = None
final = config_value or env_value or "default"
print(final)  # default