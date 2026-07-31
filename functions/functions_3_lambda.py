# Lambda functions: small anonymous functions defined with the lambda keyword
# Syntax: lambda arguments: expression

# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Lambda with default argument
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!

# Lambda with conditional expression
classify = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
print(classify(5))  # positive
print(classify(-3))  # negative
print(classify(0))  # zero

print("=" * 5, "Lambda with built-in functions", "=" * 5)

# sorted() with lambda key
words = ["banana", "apple", "cherry", "date"]
sorted_by_len = sorted(words, key=lambda w: len(w))
print(sorted_by_len)  # ['date', 'apple', 'banana', 'cherry']

sorted_by_last_char = sorted(words, key=lambda w: w[-1])
print(sorted_by_last_char)  # ['banana', 'apple', 'date', 'cherry']

# sort in reverse
sorted_desc = sorted(words, key=lambda w: len(w), reverse=True)
print(sorted_desc)  # ['banana', 'cherry', 'apple', 'date']

# map() with lambda
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# map with multiple iterables
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
sums = list(map(lambda a, b: a + b, nums1, nums2))
print(sums)  # [11, 22, 33]

# filter() with lambda
numbers = range(1, 21)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# filter with string condition
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)  # ['banana', 'cherry', 'elderberry']

# reduce() with lambda
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)  # 15

product = reduce(lambda a, b: a * b, numbers)
print(product)  # 120

# reduce with initial value
total_with_init = reduce(lambda a, b: a + b, numbers, 100)
print(total_with_init)  # 115

# Finding max with reduce
max_val = reduce(lambda a, b: a if a > b else b, numbers)
print(max_val)  # 5

print("=" * 5, "Lambda in data structures", "=" * 5)

# List of lambdas
operations = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y,
]

for op in operations:
    print(op(10, 2), end=" ")
# 12 8 20 5.0

print()

# Lambda as dictionary values
math_ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

print(math_ops["add"](10, 3))  # 13
print(math_ops["mul"](4, 5))  # 20

# Selecting operation dynamically
def calculate(op_name, a, b):
    op = math_ops.get(op_name)
    if op:
        return op(a, b)
    return None

print(calculate("add", 5, 3))  # 8
print(calculate("div", 20, 4))  # 5.0

print("=" * 5, "Lambda limitations", "=" * 5)

# Lambda can only contain an expression, not statements
# This is NOT allowed:
# lambda x: if x > 0: return "pos"  # SyntaxError

# Use a regular function instead for complex logic
def classify_number(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

# Lambda for simple key functions is idiomatic
data = [(3, 'three'), (1, 'one'), (2, 'two')]
sorted_data = sorted(data, key=lambda item: item[0])
print(sorted_data)  # [(1, 'one'), (2, 'two'), (3, 'three')]

# Lambda captures variables by reference (closure gotcha)
funcs = [lambda: i for i in range(5)]
print([f() for f in funcs])  # [4, 4, 4, 4, 4] — all reference the same i

# Fix: use default argument to capture value
funcs = [lambda i=i: i for i in range(5)]
print([f() for f in funcs])  # [0, 1, 2, 3, 4]