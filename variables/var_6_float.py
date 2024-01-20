# Example of using operators for float variables

x = 0.1
y = 3.14
z = 30

print("x =", x)
print("y =", y)

print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)
print("x % y =", x % y)
print("x ** y =", x ** y)
print("x > y =", x > y)
print("x < y =", x < y)
print("x == y =", x == y)
print("x != y =", x != y)
print("x >= y =", x >= y)
print("x <= y =", x <= y)
print("x and y =", x and y)
print("x or y =", x or y)
print("not x =", not x)
print("not y =", not y)
print("x is y =", x is y)
print("x is not y =", x is not y)

compareMultiple = x < y < z 
print("x < y < z =", compareMultiple)

# Expression of infinity
x = float("inf")
y = -float("inf")

print("Infinity float x + 100 =", x + 100)
print("Infinity float x + y =", x + y)
print("Infinity float x / y =", x / y)