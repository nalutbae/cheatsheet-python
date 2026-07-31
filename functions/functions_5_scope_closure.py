# Scope: where variables can be accessed
# LEGB rule: Local, Enclosing, Global, Built-in

print("=" * 5, "Local scope", "=" * 5)

def my_function():
    local_var = 10  # local scope: only accessible inside this function
    print(local_var)

my_function()  # 10
# print(local_var)  # NameError: name 'local_var' is not defined

print("=" * 5, "Global scope", "=" * 5)

global_var = 100  # global scope: accessible everywhere in the module

def read_global():
    print(global_var)  # can read global variables

read_global()  # 100

def modify_global_wrong():
    global_var = 200  # this creates a NEW local variable, doesn't modify the global
    print(f"Inside function: {global_var}")

modify_global_wrong()  # Inside function: 200
print(f"Outside function: {global_var}")  # Outside function: 100 (unchanged!)

# Using the 'global' keyword to modify a global variable
def modify_global_correct():
    global global_var
    global_var = 300  # now modifies the actual global variable

modify_global_correct()
print(global_var)  # 300

print("=" * 5, "Enclosing scope (nonlocal)", "=" * 5)

# Nested function and enclosing scope
def outer():
    x = "outer variable"

    def inner():
        print(f"Inner can read: {x}")  # can read enclosing scope

    inner()
    print(f"Outer still has: {x}")

outer()
# Inner can read: outer variable
# Outer still has: outer variable

# Modifying enclosing scope with 'nonlocal'
def counter():
    count = 0

    def increment():
        nonlocal count  # refers to the enclosing scope's variable
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    return increment, decrement

inc, dec = counter()
print(inc())  # 1
print(inc())  # 2
print(inc())  # 3
print(dec())  # 2
print(dec())  # 1

# Without nonlocal, inner function creates a new local variable
def outer_wrong():
    x = 10

    def inner_wrong():
        x = 20  # creates a new local x, doesn't modify outer's x
        print(f"Inner x: {x}")

    inner_wrong()
    print(f"Outer x: {x}")  # outer x is unchanged

outer_wrong()
# Inner x: 20
# Outer x: 10

# With nonlocal, inner function modifies the enclosing variable
def outer_correct():
    x = 10

    def inner_correct():
        nonlocal x
        x = 20  # modifies outer's x
        print(f"Inner x: {x}")

    inner_correct()
    print(f"Outer x: {x}")  # outer x is modified

outer_correct()
# Inner x: 20
# Outer x: 20

print("=" * 5, "Built-in scope", "=" * 5)

# Built-in functions are always accessible
print(len([1, 2, 3]))  # 3 (len is a built-in)
print(abs(-5))  # 5 (abs is a built-in)
print(max(1, 2, 3))  # 3 (max is a built-in)

# Shadowing built-in names (avoid this!)
# len = 5  # shadows the built-in len()
# print(len([1, 2, 3]))  # TypeError: 'int' object is not callable

print("=" * 5, "Closure", "=" * 5)

# A closure is a function that remembers values from its enclosing scope
# even after the enclosing scope has finished executing

def make_multiplier(factor):
    """Returns a function that multiplies by the given factor."""
    def multiply(number):
        return number * factor  # 'factor' is remembered from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(double(10))  # 20
print(triple(5))  # 15
print(triple(10))  # 30

# Each closure has its own enclosed variables
print(double(7))  # 14
print(triple(7))  # 21

# Closure for maintaining state (without classes)
def make_counter(start=0):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def get_count():
        return count

    return increment, decrement, get_count

inc, dec, get = make_counter(10)
print(inc())  # 11
print(inc())  # 12
print(dec())  # 11
print(get())  # 11

# Closure for configuration
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeter("Hello")
hi = make_greeter("Hi")
goodbye = make_greeter("Goodbye")

print(hello("Alice"))  # Hello, Alice!
print(hi("Bob"))  # Hi, Bob!
print(goodbye("Charlie"))  # Goodbye, Charlie!

# Closure with initial value
def make_accumulator(initial=0):
    total = initial

    def accumulate(value):
        nonlocal total
        total += value
        return total

    return accumulate

acc = make_accumulator(100)
print(acc(10))  # 110
print(acc(20))  # 130
print(acc(30))  # 160

# Each accumulator is independent
acc2 = make_accumulator(0)
print(acc2(5))  # 5
print(acc2(10))  # 15

# Original accumulator is unaffected
print(acc(5))  # 165

print("=" * 5, "Scope resolution order (LEGB)", "=" * 5)

x = "global"

def outer_scope():
    x = "enclosing"

    def inner_scope():
        x = "local"
        print(f"Inner x: {x}")  # Local takes priority

    inner_scope()
    print(f"Outer x: {x}")

outer_scope()
# Inner x: local
# Outer x: enclosing
print(f"Global x: {x}")  # global

# LEGB resolution without local definition
y = "global_y"

def outer_y():
    y = "enclosing_y"

    def inner_y():
        print(y)  # no local y, finds enclosing y

    inner_y()

outer_y()  # enclosing_y

# LEGB resolution without local or enclosing
z = "global_z"

def outer_z():
    def inner_z():
        print(z)  # no local or enclosing z, finds global z

    inner_z()

outer_z()  # global_z