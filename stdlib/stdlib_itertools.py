# itertools: iterator building blocks for efficient looping

from itertools import count, cycle, repeat, accumulate, chain, compress
from itertools import dropwhile, takewhile, filterfalse, groupby, islice
from itertools import starmap, zip_longest, permutations, combinations
from itertools import combinations_with_replacement, product

print("=" * 5, "Infinite iterators", "=" * 5)

# count(start, step): infinite arithmetic sequence
for i, val in enumerate(count(start=10, step=2)):
    if i >= 5:
        break
    print(val, end=" ")  # 10 12 14 16 18
print()

# cycle(iterable): repeat infinitely
colors = cycle(["red", "green", "blue"])
for i, color in enumerate(colors):
    if i >= 6:
        break
    print(color, end=" ")  # red green blue red green blue
print()

# repeat(elem, times): repeat an element
for val in repeat("hello", 3):
    print(val, end=" ")  # hello hello hello
print()

print("=" * 5, "Accumulate: running totals and reductions", "=" * 5)

# Running sum (default)
nums = [1, 2, 3, 4, 5]
print(f"Running sum: {list(accumulate(nums))}")  # [1, 3, 6, 10, 15]

# Running max
print(f"Running max: {list(accumulate(nums, max))}")  # [1, 2, 3, 4, 5]

# Running product
import operator
print(f"Running product: {list(accumulate(nums, operator.mul))}")  # [1, 2, 6, 24, 120]

# Running subtraction
print(f"Running diff: {list(accumulate([100, 10, 20, 30], operator.sub))}")  # [100, 90, 70, 40]

# Custom operation: track minimum
prices = [100, 95, 110, 85, 90, 80]
print(f"Running min: {list(accumulate(prices, min))}")  # [100, 95, 95, 85, 85, 80]

print("=" * 5, "Chain: combining iterables", "=" * 5)

# Chain multiple iterables
a = [1, 2, 3]
b = ["a", "b", "c"]
c = [True, False]
print(f"Chained: {list(chain(a, b, c))}")  # [1, 2, 3, 'a', 'b', 'c', True, False]

# chain.from_iterable: chain an iterable of iterables
nested = [[1, 2], [3, 4], [5, 6]]
print(f"Flattened: {list(chain.from_iterable(nested))}")  # [1, 2, 3, 4, 5, 6]

# Useful for combining dict views
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {"c": 3}
keys = list(chain(d1, d2, d3))
print(f"Combined keys: {keys}")  # ['a', 'b', 'c']

print("=" * 5, "Compress, filterfalse, takewhile, dropwhile", "=" * 5)

# compress: select elements using a selector mask
data = ["a", "b", "c", "d", "e"]
mask = [True, False, True, False, True]
print(f"Compressed: {list(compress(data, mask))}")  # ['a', 'c', 'e']

# filterfalse: elements where predicate is False
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Not even: {list(filterfalse(lambda x: x % 2 == 0, nums))}")  # [1, 3, 5, 7, 9]

# takewhile: take elements while predicate is True
print(f"Take while < 4: {list(takewhile(lambda x: x < 4, nums))}")  # [1, 2, 3]

# dropwhile: drop elements while predicate is True
print(f"Drop while < 4: {list(dropwhile(lambda x: x < 4, nums))}")  # [4, 5, 6, 7, 8, 9]

# Combining takewhile and dropwhile
text = "Header lines\nHeader lines\nData line 1\nData line 2"
lines = text.split("\n")
data_lines = list(dropwhile(lambda line: line.startswith("Header"), lines))
print(f"Data lines: {data_lines}")

print("=" * 5, "Groupby: grouping consecutive elements", "=" * 5)

# Group by a key function (must sort first!)
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("c", 5)]
data.sort(key=lambda x: x[0])

for key, group in groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

# Group numbers by even/odd
nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
for key, group in groupby(nums):
    print(f"  {key}: {list(group)}")  # groups consecutive same values

# Group words by first letter
words = ["apple", "apricot", "banana", "blueberry", "cherry", "coconut"]
words.sort(key=lambda w: w[0])

for letter, group in groupby(words, key=lambda w: w[0]):
    print(f"  {letter}: {list(group)}")

