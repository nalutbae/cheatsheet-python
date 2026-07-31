# Regular expressions with the re module

import re

print("=" * 5, "Basic pattern matching", "=" * 5)

# re.search: find first match anywhere in string
result = re.search(r"world", "hello world")
print(f"search 'world': {result.group()}")  # world
print(f"Match position: {result.start()}-{result.end()}")  # 6-11

# re.match: match only at the beginning
result = re.match(r"hello", "hello world")
print(f"match 'hello': {result.group()}")  # hello

result = re.match(r"world", "hello world")
print(f"match 'world': {result}")  # None (not at beginning)

# re.fullmatch: match the entire string
result = re.fullmatch(r"\d{3}", "123")
print(f"fullmatch '123': {result.group()}")  # 123

result = re.fullmatch(r"\d{3}", "1234")
print(f"fullmatch '1234': {result}")  # None

print("=" * 5, "Character classes", "=" * 5)

# \d — digit, \w — word char, \s — whitespace
result_d = re.search(r'\d+', 'abc123def').group()
result_w = re.search(r'\w+', 'hello world').group()
result_s = re.search(r'\s+', 'hello world').group()
print(f"\\d match: {result_d}")  # 123
print(f"\\w match: {result_w}")  # hello
print(f"\\s match: {result_s}")  # " " (space)

# \D — non-digit, \W — non-word, \S — non-whitespace
result_D = re.search(r'\D+', 'abc123').group()
result_W = re.search(r'\W+', 'hello!@#world').group()
print(f"\\D match: {result_D}")  # abc
print(f"\\W match: {result_W}")  # !@#

# Custom character classes
print(f"[aeiou]: {re.findall(r'[aeiou]', 'hello world')}")  # ['e', 'o', 'o']
print(f"[a-z]+: {re.findall(r'[a-z]+', 'Hello World 123')}")  # ['ello', 'orld']
print(f"[A-Z]+: {re.findall(r'[A-Z]+', 'Hello World 123')}")  # ['H', 'W']
print(f"[0-9]+: {re.findall(r'[0-9]+', 'Hello World 123')}")  # ['123']

# Negated character classes
print(f"[^aeiou]: {re.findall(r'[^aeiou]', 'hello')}")  # ['h', 'l', 'l']

print("=" * 5, "Quantifiers", "=" * 5)

# * — 0 or more, + — 1 or more, ? — 0 or 1
print(f"*: {re.findall(r'ab*c', ['ac', 'abc', 'abbc', 'abbbc'])}")  # Not like this
print(f"a*b: {re.findall(r'a*b', 'aab ab b')}")  # ['aab', 'ab', 'b']
print(f"a+b: {re.findall(r'a+b', 'aab ab b')}")  # ['aab', 'ab']
print(f"a?b: {re.findall(r'a?b', 'aab ab b')}")  # ['ab', 'ab', 'b']

# {n} — exactly n, {n,m} — between n and m
text = "123-456-7890 and 555-123-4567"
phone_pattern = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(f"Phone pattern: {phone_pattern}")  # ['123-456-7890', '555-123-4567']

# Greedy vs non-greedy (lazy)
html = "<div>Hello</div><span>World</span>"
greedy = re.findall(r'<.*>', html)
lazy = re.findall(r'<.*?>', html)
print(f"Greedy: {greedy}")  # ['<div>Hello</div><span>World</span>']
print(f"Lazy: {lazy}")  # ['<div>', '</div>', '<span>', '</span>']

print("=" * 5, "Anchors and boundaries", "=" * 5)

# ^ — start of string, $ — end of string
print(f"^Hello: {bool(re.match(r'^Hello', 'Hello World'))}")  # True
print(f"^World: {bool(re.match(r'^World', 'Hello World'))}")  # False
print(f"World$: {bool(re.search(r'World$', 'Hello World'))}")  # True
print(f"Hello$: {bool(re.search(r'Hello$', 'Hello World'))}")  # False

# \b — word boundary
text = "cat category concatenate cat"
word_cat = re.findall(r'\bcat\b', text)
print(f"\\bcat\\b: {word_cat}")  # ['cat', 'cat']

# ^ and $ with MULTILINE
text_multi = "line1\nline2\nline3"
print(f"^line (no MULTILINE): {re.findall(r'^line', text_multi)}")  # ['line']
print(f"^line (MULTILINE): {re.findall(r'^line', text_multi, re.MULTILINE)}")  # ['line', 'line', 'line']

print("=" * 5, "Groups and capturing", "=" * 5)

