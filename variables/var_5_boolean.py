# Example of using operators for boolean variables

x = True
y = False

print("x =", x) # x = True
print("y =", y) # y = False

print("x + y =", x + y) # x + y = 1
print("x - y =", x - y) # x -y = 1
print("x * y =", x * y) # x * y = 0
print("x ** y =", x ** y) # x ** y 1
print("x > y =", x > y) # x > y = True
print("x < y =", x < y)  # x < y = False
print("x == y =", x == y)   # x == y = False
print("x != y =", x != y)   # x != y = True
print("x >= y =", x >= y)   # x >= y = True
print("x <= y =", x <= y)   # x <= y = False
print("x and y =", x and y) # x and y = False
print("x or y =", x or y)   # x or y = True
print("not x =", not x) # not x = False
print("not y =", not y) # not y = True
print("x is y =", x is y)   # x is y = False
print("x is not y =", x is not y)   # x is not y = True

print(True or True and False)   # True

print(True or (True and False)) # True