# Magic methods (dunder methods) for customizing class behavior

print("=" * 5, "Object creation and destruction", "=" * 5)

class Resource:
    """Demonstrates __init__, __new__, and __del__."""

    # __new__ creates the instance (rarely overridden)
    def __new__(cls, *args, **kwargs):
        print(f"__new__ called with {args}, {kwargs}")
        instance = super().__new__(cls)
        return instance

    # __init__ initializes the instance
    def __init__(self, name):
        print(f"__init__ called: name={name}")
        self.name = name

    # __del__ is called when the object is garbage collected
    def __del__(self):
        print(f"__del__ called for {self.name}")

    def __repr__(self):
        return f"Resource('{self.name}')"

r = Resource("database")
# __new__ called with ('database',), {}
# __init__ called: name=database

print(r)  # Resource('database')
del r  # __del__ called for database

print("=" * 5, "String representation", "=" * 5)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # __str__: informal, readable string (for end users)
    def __str__(self):
        return f"{self.name} — ${self.price:.2f} x {self.quantity}"

    # __repr__: official, unambiguous string (for developers)
    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"

    # __format__: customize format() and f-string behavior
    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.name}: ${self.price:.0f}"
        elif format_spec == "detail":
            return f"{self.name} | Price: ${self.price:.2f} | Qty: {self.quantity}"
        return str(self)

p = Product("Laptop", 999.99, 5)
print(f"str: {str(p)}")  # Laptop — $999.99 x 5
print(f"repr: {repr(p)}")  # Product('Laptop', 999.99, 5)
print(f"format short: {p:short}")  # Laptop: $1000
print(f"format detail: {p:detail}")  # Laptop | Price: $999.99 | Qty: 5

print("=" * 5, "Comparison methods", "=" * 5)

from functools import total_ordering

@total_ordering  # generates __le__, __gt__, __ge__ from __eq__ and __lt__
class Version:
    def __init__(self, major, minor, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __repr__(self):
        return f"Version({self.major}, {self.minor}, {self.patch})"

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

    def __hash__(self):
        return hash((self.major, self.minor, self.patch))

v1 = Version(1, 0, 0)
v2 = Version(2, 0, 0)
v3 = Version(1, 5, 0)
v4 = Version(1, 0, 0)

print(f"{v1} == {v4}: {v1 == v4}")  # True
print(f"{v1} < {v2}: {v1 < v2}")  # True
print(f"{v1} < {v3}: {v1 < v3}")  # True
print(f"{v2} > {v3}: {v2 > v3}")  # True
print(f"{v1} <= {v4}: {v1 <= v4}")  # True
print(f"{v1} != {v2}: {v1 != v2}")  # True

# Sorting with custom comparison
versions = [Version(2, 1), Version(1, 0), Version(1, 5), Version(2, 0)]
sorted_versions = sorted(versions)
print(f"Sorted: {[str(v) for v in sorted_versions]}")  # ['1.0.0', '1.5.0', '2.0.0', '2.1.0']

# Using in sets and dicts (requires __hash__)
version_set = {v1, v2, v3, v4}
print(f"Set (unique versions): {[str(v) for v in version_set]}")  # 3 unique versions

print("=" * 5, "Container protocol methods", "=" * 5)

class Playlist:
    """A playlist that supports indexing, iteration, and membership testing."""

    def __init__(self, name, songs=None):
        self.name = name
        self.songs = list(songs) if songs else []

    def __len__(self):
        """len() support."""
        return len(self.songs)

    def __getitem__(self, index):
        """Indexing and slicing support."""
        if isinstance(index, slice):
            return Playlist(f"{self.name} (slice)", self.songs[index])
        return self.songs[index]

    def __setitem__(self, index, song):
        """Assignment by index."""
        self.songs[index] = song

    def __delitem__(self, index):
        """Delete by index."""
        del self.songs[index]

    def __contains__(self, song):
        """in operator support."""
        return song in self.songs

    def __iter__(self):
        """Iteration support."""
        return iter(self.songs)

    def __reversed__(self):
        """reversed() support."""
        return reversed(self.songs)

    def __add__(self, other):
        """+ operator: concatenate playlists."""
        return Playlist(f"{self.name} + {other.name}", self.songs + other.songs)

    def __repr__(self):
        return f"Playlist('{self.name}', {len(self.songs)} songs)"

    def append(self, song):
        self.songs.append(song)

rock = Playlist("Rock", ["Song A", "Song B", "Song C"])
pop = Playlist("Pop", ["Song D", "Song E"])

print(f"Length: {len(rock)}")  # 3
print(f"Index 0: {rock[0]}")  # Song A
print(f"Slice: {rock[1:]}")  # Playlist('Rock (slice)', 2 songs)
print(f"Contains 'Song B': {'Song B' in rock}")  # True
print(f"Contains 'Song Z': {'Song Z' in rock}")  # False

rock[1] = "Song B (Remix)"
print(f"After setitem: {rock[1]}")  # Song B (Remix)

del rock[2]
print(f"After delitem: {len(rock)}")  # 2

combined = rock + pop
print(f"Combined: {combined}")  # Playlist('Rock + Pop', 4 songs)

for song in rock:
    print(f"  Playing: {song}")

print(f"Reversed: {list(reversed(rock))}")  # ['Song B (Remix)', 'Song A']

print("=" * 5, "Arithmetic and bitwise operators", "=" * 5)

class Fraction:
    """Fraction class demonstrating arithmetic operator overloading."""

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        # Simplify using GCD
        from math import gcd
        g = gcd(numerator, denominator)
        self.num = numerator // g
        self.den = denominator // g
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)
        return Fraction(self.num + other * self.den, self.den)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)
        return Fraction(self.num - other * self.den, self.den)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.den * other.den)
        return Fraction(self.num * other, self.den)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.den, self.den * other.num)
        return Fraction(self.num, self.den * other)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num == other.num and self.den == other.den
        return self.num == other * self.den

    def __float__(self):
        return self.num / self.den

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f"{f1} + {f2} = {f1 + f2}")  # 1/2 + 1/3 = 5/6
print(f"{f1} - {f2} = {f1 - f2}")  # 1/2 - 1/3 = 1/6
print(f"{f1} * {f2} = {f1 * f2}")  # 1/2 * 1/3 = 1/6
print(f"{f1} / {f2} = {f1 / f2}")  # 1/2 / 1/3 = 3/2
print(f"{f1} == {f2}: {f1 == f2}")  # False
print(f"float({f1}) = {float(f1)}")  # 0.5

print("=" * 5, "Type conversion methods", "=" * 5)

class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"{self.temperature:.1f}°C"

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

    def __bool__(self):
        return self.temperature != 0

    def __abs__(self):
        return Celsius(abs(self.temperature))

    def __round__(self, n=0):
        return Celsius(round(self.temperature, n))

c = Celsius(36.6)
print(f"str: {str(c)}")  # 36.6°C
print(f"int: {int(c)}")  # 36
print(f"float: {float(c)}")  # 36.6
print(f"bool: {bool(c)}")  # True
print(f"bool(0°C): {bool(Celsius(0))}")  # False
print(f"abs: {abs(Celsius(-5))}")  # 5.0°C
print(f"round: {round(Celsius(36.63), 1)}")  # 36.6°C