# Named groups
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
text = "Date: 2025-07-31"
match = re.search(pattern, text)
if match:
    print(f"Year: {match.group('year')}")  # 2025
    print(f"Month: {match.group('month')}")  # 07
    print(f"Day: {match.group('day')}")  # 31
    print(f"All groups: {match.groups()}")  # ('2025', '07', '31')
    print(f"Group dict: {match.groupdict()}")  # {'year': '2025', 'month': '07', 'day': '31'}

# Non-capturing groups (?:...)
pattern = r"(?:\d{3})-(\d{4})"
match = re.search(pattern, "123-4567")
print(f"Group 1 (capturing): {match.group(1)}")  # 4567
# Group 0 is always the full match
print(f"Full match: {match.group(0)}")  # 123-4567

# Multiple groups
pattern = r"(\w+)@(\w+)\.(\w+)"
match = re.search(pattern, "user@example.com")
print(f"User: {match.group(1)}")  # user
print(f"Domain: {match.group(2)}")  # example
print(f"TLD: {match.group(3)}")  # com

print("=" * 5, "findall, finditer, and sub", "=" * 5)

# re.findall: find all matches
text = "Email: user@example.com and admin@test.org"
emails = re.findall(r'\b\w+@\w+\.\w+\b', text)
print(f"Emails: {emails}")  # ['user@example.com', 'admin@test.org']

# re.finditer: find all matches with match objects
for match in re.finditer(r'\b\w+@\w+\.\w+\b', text):
    print(f"  Found: {match.group()} at position {match.start()}")

# re.sub: replace matches
text = "Hello 123 world 456"
result = re.sub(r'\d+', 'NUM', text)
print(f"Replace digits: {result}")  # Hello NUM world NUM

# Replace with a function
def replace_with_stars(match):
    return '*' * len(match.group())

result = re.sub(r'\d+', replace_with_stars, "Secret: 1234 and 567")
print(f"Censor digits: {result}")  # Secret: **** and ***

# Replace with backreferences
text = "Smith, John"
result = re.sub(r'(\w+), (\w+)', r'\2 \1', text)
print(f"Swap names: {result}")  # John Smith

# Count replacements
text = "one two one two one"
result = re.sub(r'one', 'ONE', text, count=2)
print(f"Replace count=2: {result}")  # ONE two ONE two one

print("=" * 5, "Split and compile", "=" * 5)

# re.split: split by pattern
text = "one;two,three four"
result = re.split(r'[;,\s]+', text)
print(f"Split: {result}")  # ['one', 'two', 'three', 'four']

# Split with maxsplit
result = re.split(r'[;,\s]+', text, maxsplit=2)
print(f"Split maxsplit=2: {result}")  # ['one', 'two', 'three four']

# re.compile: pre-compile a pattern for reuse
email_pattern = re.compile(r'\b[\w.]+@[\w.]+\.\w+\b')
text = "Contact: info@company.com or support@company.org"
print(f"Compiled findall: {email_pattern.findall(text)}")  # ['info@company.com', 'support@company.org']

# Compile with flags
case_insensitive = re.compile(r'hello', re.IGNORECASE)
print(f"Case insensitive: {case_insensitive.findall('Hello HELLO hello')}")  # ['Hello', 'HELLO', 'hello']

# Common flags
dotall_result = re.findall(r'.+', 'line1\nline2', re.DOTALL)
no_dotall_result = re.findall(r'.+', 'line1\nline2')
print(f"DOTALL (. matches \\n): {dotall_result}")  # ['line1\nline2']
print(f"Without DOTALL: {no_dotall_result}")  # ['line1', 'line2']

print("=" * 5, "Common regex patterns", "=" * 5)

# Email validation (basic)
email_re = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
for email in ["user@example.com", "invalid.email", "test@org"]:
    print(f"  {email}: {bool(re.match(email_re, email))}")

# URL extraction
url_text = "Visit https://example.com and http://test.org/path"
urls = re.findall(r'https?://[\w./-]+', url_text)
print(f"URLs: {urls}")

# Phone number extraction
phone_text = "Call 010-1234-5678 or 02-987-6543"
phones = re.findall(r'\d{2,3}-\d{3,4}-\d{4}', phone_text)
print(f"Phones: {phones}")

# Extract numbers from text
number_text = "Temperature: 23.5C, Humidity: 78%, Pressure: 1013.25hPa"
numbers = re.findall(r'\d+\.?\d*', number_text)
print(f"Numbers: {numbers}")  # ['23.5', '78', '1013.25']

# Remove HTML tags
html = "<p>Hello <b>world</b></p>"
clean = re.sub(r'<[^>]+>', '', html)
print(f"Strip HTML: {clean}")  # Hello world

# Validate password (8+ chars, 1 uppercase, 1 digit)
password_re = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
for pwd in ["weak", "Strong123", "noDigitHere", "short1"]:
    print(f"  {pwd}: {bool(re.match(password_re, pwd))}")