# Impossible variable names — names that are NOT valid Python identifiers

# Variable names CANNOT start with a number
# 7what = "It cannot be assigned to variable name that starts with a number."  # SyntaxError!

# Variable names CANNOT be Python keywords
# def = "It cannot be assigned to variable names used as keywords."  # SyntaxError!
# class = "Same here."  # SyntaxError!
# return = "And this."  # SyntaxError!

# Variable names CAN shadow built-in function names (but it's not recommended)
# sum = "Although it can be used as a variable name, it shadows the built-in sum()."
# list = "Same — shadows the built-in list()."
# This is valid Python but bad practice:
_sum_result = 42  # use underscore prefix to avoid shadowing
built_in_list = [1, 2, 3]  # use descriptive names instead

print("=" * 5, "Valid variable naming rules", "=" * 5)

# Valid: starts with letter or underscore
variable_name = "valid"
_private = "valid"
__dunder__ = "valid"
camelCase = "valid"
snake_case = "valid"

# Valid: contains numbers (but not at the start)
var1 = "valid"
v2_name = "valid"
_3d_point = "valid"  # underscore + number is OK

# Valid: Unicode characters
변수 = "valid Korean name"
α = 0.5  # valid Greek letter

print(f"variable_name: {variable_name}")
print(f"_private: {_private}")
print(f"snake_case: {snake_case}")
print(f"var1: {var1}")
print(f"변수: {변수}")

# Invalid names and why:
# 7what = ...    # SyntaxError: starts with a number
# what-if = ...  # SyntaxError: contains hyphen
# class = ...    # SyntaxError: Python keyword
# def = ...      # SyntaxError: Python keyword
# my var = ...   # SyntaxError: contains space
# my@var = ...   # SyntaxError: contains special character

print("=" * 5, "Python keywords (cannot be used as variable names)", "=" * 5)

import keyword
print(f"Number of keywords: {len(keyword.kwlist)}")
print(f"Keywords: {keyword.kwlist}")
print(f"'if' is keyword: {keyword.iskeyword('if')}")
print(f"'my_var' is keyword: {keyword.iskeyword('my_var')}")

print("=" * 5, "Soft keywords (can be used but discouraged)", "=" * 5)

# These are context-sensitive keywords (soft keywords in 3.10+):
# match, case, _ (wildcard in patterns)
# They CAN be used as variable names in non-pattern contexts
match = "I'm a variable named 'match'"  # valid outside match/case
case = "I'm a variable named 'case'"    # valid outside match/case
print(f"match: {match}")
print(f"case: {case}")

print("=" * 5, "Built-in names (can shadow but shouldn't)", "=" * 5)

# These are NOT keywords — they CAN be used as variable names,
# but doing so shadows the built-in function/class:
# list, dict, str, int, float, sum, max, min, len, type, ...
# Shadowing them leads to confusing bugs:

original_sum = sum([1, 2, 3])  # correctly uses built-in sum()
print(f"sum([1,2,3]) = {original_sum}")  # 6

# If you accidentally do: sum = 0
# Then sum([1,2,3]) would fail: TypeError: 'int' object is not callable
# Always avoid shadowing built-in names!