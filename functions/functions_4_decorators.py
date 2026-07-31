# Decorators: functions that modify the behavior of other functions

print("=" * 5, "Basic decorator", "=" * 5)

# Simple decorator without arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# Before calling say_hello
# Hello, Alice!
# After calling say_hello

# Equivalent to: say_hello = my_decorator(say_hello)

# Decorator that modifies return value
def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print(add(3, 5))  # 16 (because (3+5)*2 = 16)

# Stacking multiple decorators
def bold(func):
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"*{func(*args, **kwargs)}*"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # ** *Hello, Alice* **  (bold wraps italic)

# Order matters: decorators are applied bottom-up
@italic
@bold
def greet2(name):
    return f"Hello, {name}"

print(greet2("Alice"))  # ***Hello, Alice***  (italic wraps bold)

print("=" * 5, "Decorator with functools.wraps", "=" * 5)

# Without @wraps, the function identity is lost
def without_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@without_wraps
def my_function():
    """My function docstring."""
    pass

print(my_function.__name__)  # wrapper (not my_function!)
print(my_function.__doc__)  # None (docstring lost!)

# With @wraps, function identity is preserved
from functools import wraps

def with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@with_wraps
def my_other_function():
    """My other function docstring."""
    pass

print(my_other_function.__name__)  # my_other_function
print(my_other_function.__doc__)  # My other function docstring.

print("=" * 5, "Decorator with arguments", "=" * 5)

# Decorator that accepts arguments requires an extra nesting level
def repeat(num_times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def say_hi(name):
    print(f"Hi, {name}!")

say_hi("Bob")
# Hi, Bob!
# Hi, Bob!
# Hi, Bob!

print("=" * 5, "Practical decorator examples", "=" * 5)

# Timing decorator
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    total = sum(range(1000000))
    return total

result = slow_function()
# slow_function took 0.XXXXXX seconds

# Debugging decorator
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def add_numbers(a, b):
    return a + b

add_numbers(3, 5)
# Calling add_numbers(3, 5)
# add_numbers returned 8

# Authorization decorator
def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Simulated auth check
        user = kwargs.get("user", None)
        if user != "admin":
            print(f"Access denied for user: {user}")
            return None
        return func(*args, **kwargs)
    return wrapper

@requires_auth
def delete_database(user):
    print("Database deleted!")

delete_database(user="guest")  # Access denied for user: guest
delete_database(user="admin")  # Database deleted!

# Caching / memoization decorator
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        print(f"Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
# Computing for (5,)
# Computing for (4,)
# Computing for (3,)
# Computing for (2,)
# Computing for (1,)
# Computing for (0,)
# Cache hit for (1,)
# Cache hit for (0,)
# Cache hit for (2,)
# Cache hit for (3,)
# 5

print("=" * 5, "Class-based decorator", "=" * 5)

class CountCalls:
    """A decorator that counts how many times a function is called."""
    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)  # preserve function metadata

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))  # Call 1 of say_hello
print(say_hello("Bob"))  # Call 2 of say_hello
print(f"Total calls: {say_hello.count}")  # Total calls: 2