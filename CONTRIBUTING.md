# Contributing to CheatSheet for Python

Thank you for your interest in contributing! This guide covers everything you need to know.

## Quick Start

1. **Fork** the repository
2. **Create a branch**: `git checkout -b my-new-topic`
3. **Add your file** following the naming convention below
4. **Test**: `python -m py_compile <your_file>.py`
5. **Commit & push**: `git commit -m "Add <topic> cheat sheet"`
6. **Open a Pull Request**

## File Naming Convention

All files follow the pattern:

```
category/category_sequencenumber_description.py
```

| Category | Example | Notes |
|----------|---------|-------|
| `variables/` | `var_1_simple.py` | Variable prefix (`var_`) |
| `control-flow/` | `control-flow_1_if.py` | Hyphenated category |
| `functions/` | `functions_1_definition.py` | |
| `classes/` | `classes_1_definition.py` | |
| `input-output/` | `input-output_1_input.py` | |
| `modules/` | `modules_1_basics.py` | |
| `stdlib/` | `stdlib_json.py` | One file per library, no sequence number |
| `thirdparty/` | `numpy_1_array_creation.py` | Library prefix, sequence number |

**Rules:**
- Use **underscores** (`_`) in filenames, never dots (except `.py` extension)
- Sequence numbers use **zero-padded single digit**: `_1_`, `_2_`, ..., `_9_`
- `stdlib/` files use `stdlib_<library>.py` format (no sequence number)

## Code Style

Every file must be:

1. **Self-contained** — runs independently with `python <file>.py`
2. **Pure Python** (for `stdlib/` and below) — no `pip install` required
3. **English comments** — all comments and explanations in English
4. **Inline results** — use `# result` comments to show expected output
5. **Section separators** — use `print("=" * 5, "Section Title", "=" * 5)`

Example:

```python
# Topic: brief description

print("=" * 5, "Section Title", "=" * 5)

# Explanation of the concept
result = 2 + 3
print(f"2 + 3 = {result}")  # 2 + 3 = 5

# Another example
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")  # Hello, Alice!
                                   # Hello, Bob!
                                   # Hello, Charlie!
```

## Adding a New Category

1. Create a new directory matching the category name
2. Add files following the naming convention
3. Update `README.md` with the new category table
4. Add the directory to the repository structure section

## Adding a New Standard Library Topic

For `stdlib/` files:

1. Name it `stdlib_<library>.py` (e.g., `stdlib_csv.py`)
2. Import only from the standard library — no external dependencies
3. Cover: basics → common operations → practical patterns → edge cases
4. Update `README.md` stdlib table

## Adding a Third-Party Library

For `data/` files:

1. Add the library to `requirements.txt`
2. Name files as `<library>_<number>_<topic>.py`
3. Include a comment at the top: `# Requires: pip install <package>`
4. Use `matplotlib.use("Agg")` for non-interactive backends in matplotlib/seaborn files
5. Save figures to a temp directory and clean up (no files left after running)
6. Update `README.md` data libraries table

## Running Tests Locally

```bash
# Compile check all files
find . -name '*.py' -not -path '*__pycache__*' -not -path '*examples*' | \
  xargs -I {} python -m py_compile {}

# Check naming convention (no dots in filenames except .py)
find . -name '*.py' -not -path '*__pycache__*' -not -path '*examples*' | \
  while read f; do
    basename=$(basename "$f")
    name="${basename%.py}"
    if echo "$name" | grep -q '\.'; then
      echo "BAD: $f (contains dot in filename)"
    fi
  done
```

## Commit Messages

Use clear, descriptive commit messages:

- `Add stdlib_csv.py — CSV read/write examples`
- `Fix var_4_integer.py naming convention`
- `Add numpy linear algebra examples`

## Questions?

Open an issue if you have questions about contributing. All contributions are welcome!