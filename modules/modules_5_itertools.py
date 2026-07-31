# Itertools: iterator building blocks for efficient looping

from itertools import count, cycle, repeat, accumulate, chain, compress
from itertools import dropwhile, takewhile, filterfalse, groupby
from itertools import islice, starmap, zip_longest
from itertools import permutations, combinations, combinations_with_replacement
from itertools import product

print("=" * 5, "Infinite iterators", "=" * 5)

# count(start, step): infinite arithmetic sequence
for i, val in enumerate(count(10, 2)):
    if i >= 5:
        break
    print(val, end=" ")
# 10 12 14 16 18
print()

# cycle(iterable): infinite repetition
cycle_iter = cycle(["A", "B", "C"])
for i in range(7):
    print(next(cycle_iter), end=" ")
# A B C A B C A
print()

# repeat(elem, times): repeat an element
print(list(repeat(10, 3)))  # [10, 10, 10]
print(list(repeat("hi", 4)))  # ['hi', 'hi', 'hi', 'hi']

print("=" * 5, "Accumulate: running totals and reductions", "=" * 5)

# Default: running sum
nums = [1, 2, 3, 4, 5]
print(f"Running sum: {list(accumulate(nums))}")  # [1, 3, 6, 10, 15]

# Running product
import operator
print(f"Running product: {list(accumulate(nums, operator.mul))}")  # [1, 2, 6, 24, 120]

# Running maximum
print(f"Running max: {list(accumulate(nums, max))}")  # [1, 2, 3, 4, 5]

# Running minimum
prices = [100, 80, 90, 70, 85]
print(f"Running min: {list(accumulate(prices, min))}")  # [100, 80, 80, 70, 70]

# Custom function
print(f"Running diff: {list(accumulate(nums, lambda a, b: a - b))}")  # [1, -1, -4, -8, -13]

print("=" * 5, "Chain: combining iterables", "=" * 5)

# Chain multiple iterables together
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [True, False]

print(f"Chained: {list(chain(list1, list2, list3))}")  # [1, 2, 3, 'a', 'b', 'c', True, False]

# chain.from_iterable: flatten one level
nested = [[1, 2], [3, 4], [5, 6]]
print(f"Flattened: {list(chain.from_iterable(nested))}")  # [1, 2, 3, 4, 5, 6]

# Strings are also iterables
print(f"Chain strings: {list(chain('abc', 'def'))}")  # ['a', 'b', 'c', 'd', 'e', 'f']

print("=" * 5, "Compress, filterfalse, takewhile, dropwhile", "=" * 5)

# compress: filter by selectors
data = ["a", "b", "c", "d", "e"]
selectors = [True, False, True, False, True]
print(f"Compress: {list(compress(data, selectors))}")  # ['a', 'c', 'e']

# filterfalse: elements where predicate is False
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Not even: {list(filterfalse(lambda x: x % 2 == 0, nums))}")  # [1, 3, 5, 7, 9]

# takewhile: take elements while condition is True
print(f"Take while < 5: {list(takewhile(lambda x: x < 5, nums))}")  # [1, 2, 3, 4]

# dropwhile: drop elements while condition is True, then take rest
print(f"Drop while < 5: {list(dropwhile(lambda x: x < 5, nums))}")  # [5, 6, 7, 8, 9]

print("=" * 5, "Groupby: grouping consecutive elements", "=" * 5)

# groupby groups consecutive elements with the same key
# IMPORTANT: data must be sorted by the key first!

data = [("apple", "fruit"), ("carrot", "vegetable"), ("banana", "fruit"),
        ("broccoli", "vegetable"), ("cherry", "fruit")]

# Sort by the grouping key first
data_sorted = sorted(data, key=lambda x: x[1])

for key, group in groupby(data_sorted, key=lambda x: x[1]):
    items = [item[0] for item in group]
    print(f"  {key}: {items}")
# fruit: ['apple', 'banana', 'cherry']
# vegetable: ['broccoli', 'carrot']

