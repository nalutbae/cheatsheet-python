# Basic for loop with a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

# for loop with range()
for i in range(5):
    print(i, end=" ")
# 0 1 2 3 4

print()

# range with start, stop, step
for i in range(2, 10, 3):
    print(i, end=" ")
# 2 5 8

print()

# range counting backwards
for i in range(10, 0, -2):
    print(i, end=" ")
# 10 8 6 4 2

print()

# for loop with enumerate()
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(f"{index}: {name}")
# 0: Alice
# 1: Bob
# 2: Charlie

# enumerate with custom start index
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")
# 1: Alice
# 2: Bob
# 3: Charlie

# for loop with zip()
letters = ["a", "b", "c"]
numbers = [1, 2, 3]

for letter, number in zip(letters, numbers):
    print(f"{letter}: {number}")
# a: 1
# b: 2
# c: 3

# zip with unequal lengths (stops at the shortest)
short = [10, 20]
long = [1, 2, 3, 4, 5]

for s, l in zip(short, long):
    print(s, l)
# 10 1
# 20 2

# for loop with dictionary
person = {"name": "Alice", "age": 30, "city": "Seoul"}

# Iterate over keys
for key in person:
    print(key, end=" ")
# name age city

print()

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key} = {value}")
# name = Alice
# age = 30
# city = Seoul

# Iterate over values only
for value in person.values():
    print(value, end=" ")
# Alice 30 Seoul

print()

# Iterate over keys explicitly
for key in person.keys():
    print(key, end=" ")
# name age city

print()

# Nested for loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)

# for loop with string iteration
for ch in "Hello":
    print(ch, end="-")
# H-e-l-l-o-

print()

# for loop with break
for num in range(10):
    if num == 5:
        break
    print(num, end=" ")
# 0 1 2 3 4

print()

# for loop with continue
for num in range(10):
    if num % 2 == 0:
        continue
    print(num, end=" ")
# 1 3 5 7 9

print()

# for-else: else runs when loop completes without break
for num in range(5):
    if num == 10:
        break
else:
    print("Loop completed without break")  # Loop completed without break

# for-else: else does NOT run when break is hit
for num in range(5):
    if num == 3:
        break
else:
    print("This will not print")

print("Break was hit at num =", num)  # Break was hit at num = 3

# List comprehension (concise for loop)
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension with condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
unique_squares = {x % 3 for x in range(10)}
print(unique_squares)  # {0, 1, 2}

# Generator expression (lazy evaluation, memory efficient)
total = sum(x ** 2 for x in range(1, 6))
print(total)  # 55

# Walrus operator in for loop (Python 3.8+)
# Assigns and uses a value in the same expression
data = [1, 2, 3, 4, 5]
results = [y for x in data if (y := x * 2) > 4]
print(results)  # [6, 8, 10]