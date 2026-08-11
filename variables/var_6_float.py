# Example of using operators for float variables

x = 0.1
y = 3.14
z = 30

print("x =", x) # x = 0.1
print("y =", y) # y= 3.14
print("x + y =", x + y) # x + y = 3.24
print("x - y =", x - y) # x- y = 3.04
print("x * y =", x * y) # x * y = 0.31400000000000006
print("x / y =", x / y) # / y= 0.03184713375796178
print("x // y =", x // y) # x // y = 0.0
print("x % y =", x % y) # x % y = 0.1
print("x ** y =", x ** y) # x ** y = 0.0007244359600749899
print("x > y =", x > y) # x > y = False
print("x < y =", x < y) # x < y = True
print("x == y =", x == y) # x == y = False
print("x != y =", x != y) # x != y = True
print("x >= y =", x >= y) # x >= y = False
print("x <= y =", x <= y) # x <= y = True
print("x and y =", x and y) # x and y = 3.14
print("x or y =", x or y) # x or y = 0.1
print("not x =", not x) # not x = False
print("not y =", not y) # not y = False
print("x is y =", x is y) # x is y = False
print("x is not y =", x is not y) # x is not y = True

compareMultiple = x < y < z 
print("x < y < z =", compareMultiple) # x < y < z = True

# Expression of infinity
x = float("inf")
y = -float("inf")

print("Infinity float x + 100 =", x + 100) # Infinity float x + 100 = inf
print("Infinity float x + y =", x + y) # Infinity float x + y = nan
print("Infinity float x / y =", x / y) # Infinity float x / y = nan