# Group numbers by even/odd
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]
for key, group in groupby(nums, key=lambda x: "even" if x % 2 == 0 else "odd"):
    print(f"  {key}: {list(group)}")
# odd: [1, 1]
# even: [2, 2]
# odd: [3, 3]
# even: [4, 4]
# odd: [5]

# Group by first letter
words = ["apple", "ant", "banana", "bear", "cat", "camel"]
words.sort(key=lambda w: w[0])
for key, group in groupby(words, key=lambda w: w[0]):
    print(f"  '{key}': {list(group)}")
# 'a': ['apple', 'ant']
# 'b': ['banana', 'bear']
# 'c': ['cat', 'camel']

print("=" * 5, "islice: slicing iterators", "=" * 5)

# islice: slice an iterator (doesn't create a full list)
nums = range(100)
print(f"First 5: {list(islice(nums, 5))}")  # [0, 1, 2, 3, 4]
print(f"From 10 to 15: {list(islice(nums, 10, 15))}")  # [10, 11, 12, 13, 14]
print(f"Every 3rd from 0 to 20: {list(islice(nums, 0, 20, 3))}")  # [0, 3, 6, 9, 12, 15, 18]

# Useful with infinite iterators
for i, val in enumerate(islice(count(100), 5)):
    print(val, end=" ")
# 100 101 102 103 104
print()

print("=" * 5, "Permutations and combinations", "=" * 5)

# Permutations: all possible orderings
print(f"Permutations of [1,2,3]:")
for p in permutations([1, 2, 3]):
    print(f"  {p}")
# (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)

# Permutations of length r
print(f"Permutations of [1,2,3,4], length 2:")
for p in permutations([1, 2, 3, 4], 2):
    print(f"  {p}", end="")
print()

# Combinations: selection without order
print(f"Combinations of [1,2,3,4], length 2:")
for c in combinations([1, 2, 3, 4], 2):
    print(f"  {c}", end="")
print()
# (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)

# Combinations with replacement: allows repeated elements
print(f"Combinations with replacement of [1,2,3], length 2:")
for c in combinations_with_replacement([1, 2, 3], 2):
    print(f"  {c}", end="")
print()
# (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)

# Product: Cartesian product
print(f"Cartesian product of [1,2] and ['a','b']:")
for item in product([1, 2], ["a", "b"]):
    print(f"  {item}", end="")
print()
# (1,'a'), (1,'b'), (2,'a'), (2,'b')

# Product with repeat
print(f"Product of [0,1] with repeat=3 (binary triples):")
for item in product([0, 1], repeat=3):
    print(f"  {item}", end="")
print()
# (0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)

print("=" * 5, "zip_longest: zip with fill value", "=" * 5)

# Regular zip stops at the shortest iterable
short = [1, 2, 3]
long = ["a", "b", "c", "d", "e"]
print(f"Regular zip: {list(zip(short, long))}")  # [(1, 'a'), (2, 'b'), (3, 'c')]

# zip_longest fills missing values
print(f"zip_longest: {list(zip_longest(short, long))}")  # [(1, 'a'), (2, 'b'), (3, 'c'), (None, 'd'), (None, 'e')]

# Custom fill value
print(f"zip_longest fillvalue: {list(zip_longest(short, long, fillvalue=0))}")
# [(1, 'a'), (2, 'b'), (3, 'c'), (0, 'd'), (0, 'e')]

print("=" * 5, "starmap: apply function with argument unpacking", "=" * 5)

# starmap: like map but unpacks arguments from tuples
points = [(1, 2), (3, 4), (5, 6)]
distances = list(starmap(lambda x, y: (x ** 2 + y ** 2) ** 0.5, points))
print(f"Distances: {distances}")  # [2.236..., 5.0, 7.810...]

# Compare with map: map would pass the whole tuple as one argument
# map(lambda p: (p[0]**2 + p[1]**2)**0.5, points) — less clean

# Practical: applying a function to pairs
data = [(2, 10), (3, 5), (4, 2)]
results = list(starmap(pow, data))
print(f"2^10, 3^5, 4^2: {results}")  # [1024, 243, 16]