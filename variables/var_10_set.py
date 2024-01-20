# Set type use example

s = {1,2,3,4,5}
print(s) # {1, 2, 3, 4, 5}
print(type(s)) # <class 'set'>
s.add(6)
print(s) # {1, 2, 3, 4, 5, 6}
s.add(6)
print(s) # {1, 2, 3, 4, 5, 6}
s.remove(6)
print(s) # {1, 2, 3, 4, 5}
s.discard(3)
print(s) # {1, 2, 4, 5}
s.clear()
print(s) # set()
print(type(s)) # <class 'set'>

s = set([1,2,3,4,5])
print(s) # {1, 2, 3, 4, 5}
print(type(s)) # <class 'set'>
s.pop()
print(s) # {1, 2, 3, 4}
s.pop()
print(s) # {1, 2, 3}
s.pop()
print(s) # {1, 2}
s.pop()
print(s) # {1}
s.pop()
print(s) # set()

# Example of confirmation of SET elements
s = {1,2,3,4,5}
print(1 in s) # True
print(6 in s) # False
print(6 not in s) # True
print(1 not in s) # False

print(s.issuperset({1,2,3})) # True
print(s.issuperset({1,2,3,6})) # False

print(s.issubset({1,2,3})) # True
print(s.issubset({1,2,3,6})) # False

print(s.isdisjoint({1,6})) # False
print(s.isdisjoint({6,7})) # True  

# SET Logic Operation Example
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.intersection(s2)) # {4, 5}
print(s1.difference(s2)) # {1, 2, 3}
print(s2.difference(s1)) # {6, 7, 8}
print(s1.symmetric_difference(s2)) # {1, 2, 3, 6, 7, 8}
print(s2.symmetric_difference(s1)) # {1, 2, 3, 6, 7, 8}
print(s1.issuperset(s2)) # False
print(s2.issuperset(s1)) # True
print(s2.issuperset(s1)) # False
print(s1.issubset(s2)) # False
print(s2.issubset(s1)) # True
print(s2.issubset(s1)) # False
print(s1.isdisjoint(s2)) # False
print(s2.isdisjoint(s1)) # True
