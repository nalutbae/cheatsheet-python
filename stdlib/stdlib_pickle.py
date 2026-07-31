# pickle: object serialization and deserialization

import pickle
import os

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "stdlib_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "Basic serialization", "=" * 5)

# Pickle a simple object to bytes
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}
pickled = pickle.dumps(data)
print(f"Type: {type(pickled)}")  # <class 'bytes'>
print(f"Size: {len(pickled)} bytes")

# Unpickle from bytes
restored = pickle.loads(pickled)
print(f"Restored: {restored}")  # {'name': 'Alice', 'age': 30, 'scores': [95, 87, 92]}
print(f"Equal: {data == restored}")  # True

print("=" * 5, "Pickleable types", "=" * 5)

# Basic types
for obj in [42, 3.14, True, "hello", b"bytes", None]:
    pickled = pickle.dumps(obj)
    restored = pickle.loads(pickled)
    print(f"  {type(obj).__name__}: {obj} → {restored} (equal: {obj == restored})")

# Collections
for obj in [[1, 2, 3], (1, 2, 3), {1, 2, 3}, {"a": 1, "b": 2}]:
    pickled = pickle.dumps(obj)
    restored = pickle.loads(pickled)
    print(f"  {type(obj).__name__}: {obj} → {restored} (equal: {obj == restored})")

# Nested structures
nested = {
    "list": [1, [2, [3, [4]]]],
    "dict": {"a": {"b": {"c": "deep"}}},
    "mixed": [{"x": 1}, (2, 3), {4, 5}],
}
pickled = pickle.dumps(nested)
restored = pickle.loads(pickled)
print(f"Nested equal: {nested == restored}")  # True

# Sets with different types
mixed_set = {1, "hello", 3.14, True, (1, 2)}
pickled = pickle.dumps(mixed_set)
restored = pickle.loads(pickled)
print(f"Set equal: {mixed_set == restored}")  # True

print("=" * 5, "Custom classes", "=" * 5)

class Person:
    def __init__(self, name, age, hobbies=None):
        self.name = name
        self.age = age
        self.hobbies = hobbies or []

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (self.name == other.name and
                self.age == other.age and
                self.hobbies == other.hobbies)

# Pickle a custom object
alice = Person("Alice", 30, ["reading", "coding"])
pickled = pickle.dumps(alice)
restored = pickle.loads(pickled)
print(f"Original: {alice}")
print(f"Restored: {restored}")
print(f"Equal: {alice == restored}")  # True
print(f"Same class: {type(restored).__name__}")  # Person

# List of custom objects
people = [
    Person("Alice", 30, ["reading"]),
    Person("Bob", 25, ["gaming"]),
    Person("Charlie", 35, ["cooking"]),
]
pickled = pickle.dumps(people)
restored = pickle.loads(pickled)
print(f"Restored {len(restored)} people")
for p in restored:
    print(f"  {p}")

print("=" * 5, "Pickling with __getstate__ and __setstate__", "=" * 5)

class SafeObject:
    def __init__(self, public_data, secret_key):
        self.public_data = public_data
        self.secret_key = secret_key

    def __getstate__(self):
        """Customize what gets pickled — exclude sensitive data."""
        state = self.__dict__.copy()
        state["secret_key"] = "***REDACTED***"
        return state

    def __setstate__(self, state):
        """Customize unpickling behavior."""
        self.__dict__.update(state)

    def __repr__(self):
        return f"SafeObject(public={self.public_data!r}, secret={self.secret_key!r})"

obj = SafeObject("important data", "super_secret_key_123")
pickled = pickle.dumps(obj)
restored = pickle.loads(pickled)
print(f"Original: {obj}")  # secret_key=super_secret_key_123
print(f"Restored: {restored}")  # secret_key=***REDACTED***

print("=" * 5, "File I/O with pickle", "=" * 5)

# Write pickle to file
file_path = os.path.join(EXAMPLE_DIR, "data.pkl")

data = {
    "users": [
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 87},
        {"name": "Charlie", "score": 92},
    ],
    "metadata": {
        "version": "1.0",
        "created": "2025-07-31",
    }
}

