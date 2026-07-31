# Recursion: a function that calls itself

print("=" * 5, "Basic recursion", "=" * 5)

# Factorial: n! = n * (n-1)!
def factorial(n):
    if n <= 1:  # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(5))  # 120
print(factorial(10))  # 3628800

# Fibonacci: F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(10))  # 55

print("=" * 5, "Recursive data structures", "=" * 5)

# Recursive list flattening
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [[1, [2, 3]], [4, [5, 6]], 7]
print(flatten(nested))  # [1, 2, 3, 4, 5, 6, 7]

# Recursive sum of nested lists
def nested_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total

print(nested_sum([1, [2, 3], [4, [5, 6]]]))  # 21

# Recursive depth of nested list
def depth(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(depth(item) for item in lst)

print(depth([1, [2, [3, [4]]]]))  # 4
print(depth([1, 2, 3]))  # 1
print(depth([]))  # 1

print("=" * 5, "Recursive string operations", "=" * 5)

# Recursive string reversal
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # olleh
print(reverse_string("python"))  # nohtyp

# Recursive palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True

# Recursive character count
def count_char(s, char):
    if not s:
        return 0
    if s[0] == char:
        return 1 + count_char(s[1:], char)
    return count_char(s[1:], char)

print(count_char("hello world", "l"))  # 3
print(count_char("mississippi", "s"))  # 4

print("=" * 5, "Recursive tree traversal", "=" * 5)

# Simple binary tree using dictionaries
tree = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {"value": 4, "left": None, "right": None},
        "right": {"value": 5, "left": None, "right": None},
    },
    "right": {
        "value": 3,
        "left": {"value": 6, "left": None, "right": None},
        "right": {"value": 7, "left": None, "right": None},
    },
}

# Pre-order traversal (root, left, right)
def pre_order(node):
    if node is None:
        return []
    return [node["value"]] + pre_order(node["left"]) + pre_order(node["right"])

print(pre_order(tree))  # [1, 2, 4, 5, 3, 6, 7]

# In-order traversal (left, root, right)
def in_order(node):
    if node is None:
        return []
    return in_order(node["left"]) + [node["value"]] + in_order(node["right"])

print(in_order(tree))  # [4, 2, 5, 1, 6, 3, 7]

# Post-order traversal (left, right, root)
def post_order(node):
    if node is None:
        return []
    return post_order(node["left"]) + post_order(node["right"]) + [node["value"]]

print(post_order(tree))  # [4, 5, 2, 6, 7, 3, 1]

# Recursive tree sum
def tree_sum(node):
    if node is None:
        return 0
    return node["value"] + tree_sum(node["left"]) + tree_sum(node["right"])

print(tree_sum(tree))  # 28

# Recursive tree depth
def tree_depth(node):
    if node is None:
        return 0
    return 1 + max(tree_depth(node["left"]), tree_depth(node["right"]))

print(tree_depth(tree))  # 3

print("=" * 5, "Recursive file/directory simulation", "=" * 5)

# Simulate directory structure
file_system = {
    "name": "root",
    "type": "dir",
    "children": [
        {"name": "src", "type": "dir", "children": [
            {"name": "main.py", "type": "file", "size": 1024},
            {"name": "utils.py", "type": "file", "size": 512},
        ]},
        {"name": "docs", "type": "dir", "children": [
            {"name": "readme.md", "type": "file", "size": 256},
        ]},
        {"name": "config.ini", "type": "file", "size": 128},
    ]
}

# Recursive directory listing
def list_files(node, indent=0):
    prefix = "  " * indent
    if node["type"] == "file":
        print(f"{prefix}- {node['name']} ({node['size']}B)")
    else:
        print(f"{prefix}+ {node['name']}/")
        for child in node.get("children", []):
            list_files(child, indent + 1)

list_files(file_system)
# + root/
#   + src/
#     - main.py (1024B)
#     - utils.py (512B)
#   + docs/
#     - readme.md (256B)
#   - config.ini (128B)

# Recursive total size calculation
def total_size(node):
    if node["type"] == "file":
        return node["size"]
    return sum(total_size(child) for child in node.get("children", []))

print(f"Total size: {total_size(file_system)}B")  # Total size: 1920B

print("=" * 5, "Memoization for recursion optimization", "=" * 5)

# Naive Fibonacci is extremely slow for large numbers
# O(2^n) time complexity — recalculates same values repeatedly

# Using functools.lru_cache for memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_memo(n - 1) + fib_memo(n - 2)

print(fib_memo(50))  # 12586269025 (fast!)
print(fib_memo(100))  # 354224848179261915075 (instant!)

# Manual memoization with a dictionary
def fib_manual(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib_manual(n - 1, memo) + fib_manual(n - 2, memo)
    return memo[n]

print(fib_manual(50))  # 12586269025

print("=" * 5, "Tail recursion and iteration", "=" * 5)

# Python does NOT optimize tail recursion
# For deep recursion, use iteration instead

# Recursive factorial (can hit recursion limit)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative factorial (no recursion limit)
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_recursive(10))  # 3628800
print(factorial_iterative(10))  # 3628800

# Check recursion limit
import sys
print(f"Default recursion limit: {sys.getrecursionlimit()}")  # 1000

# For deep recursion, prefer iteration
def factorial_safe(n):
    """Iterative version avoids recursion limit."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_safe(100))  # Very large number, works fine