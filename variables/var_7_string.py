# Various string declaration examples

str1 = "Hello, World!"
print(str1)

str2 = 'Hello, World!'
print(str2)

str3 = """Hello, World!"""
print(str3)

str4 = '''Hello, World!'''
print(str4)

three = str(3)
print(three, type(three))

# Example of string operation

print(str1, type(str1))
print("str1's size:", len(str1))
print(str1[0])
print(str1[2:5])
print(str1[2:])
print(str1 * 2) 
print(str1 + " " + str2)


# Escape special characters

esc1 = "\"I'm a developer.\""
print(esc1)

esc2 = '"I\'m a developer."'
print(esc2)

esc3 = "aaa\tbbb\tccc\nddd\teee\tfff"
print(esc3)

esc4 = '"\\" is reverse slash.'
print(esc4)

raw_str = r'"\" is reverse slash.'
print(raw_str)