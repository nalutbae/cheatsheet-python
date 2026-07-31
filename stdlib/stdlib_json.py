# json: JSON serialization and deserialization

import json

print("=" * 5, "Encoding (Python → JSON)", "=" * 5)

# Python dict to JSON string
data = {
    "name": "Alice",
    "age": 30,
    "active": True,
    "score": 95.5,
    "hobbies": ["reading", "coding"],
    "address": {"city": "Seoul", "zip": "04500"},
    "courses": None,
}

json_string = json.dumps(data)
print(f"JSON string: {json_string[:80]}...")

# Pretty-printed JSON
json_pretty = json.dumps(data, indent=2)
print(f"Pretty JSON:\n{json_pretty}")

# Custom formatting options
json_sorted = json.dumps(data, indent=2, sort_keys=True)
print(f"Sorted keys:\n{json_sorted[:120]}...")

# Compact JSON (no whitespace)
json_compact = json.dumps(data, separators=(",", ":"))
print(f"Compact: {json_compact[:80]}...")

# Ensure ASCII (escape non-ASCII characters)
korean_data = {"이름": "홍길동", "도시": "서울"}
json_ascii = json.dumps(korean_data, ensure_ascii=True)
json_utf8 = json.dumps(korean_data, ensure_ascii=False)
print(f"ASCII escaped: {json_ascii}")  # {"\uc774\ub984": "\ud64d\uae38\ub3d9", ...}
print(f"UTF-8 preserved: {json_utf8}")  # {"이름": "홍길동", ...}

# Type mapping: Python → JSON
print(f"dict → object: {json.dumps({'key': 'value'})}")  # {"key": "value"}
print(f"list → array: {json.dumps([1, 2, 3])}")  # [1, 2, 3]
print(f"str → string: {json.dumps('hello')}")  # "hello"
print(f"int → number: {json.dumps(42)}")  # 42
print(f"float → number: {json.dumps(3.14)}")  # 3.14
print(f"True → true: {json.dumps(True)}")  # true
print(f"False → false: {json.dumps(False)}")  # false
print(f"None → null: {json.dumps(None)}")  # null

print("=" * 5, "Decoding (JSON → Python)", "=" * 5)

# JSON string to Python dict
json_text = '{"name": "Bob", "age": 25, "active": true, "score": null}'
parsed = json.loads(json_text)
print(f"Parsed: {parsed}")  # {'name': 'Bob', 'age': 25, 'active': True, 'score': None}
print(f"Type: {type(parsed)}")  # <class 'dict'>
print(f"Name: {parsed['name']}")  # Bob

# Type mapping: JSON → Python
obj_type = type(json.loads('{}'))
arr_type = type(json.loads('[]'))
str_result = json.loads('"hello"')
int_type = type(json.loads('42'))
float_type = type(json.loads('3.14'))
print(f"object → dict: {obj_type}")  # <class 'dict'>
print(f"array → list: {arr_type}")  # <class 'list'>
print(f"string → str: {type(str_result)}")  # <class 'str'>
print(f"number (int) → int: {int_type}")  # <class 'int'>
print(f"number (float) → float: {float_type}")  # <class 'float'>
print(f"true → True: {json.loads('true')}")  # True
print(f"false → False: {json.loads('false')}")  # False
print(f"null → None: {json.loads('null')}")  # None

print("=" * 5, "File I/O with JSON", "=" * 5)

import os

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "stdlib_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

# Write JSON to file
file_path = os.path.join(EXAMPLE_DIR, "data.json")

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Read JSON from file
with open(file_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"Loaded from file: {loaded['name']}")  # Alice
print(f"Hobbies: {loaded['hobbies']}")  # ['reading', 'coding']

print("=" * 5, "Custom serialization with default", "=" * 5)

# Handling non-serializable types
from datetime import datetime

event = {
    "title": "Meeting",
    "date": datetime(2025, 7, 31, 14, 30),
    "attendees": 5,
}

# Default handler for non-serializable types
def json_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

json_with_date = json.dumps(event, default=json_default, indent=2)
print(f"Custom serialization:\n{json_with_date}")

# Parsing dates back
def json_object_hook(d):
    for key, value in d.items():
        if isinstance(value, str) and "T" in value and value.count("-") >= 2:
            try:
                d[key] = datetime.fromisoformat(value)
            except (ValueError, TypeError):
                pass
    return d

parsed_back = json.loads(json_with_date, object_hook=json_object_hook)
print(f"Date type: {type(parsed_back['date'])}")  # <class 'datetime.datetime'>
print(f"Date value: {parsed_back['date']}")  # 2025-07-31 14:30:00

print("=" * 5, "JSON with custom objects", "=" * 5)

class Student:
    def __init__(self, name, grade, student_id):
        self.name = name
        self.grade = grade
        self.student_id = student_id

    def to_dict(self):
        return {"name": self.name, "grade": self.grade, "id": self.student_id}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["grade"], data["id"])

# Serialize custom object
student = Student("Charlie", 92, "S001")
student_json = json.dumps(student.to_dict(), indent=2)
print(f"Student JSON: {student_json}")

# Deserialize back to custom object
restored = Student.from_dict(json.loads(student_json))
print(f"Restored: {restored.name}, grade={restored.grade}, id={restored.student_id}")

# Serialize a list of custom objects
students = [
    Student("Alice", 95, "S001"),
    Student("Bob", 88, "S002"),
    Student("Charlie", 92, "S003"),
]
students_json = json.dumps([s.to_dict() for s in students], indent=2)
print(f"Students JSON:\n{students_json}")

# Deserialize list of custom objects
restored_students = [Student.from_dict(d) for d in json.loads(students_json)]
print(f"Restored {len(restored_students)} students")
for s in restored_students:
    print(f"  {s.name}: {s.grade}")

print("=" * 5, "JSON validation and error handling", "=" * 5)

# Valid JSON
try:
    result = json.loads('{"valid": true}')
    print(f"Valid JSON: {result}")  # {'valid': True}
except json.JSONDecodeError as e:
    print(f"Error: {e}")

# Invalid JSON
try:
    result = json.loads("{'invalid': true}")  # single quotes
except json.JSONDecodeError as e:
    print(f"JSON error: {e.msg}")  # Expecting property name enclosed in double quotes

# Common JSON errors
invalid_jsons = [
    "{missing_quotes: true}",           # unquoted key
    "{'single_quotes': true}",          # single quotes
    "{trailing_comma: true,}",          # trailing comma
    "{unquoted_string: hello}",          # unquoted string value
    "{missing_colon true}",             # missing colon
]
for invalid in invalid_jsons:
    try:
        json.loads(invalid)
    except json.JSONDecodeError as e:
        print(f"  Error in '{invalid[:20]}...': {e.msg}")