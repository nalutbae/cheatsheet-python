# break: exit the innermost loop immediately

# break in a for loop
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
# 0 1 2 3 4

print()

# break in a while loop
n = 0
while True:
    if n >= 5:
        break
    print(n, end=" ")
    n += 1
# 0 1 2 3 4

print()

# break in a nested loop only exits the inner loop
for i in range(3):
    for j in range(5):
        if j == 2:
            break  # only exits the inner loop
        print(f"({i},{j})", end=" ")
    print()
# (0,0) (0,1)
# (1,0) (1,1)
# (2,0) (2,1)

# break with for-else: else is skipped when break is executed
for num in range(10):
    if num == 7:
        print(f"Found {num}, breaking")
        break
else:
    print("Not found")
# Found 7, breaking

# for-else without break: else is executed
for num in range(3):
    pass
else:
    print("Loop completed without break")  # Loop completed without break

# Searching with break
def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None

print(find_first_even([1, 3, 4, 6]))  # 4
print(find_first_even([1, 3, 5]))  # None

print("=" * 5, "continue", "=" * 5)

# continue: skip the rest of the current iteration and move to the next

# continue in a for loop (skip even numbers)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
# 1 3 5 7 9

print()

# continue in a while loop
n = 0
while n < 10:
    n += 1
    if n % 3 == 0:
        continue
    print(n, end=" ")
# 1 2 4 5 7 8 10

print()

# continue with nested loops
for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # skip j=1
        print(f"({i},{j})", end=" ")
    print()
# (0,0) (0,2)
# (1,0) (1,2)
# (2,0) (2,2)

# Filter items using continue
words = ["apple", "", "banana", None, "cherry", "", "date"]
valid_words = []

for word in words:
    if not word:
        continue
    valid_words.append(word)

print(valid_words)  # ['apple', 'banana', 'cherry', 'date']

print("=" * 5, "pass", "=" * 5)

# pass: null operation, does nothing; used as a placeholder

# pass in an if block (placeholder for future code)
x = 10

if x > 0:
    pass  # TODO: implement positive case
else:
    print("x is not positive")

# pass in a for loop
for i in range(3):
    pass  # TODO: implement loop body

# pass in a function definition
def my_function():
    pass  # TODO: implement this function

# pass in a class definition
class MyError(Exception):
    pass  # TODO: add custom error details

# pass vs continue vs break
print("pass vs continue vs break:")
for i in range(5):
    if i == 2:
        pass    # does nothing, still prints i=2
    print(i, end=" ")
# 0 1 2 3 4

print()

for i in range(5):
    if i == 2:
        continue  # skips i=2
    print(i, end=" ")
# 0 1 3 4

print()

for i in range(5):
    if i == 2:
        break  # stops at i=2
    print(i, end=" ")
# 0 1