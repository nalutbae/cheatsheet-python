# Inheritance: creating subclasses from parent classes

print("=" * 5, "Basic inheritance", "=" * 5)

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def info(self):
        return f"{self.name} (sound: {self.sound})"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
print(f"Dog breed: {dog.breed}")  # Dog breed: Golden Retriever
print(f"Cat indoor: {cat.indoor}")  # Cat indoor: True

print("=" * 5, "super() for calling parent methods", "=" * 5)

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} ({self.year})"

class ElectricCar(Vehicle):
    def __init__(self, brand, year, battery_kwh):
        super().__init__(brand, year)  # call parent __init__
        self.battery_kwh = battery_kwh

    def info(self):
        base_info = super().info()  # call parent method
        return f"{base_info}, Battery: {self.battery_kwh}kWh"

car = ElectricCar("Tesla", 2024, 75)
print(car.info())  # Tesla (2024), Battery: 75kWh

# super() with multiple inheritance (MRO order)
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B, " + super().greet()

class C(A):
    def greet(self):
        return "Hello from C, " + super().greet()

class D(B, C):
    def greet(self):
        return "Hello from D, " + super().greet()

d = D()
print(d.greet())  # Hello from D, Hello from B, Hello from C, Hello from A
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")  # ['D', 'B', 'C', 'A', 'object']

print("=" * 5, "Method overriding", "=" * 5)

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def __str__(self):
        return f"{self.name}: area = {self.area()}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape)
# Circle: area = 78.53981633974483
# Square: area = 16

print("=" * 5, "isinstance() and issubclass()", "=" * 5)

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(f"isinstance(dog, Dog): {isinstance(dog, Dog)}")  # True
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")  # True
print(f"isinstance(dog, Cat): {isinstance(dog, Cat)}")  # False
print(f"isinstance(dog, object): {isinstance(dog, object)}")  # True

# Check against multiple types
print(f"isinstance(dog, (Dog, Cat)): {isinstance(dog, (Dog, Cat))}")  # True

print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")  # True
print(f"issubclass(Cat, Animal): {issubclass(Cat, Animal)}")  # True
print(f"issubclass(Dog, Cat): {issubclass(Dog, Cat)}")  # False
print(f"issubclass(Animal, object): {issubclass(Animal, object)}")  # True

print("=" * 5, "Multiple inheritance", "=" * 5)

class Swimmer:
    def swim(self):
        return "Swimming"

class Flyer:
    def fly(self):
        return "Flying"

class Duck(Swimmer, Flyer):
    def quack(self):
        return "Quack!"

donald = Duck()
print(donald.swim())  # Swimming
print(donald.fly())  # Flying
print(donald.quack())  # Quack!

# Diamond problem: MRO resolves it
class Base:
    def method(self):
        return "Base"

class Left(Base):
    def method(self):
        return "Left"

class Right(Base):
    def method(self):
        return "Right"

class Child(Left, Right):
    pass

c = Child()
print(c.method())  # Left (MRO: Child → Left → Right → Base)

# View MRO
print(f"MRO: {[cls.__name__ for cls in Child.__mro__]}")  # ['Child', 'Left', 'Right', 'Base', 'object']

print("=" * 5, "Abstract base classes (ABC)", "=" * 5)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

# Cannot instantiate an abstract class
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

c = Circle(5)
r = Rectangle(3, 4)

print(c.describe())  # Circle: area=78.54, perimeter=31.42
print(r.describe())  # Rectangle: area=12.00, perimeter=14.00

print(f"isinstance(c, Shape): {isinstance(c, Shape)}")  # True

print("=" * 5, "Mixins", "=" * 5)

class JsonMixin:
    """Mixin that adds JSON serialization."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__, default=str)

class LogMixin:
    """Mixin that adds logging capability."""
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class User(JsonMixin, LogMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(user.to_json())  # {"name": "Alice", "email": "alice@example.com"}
user.log("User created")  # [User] User created