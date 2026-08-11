# Example of using operators for integer variables

x = 10
y = 20
z = 30

print("x =", x) # 10 
print("y =", y) # 20

print("x + y =", x + y) # x + y = 30
print("x - y =", x - y) # x- y = -10
print("x * y =", x * y) # x * y = 200
print("x / y =", x / y) # x / y = 0.5
print("x // y =", x // y) # x // y = 0 (floor division)
print("x % y =", x % y) # x % y = 10
print("x ** y =", x ** y) # x ** y = 100000000000000000000 (Exponentiation: x*x*... yple)
print("x > y =", x > y) # x > y = False
print("x < y =", x < y) # x < y = True
print("x == y =", x == y) # x == y = False
print("x != y =", x != y) # x != y = True
print("x >= y =", x >= y) # x >= y = False
print("x <= y =", x <= y) # x <= y = True
print("x and y =", x and y) # x and y = 20
print("x or y =", x or y) # x or y = 10
print("not x =", not x) # not x = False
print("not y =", not y) # not y = False
print("x is y =", x is y) # x is y = Fals
print("x is not y =", x is not y) # x is not y = True

compareMultiple = x < y < z # == (x < y) and (y < z)
print("x < y < z =", compareMultiple) # x < y < z = True