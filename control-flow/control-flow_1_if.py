# Simple if statement
x = 10

if x > 0:
    print("x is positive")  # x is positive

# if-else statement
y = -5

if y > 0:
    print("y is positive")
else:
    print("y is negative")  # y is negative

# if-elif-else statement
z = 0

if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")  # z is zero

# Multiple elif branches
grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")  # B
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Nested if statements
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")  # Positive odd number

# Checking multiple conditions with and/or
age = 25
has_id = True

if age >= 18 and has_id:
    print("Access granted")  # Access granted

if age < 13 or age > 65:
    print("Discount applies")
else:
    print("Regular price")  # Regular price

# Using not keyword
is_active = False

if not is_active:
    print("Account is inactive")  # Account is inactive

# Checking if a value is in a list
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana found")  # Banana found

if "grape" not in fruits:
    print("Grape not found")  # Grape not found

# Checking if a key exists in a dictionary
person = {"name": "Alice", "age": 30}

if "name" in person:
    print("Name key exists")  # Name key exists

if "email" not in person:
    print("Email key missing")  # Email key missing

# Truthiness in if statements
values = [0, "", None, [], {}, False, 1, "hello", [1], {"a": 1}, True]

for v in values:
    if v:
        print(f"{v!r} is truthy")
    else:
        print(f"{v!r} is falsy")

# 0 is falsy
# '' is falsy
# None is falsy
# [] is falsy
# {} is falsy
# False is falsy
# 1 is truthy
# 'hello' is truthy
# [1] is truthy
# {'a': 1} is truthy
# True is truthy

# Comparing different types
# Python 3 does not allow comparing incompatible types
# "3" > 2  # TypeError: '>' not supported between instances of 'str' and 'int'

# But numeric types can be compared
print(1 < 1.5)  # True
print(1.0 == 1)  # True
print(3 == 3 + 0j)  # True

# Chained comparisons
x = 5
print(1 < x < 10)  # True
print(1 < x > 3)  # True
print(10 < x < 20)  # False

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True  (same values)
print(a is b)  # False (different objects)
print(a is c)  # True  (same object)