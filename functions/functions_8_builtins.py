# Built-in functions commonly used in Python

print("=" * 5, "Type conversion functions", "=" * 5)

# int(), float(), str(), bool()
print(int("42"))  # 42
print(int(3.7))  # 3 (truncates toward zero)
print(int("0xff", 16))  # 255 (hex base)
print(float("3.14"))  # 3.14
print(str(42))  # '42'
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("hello"))  # True

# list(), tuple(), set(), dict()
print(list("hello"))  # ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set([1, 2, 2, 3, 3]))  # {1, 2, 3}
print(dict(a=1, b=2))  # {'a': 1, 'b': 2}
print(dict([(1, 'a'), (2, 'b')]))  # {1: 'a', 2: 'b'}

print("=" * 5, "Mathematical functions", "=" * 5)

# abs(), round(), min(), max(), sum()
print(abs(-5))  # 5
print(abs(3.14))  # 3.14
print(round(3.14159, 2))  # 3.14
print(round(3.5))  # 4 (banker's rounding)
print(round(2.5))  # 2 (banker's rounding)
print(min(1, 2, 3))  # 1
print(max(1, 2, 3))  # 3
print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3], 10))  # 16 (with start value)

# pow()
print(pow(2, 3))  # 8
print(pow(2, 3, 5))  # 3 (2^3 % 5)

# divmod()
print(divmod(17, 5))  # (3, 2) → quotient and remainder

print("=" * 5, "Iterable functions", "=" * 5)

# len()
print(len("hello"))  # 5
print(len([1, 2, 3]))  # 3
print(len({"a": 1, "b": 2}))  # 2

# range()
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(2, 8)))  # [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

# enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}", end=" | ")
# 0: apple | 1: banana | 2: cherry |
print()

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}", end=" | ")
# 1: apple | 2: banana | 3: cherry |
print()

# zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Seoul", "Tokyo", "London"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}", end=" | ")
# Alice, 25, Seoul | Bob, 30, Tokyo | Charlie, 35, London |
print()

# zip creates tuples
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# zip with unequal lengths (stops at shortest)
short = [1, 2]
long = [10, 20, 30, 40]
print(list(zip(short, long)))  # [(1, 10), (2, 20)]

# map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# map with multiple iterables
squares = list(map(pow, [2, 3, 4], [3, 2, 1]))
print(squares)  # [8, 9, 4]

# map with built-in functions
strings = ["1", "2", "3"]
ints = list(map(int, strings))
print(ints)  # [1, 2, 3]

# filter()
numbers = range(1, 11)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# filter with None removes falsy values
mixed = [0, 1, "", "hello", None, [], [1, 2], False, True]
truthy = list(filter(None, mixed))
print(truthy)  # [1, 'hello', [1, 2], True]

# sorted()
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))  # [1, 1, 2, 3, 4, 5, 6, 9]
print(sorted(numbers, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted with key function
words = ["banana", "apple", "cherry", "date"]
print(sorted(words, key=len))  # ['date', 'apple', 'banana', 'cherry']
print(sorted(words, key=str.lower))  # ['apple', 'banana', 'cherry', 'date']

# reversed()
numbers = [1, 2, 3, 4, 5]
print(list(reversed(numbers)))  # [5, 4, 3, 2, 1]

# any() and all()
print(any([False, False, True]))  # True
print(any([False, False, False]))  # False
print(all([True, True, True]))  # True
print(all([True, False, True]))  # False
print(any([]))  # False
print(all([]))  # True

# Practical: check if any number is even
nums = [1, 3, 5, 7, 8]
print(any(n % 2 == 0 for n in nums))  # True

# Practical: check if all numbers are positive
nums = [1, 2, 3, 4, 5]
print(all(n > 0 for n in nums))  # True

print("=" * 5, "String functions", "=" * 5)

# chr() and ord()
print(chr(65))  # 'A'
print(chr(97))  # 'a'
print(ord('A'))  # 65
print(ord('a'))  # 97

# ASCII alphabet
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(alphabet)  # ['a', 'b', 'c', ..., 'z']

# format()
print(format(3.14159, ".2f"))  # 3.14
print(format(255, "x"))  # ff
print(format(42, "05d"))  # 00042
print(format(0.75, "%"))  # 75.000000%

# repr()
print(repr("hello\n"))  # "'hello\\n'"
print(repr([1, 2, 3]))  # '[1, 2, 3]'

print("=" * 5, "Type checking functions", "=" * 5)

# type()
print(type(42))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type([1, 2]))  # <class 'list'>
print(type(True))  # <class 'bool'>

# isinstance()
print(isinstance(42, int))  # True
print(isinstance(42, float))  # False
print(isinstance(42, (int, float)))  # True
print(isinstance("hello", str))  # True
print(isinstance([1, 2], (list, tuple)))  # True

# issubclass()
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
print(issubclass(Dog, Dog))  # True

# callable()
def my_func():
    pass

print(callable(my_func))  # True
print(callable(42))  # False
print(callable(len))  # True

# hasattr(), getattr(), setattr(), delattr()
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(hasattr(p, "name"))  # True
print(hasattr(p, "age"))  # False
print(getattr(p, "name"))  # Alice
print(getattr(p, "age", 25))  # 25 (default value)
setattr(p, "age", 30)
print(p.age)  # 30
delattr(p, "age")
# print(p.age)  # AttributeError

print("=" * 5, "Utility functions", "=" * 5)

# id() — unique object identifier
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a) != id(b))  # True (different objects)

# hash() — hash value for immutable objects
print(hash(42))  # integer hash
print(hash("hello"))  # string hash
# hash([1, 2])  # TypeError: unhashable type: 'list'

# dir() — list attributes
print("count" in dir([1, 2, 3]))  # True
print("upper" in dir("hello"))  # True

# vars() — __dict__ of an object
class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 20

obj = MyClass()
print(vars(obj))  # {'x': 10, 'y': 20}

# help() and print()
# help(len)  # shows documentation for len()
print(print("hello"))  # hello → None (print returns None)

# input() — get user input (commented out for automation)
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# eval() — evaluate a string expression (use with caution!)
expr = "2 + 3 * 4"
print(eval(expr))  # 14

# exec() — execute a string as code (use with caution!)
code = "x = 10\ny = 20\nprint(x + y)"
exec(code)  # 30