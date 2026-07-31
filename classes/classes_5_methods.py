# Class methods, static methods, and the @property pattern

print("=" * 5, "Instance methods, class methods, and static methods", "=" * 5)

class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    # Instance method — takes self as first argument
    def instance_method(self):
        return f"Instance method: self.instance_variable = {self.instance_variable}"

    # Class method — takes cls as first argument
    @classmethod
    def class_method(cls):
        return f"Class method: cls.class_variable = {cls.class_variable}"

    # Static method — takes no implicit arguments
    @staticmethod
    def static_method(x, y):
        return f"Static method: {x} + {y} = {x + y}"

obj = MyClass(42)

# Instance method — called on the instance
print(obj.instance_method())  # Instance method: self.instance_variable = 42

# Class method — can be called on class or instance
print(MyClass.class_method())  # Class method: cls.class_variable = 0
print(obj.class_method())  # Class method: cls.class_variable = 0

# Static method — can be called on class or instance
print(MyClass.static_method(3, 5))  # Static method: 3 + 5 = 8
print(obj.static_method(3, 5))  # Static method: 3 + 5 = 8

print("=" * 5, "Class methods as alternative constructors", "=" * 5)

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    @classmethod
    def from_dict(cls, data):
        """Create a Person from a dictionary."""
        return cls(name=data["name"], age=data["age"])

    @classmethod
    def from_string(cls, text):
        """Create a Person from a comma-separated string."""
        name, age = text.split(",")
        return cls(name=name.strip(), age=int(age.strip()))

    @classmethod
    def from_json(cls, json_string):
        """Create a Person from a JSON string."""
        data = json.loads(json_string)
        return cls(name=data["name"], age=data["age"])

    @classmethod
    def default(cls):
        """Create a Person with default values."""
        return cls(name="Unknown", age=0)

# Standard constructor
p1 = Person("Alice", 30)
print(p1)  # Person(name='Alice', age=30)

# Alternative constructors
p2 = Person.from_dict({"name": "Bob", "age": 25})
print(p2)  # Person(name='Bob', age=25)

p3 = Person.from_string("Charlie, 35")
print(p3)  # Person(name='Charlie', age=35)

p4 = Person.from_json('{"name": "Diana", "age": 28}')
print(p4)  # Person(name='Diana', age=28)

p5 = Person.default()
print(p5)  # Person(name='Unknown', age=0)

print("=" * 5, "Static methods: utility functions in class namespace", "=" * 5)

class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // MathUtils.gcd(a, b)

print(f"Is 4 even? {MathUtils.is_even(4)}")  # True
print(f"Is 7 prime? {MathUtils.is_prime(7)}")  # True
print(f"GCD of 12 and 8: {MathUtils.gcd(12, 8)}")  # 4
print(f"LCM of 12 and 8: {MathUtils.lcm(12, 8)}")  # 24

print("=" * 5, "Practical example: Date class", "=" * 5)

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.year}, {self.month:02d}, {self.day:02d})"

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    @classmethod
    def from_string(cls, date_string):
        """Create Date from 'YYYY-MM-DD' format."""
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    @classmethod
    def from_tuple(cls, date_tuple):
        """Create Date from (year, month, day) tuple."""
        year, month, day = date_tuple
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Create Date from today's date."""
        from datetime import date
        t = date.today()
        return cls(t.year, t.month, t.day)

    @staticmethod
    def is_valid_date(year, month, day):
        """Check if the given year, month, day form a valid date."""
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month in (4, 6, 9, 11) and day > 30:
            return False
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return day <= 29
            return day <= 28
        return True

d1 = Date(2025, 7, 31)
d2 = Date.from_string("2025-01-15")
d3 = Date.from_tuple((2025, 12, 25))

print(f"d1: {d1}")  # 2025-07-31
print(f"d2: {d2}")  # 2025-01-15
print(f"d3: {d3}")  # 2025-12-25
print(f"repr: {repr(d1)}")  # Date(2025, 07, 31)
print(f"d1 == d2: {d1 == d2}")  # False
print(f"d2 < d1: {d2 < d1}")  # True
print(f"Valid date: {Date.is_valid_date(2025, 2, 28)}")  # True
print(f"Invalid date: {Date.is_valid_date(2025, 2, 30)}")  # False
print(f"Today: {Date.today()}")  # current date

print("=" * 5, "Class method for tracking instances", "=" * 5)

class Student:
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1
        self.id = Student.total_students

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', grade={self.grade})"

    @classmethod
    def get_total(cls):
        return cls.total_students

    @classmethod
    def from_grade_file(cls, filename):
        """Example: create students from a file."""
        students = []
        # Simulated file data
        data = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
        for name, grade in data:
            students.append(cls(name, grade))
        return students

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)
s3 = Student("Charlie", 92)

print(f"Total students: {Student.get_total()}")  # 3
print(f"s1: {s1}")  # Student(id=1, name='Alice', grade=90)
print(f"s2: {s2}")  # Student(id=2, name='Bob', grade=85)

batch = Student.from_grade_file("grades.txt")
print(f"Batch size: {len(batch)}")  # 3
print(f"Total after batch: {Student.get_total()}")  # 6