# Polymorphism and duck typing

print("=" * 5, "Polymorphism through inheritance", "=" * 5)

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Polymorphic function — works with any Animal subclass
def make_sound(animal):
    print(f"{animal.__class__.__name__}: {animal.speak()}")

animals = [Dog(), Cat(), Duck()]
for animal in animals:
    make_sound(animal)
# Dog: Woof!
# Cat: Meow!
# Duck: Quack!

print("=" * 5, "Duck typing", "=" * 5)

# "If it walks like a duck and quacks like a duck, it's a duck"
# Python doesn't require inheritance — just matching methods

class PDFDocument:
    def read(self):
        return "Reading PDF document"

class TextDocument:
    def read(self):
        return "Reading text document"

class SpreadsheetDocument:
    def read(self):
        return "Reading spreadsheet"

# No common base class needed — duck typing
def open_document(doc):
    return doc.read()  # works with any object that has a read() method

pdf = PDFDocument()
txt = TextDocument()
xls = SpreadsheetDocument()

print(open_document(pdf))  # Reading PDF document
print(open_document(txt))  # Reading text document
print(open_document(xls))  # Reading spreadsheet

# Duck typing with built-in types
class CustomContainer:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        return iter(self.items)

container = CustomContainer([1, 2, 3, 4, 5])
print(f"Length: {len(container)}")  # 5
print(f"Index 0: {container[0]}")  # 1
print(f"Iteration: {list(container)}")  # [1, 2, 3, 4, 5]

print("=" * 5, "Operator overloading", "=" * 5)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Arithmetic operators
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Comparison operators
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    # String representation
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Container protocol
    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError(f"Vector index out of range: {index}")

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Addition: {v1 + v2}")  # (4, 6)
print(f"Subtraction: {v1 - v2}")  # (2, 2)
print(f"Scalar multiply: {v1 * 3}")  # (9, 12)
print(f"Reverse multiply: {3 * v1}")  # (9, 12)
print(f"Division: {v2 / 2}")  # (0.5, 1.0)
print(f"Negation: {-v1}")  # (-3, -4)
print(f"Magnitude: {abs(v1):.2f}")  # 5.00
print(f"Equality: {Vector(1, 2) == Vector(1, 2)}")  # True
print(f"Less than: {v2 < v1}")  # True
print(f"Length: {len(v1)}")  # 2
print(f"Indexing: v1[0]={v1[0]}, v1[1]={v1[1]}")  # v1[0]=3, v1[1]=4

print("=" * 5, "Common dunder methods", "=" * 5)

class Money:
    """Demonstrates common dunder (magic) methods."""
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    # __str__ and __repr__
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

    # __eq__, __ne__, __hash__
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __hash__(self):
        return hash((self.amount, self.currency))

    # __lt__, __le__, __gt__, __ge__
    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        return self.amount < other.amount

    # __bool__
    def __bool__(self):
        return self.amount != 0

    # __add__, __sub__
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        return Money(self.amount - other.amount, self.currency)

    # __format__
    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.currency}{self.amount:.0f}"
        elif format_spec == "long":
            return f"{self.amount:.2f} {self.currency}"
        return str(self)

m1 = Money(100, "USD")
m2 = Money(50, "USD")
m3 = Money(0, "USD")

print(f"str: {str(m1)}")  # USD 100.00
print(f"repr: {repr(m1)}")  # Money(100, 'USD')
print(f"Add: {m1 + m2}")  # USD 150.00
print(f"Sub: {m1 - m2}")  # USD 50.00
print(f"Equal: {Money(100, 'USD') == Money(100, 'USD')}")  # True
print(f"Less than: {m2 < m1}")  # True
print(f"Bool (nonzero): {bool(m1)}")  # True
print(f"Bool (zero): {bool(m3)}")  # False
print(f"Format short: {m1:short}")  # USD100
print(f"Format long: {m1:long}")  # 100.00 USD

print("=" * 5, "Callable objects with __call__", "=" * 5)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# Callable objects are function-like
print(f"Is callable: {callable(double)}")  # True

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

print("=" * 5, "Context manager with __enter__ and __exit__", "=" * 5)

class Timer:
    import time

    def __enter__(self):
        self.start = self.time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = self.time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.6f} seconds")
        return False

with Timer():
    total = sum(range(1000000))
# Elapsed time: 0.XXXXXX seconds

class IndentPrinter:
    def __init__(self, prefix="  "):
        self.prefix = prefix
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
        return False

    def write(self, text):
        print(f"{self.prefix * self.level}{text}")

printer = IndentPrinter("  ")
printer.write("Level 0")
with printer:
    printer.write("Level 1")
    with printer:
        printer.write("Level 2")
    printer.write("Back to Level 1")
printer.write("Back to Level 0")
# Level 0
#   Level 1
#     Level 2
#   Back to Level 1
# Back to Level 0