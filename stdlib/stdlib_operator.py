# operator: standard operators as functions

import operator

print("=" * 5, "Arithmetic operators", "=" * 5)

# Addition and subtraction
print(f"add(1, 2): {operator.add(1, 2)}")  # 3
print(f"sub(10, 3): {operator.sub(10, 3)}")  # 7
print(f"mul(4, 5): {operator.mul(4, 5)}")  # 20
print(f"truediv(10, 3): {operator.truediv(10, 3)}")  # 3.3333...
print(f"floordiv(10, 3): {operator.floordiv(10, 3)}")  # 3
print(f"mod(10, 3): {operator.mod(10, 3)}")  # 1
print(f"pow(2, 10): {operator.pow(2, 10)}")  # 1024
print(f"neg(5): {operator.neg(5)}")  # -5
print(f"pos(-3): {operator.pos(-3)}")  # -3
print(f"abs(-7): {operator.abs(-7)}")  # 7

# In-place operators (for mutable objects)
lst = [1, 2, 3]
operator.iadd(lst, [4, 5])
print(f"iadd([1,2,3], [4,5]): {lst}")  # [1, 2, 3, 4, 5]

lst2 = [1, 2]
operator.imul(lst2, 3)
print(f"imul([1,2], 3): {lst2}")  # [1, 2, 1, 2, 1, 2]

print("=" * 5, "Comparison operators", "=" * 5)

print(f"lt(1, 2): {operator.lt(1, 2)}")  # True
print(f"le(2, 2): {operator.le(2, 2)}")  # True
print(f"eq(3, 3): {operator.eq(3, 3)}")  # True
print(f"ne(3, 4): {operator.ne(3, 4)}")  # True
print(f"ge(5, 3): {operator.ge(5, 3)}")  # True
print(f"gt(5, 3): {operator.gt(5, 3)}")  # True

# Comparison with different types
print(f"lt('a', 'b'): {operator.lt('a', 'b')}")  # True
print(f"eq([1,2], [1,2]): {operator.eq([1,2], [1,2])}")  # True

# Use with sorted (key function)
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
by_score = sorted(students, key=operator.itemgetter(1))
print(f"Sorted by score: {by_score}")

by_name = sorted(students, key=operator.itemgetter(0))
print(f"Sorted by name: {by_name}")

print("=" * 5, "Logical operators", "=" * 5)

print(f"not_(True): {operator.not_(True)}")  # False
print(f"not_(False): {operator.not_(False)}")  # True
print(f"truth([]): {operator.truth([])}")  # False
print(f"truth([1]): {operator.truth([1])}")  # True
print(f"truth(0): {operator.truth(0)}")  # False
print(f"truth(1): {operator.truth(1)}")  # True
print(f"is_(None, None): {operator.is_(None, None)}")  # True
print(f"is_('a', 'a'): {operator.is_('a', 'a')}")  # True (interned)
print(f"is_not(1, 2): {operator.is_not(1, 2)}")  # True

print("=" * 5, "Item and attribute accessors", "=" * 5)

# itemgetter: get items by index or key
data = [10, 20, 30, 40, 50]
get_second = operator.itemgetter(1)
print(f"itemgetter(1)([10,20,30]): {get_second(data)}")  # 20

get_last = operator.itemgetter(-1)
print(f"itemgetter(-1)(list): {get_last(data)}")  # 50

# Multiple indices
get_first_last = operator.itemgetter(0, -1)
print(f"itemgetter(0,-1): {get_first_last(data)}")  # (10, 50)

# itemgetter with dicts
person = {"name": "Alice", "age": 30, "city": "Seoul"}
get_name = operator.itemgetter("name")
print(f"Dict itemgetter: {get_name(person)}")  # Alice

# Slicing with itemgetter
get_range = operator.itemgetter(slice(1, 4))
print(f"Slice itemgetter: {get_range(data)}")  # [20, 30, 40]

# attrgetter: get attributes from objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

points = [Point(3, 1), Point(1, 2), Point(2, 3)]
get_x = operator.attrgetter("x")
print(f"attrgetter('x'): {get_x(points[0])}")  # 3

# Sort objects by attribute
sorted_by_x = sorted(points, key=operator.attrgetter("x"))
print(f"Sorted by x: {sorted_by_x}")  # Point(1,2), Point(2,3), Point(3,1)

sorted_by_y = sorted(points, key=operator.attrgetter("y"))
print(f"Sorted by y: {sorted_by_y}")  # Point(3,1), Point(1,2), Point(2,3)

# Multiple attributes
get_xy = operator.attrgetter("x", "y")
print(f"attrgetter('x','y'): {get_xy(points[0])}")  # (3, 1)

print("=" * 5, "methodcaller: call methods by name", "=" * 5)

# methodcaller: create a callable that calls a method
upper = operator.methodcaller("upper")
print(f"methodcaller('upper'): {upper('hello')}")  # HELLO

split = operator.methodcaller("split", ",")
print(f"methodcaller('split', ','): {split('a,b,c')}")  # ['a', 'b', 'c']

replace = operator.methodcaller("replace", "o", "0")
print(f"methodcaller('replace', 'o', '0'): {replace('hello world')}")  # hell0 w0rld

strip = operator.methodcaller("strip", " ")
print(f"methodcaller('strip'): {strip('  hello  ')}")  # hello

# Practical: sort strings ignoring case
words = ["banana", "Apple", "cherry", "Blueberry"]
sorted_words = sorted(words, key=operator.methodcaller("lower"))
print(f"Case-insensitive sort: {sorted_words}")  # ['Apple', 'banana', 'Blueberry', 'cherry']

# Practical: call count() on each string
sentences = ["hello world", "python is great", "hello python"]
counts = list(map(operator.methodcaller("count", "hello"), sentences))
print(f"'hello' counts: {counts}")  # [1, 0, 1]

print("=" * 5, "Practical: operator with functional tools", "=" * 5)

# operator.add with reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(operator.add, numbers)
print(f"Sum with operator.add: {total}")  # 15

# operator.mul with reduce
product = reduce(operator.mul, numbers, 1)
print(f"Product with operator.mul: {product}")  # 120

# operator.contains with filter
items = ["apple", "banana", "cherry", "date", "elderberry"]
short = list(filter(lambda s: operator.lt(len(s), 6), items))
print(f"Short words: {short}")  # ['apple']

# Sorting with itemgetter (common pattern)
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92},
    {"name": "Diana", "grade": 88},
]

by_grade = sorted(students, key=operator.itemgetter("grade"), reverse=True)
print(f"By grade (desc): {by_grade}")

# Multi-level sort
by_grade_name = sorted(students, key=operator.itemgetter("grade", "name"))
print(f"By grade then name: {by_grade_name}")

# Grouping with itemgetter
from itertools import groupby
students_sorted = sorted(students, key=operator.itemgetter("grade"))
for grade, group in groupby(students_sorted, key=operator.itemgetter("grade")):
    names = [s["name"] for s in group]
    print(f"  Grade {grade}: {names}")

# Dictionary operations
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# setitem and delitem
operator.setitem(d1, "e", 5)
print(f"After setitem: {d1}")  # {'a': 1, 'b': 2, 'e': 5}

operator.delitem(d1, "e")
print(f"After delitem: {d1}")  # {'a': 1, 'b': 2}

# getitem with default
value = d1.get("x", 0)
print(f"Get with default: {value}")  # 0