# typing: type hints and annotations

from typing import (
    List, Dict, Set, Tuple, Optional, Union, Any, Callable,
    Iterable, Iterator, Generator, TypeVar, Generic, Protocol,
    Final, Literal, TypeAlias, TypedDict, overload
)
from collections.abc import Sequence, Mapping

print("=" * 5, "Basic type hints", "=" * 5)

# Function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!

# Multiple parameters with defaults
def search(query: str, limit: int = 10, case_sensitive: bool = False) -> list[str]:
    return [f"result_{i}" for i in range(limit)]

results = search("test", limit=3)
print(f"Search results: {results}")  # ['result_0', 'result_1', 'result_2']

# Optional parameters (can be None)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)

print(f"User 1: {find_user(1)}")  # Alice
print(f"User 99: {find_user(99)}")  # None

# Union types (multiple possible types)
def process_value(value: Union[int, float, str]) -> str:
    if isinstance(value, (int, float)):
        return f"Number: {value}"
    return f"String: {value}"

print(process_value(42))  # Number: 42
print(process_value(3.14))  # Number: 3.14
print(process_value("hello"))  # String: hello

# Modern union syntax (Python 3.10+)
def modern_union(value: int | float | str) -> str:
    return str(value)

print(modern_union(42))  # 42

print("=" * 5, "Collection types", "=" * 5)

# List type hints
def get_names() -> list[str]:
    return ["Alice", "Bob", "Charlie"]

def filter_positive(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n > 0]

print(filter_positive([-2, -1, 0, 1, 2, 3]))  # [1, 2, 3]

# Dict type hints
def count_words(text: str) -> dict[str, int]:
    words = text.lower().split()
    result: dict[str, int] = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

print(count_words("hello world hello"))  # {'hello': 2, 'world': 1}

# Set type hints
def unique_items(items: list[str]) -> set[str]:
    return set(items)

print(unique_items(["a", "b", "a", "c", "b"]))  # {'a', 'b', 'c'}

# Tuple type hints
def get_coordinates() -> tuple[float, float]:
    return (3.14, 2.71)

x, y = get_coordinates()
print(f"Coordinates: ({x}, {y})")  # (3.14, 2.71)

# Fixed-length tuple vs variable-length tuple
point: tuple[float, float] = (1.0, 2.0)  # exactly 2 floats
coordinates: tuple[int, ...] = (1, 2, 3, 4)  # any number of ints

print("=" * 5, "Callable and function types", "=" * 5)

# Callable type hint
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

def double(x: int) -> int:
    return x * 2

print(apply(double, 5))  # 10

# Callable with multiple parameters
def reduce_values(
    func: Callable[[int, int], int],
    values: list[int]
) -> int:
    result = values[0]
    for v in values[1:]:
        result = func(result, v)
    return result

print(reduce_values(lambda a, b: a + b, [1, 2, 3, 4]))  # 10

# Optional callable (callback pattern)
def process_data(data: list[int], callback: Optional[Callable[[int], str]] = None) -> list[str]:
    if callback:
        return [callback(x) for x in data]
    return [str(x) for x in data]

print(process_data([1, 2, 3]))  # ['1', '2', '3']
print(process_data([1, 2, 3], lambda x: f"item_{x}"))  # ['item_1', 'item_2', 'item_3']

print("=" * 5, "TypeVar: generic types", "=" * 5)

# TypeVar for generic functions
T = TypeVar("T")

def first(items: list[T]) -> Optional[T]:
    return items[0] if items else None

print(first([1, 2, 3]))  # 1
print(first(["a", "b", "c"]))  # a
print(first([]))  # None

def flatten(nested: list[list[T]]) -> list[T]:
    result: list[T] = []
    for sublist in nested:
        result.extend(sublist)
    return result

print(flatten([[1, 2], [3, 4], [5, 6]]))  # [1, 2, 3, 4, 5, 6]

# Bounded TypeVar
Number = TypeVar("Number", int, float)

def add_numbers(a: Number, b: Number) -> Number:
    return a + b  # type: ignore

print(add_numbers(3, 5))  # 8
print(add_numbers(1.5, 2.5))  # 4.0

print("=" * 5, "Generic classes", "=" * 5)

class Stack(Generic[T]):
    """A generic stack implementation."""

    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self) -> Optional[T]:
        return self.items[-1] if self.items else None

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f"Stack({self.items})"

# Using generic stack with different types
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack)  # Stack([1, 2, 3])
print(f"Popped: {int_stack.pop()}")  # 3
print(f"Peek: {int_stack.peek()}")  # 2

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(str_stack)  # Stack(['hello', 'world'])

print("=" * 5, "TypedDict: structured dictionaries", "=" * 5)

class User(TypedDict):
    name: str
    age: int
    email: str

class UserOptional(TypedDict, total=False):
    name: str
    age: int
    email: str  # all fields optional

def create_user(data: User) -> str:
    return f"{data['name']} ({data['age']}): {data['email']}"

user: User = {"name": "Alice", "age": 30, "email": "alice@example.com"}
print(create_user(user))  # Alice (30): alice@example.com

# Partial user (with total=False)
partial_user: UserOptional = {"name": "Bob"}
print(f"Partial: {partial_user}")  # {'name': 'Bob'}

print("=" * 5, "Literal and Final", "=" * 5)

# Literal: restrict values to specific literals
def set_mode(mode: Literal["read", "write", "append"]) -> str:
    return f"Mode set to: {mode}"

print(set_mode("read"))  # Mode set to: read
# set_mode("delete")  # Type checker would flag this

# Final: prevent reassignment or overriding
MAX_CONNECTIONS: Final[int] = 100
print(f"Max connections: {MAX_CONNECTIONS}")
# MAX_CONNECTIONS = 200  # Type checker would flag this

# Final in classes
class Config:
    DATABASE_URL: Final[str] = "postgresql://localhost/mydb"
    MAX_RETRIES: Final[int] = 3

config = Config()
print(f"DB URL: {config.DATABASE_URL}")

print("=" * 5, "Protocol: structural typing", "=" * 5)

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Drawing circle"

class Square:
    def draw(self) -> str:
        return "Drawing square"

def render(shape: Drawable) -> None:
    print(shape.draw())

render(Circle())  # Drawing circle
render(Square())  # Drawing square

# Any object with a draw() method satisfies the Drawable protocol
class Triangle:
    def draw(self) -> str:
        return "Drawing triangle"

render(Triangle())  # Drawing triangle

print("=" * 5, "TypeAlias: creating type aliases", "=" * 5)

# TypeAlias for complex types
Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[list[float]]
UserID: TypeAlias = int
UserName: TypeAlias = str
UserData: TypeAlias = dict[UserID, UserName]

def normalize(vector: Vector) -> Vector:
    total = sum(x ** 2 for x in vector) ** 0.5
    return [x / total for x in vector]

v: Vector = [3.0, 4.0]
print(f"Normalized: {normalize(v)}")  # [0.6, 0.8]

print("=" * 5, "overload: function overloading", "=" * 5)

class Formatter:
    @overload
    def format(self, value: int) -> str: ...
    @overload
    def format(self, value: str) -> str: ...
    @overload
    def format(self, value: list[int]) -> str: ...

    def format(self, value: int | str | list[int]) -> str:
        if isinstance(value, int):
            return f"Number: {value}"
        elif isinstance(value, str):
            return f"String: {value}"
        else:
            return f"List: {', '.join(str(v) for v in value)}"

fmt = Formatter()
print(fmt.format(42))  # Number: 42
print(fmt.format("hello"))  # String: hello
print(fmt.format([1, 2, 3]))  # List: 1, 2, 3