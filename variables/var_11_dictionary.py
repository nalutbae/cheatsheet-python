# Dictionary Examples
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Create dictionary
empty = {}

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, '\n') # {'first_name': 'John', 'last_name': 'Doe', 'age': 30}
print(person['first_name'], '\n') # John
print(person.get('last_name'), '\n') # Doe
print(person.keys(), '\n') # dict_keys(['first_name', 'last_name', 'age'])
print(person.values(), '\n') # dict_values(['John', 'Doe', 30])
print(person.items(), '\n') # dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 30)])
person['phone'] = '000000000000' 
print(person, '\n') # {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': '000000000000'}

person1 = dict(first_name='Mary', last_name='Smith') # {'first_name': 'Mary', 'last_name': 'Smith'}
print(person1, '\n') # {'first_name': 'Mary', 'last_name': 'Smith'}
print(len(person1), '\n') # 2
person.pop('age')
print(person, '\n') # {'first_name': 'John', 'last_name': 'Doe', 'phone': '000000000000'}
person.clear()
print(person, '\n') # {}
del person
# print(person, '\n') # NameError: name 'person' is not defined

print(person1, '\n') # {'first_name': 'Mary', 'last_name': 'Smith'}
person1.popitem() # ('first_name', 'Mary')
print(person1, '\n') # {'first_name': 'Mary'}
person1.clear() 
print(person1, '\n') # {}
del person1
# print(person1, '\n') # NameError: name 'person1' is not defined
# person2 = person1.copy() # NameError: name 'person1' is not defined


print("=" * 5, "Dictionary Comprehension", "=" * 5)

# Dictionary Comprehension
numbers = {x: x**2 for x in range(1, 7)}
print(numbers, '\n') # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
numbers = {x: x**2 for x in range(1, 7) if x % 2 == 0}
print(numbers, '\n') # {2: 4, 4: 16, 6: 36}
numbers = {x: x**2 for x in range(1, 7) if x % 2 == 0 if x % 3 == 0}
print(numbers, '\n') # {6: 36}


print("=" * 5, "Dictionary as a list", "=" * 5)

# Create a dictionary as a list
people = [
    ['John', 30],
    ['Jane', 25],
    ['Alex', 42],
    ['Peter', 19],
    ['Mary', 27],
    ['Mark', 32],
    ['Bob', 43]
]

print(people, '\n') # [['John', 30], ['Jane', 25], ['Alex', 42], ['Peter', 19], ['Mary', 27], ['Mark', 32], ['Bob', 43]]
print(people[0], '\n') # ['John', 30]
print(people[0][0], '\n') # John
print(people[0][1], '\n') # 30
print(people[0][0], people[0][1]) # John 30
# print(people[0].keys(), '\n') # AttributeError: 'list' object has no attribute 'keys'


print("=" * 5, "Dictionary as a set list", "=" * 5)

# Create a dictionary as a set list
people = [
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 25},
    {'name': 'Alex', 'age': 42},
    {'name': 'Peter', 'age': 19},
    {'name': 'Mary', 'age': 27},
    {'name': 'Mark', 'age': 32},
    {'name': 'Bob', 'age': 43}
]

print(people, '\n') # [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}, {'name': 'Alex', 'age': 42}, {'name': 'Peter', 'age': 19}, {'name': 'Mary', 'age': 27
print(people[0], '\n') # {'name': 'John', 'age': 30}
print(people[0]['name'], '\n') # John
print(people[0]['age'], '\n') # 30
print(people[0]['name'], people[0]['age']) # John 30
print(people[0].keys(), '\n') # dict_keys(['name', 'age'])
print(people[0].values(), '\n') # dict_values(['John', 30])
print(people[0].items(), '\n') # dict_items([('name', 'John'), ('age', 30)])
print(people[0].get('name'), '\n') # John
print(people[0].get('age'), '\n') # 30
print(people[0].get('name'), people[0].get('age')) # John 30


print("=" * 5, "Dictionary by dict() function", "=" * 5)

# Create a dictionary by dict() function
people = dict(
    John=30,
    Jane=25,
    Alex=42,
    Peter=19,
    Mary=27,
    Mark=32,
    Bob=43
)

print(people, '\n') # {'John': 30, 'Jane': 25, 'Alex': 42, 'Peter': 19, 'Mary': 27, 'Mark': 32, 'Bob': 43}
print(people['John'], '\n') # 30
print(people['Jane'], '\n') # 25
print(people.keys(), '\n') # dict_keys(['John', 'Jane', 'Alex', 'Peter', 'Mary', 'Mark', 'Bob'])
print(people.values(), '\n') # dict_values([30, 25, 42, 19, 27, 32, 43])
print(people.items(), '\n') # dict_items([('John', 30), ('Jane', 25), ('Alex', 42), ('Peter', 19), ('Mary', 27), ('Mark', 32), ('Bob', 43)])
print("Mary" in people.keys(), '\n') # True
print(70 in people.values(), '\n') # False
print(('Bob', 43) in people.items(), '\n') # True
print(people.get('John'), '\n') # 30
print(people.get('Jane'), '\n') # 25
print(people.get('John'), people.get('Jane')) # 30 25
print(people.get('John', 'Not Found'), '\n') # 30
print(people.get('Who')) # None
print(people.get('Who', 'Not Found'), '\n') # Not Found


print("=" * 5, "Dictionary by fromkeys() function", "=" * 5)

# Create a dictionary by fromkeys() function
people = dict.fromkeys(['John', 'Jane', 'Alex', 'Peter', 'Mary', 'Mark', 'Bob'])
print(people, '\n') # {'John': None, 'Jane': None, 'Alex': None, 'Peter': None, 'Mary': None, 'Mark': None, 'Bob': None}
print(people.keys(), '\n') # dict_keys(['John', 'Jane', 'Alex', 'Peter', 'Mary', 'Mark', 'Bob'])    
print(people.values(), '\n') # dict_values([None, None, None, None, None, None, None])
print(people.items(), '\n') # dict_items([('John', None), ('Jane', None), ('Alex', None), ('Peter', None), ('Mary', None), ('Mark', None), ('Bob', None)])
print(people.get('John'), '\n') # None
print(people.get('John', 'Not Found'), '\n') # None


print("=" * 5, "Convert the dictionary element to a list", "=" * 5)

# Convert the dictionary element to a list
people = {
    'John': 30,
    'Jane': 25,
    'Alex': 42,
    'Peter': 19,
    'Mary': 27,
    'Mark': 32,
    'Bob': 43
}
people_list = list(people)
print(people_list, '\n') # ['John', 'Jane', 'Alex', 'Peter', 'Mary', 'Mark', 'Bob']
print(type(people_list), '\n') # <class 'list'>
people_list = list(people.keys())
print(people_list, '\n') # ['John', 'Jane', 'Alex', 'Peter', 'Mary', 'Mark', 'Bob']
print(type(people_list), '\n') # <class 'list'>
people_list = list(people.values())
print(people_list, '\n') # [30, 25, 42, 19, 27, 32, 43]
print(type(people_list), '\n') # <class 'list'>
people_list = list(people.items())
print(people_list, '\n') # [('John', 30), ('Jane', 25), ('Alex', 42), ('Peter', 19), ('Mary', 27), ('Mark', 32), ('Bob', 43)]
print(type(people_list), '\n') # <class 'list'>
people_list = list(people.items())[0]
print(people_list, '\n') # ('John', 30)
print(type(people_list), '\n') # <class 'tuple'>
people_list = list(people.items())[0][0]
print(people_list, '\n') # John
print(type(people_list), '\n') # <class 'str'>
