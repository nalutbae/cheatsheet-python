# usage of list type variable

list1 = [1, 2, 3, 4, 5]
print(list1)  # [1, 2, 3, 4, 5]
print(type(list1))  # <class 'list'>
print(len(list1))  # 5
print(list1[0])  # 1
print(list1[1])  # 2
print(list1[2])  # 3
print(list1[3])  # 4
print(list1[4])  # 5
print(list1[-1]) # 5
print(list1[-2]) # 4
print(list1[-3]) # 3
print(list1[-4]) # 2
print(list1[-5]) # 1
print(list1[0:3])  # [1, 2, 3]
print(list1[2:5])  # [3, 4, 5]
print(list1[2:])  # [3, 4, 5]
print(list1 * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(list1 + [6, 7, 8])  # [1, 2, 3, 4, 5, 6, 7, 8]


print("=" * 5, "change list elements examples", "=" * 5)

# change list elements examples
list1[0] = 10
print(list1)  # [10, 2, 3, 4, 5]
list1[1:3] = [20, 30]
print(list1)  # [10, 20, 30, 4, 5]
list1[1:3] = []
print(list1)  # [10, 4, 5]

print("=" * 5, "append list elements examples", "=" * 5)

# append list elements examples
list1.append(40)
print(list1)  # [10, 4, 5, 40]
list1.append(50)
print(list1)  # [10, 4, 5, 40, 50]

list1.insert(0, 60)
print(list1)  # [60, 10, 4, 5, 40, 50]
list1.insert(2, 70)
print(list1)  # [60, 10, 70, 4, 5, 40, 50]

print("=" * 5, "remove list elements examples", "=" * 5)

# remove list elements examples
list1.remove(70)
print(list1)  # [60, 10, 4, 5, 40, 50]

list1.pop()
print(list1)  # [60, 10, 4, 5, 40]

list1.pop()
print(list1)  # [60, 10, 4, 5]

print("=" * 5, "sorting list elements examples", "=" * 5)

# sorting list elements examples
list1.sort()
print(list1)  # [4, 5, 10, 60]

list1.sort(reverse=True)
print(list1)  # [60, 10, 5, 4]

list1.reverse()
print(list1)  # [4, 5, 10, 60]

print("=" * 5, "clear list elements examples", "=" * 5)

# clear list elements examples
list1.clear()
print(list1)

del list1
# print(list1)  # NameError: name 'list1' is not defined

print("=" * 5, "copy list example", "=" * 5)

# copy list example
list2 = [1, 2, 3, 4, 5]
list3 = list2
print(list2)  # [1, 2, 3, 4, 5]
print(list3)  # [1, 2, 3, 4, 5]
list2[0] = 10
print(list2)  # [10, 2, 3, 4, 5]
print(list3)  # [10, 2, 3, 4, 5]
list2.append(20)
print(list2)  # [10, 2, 3, 4, 5, 20]
print(list3)  # [10, 2, 3, 4, 5, 20]
list2.pop()
print(list2)  # [10, 2, 3, 4, 5]
print(list3)  # [10, 2, 3, 4, 5]
list2.clear()
print(list2)  # []
print(list3)  # []
del list2
# print(list2)  # NameError: name 'list2' is not defined
print(list3)  # []
del list3
# print(list3)  # NameError: name 'list3' is not defined

print("=" * 5, "copy list using copy() function example", "=" * 5)

# copy list using copy() function example
list4 = [1, 2, 3, 4, 5]
list5 = list4.copy()
print(list4)  # [1, 2, 3, 4, 5]
print(list5)  # [1, 2, 3, 4, 5]
list4[0] = 10
print(list4)  # [10, 2, 3, 4, 5]
print(list5)  # [1, 2, 3, 4, 5]
list4.append(20)
print(list4)  # [10, 2, 3, 4, 5, 20]
print(list5)  # [1, 2, 3, 4, 5]
list4.pop()
print(list4)  # [10, 2, 3, 4, 5]
print(list5)  # [1, 2, 3, 4, 5]
list4.clear()
print(list4)  # []
print(list5)  # [1, 2, 3, 4, 5]
del list4
# print(list4)  # NameError: name 'list4' is not defined
print(list5)  # [1, 2, 3, 4, 5]
del list5
# print(list5)  # NameError: name 'list5' is not defined

print("=" * 5, "copy list using [:] operator example", "=" * 5)

# copy list using [:] operator example
list6 = [1, 2, 3, 4, 5]
list7 = list6[:]
print(list6)  # [1, 2, 3, 4, 5]
print(list7)  # [1, 2, 3, 4, 5]
list6[0] = 10
print(list6)  # [10, 2, 3, 4, 5]
print(list7)  # [1, 2, 3, 4, 5]
list6.append(20)
print(list6)  # [10, 2, 3, 4, 5, 20]
print(list7)  # [1, 2, 3, 4, 5]
list6.pop()
print(list6)  # [10, 2, 3, 4, 5]
print(list7)  # [1, 2, 3, 4, 5]
list6.clear()
print(list6)  # []
print(list7)  # [1, 2, 3, 4, 5]
del list6
# print(list6)  # NameError: name 'list6' is not defined
print(list7)  # [1, 2, 3, 4, 5]
del list7
# print(list7)  # NameError: name 'list7' is not defined

print("=" * 5, "range() function examples", "=" * 5)

# range() function examples
# range(start, stop, step)
# start: start index (default: 0)
# stop: stop index (default: stop of the list)
# step: step size (default: 1)
# range(stop)
list8 = list(range(1, 6))
print(list8)  # [1, 2, 3, 4, 5]
list9 = list(range(1, 11, 2))
print(list9)  # [1, 3, 5, 7, 9]
list10 = list(range(10, 0, -1))
print(list10)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list11 = list(range(10))
print(list11)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list12 = list(range(0, 10))
print(list12)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list13 = list(range(10, 0))
print(list13) # []
list14 = list(range(0, 10, 1))
print(list14) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=" * 5, "One list may contain multiple types of values", "=" * 5)

# One list may contain multiple types of values
list15 = [10, "string", 3.14]
print(list15)  # [10, 'string', 3.14]

# Initialize the list with an empty array
list16 = []
print(list16)  # []

print("=" * 5, "split() function examples", "=" * 5)

# Example of use of split() function
# split(sep=None, maxsplit=-1)
# sep: separator (default: any whitespace)
# maxsplit: maximum number of splits (default: -1, no limit)
# split() function returns a list of strings
# split() function does not modify the original string
# split() function splits the string at the specified separator
stringValue = "my list is this."
list17 = list(stringValue)
print(list17)  # ['m', 'y', ' ', 'l', 'i', 's', 't', ' ', 'i', 's', ' ', 't', 'h', 'i', 's', '.']
list18 = list(stringValue.split())
print(list18)  # ['my', 'list', 'is', 'this.']
list19 = list(stringValue.split('i'))
print(list19)  # ['my l', 'st ', 's th', 's.']
list20 = list(stringValue.split('i', 1))
print(list20)  # ['my l', 'st is this.']
list21 = list(stringValue.split('i', 2))
print(list21)  # ['my l', 'st', 's this.']

print("=" * 5, "slice() function examples", "=" * 5)

# Example of use of slice() function
# slice(start, stop, step)
# start: start index (default: 0)
# stop: stop index (default: stop of the list)
# step: step size (default: 1)
# slice() function does not modify the original list
# slice() function returns a slice of the list
list22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list22)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list22[0:3])  # [1, 2, 3]
print(list22[3:])  # [4, 5, 6, 7, 8, 9, 10]
print(list22[:3])  # [1, 2, 3]
print(list22[3:6])  # [4, 5, 6]
print(list22[6:9])  # [7, 8, 9]
print(list22[9:])  # [10]
print(list22[::2])  # [1, 3, 5, 7, 9]
print(list22[1::2])  # [2, 4, 6, 8, 10]
print(list22[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list22[::-2])  # [10, 8, 6, 4, 2]
print(list22[2:8:2])  # [3, 5, 7]
print(list22[8:2:-2])  # [9, 7, 5]
print(list22[2:8:-2])  # [] 
print(list22[8:2:2])  # []

print("=" * 5, "modify list elements examples", "=" * 5)

# modify list elements examples
list23 = ["Melon", "Apple", "Berry"]
list23[2] = "Banana"
print(list23)  # ['Melon', 'Apple', 'Banana']
list23[1:2] = ["Orange", "Pear"]
print(list23)  # ['Melon', 'Orange', 'Pear', 'Banana']
list23[1:2] = []
print(list23)  # ['Melon', 'Pear', 'Banana']
list23.append("Cherry")
print(list23)  # ['Melon', 'Pear', 'Banana', 'Cherry']
list23.append("Apple")
print(list23)  # ['Melon', 'Pear', 'Banana', 'Cherry', 'Apple']
list23.append("Strawberry")
print(list23)  # ['Melon', 'Pear', 'Banana', 'Cherry', 'Apple', 'Strawberry']
list23.insert(1, "Grape")
print(list23)  # ['Melon', 'Grape', 'Pear', 'Banana', 'Cherry', 'Apple', 'Strawberry']
list23.insert(3, "Peach")
print(list23)  # ['Melon', 'Grape', 'Pear', 'Peach', 'Banana', 'Cherry', 'Apple', 'Strawberry']
list23.insert(5, "Kiwi")
print(list23)  # ['Melon', 'Grape', 'Pear', 'Peach', 'Banana', 'Kiwi', 'Cherry', 'Apple', 'Strawberry']
list23.insert(9, "Mango")
print(list23)  # ['Melon', 'Grape', 'Pear', 'Peach', 'Banana', 'Kiwi', 'Cherry', 'Apple', 'Strawberry', 'Mango']
print(list23.index)  # AttributeError: 'list' object has no attribute 'index'
print(list23.index("Apple"))  # 7
list23.remove("Apple")
print(list23)  # ['Melon', 'Grape', 'Pear', 'Peach', 'Banana', 'Kiwi', 'Cherry', 'Strawberry', 'Mango']
list23.pop()
print(list23)  # ['Melon', 'Grape', 'Pear', 'Peach', 'Banana', 'Kiwi', 'Cherry', 'Strawberry']
list23.pop(1)
print(list23)  # ['Melon', 'Pear', 'Peach', 'Banana', 'Kiwi', 'Cherry', 'Strawberry']
list23.pop(3)
print(list23)  # ['Melon', 'Pear', 'Peach', 'Kiwi', 'Cherry', 'Strawberry']
del list23[1]
print(list23)  # ['Melon', 'Peach', 'Kiwi', 'Cherry', 'Strawberry']
del list23[3]
print(list23)  # ['Melon', 'Peach', 'Kiwi', 'Strawberry']
list23.clear()
print(list23)  # []
del list23
# print(list23)  # NameError: name 'list23' is not defined

print("=" * 5, "unpacking examples", "=" * 5)

# Examples of unpacking
list24 = [1, 2, 3]
a, b, c = list24
print(a)  # 1
print(b)  # 2
print(c)  # 3

list25 = [1, 2, 3, 4, 5]
a, b, *c = list25
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]

a, *b, c = list25
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

*a, b, c = list25
print(a)  # [1, 2, 3]
print(b)  # 4
print(c)  # 5