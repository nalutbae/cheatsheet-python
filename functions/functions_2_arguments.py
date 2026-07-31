# Positional and keyword arguments

# Positional arguments
def add(a, b):
    return a + b

print(add(3, 5))  # 8

# Keyword arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Hello, Alice!
greet("Alice", greeting="Hi")  # Hi, Alice!
greet(name="Bob", greeting="Hey")  # Hey, Bob!

# Default parameter values
def power(base, exponent=2):
    return base ** exponent

print(power(3))  # 9
print(power(3, 3))  # 27
print(power(2, exponent=10))  # 1024

# Mutable default values gotcha (use None instead)
# Wrong: mutable default is shared across calls
def append_wrong(item, lst=[]):
    lst.append(item)
    return lst

print(append_wrong(1))  # [1]
print(append_wrong(2))  # [1, 2] — shared mutable default!

# Correct: use None as default
def append_correct(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_correct(1))  # [1]
print(append_correct(2))  # [2] — each call gets a fresh list

print("=" * 5, "*args: variable positional arguments", "=" * 5)

# *args collects excess positional arguments as a tuple
def sum_all(*args):
    print(f"args type: {type(args)}")  # <class 'tuple'>
    print(f"args value: {args}")
    return sum(args)

print(sum_all(1, 2, 3))  # args value: (1, 2, 3) → 6
print(sum_all(10, 20))  # args value: (10, 20) → 30
print(sum_all())  # args value: () → 0

# Combining regular args and *args
def show_info(name, *hobbies):
    print(f"Name: {name}")
    print(f"Hobbies: {hobbies}")

show_info("Alice", "reading", "coding", "hiking")
# Name: Alice
# Hobbies: ('reading', 'coding', 'hiking')

# *args with regular parameters
def calculate(operation, *numbers):
    if operation == "sum":
        return sum(numbers)
    elif operation == "product":
        result = 1
        for n in numbers:
            result *= n
        return result
    return 0

print(calculate("sum", 1, 2, 3, 4))  # 10
print(calculate("product", 2, 3, 4))  # 24

print("=" * 5, "**kwargs: variable keyword arguments", "=" * 5)

# **kwargs collects excess keyword arguments as a dictionary
def print_info(**kwargs):
    print(f"kwargs type: {type(kwargs)}")  # <class 'dict'>
    print(f"kwargs value: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, city="Seoul")
# kwargs value: {'name': 'Alice', 'age': 30, 'city': 'Seoul'}
#   name: Alice
#   age: 30
#   city: Seoul

# Combining positional args, *args, and **kwargs
def func_demo(a, b, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

func_demo(1, 2, 3, 4, x=10, y=20)
# a = 1
# b = 2
# args = (3, 4)
# kwargs = {'x': 10, 'y': 20}

# Full parameter order: pos, *args, kwonly, **kwargs
def full_example(a, b, *args, required, optional=None, **kwargs):
    print(f"a={a}, b={b}, args={args}, required={required}, optional={optional}, kwargs={kwargs}")

full_example(1, 2, 3, 4, required=True, extra="data")
# a=1, b=2, args=(3, 4), required=True, optional=None, kwargs={'extra': 'data'}

print("=" * 5, "Unpacking arguments", "=" * 5)

# Unpacking a list/tuple with * for positional args
def subtract(a, b, c):
    return a - b - c

values = [10, 3, 2]
print(subtract(*values))  # 5

# Unpacking a dict with ** for keyword args
def display(name, age, city):
    print(f"{name}, {age} years old, from {city}")

person = {"name": "Alice", "age": 30, "city": "Seoul"}
display(**person)  # Alice, 30 years old, from Seoul

# Merging dicts with ** unpacking
defaults = {"color": "red", "size": "M", "quantity": 1}
custom = {"color": "blue", "price": 29.99}
merged = {**defaults, **custom}
print(merged)  # {'color': 'blue', 'size': 'M', 'quantity': 1, 'price': 29.99}

# Keyword-only arguments (after * or *args)
def kw_only(a, b, *, option):
    print(f"a={a}, b={b}, option={option}")

kw_only(1, 2, option=True)  # a=1, b=2, option=True
# kw_only(1, 2, True)  # TypeError: kw_only() takes 2 positional arguments but 3 were given

# Positional-only arguments (before /, Python 3.8+)
def pos_only(a, b, /, c):
    print(f"a={a}, b={b}, c={c}")

pos_only(1, 2, 3)  # a=1, b=2, c=3
pos_only(1, 2, c=3)  # a=1, b=2, c=3
# pos_only(a=1, b=2, c=3)  # TypeError: pos_only() got some positional-only arguments passed as keyword arguments

# Full signature: pos-only, pos-or-kw, *args, kw-only, **kwargs
def full_signature(a, b, /, c, d, *args, e, f=10, **kwargs):
    print(f"a={a}, b={b}, c={c}, d={d}, args={args}, e={e}, f={f}, kwargs={kwargs}")

full_signature(1, 2, 3, 4, 5, 6, e=7, f=8, g=9, h=10)
# a=1, b=2, c=3, d=4, args=(5, 6), e=7, f=8, kwargs={'g': 9, 'h': 10}