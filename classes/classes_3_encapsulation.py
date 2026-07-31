# Encapsulation: controlling access to attributes

print("=" * 5, "Public, protected, and private attributes", "=" * 5)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # public attribute
        self._bank_code = "BANK001"  # protected (convention: single underscore)
        self.__balance = balance     # private (name mangling: double underscore)

    # Getter for private attribute
    def get_balance(self):
        return self.__balance

    # Setter for private attribute
    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance

    def __private_method(self):
        """Private method — name mangled."""
        return "This is private"

    def public_method(self):
        """Public method can call private method."""
        return self.__private_method()

account = BankAccount("Alice", 1000)

# Public attribute — accessible directly
print(f"Owner: {account.owner}")  # Alice

# Protected attribute — accessible but convention says "don't touch"
print(f"Bank code: {account._bank_code}")  # BANK001 (accessible but not recommended)

# Private attribute — name mangled, not directly accessible
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Access private attribute through getter
print(f"Balance: {account.get_balance()}")  # 1000

# Modify private attribute through setter
account.set_balance(2000)
print(f"New balance: {account.get_balance()}")  # 2000

# Deposit and withdraw
print(f"After deposit: {account.deposit(500)}")  # 2500
print(f"After withdraw: {account.withdraw(1000)}")  # 1500

# Private method — not directly accessible
# account.__private_method()  # AttributeError

# Access private method through public method
print(account.public_method())  # This is private

# Name mangling: private attributes are accessible as _ClassName__attr
print(f"Mangled access: {account._BankAccount__balance}")  # 1500
print(f"Mangled method: {account._BankAccount__private_method()}")  # This is private

print("=" * 5, "Property decorator: Pythonic getters and setters", "=" * 5)

class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius  # uses the setter below

    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation."""
        if value < -273.15:
            raise ValueError(f"Temperature cannot be below -273.15°C, got {value}")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit (computed, no setter)."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature from Fahrenheit."""
        self.celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self):
        """Get temperature in Kelvin (computed)."""
        return self._celsius + 273.15

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")  # 25
print(f"Fahrenheit: {temp.fahrenheit}")  # 77.0
print(f"Kelvin: {temp.kelvin}")  # 298.15

# Set via property
temp.celsius = 100
print(f"100°C = {temp.fahrenheit}°F")  # 100°C = 212.0°F

# Set fahrenheit — converts and stores as celsius
temp.fahrenheit = 32
print(f"32°F = {temp.celsius}°C")  # 32°F = 0.0°C

# Validation works through property
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")  # Temperature cannot be below -273.15°C, got -300

# fahrenheit is read-write, kelvin is read-only
# temp.kelvin = 0  # AttributeError: can't set attribute

print("=" * 5, "Read-only and computed properties", "=" * 5)

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def diameter(self):
        """Computed property — read-only."""
        return self._radius * 2

    @property
    def area(self):
        """Computed property — read-only."""
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        """Computed property — read-only."""
        import math
        return 2 * math.pi * self._radius

c = Circle(5)
print(f"Radius: {c.radius}")  # 5
print(f"Diameter: {c.diameter}")  # 10
print(f"Area: {c.area:.2f}")  # 78.54
print(f"Circumference: {c.circumference:.2f}")  # 31.42

# Computed properties are always up to date
c.radius = 10
print(f"New diameter: {c.diameter}")  # 20
print(f"New area: {c.area:.2f}")  # 314.16

# diameter, area, circumference are read-only
# c.diameter = 20  # AttributeError: can't set attribute

print("=" * 5, "Deleting attributes with @property.deleter", "=" * 5)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @salary.deleter
    def salary(self):
        print("Salary has been cleared")
        del self._salary

emp = Employee("Alice", 50000)
print(f"Salary: {emp.salary}")  # 50000

emp.salary = 60000
print(f"Updated salary: {emp.salary}")  # 60000

del emp.salary  # Salary has been cleared
# emp.salary  # AttributeError: 'Employee' object has no attribute '_salary'

# Re-assign after deletion
emp.salary = 70000
print(f"Re-assigned salary: {emp.salary}")  # 70000

print("=" * 5, "__slots__: restricting attribute creation", "=" * 5)

class Point:
    __slots__ = ("x", "y")  # only allow x and y attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(f"Point: ({p.x}, {p.y})")  # Point: (3, 4)

p.x = 10
print(f"Updated x: {p.x}")  # 10

# Cannot add new attributes
try:
    p.z = 5
except AttributeError as e:
    print(f"Error: {e}")  # 'Point' object has no attribute 'z'

# No __dict__ when using __slots__
# print(p.__dict__)  # AttributeError: 'Point' object has no attribute '__dict__'

# Memory savings with __slots__
import sys

class PointWithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointWithSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = PointWithDict(1, 2)
p2 = PointWithSlots(1, 2)

print(f"With __dict__: {sys.getsizeof(p1)} bytes")  # ~56 bytes
print(f"With __slots__: {sys.getsizeof(p2)} bytes")  # ~48 bytes (smaller)