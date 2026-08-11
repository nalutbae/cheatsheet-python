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
print(three, type(three)) # 3 <class 'str'>

# Example of string operation

print(str1, type(str1)) # Hello, World! <class 'str'>
print("str1's size:", len(str1)) # str1's size: 13
print(str1[0]) # H
print(str1[2:5]) # llo
print(str1[2:]) # llo, World!
print(str1 * 2) # Hello, World!Hello, World!
print(str1 + " " + str2) # Hello, World! Hello, World!


# Escape special characters

esc1 = "\"I'm a developer.\""
print(esc1) # "I'm a developer."

esc2 = '"I\'m a developer."'
print(esc2) # "I'm a developer."

esc3 = "aaa\tbbb\tccc\nddd\teee\tfff"
print(esc3) # aaa     bbb     ccc

esc4 = '"\\" is reverse slash.'
print(esc4) # ddd     eee     fff

raw_str = r'"\" is reverse slash.'
print(raw_str) # "\" is reverse slash.