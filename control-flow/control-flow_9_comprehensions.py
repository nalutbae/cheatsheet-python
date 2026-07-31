# Comprehensions: concise syntax for creating collections from iterables

print("=" * 5, "List Comprehension", "=" * 5)

# Basic list comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# List comprehension with condition (filtering)
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# List comprehension with if-else (transforming)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# Nested list comprehension (flattening)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Nested loops in comprehension
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# List comprehension with function call
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)  # ['HELLO', 'WORLD', 'PYTHON']

# List comprehension with string methods
sentences = ["Hello World", "python is great", "  SPACES  "]
cleaned = [s.strip().lower() for s in sentences]
print(cleaned)  # ['hello world', 'python is great', 'spaces']

print("=" * 5, "Dictionary Comprehension", "=" * 5)

# Basic dictionary comprehension
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "Seoul"]
person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'Seoul'}

# Dictionary comprehension with condition
scores = {"Alice": 85, "Bob": 62, "Charlie": 91, "Diana": 58}
passed = {name: score for name, score in scores.items() if score >= 70}
print(passed)  # {'Alice': 85, 'Charlie': 91}

# Dictionary comprehension with transformation
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(doubled)  # {'a': 2, 'b': 4, 'c': 6}

# Swapping keys and values
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}

# Character frequency count
text = "hello"
freq = {ch: text.count(ch) for ch in set(text)}
print(freq)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print("=" * 5, "Set Comprehension", "=" * 5)

# Basic set comprehension
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in nums}
print(unique)  # {1, 2, 3, 4}

# Set comprehension with condition
numbers = range(20)
even_squares = {x ** 2 for x in numbers if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64, 100, 144, 196, 256, 324}

# Set comprehension for finding unique lengths
words = ["cat", "dog", "bird", "fish", "ant"]
lengths = {len(w) for w in words}
print(lengths)  # {3, 4}

# Set comprehension for finding common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = {x for x in list1 if x in list2}
print(common)  # {4, 5}

print("=" * 5, "Generator Expression", "=" * 5)

# Generator expression (lazy evaluation, memory efficient)
# Uses parentheses instead of brackets
squares_gen = (x ** 2 for x in range(1, 6))
print(squares_gen)  # <generator object <genexpr> at 0x...>
print(list(squares_gen))  # [1, 4, 9, 16, 25]

# Generator expressions are consumed after one iteration
squares_gen = (x ** 2 for x in range(1, 6))
print(sum(squares_gen))  # 55
print(list(squares_gen))  # [] (already consumed)

# Using generator with built-in functions
total = sum(x for x in range(1, 101))
print(total)  # 5050

maximum = max(x ** 2 for x in range(1, 11))
print(maximum)  # 100

minimum = min(x for x in [5, 3, 8, 1, 9])
print(minimum)  # 1

# Generator vs list comprehension memory comparison
import sys

list_comp = [x for x in range(1000)]
gen_exp = (x for x in range(1000))

print(f"List size: {sys.getsizeof(list_comp)} bytes")  # ~8856 bytes
print(f"Generator size: {sys.getsizeof(gen_exp)} bytes")  # ~200 bytes

# Filtering with generator
numbers = range(1, 20)
primes = (n for n in numbers if n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)))
print(list(primes))  # [2, 3, 5, 7, 11, 13, 17, 19]