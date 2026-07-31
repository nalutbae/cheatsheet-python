# Enumerations and naming patterns

from enum import Enum, IntEnum, Flag, IntFlag, auto
from typing import NamedTuple

print("=" * 5, "Basic Enum", "=" * 5)

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

# Accessing enum members
print(Color.RED)  # Color.RED
print(Color.RED.name)  # RED
print(Color.RED.value)  # red

# Access by name
print(Color["RED"])  # Color.RED

# Access by value
print(Color("red"))  # Color.RED

# Iteration
for color in Color:
    print(f"  {color.name} = {color.value}")
# RED = red
# GREEN = green
# BLUE = blue

# Comparison
print(f"Color.RED == Color.RED: {Color.RED == Color.RED}")  # True
print(f"Color.RED == Color.BLUE: {Color.RED == Color.BLUE}")  # False
print(f"Color.RED is Color.RED: {Color.RED is Color.RED}")  # True

# Enums are singletons
a = Color.RED
b = Color.RED
print(f"a is b: {a is b}")  # True

# Cannot compare different enum types
class Shape(Enum):
    CIRCLE = "circle"

# Color.RED == Shape.CIRCLE  # False in Python 3.11+; TypeError in earlier

# Using in if/elif
def describe_color(color):
    if color == Color.RED:
        return "Hot and fiery"
    elif color == Color.GREEN:
        return "Fresh and natural"
    elif color == Color.BLUE:
        return "Cool and calm"
    return "Unknown color"

print(describe_color(Color.RED))  # Hot and fiery
print(describe_color(Color.GREEN))  # Fresh and natural

# Using in dictionaries as keys
color_hex = {
    Color.RED: "#FF0000",
    Color.GREEN: "#00FF00",
    Color.BLUE: "#0000FF",
}
print(f"Hex for RED: {color_hex[Color.RED]}")  # #FF0000

print("=" * 5, "IntEnum (integer values)", "=" * 5)

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

# IntEnum members are also integers
print(f"Priority.HIGH: {Priority.HIGH}")  # Priority.HIGH
print(f"Priority.HIGH.value: {Priority.HIGH.value}")  # 3
print(f"Priority.HIGH == 3: {Priority.HIGH == 3}")  # True
print(f"Priority.HIGH > Priority.MEDIUM: {Priority.HIGH > Priority.MEDIUM}")  # True

# Sorting IntEnum values
priorities = [Priority.CRITICAL, Priority.LOW, Priority.HIGH, Priority.MEDIUM]
sorted_priorities = sorted(priorities)
print(f"Sorted: {sorted_priorities}")  # [Priority.LOW, Priority.MEDIUM, Priority.HIGH, Priority.CRITICAL]

# IntEnum in switch-like patterns
def handle_priority(priority):
    match priority:
        case Priority.LOW:
            return "Handle when convenient"
        case Priority.MEDIUM:
            return "Handle soon"
        case Priority.HIGH:
            return "Handle promptly"
        case Priority.CRITICAL:
            return "Handle immediately!"

print(handle_priority(Priority.HIGH))  # Handle promptly

print("=" * 5, "auto() for automatic values", "=" * 5)

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

for d in Direction:
    print(f"  {d.name} = {d.value}")
# NORTH = 1
# SOUTH = 2
# EAST = 3
# WEST = 4

# Custom auto values
class Status(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    PENDING = auto()
    ACTIVE = auto()
    COMPLETED = auto()
    FAILED = auto()

for s in Status:
    print(f"  {s.name} = {s.value}")
# PENDING = pending
# ACTIVE = active
# COMPLETED = completed
# FAILED = failed

print("=" * 5, "Flag and IntFlag (bitwise combinations)", "=" * 5)

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

# Single flag
print(Permission.READ)  # Permission.READ

# Combining flags with bitwise OR
rw = Permission.READ | Permission.WRITE
print(f"READ|WRITE: {rw}")  # Permission.READ|WRITE
print(f"Has READ: {Permission.READ in rw}")  # True
print(f"Has EXECUTE: {Permission.EXECUTE in rw}")  # False

# Checking flags with bitwise AND
print(f"rw & READ: {bool(rw & Permission.READ)}")  # True
print(f"rw & EXECUTE: {bool(rw & Permission.EXECUTE)}")  # False

# All flags
all_perms = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(f"All permissions: {all_perms}")  # Permission.READ|WRITE|EXECUTE

# IntFlag allows integer operations
class FileMode(IntFlag):
    READ = 1
    WRITE = 2
    APPEND = 4
    BINARY = 8

mode = FileMode.READ | FileMode.BINARY
print(f"Mode: {mode}")  # FileMode.READ|BINARY
print(f"Mode value: {mode.value}")  # 9
print(f"Has READ: {bool(mode & FileMode.READ)}")  # True
print(f"Has WRITE: {bool(mode & FileMode.WRITE)}")  # False

print("=" * 5, "NamedTuple", "=" * 5)

# NamedTuple: immutable, named fields, lightweight
class Point(NamedTuple):
    x: float
    y: float

p = Point(3.0, 4.0)
print(p)  # Point(x=3.0, y=4.0)
print(f"x={p.x}, y={p.y}")  # x=3.0, y=4.0
print(f"Index 0={p[0]}, Index 1={p[1]}")  # Index 0=3.0, Index 1=4.0

# NamedTuple features
print(f"Fields: {p._fields}")  # ('x', 'y')
print(f"As dict: {p._asdict()}")  # {'x': 3.0, 'y': 4.0}

# _replace creates a new instance with changed fields
p2 = p._replace(x=5.0)
print(f"Replaced: {p2}")  # Point(x=5.0, y=4.0)
print(f"Original unchanged: {p}")  # Point(x=3.0, y=4.0)

# Immutable — cannot change fields
try:
    p.x = 10.0
except AttributeError as e:
    print(f"Error: {e}")  # can't set attribute

# NamedTuple with default values
class Student(NamedTuple):
    name: str
    grade: float
    school: str = "Unknown"

s = Student("Alice", 95.0)
print(s)  # Student(name='Alice', grade=95.0, school='Unknown')

# Alternative: functional syntax
ColorRGB = NamedTuple("ColorRGB", [("red", int), ("green", int), ("blue", int)])
c = ColorRGB(255, 128, 0)
print(c)  # ColorRGB(red=255, green=128, blue=0)

print("=" * 5, "Comparison: Enum vs dataclass vs NamedTuple", "=" * 5)

# Use Enum when you have a fixed set of named constants
# Use dataclass when you need mutable data with methods
# Use NamedTuple when you need lightweight immutable records

# Enum: fixed set of choices
class HttpStatus(Enum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

# dataclass: rich data with behavior
@dataclass
class HttpResponse:
    status: HttpStatus
    body: str
    headers: dict = field(default_factory=dict)

# NamedTuple: lightweight immutable record
class HttpHeader(NamedTuple):
    name: str
    value: str

header = HttpHeader("Content-Type", "application/json")
response = HttpResponse(HttpStatus.OK, '{"message": "hello"}', {"Content-Type": "application/json"})

print(f"Status: {response.status.name} ({response.status.value})")  # OK (200)
print(f"Header: {header}")  # HttpHeader(name='Content-Type', value='application/json')