# Pickle to file
with open(file_path, "wb") as f:
    pickle.dump(data, f)

print(f"Saved to: {file_path}")
print(f"File size: {os.path.getsize(file_path)} bytes")

# Read pickle from file
with open(file_path, "rb") as f:
    loaded = pickle.load(f)

print(f"Loaded: {loaded}")
print(f"Equal: {data == loaded}")  # True

# Pickle multiple objects to one file
file_path2 = os.path.join(EXAMPLE_DIR, "multi.pkl")
with open(file_path2, "wb") as f:
    pickle.dump("first object", f)
    pickle.dump([1, 2, 3], f)
    pickle.dump({"key": "value"}, f)

with open(file_path2, "rb") as f:
    obj1 = pickle.load(f)
    obj2 = pickle.load(f)
    obj3 = pickle.load(f)

print(f"Object 1: {obj1}")  # first object
print(f"Object 2: {obj2}")  # [1, 2, 3]
print(f"Object 3: {obj3}")  # {'key': 'value'}

print("=" * 5, "Pickle protocols", "=" * 5)

# Different protocol versions
for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
    size = len(pickle.dumps(data, protocol=protocol))
    print(f"  Protocol {protocol}: {size} bytes")

print(f"Highest protocol: {pickle.HIGHEST_PROTOCOL}")
print(f"Default protocol: {pickle.DEFAULT_PROTOCOL}")

# Protocol comparison
p0 = pickle.dumps(data, protocol=0)  # ASCII (human-readable)
p_highest = pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)
print(f"Protocol 0 (ASCII): {len(p0)} bytes")
print(f"Protocol {pickle.HIGHEST_PROTOCOL} (binary): {len(p_highest)} bytes")
print(f"Compression ratio: {len(p_highest) / len(p0):.2f}")

print("=" * 5, "Practical: caching expensive computations", "=" * 5)

import time

cache_file = os.path.join(EXAMPLE_DIR, "computation_cache.pkl")

def expensive_computation(n):
    """Simulate an expensive computation."""
    time.sleep(0.01)  # simulate delay
    return sum(i ** 2 for i in range(n))

def compute_with_cache(n, cache_path):
    """Compute with pickle-based caching."""
    if os.path.exists(cache_path):
        with open(cache_path, "rb") as f:
            cache = pickle.load(f)
    else:
        cache = {}

    if n in cache:
        print(f"  Cache hit for n={n}")
        return cache[n]

    print(f"  Computing for n={n}...")
    result = expensive_computation(n)
    cache[n] = result

    with open(cache_path, "wb") as f:
        pickle.dump(cache, f)

    return result

# First call: computes and caches
result1 = compute_with_cache(10000, cache_file)
# Second call: loads from cache
result2 = compute_with_cache(10000, cache_file)
print(f"Results equal: {result1 == result2}")

print("=" * 5, "Unpickling safety", "=" * 5)

# WARNING: Never unpickle data from untrusted sources!
# pickle can execute arbitrary code during unpickling.

class Dangerous:
    def __reduce__(self):
        # This demonstrates how pickle can execute arbitrary code
        import os
        return (os.system, ("echo 'Pickle safety warning'",))

# Demonstrate __reduce__ (custom pickling)
class CustomPickle:
    def __init__(self, value):
        self.value = value

    def __reduce__(self):
        # Return (callable, args) for reconstruction
        return (CustomPickle, (self.value,))

    def __repr__(self):
        return f"CustomPickle({self.value})"

obj = CustomPickle(42)
pickled = pickle.dumps(obj)
restored = pickle.loads(pickled)
print(f"Custom pickle: {restored}")  # CustomPickle(42)

print("\n⚠️  IMPORTANT: Never unpickle data from untrusted sources!")
print("    pickle can execute arbitrary Python code during unpickling.")

print("=" * 5, "Cleanup", "=" * 5)

import shutil
shutil.rmtree(EXAMPLE_DIR)
print("Cleaned up examples directory")