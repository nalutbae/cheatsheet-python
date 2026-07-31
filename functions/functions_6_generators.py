# Generator functions: use 'yield' instead of 'return' to produce values lazily

print("=" * 5, "Basic generator", "=" * 5)

# A generator function uses 'yield' to produce values one at a time
def count_up_to(n):
    """Yield numbers from 1 to n."""
    num = 1
    while num <= n:
        yield num
        num += 1

# Creating a generator object
gen = count_up_to(5)
print(type(gen))  # <class 'generator'>

# Iterating over a generator
for num in count_up_to(5):
    print(num, end=" ")
# 1 2 3 4 5

print()

# Using next() to get values one at a time
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration

# Converting generator to list
gen = count_up_to(5)
print(list(gen))  # [1, 2, 3, 4, 5]

# Generator is exhausted after iteration
gen = count_up_to(3)
print(list(gen))  # [1, 2, 3]
print(list(gen))  # [] (already exhausted)

print("=" * 5, "Generator vs list memory comparison", "=" * 5)

import sys

# List: stores all values in memory
list_comp = [x ** 2 for x in range(1000)]
print(f"List size: {sys.getsizeof(list_comp)} bytes")  # ~8856 bytes

# Generator: produces values on demand
gen_expr = (x ** 2 for x in range(1000))
print(f"Generator size: {sys.getsizeof(gen_expr)} bytes")  # ~200 bytes

# Sum with generator (no intermediate list)
total = sum(x ** 2 for x in range(1000))
print(f"Sum: {total}")  # 332833500

print("=" * 5, "Yielding multiple values", "=" * 5)

# Generator that yields pairs
def pairs(n):
    for i in range(n):
        yield i, i ** 2

for index, square in pairs(5):
    print(f"{index} -> {square}")
# 0 -> 0
# 1 -> 1
# 2 -> 4
# 3 -> 9
# 4 -> 16

# Generator that yields different types
def alternating(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
        else:
            yield str(i)

print(list(alternating(6)))  # [0, '1', 2, '3', 4, '5']

print("=" * 5, "Generator with send()", "=" * 5)

# Generators can receive values via send()
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)  # prime the generator (advances to first yield)
print(gen.send(10))  # 10
print(gen.send(20))  # 30
print(gen.send(30))  # 60

print("=" * 5, "Generator methods: send, throw, close", "=" * 5)

# throw(): raise an exception inside the generator
def gen_with_exception():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError as e:
        yield f"Caught: {e}"
    yield 4

g = gen_with_exception()
print(next(g))  # 1
print(g.throw(ValueError, "test error"))  # Caught: test error
print(next(g))  # 4

# close(): closes the generator
g2 = gen_with_exception()
print(next(g2))  # 1
g2.close()
# next(g2)  # StopIteration

print("=" * 5, "yield from: delegating to a sub-generator", "=" * 5)

# yield from delegates iteration to another iterable
def chain(*iterables):
    for iterable in iterables:
        yield from iterable

print(list(chain([1, 2], [3, 4], [5, 6])))  # [1, 2, 3, 4, 5, 6]

# Nested generators with yield from
def inner_gen():
    yield 1
    yield 2

def outer_gen():
    yield "start"
    yield from inner_gen()
    yield "end"

print(list(outer_gen()))  # ['start', 1, 2, 'end']

print("=" * 5, "Practical generator examples", "=" * 5)

# Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print(list(fibonacci(50)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Prime number generator
def primes(limit):
    for num in range(2, limit):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

print(list(primes(30)))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# File line generator (memory efficient for large files)
def read_lines(filepath):
    """Yield one line at a time from a file."""
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

# Infinite counter
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

# Using islice to take a finite number from an infinite generator
from itertools import islice

counter = infinite_counter(10)
first_five = list(islice(counter, 5))
print(first_five)  # [10, 11, 12, 13, 14]

# Chunk generator: split iterable into chunks
def chunked(iterable, size):
    """Yield successive chunks of the given size."""
    it = iter(iterable)
    while True:
        chunk = list(islice(it, size))
        if not chunk:
            break
        yield chunk

print(list(chunked(range(10), 3)))  # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

# Permutation generator
def permutations(items):
    """Generate all permutations of the given items."""
    if len(items) <= 1:
        yield items
    else:
        for i in range(len(items)):
            for perm in permutations(items[:i] + items[i + 1:]):
                yield [items[i]] + perm

print(list(permutations([1, 2, 3])))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]