# match-case statement (Python 3.10+)
# Similar to switch-case in other languages

# Basic match-case with literals
command = "start"

match command:
    case "start":
        print("Starting...")  # Starting...
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:
        print("Unknown command")

# match-case with multiple patterns (OR pattern)
status = "warn"

match status:
    case "error" | "critical":
        print("Critical issue!")  # not matched
    case "warn" | "warning":
        print("Warning issued")  # Warning issued
    case "ok" | "success":
        print("All good")
    case _:
        print("Unknown status")

# match-case with variable binding
point = (3, 5)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at x={x}")
    case (0, y):
        print(f"On y-axis at y={y}")
    case (x, y):
        print(f"Point at ({x}, {y})")  # Point at (3, 5)

# match-case with type matching
value = [1, 2, 3]

match value:
    case int(n):
        print(f"Integer: {n}")
    case float(n):
        print(f"Float: {n}")
    case str(s):
        print(f"String: {s}")
    case list(l):
        print(f"List: {l}")  # List: [1, 2, 3]
    case dict(d):
        print(f"Dict: {d}")
    case _:
        print(f"Unknown type: {type(value)}")

# match-case with list patterns
data = [1, 2, 3, 4, 5]

match data:
    case []:
        print("Empty list")
    case [x]:
        print(f"Single element: {x}")
    case [x, y]:
        print(f"Two elements: {x}, {y}")
    case [x, y, *rest]:
        print(f"First: {x}, Second: {y}, Rest: {rest}")  # First: 1, Second: 2, Rest: [3, 4, 5]

# match-case with dict patterns
person = {"name": "Alice", "age": 30}

match person:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")  # Name: Alice, Age: 30
    case {"name": name}:
        print(f"Name: {name}")
    case _:
        print("Unknown format")

# match-case with guard (if clause)
number = 15

match number:
    case n if n < 0:
        print("Negative")
    case n if n % 2 == 0:
        print("Even positive")
    case n if n % 2 != 0:
        print("Odd positive")  # Odd positive
    case _:
        print("Unknown")

# match-case with class instances
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)

match p:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=x, y=0):
        print(f"On x-axis at {x}")
    case Point(x=0, y=y):
        print(f"On y-axis at {y}")
    case Point(x=x, y=y) if x == y:
        print(f"On diagonal at ({x}, {y})")
    case Point(x=x, y=y):
        print(f"Point at ({x}, {y})")  # Point at (3, 4)

# match-case with nested patterns
command = ("move", 10, 20)

match command:
    case ("quit",):
        print("Quitting")
    case ("move", dx, dy):
        print(f"Moving by ({dx}, {dy})")  # Moving by (10, 20)
    case ("attack", target):
        print(f"Attacking {target}")
    case _:
        print("Unknown command")