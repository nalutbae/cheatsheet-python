# Basic while loop
count = 0

while count < 5:
    print(count, end=" ")
    count += 1
# 0 1 2 3 4

print()

# while loop with a condition based on user-defined logic
total = 0
num = 1

while total < 50:
    total += num
    num += 1

print(f"Total: {total}, Num: {num}")  # Total: 55, Num: 11

# while loop with break
n = 0

while True:
    if n == 5:
        break
    print(n, end=" ")
    n += 1
# 0 1 2 3 4

print()

# while loop with continue
n = 0

while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n, end=" ")
# 1 3 5 7 9

print()

# while-else: else runs when condition becomes False (no break)
n = 0

while n < 3:
    print(n, end=" ")
    n += 1
else:
    print("| loop finished normally")
# 0 1 2 | loop finished normally

# while-else: else does NOT run when break is used
n = 0

while n < 10:
    if n == 3:
        break
    print(n, end=" ")
    n += 1
else:
    print("This will not print")

print(f"| break hit at n = {n}")  # | break hit at n = 3

# Summing numbers until a threshold
total = 0
i = 1

while total <= 100:
    total += i
    i += 1

print(f"Sum: {total}, Count: {i - 1}")  # Sum: 105, Count: 14

# Counting down
count = 5

while count > 0:
    print(count, end=" ")
    count -= 1
print("Go!")
# 5 4 3 2 1 Go!

# Using while to find first occurrence
items = [3, 7, 2, 9, 4, 7, 1]
target = 9
index = 0

while index < len(items):
    if items[index] == target:
        print(f"Found {target} at index {index}")  # Found 9 at index 3
        break
    index += 1

# Removing items from a list safely (iterate backwards)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = len(numbers) - 1

while i >= 0:
    if numbers[i] % 2 == 0:
        numbers.pop(i)
    i -= 1

print(numbers)  # [1, 3, 5, 7, 9]

# Nested while loops
i = 1

while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i}, {j})", end=" ")
        j += 1
    print()
    i += 1
# (1, 1) (1, 2) (1, 3)
# (2, 1) (2, 2) (2, 3)
# (3, 1) (3, 2) (3, 3)

# Fibonacci sequence using while
a, b = 0, 1

while a < 100:
    print(a, end=" ")
    a, b = b, a + b
# 0 1 1 2 3 5 8 13 21 34 55 89

print()

# GCD using Euclidean algorithm with while
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6
print(gcd(100, 75))  # 25

# Infinite loop pattern (use with caution)
# while True:
#     response = input("Enter 'quit' to stop: ")
#     if response == "quit":
#         break
#     print(f"You entered: {response}")