# usage of tuple examples
# tuple is immutable
# tuple is faster than list
# tuple is used for data that should not be changed

# See tuple elements and elements
t = (1, 2, 3, 4, 5)
print(t)  # (1, 2, 3, 4, 5)
print(type(t))  # <class 'tuple'>
print(t[0])  # 1
print(t[1])  # 2
print(t[2])  # 3 
print(t[3])  # 4
print(t[4])  # 5
print(t[-1]) # 5
print(t[-2]) # 4
print(t[-3]) # 3
print(t[-4]) # 2
print(t[-5]) # 1
print(t[0:3])  # (1, 2, 3)
print(t[2:5])  # (3, 4, 5)
print(t[2:])  # (3, 4, 5)
print(t * 2)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(len(t))  # 5
print(t.index(1))  # 0
print(t.index(2))  # 1
print(t.index(3))  # 2
print(t.index(4))  # 3
print(t.index(5))  # 4

print("=" * 5, "modify list elements examples", "=" * 5)

# Type comparison
# Note that tuples have to be a comma at the end even when one element is one. Omitted by the rest is considered a single variable.
t = (1, )
print(t) # (1,)
print(type(t)) # <class 'tuple'>

t = (1)
print(t) # 1
print(type(t)) # <class 'int'>

t = 'book', 'pen', 'eraser'
print(t) # ('book', 'pen', 'eraser')
print(type(t)) # <class 'tuple'>
print(t[0]) # book

list1 = [1, 2, 3, 4, 5] 
print(list1, type(list1)) # [1, 2, 3, 4, 5] <class 'list'>
t = tuple(list1)
print(t, type(t)) # (1, 2, 3, 4, 5) <class 'tuple'>


print("=" * 5, "unpacking examples", "=" * 5)

# Examples of unpacking
t = (1, 2, 3)
a, b, c = t
print(a)  # 1
print(b)  # 2
print(c)  # 3

t = (1, 2, 3, 4, 5)
a, b, *c = t
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]

a, *b, c = t
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

*a, b, c = t
print(a)  # [1, 2, 3]
print(b)  # 4
print(c)  # 5