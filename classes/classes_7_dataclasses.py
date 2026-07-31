# Data classes: a decorator for classes that primarily store data

from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional

print("=" * 5, "Basic dataclass", "=" * 5)

@dataclass
class Point:
    x: float
    y: float

p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)
p3 = Point(0.0, 0.0)

print(p1)  # Point(x=3.0, y=4.0)
print(f"Equality: {p1 == p2}")  # True (auto-generated __eq__)
print(f"Inequality: {p1 == p3}")  # False

# Dataclasses are mutable by default
p1.x = 5.0
print(f"After mutation: {p1}")  # Point(x=5.0, y=4.0)

# Unpacking with astuple
p = Point(1.0, 2.0)
print(f"Tuple: {astuple(p)}")  # (1.0, 2.0)
print(f"Dict: {asdict(p)}")  # {'x': 1.0, 'y': 2.0}

print("=" * 5, "Default values and field()", "=" * 5)

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)
    discount: Optional[float] = None

    @property
    def total(self):
        subtotal = self.price * self.quantity
        if self.discount:
            subtotal *= (1 - self.discount)
        return subtotal

p1 = Product("Laptop", 999.99, 5)
p2 = Product("Phone", 699.99, 3, tags=["electronics", "mobile"])
p3 = Product("Tablet", 499.99, 2, discount=0.1)

print(p1)  # Product(name='Laptop', price=999.99, quantity=5, tags=[], discount=None)
print(p2)  # Product(name='Phone', price=699.99, quantity=3, tags=['electronics', 'mobile'], discount=None)
print(p3)  # Product(name='Tablet', price=499.99, quantity=2, tags=[], discount=0.1)
print(f"Total: ${p3.total:.2f}")  # Total: $899.98

# field() options
@dataclass
class Config:
    name: str
    value: int = field(default=0)
    readonly: bool = field(default=False, repr=False)  # excluded from repr
    internal_id: int = field(default_factory=lambda: id(object()), repr=False, compare=False)

c = Config("test", value=42, readonly=True)
print(c)  # Config(name='test', value=42) — readonly and internal_id hidden from repr

print("=" * 5, "Frozen dataclass (immutable)", "=" * 5)

@dataclass(frozen=True)
class Coordinate:
    latitude: float
    longitude: float

loc1 = Coordinate(37.5665, 126.9780)
loc2 = Coordinate(37.5665, 126.9780)

print(loc1)  # Coordinate(latitude=37.5665, longitude=126.9780)
print(f"Equality: {loc1 == loc2}")  # True

# Cannot modify frozen dataclass
try:
    loc1.latitude = 35.0
except AttributeError as e:
    print(f"Error: {e}")  # cannot assign to field 'latitude'

# Frozen dataclasses are hashable — can be used in sets and dicts
locations = {loc1, loc2}
print(f"Set size: {len(locations)}")  # 1 (loc1 == loc2, so only one unique)

print("=" * 5, "Inheritance with dataclasses", "=" * 5)

@dataclass
class Employee:
    name: str
    employee_id: int

@dataclass
class Manager(Employee):
    department: str
    reports: List[str] = field(default_factory=list)

m = Manager("Alice", 1001, "Engineering", ["Bob", "Charlie"])
print(m)  # Manager(name='Alice', employee_id=1001, department='Engineering', reports=['Bob', 'Charlie'])

# Inheritance with default values — fields without defaults must come before fields with defaults
@dataclass
class Shape:
    name: str
    color: str = "black"

@dataclass
class CircleShape(Shape):
    radius: float = 1.0

cs = CircleShape("my circle", radius=5.0)
print(cs)  # CircleShape(name='my circle', color='black', radius=5.0)

print("=" * 5, "Ordering with dataclasses", "=" * 5)

@dataclass(order=True)
class Student:
    name: str = field(compare=False)  # excluded from comparison
    grade: float
    student_id: int = field(compare=False)  # excluded from comparison

s1 = Student("Alice", 90.5, 1)
s2 = Student("Bob", 85.0, 2)
s3 = Student("Charlie", 90.5, 3)

print(f"s1 < s2: {s1 < s2}")  # False (90.5 > 85.0)
print(f"s2 < s1: {s2 < s1}")  # True (85.0 < 90.5)
print(f"s1 == s3: {s1 == s3}")  # True (same grade, name and id excluded from comparison)

students = [s1, s2, s3]
sorted_students = sorted(students)
print(f"Sorted by grade: {[(s.name, s.grade) for s in sorted_students]}")  # [('Bob', 85.0), ('Alice', 90.5), ('Charlie', 90.5)]

print("=" * 5, "post_init for computed fields", "=" * 5)

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)  # not passed to __init__
    perimeter: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)

r = Rectangle(3, 4)
print(r)  # Rectangle(width=3, height=4, area=12.0, perimeter=14.0)
print(f"Area: {r.area}")  # 12.0
print(f"Perimeter: {r.perimeter}")  # 14.0

# __post_init__ with validation
@dataclass
class Temperature:
    celsius: float

    def __post_init__(self):
        if self.celsius < -273.15:
            raise ValueError(f"Temperature cannot be below -273.15°C, got {self.celsius}")

t = Temperature(25.0)
print(f"Temperature: {t.celsius}°C")  # 25.0°C

try:
    invalid = Temperature(-300)
except ValueError as e:
    print(f"Error: {e}")  # Temperature cannot be below -273.15°C, got -300

print("=" * 5, "Conversion utilities", "=" * 5)

@dataclass
class Book:
    title: str
    author: str
    pages: int
    isbn: str = ""

b = Book("1984", "George Orwell", 328, "978-0451524935")

# asdict: convert dataclass to dictionary
d = asdict(b)
print(f"Dict: {d}")  # {'title': '1984', 'author': 'George Orwell', 'pages': 328, 'isbn': '978-0451524935'}

# astuple: convert dataclass to tuple
t = astuple(b)
print(f"Tuple: {t}")  # ('1984', 'George Orwell', 328, '978-0451524935')

# Creating from a dictionary (unpacking)
data = {"title": "Brave New World", "author": "Aldous Huxley", "pages": 311, "isbn": "978-0060850524"}
b2 = Book(**data)
print(f"From dict: {b2}")  # Book(title='Brave New World', author='Aldous Huxley', pages=311, isbn='978-0060850524')

# Replacing values with dataclasses.replace
from dataclasses import replace

b3 = replace(b, pages=350, title="Nineteen Eighty-Four")
print(f"Original: {b}")  # Book(title='1984', ...)
print(f"Replaced: {b3}")  # Book(title='Nineteen Eighty-Four', pages=350, ...)

# replace creates a new instance — original is unchanged
print(f"Original pages: {b.pages}")  # 328