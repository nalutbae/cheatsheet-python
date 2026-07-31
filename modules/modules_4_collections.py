# Collections module: specialized container data types

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
from collections import ChainMap

print("=" * 5, "Counter: counting hashable objects", "=" * 5)

# Basic counting
text = "abracadabra"
counter = Counter(text)
print(f"Counter: {counter}")  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(f"Most common 3: {counter.most_common(3)}")  # [('a', 5), ('b', 2), ('r', 2)]

# Counter from a list
words = ["the", "cat", "sat", "on", "the", "mat", "the", "cat"]
word_count = Counter(words)
print(f"Word count: {word_count}")  # Counter({'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1})
print(f"'the' appears: {word_count['the']} times")  # 3
print(f"'dog' appears: {word_count['dog']} times")  # 0 (no KeyError!)

# Counter arithmetic
c1 = Counter(a=3, b=1, c=2)
c2 = Counter(a=1, b=2, d=3)

print(f"Addition: {c1 + c2}")  # Counter({'a': 4, 'b': 3, 'd': 3, 'c': 2})
print(f"Subtraction: {c1 - c2}")  # Counter({'a': 2, 'c': 2}) (no negatives)
print(f"Intersection: {c1 & c2}")  # Counter({'a': 1, 'b': 1}) (min of each)
print(f"Union: {c1 | c2}")  # Counter({'a': 3, 'd': 3, 'b': 2, 'c': 2}) (max of each)

# Updating a Counter
c = Counter("hello")
c.update("world")
print(f"Updated: {c}")  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})

# Elements (iterable of items repeated by count)
print(f"Elements: {sorted(c.elements())}")

print("=" * 5, "defaultdict: dictionary with default values", "=" * 5)

# defaultdict with list
dd_list = defaultdict(list)
for word in ["apple", "banana", "apricot", "blueberry", "avocado"]:
    dd_list[word[0]].append(word)
print(f"By first letter: {dict(dd_list)}")  # {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry']}

# defaultdict with int (counter pattern)
dd_int = defaultdict(int)
for char in "mississippi":
    dd_int[char] += 1
print(f"Char count: {dict(dd_int)}")  # {'m': 1, 'i': 4, 's': 4, 'p': 2}

# defaultdict with set (unique values)
dd_set = defaultdict(set)
pairs = [("a", 1), ("b", 2), ("a", 3), ("b", 2), ("a", 1)]
for key, val in pairs:
    dd_set[key].add(val)
print(f"Unique values: {dict(dd_set)}")  # {'a': {1, 3}, 'b': {2}}

# Regular dict would raise KeyError
# d = {}
# d["missing"]  # KeyError

# defaultdict returns default for missing keys
dd = defaultdict(str)
print(f"Missing key: '{dd['missing']}'")  # '' (empty string)
print(f"After access: {dict(dd)}")  # {'missing': ''}

# Custom default factory
dd_custom = defaultdict(lambda: "N/A")
print(f"Custom default: {dd_custom['unknown']}")  # N/A

print("=" * 5, "OrderedDict: dictionary with insertion order", "=" * 5)

# OrderedDict preserves insertion order (Python 3.7+ dict also does, but OrderedDict has extra methods)
od = OrderedDict()
od["banana"] = 3
od["apple"] = 4
od["cherry"] = 1
od["date"] = 2
print(f"OrderedDict: {od}")  # {'banana': 3, 'apple': 4, 'cherry': 1, 'date': 2}

# Move an item to the end
od.move_to_end("banana")
print(f"After move_to_end: {od}")  # {'apple': 4, 'cherry': 1, 'date': 2, 'banana': 3}

# Move an item to the beginning
od.move_to_end("banana", last=False)
print(f"After move_to_start: {od}")  # {'banana': 3, 'apple': 4, 'cherry': 1, 'date': 2}

# Pop last item (FIFO or LIFO)
last = od.popitem()
print(f"Popped last: {last}")  # ('date', 2)

# Pop first item
first = od.popitem(last=False)
print(f"Popped first: {first}")  # ('banana', 3)

# Equality: order matters for OrderedDict
od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
print(f"OrderedDict equality (different order): {od1 == od2}")  # False

# Regular dict: order doesn't matter for equality
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(f"Dict equality (different order): {d1 == d2}")  # True

print("=" * 5, "deque: double-ended queue", "=" * 5)

# Creating a deque
dq = deque([1, 2, 3, 4, 5])
print(f"Deque: {dq}")  # deque([1, 2, 3, 4, 5])

