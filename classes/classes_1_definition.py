# Class definition, instantiation, and basic attributes

print("=" * 5, "Defining a class", "=" * 5)

# Simple class with no methods
class Dog:
    """A simple class representing a dog."""
    pass

# Creating an instance
dog1 = Dog()
dog1.name = "Buddy"
dog1.age = 3
print(f"{dog1.name} is {dog1.age} years old")  # Buddy is 3 years old

# Each instance is independent
dog2 = Dog()
dog2.name = "Max"
dog2.age = 5
print(f"{dog2.name} is {dog2.age} years old")  # Max is 5 years old

print("=" * 5, "__init__ constructor and self", "=" * 5)

class Person:
    """A class with an initializer."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}, age {self.age}"

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1.greet())  # Hi, I'm Alice, age 30
print(p2.greet())  # Hi, I'm Bob, age 25

# self refers to the instance, not the class
print(f"p1.name: {p1.name}")  # Alice
print(f"p2.name: {p2.name}")  # Bob

print("=" * 5, "Instance attributes vs class attributes", "=" * 5)

class Car:
    # Class attribute — shared by all instances
    wheel_count = 4
    category = "vehicle"

    def __init__(self, brand, model):
        # Instance attributes — unique to each instance
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Access class attributes from instances
print(f"car1.wheel_count: {car1.wheel_count}")  # 4
print(f"car2.wheel_count: {car2.wheel_count}")  # 4

# Access class attribute from the class
print(f"Car.wheel_count: {Car.wheel_count}")  # 4

# Modifying class attribute affects all instances
Car.wheel_count = 6
print(f"car1.wheel_count after class change: {car1.wheel_count}")  # 6
print(f"car2.wheel_count after class change: {car2.wheel_count}")  # 6

# Modifying instance attribute only affects that instance
car1.brand = "Lexus"
print(f"car1.brand: {car1.brand}")  # Lexus
print(f"car2.brand: {car2.brand}")  # Honda (unchanged)

# Assigning to an instance attribute shadows the class attribute
Car.wheel_count = 4  # reset
car1.wheel_count = 3  # creates instance attribute, shadows class
print(f"car1.wheel_count: {car1.wheel_count}")  # 3 (instance)
print(f"car2.wheel_count: {car2.wheel_count}")  # 4 (class)
print(f"Car.wheel_count: {Car.wheel_count}")  # 4 (class)

# Checking attribute ownership
print(f"'wheel_count' in car1.__dict__: {'wheel_count' in car1.__dict__}")  # True
print(f"'wheel_count' in car2.__dict__: {'wheel_count' in car2.__dict__}")  # False

print("=" * 5, "Instance methods", "=" * 5)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor
        return self

rect = Rectangle(3, 4)
print(f"Area: {rect.area()}")  # 12
print(f"Perimeter: {rect.perimeter()}")  # 14
print(f"Is square: {rect.is_square()}")  # False

rect.scale(2)
print(f"After scale: {rect.width} x {rect.height}")  # 6 x 8

# Method chaining by returning self
rect.scale(0.5).scale(3)
print(f"After chaining: {rect.width} x {rect.height}")  # 9 x 12

print("=" * 5, "String representation: __str__ and __repr__", "=" * 5)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Informal string — used by print() and str()."""
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """Official string — used by repr() and in containers."""
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 4)
print(str(p))   # Point(3, 4)
print(repr(p))  # Point(x=3, y=4)
print(p)         # Point(3, 4)  (uses __str__)

# Inside containers, __repr__ is used
points = [Point(1, 2), Point(3, 4)]
print(points)  # [Point(x=1, y=2), Point(x=3, y=4)]

# If only __repr__ is defined, it is also used by print()
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(5, 6)
print(v)        # Vector(5, 6)  (__repr__ fallback for __str__)
print(repr(v))  # Vector(5, 6)

print("=" * 5, "Deleting attributes and instances", "=" * 5)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
print(f"Title: {book.title}")  # Title: 1984

# Deleting an attribute
del book.title
# print(book.title)  # AttributeError: 'Book' object has no attribute 'title'

# Checking if attribute exists
print(f"hasattr(book, 'title'): {hasattr(book, 'title')}")  # False
print(f"hasattr(book, 'author'): {hasattr(book, 'author')}")  # True

# getattr with default value
print(f"getattr default: {getattr(book, 'title', 'Unknown')}")  # Unknown

# Deleting the entire instance reference
del book
# print(book)  # NameError: name 'book' is not defined

print("=" * 5, "Dynamic attribute assignment", "=" * 5)

class Flexible:
    """A class that accepts any attributes."""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

f = Flexible(name="Alice", age=30, city="Seoul")
print(f"{f.name}, {f.age}, {f.city}")  # Alice, 30, Seoul

# Adding attributes dynamically
f.email = "alice@example.com"
print(f"Email: {f.email}")  # Email: alice@example.com

# Using __dict__ to inspect all attributes
print(f"Attributes: {f.__dict__}")  # {'name': 'Alice', 'age': 30, 'city': 'Seoul', 'email': 'alice@example.com'}