# Practical: grouping records by category
records = [
    {"category": "fruit", "name": "apple"},
    {"category": "fruit", "name": "banana"},
    {"category": "vegetable", "name": "carrot"},
    {"category": "vegetable", "name": "daikon"},
]
records.sort(key=lambda r: r["category"])

for category, items in groupby(records, key=lambda r: r["category"]):
    names = [item["name"] for item in items]
    print(f"  {category}: {names}")

print("=" * 5, "islice: slicing iterators", "=" * 5)

# islice(iterable, stop): first N elements
nums = range(100)
print(f"First 5: {list(islice(nums, 5))}")  # [0, 1, 2, 3, 4]

# islice(iterable, start, stop)
print(f"Elements 10-14: {list(islice(nums, 10, 15))}")  # [10, 11, 12, 13, 14]

# islice(iterable, start, stop, step)
print(f"Every other 0-10: {list(islice(nums, 0, 10, 2))}")  # [0, 2, 4, 6, 8]

# Infinite iterator with islice
print(f"First 5 even numbers: {list(islice(count(0, 2), 5))}")  # [0, 2, 4, 6, 8]

# Reading first N lines from a large file (without loading entire file)
def read_first_n(iterable, n):
    return list(islice(iterable, n))

sample_lines = [f"line {i}" for i in range(1000)]
print(f"First 3 lines: {read_first_n(sample_lines, 3)}")

print("=" * 5, "Starmap: apply function with argument tuples", "=" * 5)

# starmap: like map but unpacks each tuple as arguments
points = [(1, 2), (3, 4), (5, 12)]
distances = list(starmap(lambda x, y: (x**2 + y**2)**0.5, points))
print(f"Distances: {[f'{d:.2f}' for d in distances]}")  # 2.24, 5.00, 13.00

# Practical: batch processing with argument tuples
operations = [(10, 2, "+"), (10, 2, "-"), (10, 2, "*"), (10, 2, "/")]
def compute(a, b, op):
    ops = {"+": a + b, "-": a - b, "*": a * b, "/": a / b}
    return ops[op]

results = list(starmap(compute, operations))
print(f"Results: {results}")  # [12, 8, 20, 5.0]

print("=" * 5, "zip_longest: zip with fill value", "=" * 5)

# zip stops at shortest iterable
short = list(zip([1, 2, 3], ["a", "b"]))
print(f"zip (shortest): {short}")  # [(1, 'a'), (2, 'b')]

# zip_longest continues to longest
long = list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="N/A"))
print(f"zip_longest: {long}")  # [(1, 'a'), (2, 'b'), (3, 'N/A')]

# Fill with None (default) or custom value
keys = ["name", "age", "city"]
values = ["Alice", 30]
paired = dict(zip_longest(keys, values, fillvalue="unknown"))
print(f"Paired dict: {paired}")  # {'name': 'Alice', 'age': 30, 'city': 'unknown'}

print("=" * 5, "Combinatorics", "=" * 5)

# permutations: all possible orderings
print(f"Permutations of [1,2,3]: {list(permutations([1, 2, 3]))}")
print(f"Permutations of length 2: {list(permutations([1, 2, 3], 2))}")

# combinations: all possible selections (order doesn't matter)
print(f"Combinations of [1,2,3,4] choose 2: {list(combinations([1, 2, 3, 4], 2))}")
print(f"Combinations of [1,2,3] choose 2: {list(combinations([1, 2, 3], 2))}")

# combinations_with_replacement: allow repeats
print(f"Combinations with replacement: {list(combinations_with_replacement([1, 2, 3], 2))}")

# product: Cartesian product
print(f"Product of [1,2] × [3,4]: {list(product([1, 2], [3, 4]))}")
print(f"Product of 3 dice: {len(list(product(range(1, 7), repeat=3)))} combinations")

# Practical: generating passwords
import string
lower = string.ascii_lowercase[:3]  # abc
digits = string.digits[:3]  # 012
passwords = list(product(lower, digits, lower))
print(f"Sample passwords: {[''.join(p) for p in passwords[:5]]}")

# Practical: all possible schedule slots
days = ["Mon", "Wed", "Fri"]
times = ["09:00", "11:00", "14:00"]
rooms = ["A", "B"]
slots = list(product(days, times, rooms))
print(f"Schedule slots: {len(slots)} total")
for slot in slots[:3]:
    print(f"  {slot}")