# Append to the right (same as list)
dq.append(6)
print(f"After append(6): {dq}")  # deque([1, 2, 3, 4, 5, 6])

# Append to the left (O(1), much faster than list.insert(0, x))
dq.appendleft(0)
print(f"After appendleft(0): {dq}")  # deque([0, 1, 2, 3, 4, 5, 6])

# Pop from the right
right = dq.pop()
print(f"Popped right: {right}")  # 6
print(f"After pop: {dq}")  # deque([0, 1, 2, 3, 4, 5])

# Pop from the left (O(1), much faster than list.pop(0))
left = dq.popleft()
print(f"Popped left: {left}")  # 0
print(f"After popleft: {dq}")  # deque([1, 2, 3, 4, 5])

# Bounded deque (fixed size, sliding window)
limited = deque(maxlen=3)
for i in range(10):
    limited.append(i)
print(f"Last 3 items: {list(limited)}")  # [7, 8, 9]

# Rotate
dq = deque([1, 2, 3, 4, 5])
dq.rotate(2)  # rotate right by 2
print(f"Rotate right 2: {dq}")  # deque([4, 5, 1, 2, 3])

dq.rotate(-2)  # rotate left by 2
print(f"Rotate left 2: {dq}")  # deque([1, 2, 3, 4, 5])

# Extend from both sides
dq = deque([1, 2, 3])
dq.extend([4, 5])
print(f"After extend: {dq}")  # deque([1, 2, 3, 4, 5])
dq.extendleft([0, -1])  # note: items are reversed
print(f"After extendleft: {dq}")  # deque([-1, 0, 1, 2, 3, 4, 5])

# Performance comparison: deque vs list for left operations
from time import perf_counter

# deque appendleft: O(1)
dq_test = deque()
start = perf_counter()
for i in range(10000):
    dq_test.appendleft(i)
deque_time = perf_counter() - start

# list insert(0, x): O(n)
lst_test = []
start = perf_counter()
for i in range(10000):
    lst_test.insert(0, i)
list_time = perf_counter() - start

print(f"Deque appendleft: {deque_time:.6f}s")
print(f"List insert(0): {list_time:.6f}s")
print(f"Deque is {list_time / deque_time:.1f}x faster for left operations")

print("=" * 5, "namedtuple: lightweight immutable classes", "=" * 5)

# Define a namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"Point: {p}")  # Point(x=3, y=4)
print(f"x={p.x}, y={p.y}")  # x=3, y=4
print(f"x={p[0]}, y={p[1]}")  # x=3, y=4 (also indexable)

# Named tuples are immutable
try:
    p.x = 10
except AttributeError as e:
    print(f"Error: {e}")  # cannot set attribute

# _replace creates a new instance with changed fields
p2 = p._replace(x=10)
print(f"Original: {p}")  # Point(x=3, y=4)
print(f"Replaced: {p2}")  # Point(x=10, y=4)

# _asdict converts to OrderedDict
print(f"As dict: {p._asdict()}")  # {'x': 3, 'y': 4}

# _fields tuple
print(f"Fields: {Point._fields}")  # ('x', 'y')

# Creating from a dict or iterable
d = {"x": 5, "y": 6}
p3 = Point(**d)
print(f"From dict: {p3}")  # Point(x=5, y=6)

coords = [7, 8]
p4 = Point._make(coords)
print(f"From list: {p4}")  # Point(x=7, y=8)

# Multiple fields
Student = namedtuple("Student", ["name", "age", "grade", "school"])
s = Student("Alice", 20, "A", "MIT")
print(f"Student: {s}")  # Student(name='Alice', age=20, grade='A', school='MIT')

print("=" * 5, "ChainMap: combining multiple mappings", "=" * 5)

# ChainMap groups multiple dicts together
defaults = {"theme": "dark", "font_size": 14, "language": "en"}
user_config = {"theme": "light", "font_size": 16}
session_config = {"language": "ko"}

config = ChainMap(session_config, user_config, defaults)
print(f"Theme: {config['theme']}")  # light (from user_config)
print(f"Font size: {config['font_size']}")  # 16 (from user_config)
print(f"Language: {config['language']}")  # ko (from session_config)

# Keys are searched in order: session → user → defaults
print(f"All keys: {sorted(config.keys())}")  # ['font_size', 'language', 'theme']

# New values go to the first mapping
config["debug"] = True
print(f"New key in first map: {'debug' in session_config}")  # True

# Updating a lower-priority map doesn't override higher-priority
defaults["theme"] = "blue"
print(f"Theme still: {config['theme']}")  # light (user_config takes priority)