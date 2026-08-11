# 🐍 CheatSheet for Python

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/YOUR_USERNAME/cheatsheet-python/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/cheatsheet-python/actions/workflows/ci.yml)

A copy-paste-ready Python cheat sheet — every file is self-contained, runnable, and loaded with inline `# result` comments so you can learn by reading **or** by running.

> **Python 3.10+** is required (we use `match`/`case`, `|` union syntax, and other modern features).

---

## 📑 Table of Contents

- [Quick Start](#quick-start)
- [Learning Path](#learning-path)
- [Categories](#categories)
  - [🟢 Beginner — Variables](#-variables--basic-types)
  - [🟢 Beginner — Control Flow](#-control-flow--decision-making)
  - [🟢 Beginner — Functions](#-functions--modular-code)
  - [🟡 Intermediate — Classes](#-classes--object-oriented-programming)
  - [🟡 Intermediate — Input/Output](#-input-output--files-and-arguments)
  - [🟡 Intermediate — Modules](#-modules--packages-and-standard-library)
  - [🟡 Intermediate — Standard Library](#-stdlib--standard-library-reference)
  - [🔴 Advanced — Data Libraries (NumPy, Pandas, Matplotlib, Seaborn)](#-data-libraries--numpy-pandas-matplotlib-seaborn)
  - [🌐 Web Scraping](#-web-scraping)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/cheatsheet-python.git
cd cheatsheet-python

# 2. Run any file directly — no setup needed for standard library examples
python variables/var_1_simple.py
python control-flow/control-flow_1_if.py
python stdlib/stdlib_json.py

# 3. For data library examples (NumPy, Pandas, Matplotlib, Seaborn), install dependencies
pip install -r requirements.txt
python data/numpy_1_array_creation.py
```

> **Tip:** Every `.py` file is self-contained. Just pick a topic and run it — the output with inline comments will guide you.

---

## Learning Path

| Stage | What to learn | Files to start with |
|-------|--------------|---------------------|
| **🟢 Day 1** | Variables, basic types | `var_1_simple` → `var_8_list` |
| **🟢 Day 2** | Control flow | `control-flow_1_if` → `control-flow_9_comprehensions` |
| **🟢 Day 3** | Functions | `functions_1_definition` → `functions_3_lambda` |
| **🟡 Week 2** | Classes & OOP | `classes_1_definition` → `classes_7_dataclasses` |
| **🟡 Week 2** | File I/O & arguments | `input-output_1_input` → `input-output_4_argv_argparse` |
| **🟡 Week 3** | Modules & stdlib | `modules_1_basics`, `stdlib_json`, `stdlib_pathlib` |
| **🔴 Week 4** | NumPy & data | `numpy_1_array_creation` → `numpy_5_linalg_random_io` |
| **🔴 Week 5** | Pandas | `pandas_1_basics` → `pandas_3_io_cleaning_patterns` |
| **🔴 Week 6** | Visualization | `matplotlib_1_basic_plots`, `seaborn_1_statistical_visualization` |

---

## Categories

### 🟢 Variables — Basic Types
| File | Description |
|------|-------------|
| [`var_1_simple.py`](variables/var_1_simple.py) | Variable assignment, naming rules, multiple assignment |
| [`var_2_impossible.py`](variables/var_2_impossible.py) | Impossible values, None, sentinel patterns |
| [`var_3_no_value.py`](variables/var_3_no_value.py) | Uninitialized variables, defaults, None vs missing |
| [`var_4_integer.py`](variables/var_4_integer.py) | Integer operations, division, bitwise, binary/hex/octal |
| [`var_5_boolean.py`](variables/var_5_boolean.py) | Boolean logic, truthiness, short-circuit evaluation |
| [`var_6_float.py`](variables/var_6_float.py) | Float precision, decimal module, formatting |
| [`var_7_string.py`](variables/var_7_string.py) | String methods, formatting, slicing, regex basics |
| [`var_8_list.py`](variables/var_8_list.py) | List creation, methods, comprehensions, slicing |
| [`var_9_tuple.py`](variables/var_9_tuple.py) | Tuple creation, packing/unpacking, named tuples |
| [`var_10_set.py`](variables/var_10_set.py) | Set operations, frozenset, mathematical set theory |
| [`var_11_dictionary.py`](variables/var_11_dictionary.py) | Dict creation, methods, comprehensions, defaultdict |
| [`var_12_bytes.py`](variables/var_12_bytes.py) | Bytes vs str, encoding/decoding, bytearray |

### 🟢 Control Flow — Decision Making
| File | Description |
|------|-------------|
| [`control-flow_1_if.py`](control-flow/control-flow_1_if.py) | if/elif/else, nested, and/or/not, chained comparison |
| [`control-flow_2_for.py`](control-flow/control-flow_2_for.py) | for+list, range, enumerate, zip, nested, break/continue |
| [`control-flow_3_while.py`](control-flow/control-flow_3_while.py) | while, while True, while-else, countdown, Fibonacci |
| [`control-flow_4_break_continue_pass.py`](control-flow/control-flow_4_break_continue_pass.py) | break, continue, pass, for-else pattern |
| [`control-flow_5_match_case.py`](control-flow/control-flow_5_match_case.py) | match-case, OR patterns, variable binding, guards (3.10+) |
| [`control-flow_6_ternary.py`](control-flow/control-flow_6_ternary.py) | Ternary operator, nested ternary, comprehension ternary |
| [`control-flow_7_exception_handling.py`](control-flow/control-flow_7_exception_handling.py) | try/except/else/finally, custom exceptions, raise, assert |
| [`control-flow_8_with_context.py`](control-flow/control-flow_8_with_context.py) | with statement, context managers, contextlib |
| [`control-flow_9_comprehensions.py`](control-flow/control-flow_9_comprehensions.py) | List/dict/set/generator comprehensions, filtering, nesting |

### 🟢 Functions — Modular Code
| File | Description |
|------|-------------|
| [`functions_1_definition.py`](functions/functions_1_definition.py) | Function definition, parameters, return, docstrings, type hints |
| [`functions_2_arguments.py`](functions/functions_2_arguments.py) | Positional/keyword args, *args/**kwargs, defaults, / and * |
| [`functions_3_lambda.py`](functions/functions_3_lambda.py) | Lambda, conditional expressions, closures, common pitfalls |
| [`functions_4_decorators.py`](functions/functions_4_decorators.py) | Decorator basics, @wraps, parameterized decorators, stacking |
| [`functions_5_scope_closure.py`](functions/functions_5_scope_closure.py) | LEGB scope, global/nonlocal, closures, state preservation |
| [`functions_6_generators.py`](functions/functions_6_generators.py) | yield/next, send/throw/close, yield from, memory efficiency |
| [`functions_7_recursion.py`](functions/functions_7_recursion.py) | Factorial, Fibonacci, tree traversal, memoization, tail recursion |
| [`functions_8_builtins.py`](functions/functions_8_builtins.py) | Type conversion, math, iterable, string, inspection builtins |
| [`functions_9_higher_order.py`](functions/functions_9_higher_order.py) | map/filter/reduce, sort keys, compose, partial, currying |

### 🟡 Classes — Object-Oriented Programming
| File | Description |
|------|-------------|
| [`classes_1_definition.py`](classes/classes_1_definition.py) | Class definition, __init__, self, instance/class attributes |
| [`classes_2_inheritance.py`](classes/classes_2_inheritance.py) | Inheritance, super(), MRO, ABC, mixins |
| [`classes_3_encapsulation.py`](classes/classes_3_encapsulation.py) | Public/protected/private, @property, __slots__ |
| [`classes_4_polymorphism.py`](classes/classes_4_polymorphism.py) | Polymorphism, duck typing, operator overloading |
| [`classes_5_methods.py`](classes/classes_5_methods.py) | @classmethod, @staticmethod, alternative constructors |
| [`classes_6_magic_methods.py`](classes/classes_6_magic_methods.py) | __str__/__repr__, comparison, container protocol |
| [`classes_7_dataclasses.py`](classes/classes_7_dataclasses.py) | @dataclass, field(), frozen, __post_init__, asdict |
| [`classes_8_enum_namedtuple.py`](classes/classes_8_enum_namedtuple.py) | Enum, IntEnum, Flag, NamedTuple, comparison |

### 🟡 Input/Output — Files and Arguments
| File | Description |
|------|-------------|
| [`input-output_1_input.py`](input-output/input-output_1_input.py) | input(), type conversion, validation, getpass |
| [`input-output_2_output.py`](input-output/input-output_2_output.py) | print(), f-strings, format(), alignment, pprint |
| [`input-output_3_file_io.py`](input-output/input-output_3_file_io.py) | File read/write, CSV, JSON, seek/tell |
| [`input-output_4_argv_argparse.py`](input-output/input-output_4_argv_argparse.py) | sys.argv, argparse, subcommands |
| [`input-output_5_env_config.py`](input-output/input-output_5_env_config.py) | Environment variables, configparser, TOML |
| [`input-output_6_paths_directories.py`](input-output/input-output_6_paths_directories.py) | os.path, pathlib, shutil, tempfile |
| [`input-output_7_logging.py`](input-output/input-output_7_logging.py) | Log levels, handlers, RotatingFileHandler |

### 🟡 Modules — Packages and Standard Library
| File | Description |
|------|-------------|
| [`modules_1_basics.py`](modules/modules_1_basics.py) | Import styles, module attributes, __all__, reload |
| [`modules_2_packages.py`](modules/modules_2_packages.py) | Package structure, __init__.py, relative imports |
| [`modules_3_os_sys.py`](modules/modules_3_os_sys.py) | os environment, sys.argv, pathlib basics |
| [`modules_4_collections.py`](modules/modules_4_collections.py) | Counter, defaultdict, deque, namedtuple, ChainMap |
| [`modules_5_itertools.py`](modules/modules_5_itertools.py) | count/cycle/repeat, accumulate, chain, groupby |
| [`modules_6_functools.py`](modules/modules_6_functools.py) | reduce, partial, lru_cache, singledispatch |
| [`modules_7_datetime.py`](modules/modules_7_datetime.py) | date, time, datetime, timedelta, timezone |
| [`modules_8_re.py`](modules/modules_8_re.py) | Regex patterns, groups, findall, sub, compile |
| [`modules_9_util.py`](modules/modules_9_util.py) | Utility module (imported by modules_1) |

### 🟡 Stdlib — Standard Library Reference
> Each file covers one library. Run directly — no installation needed.

| File | Library | Description |
|------|---------|-------------|
| [`stdlib_json.py`](stdlib/stdlib_json.py) | `json` | Serialization, custom objects, error handling |
| [`stdlib_math.py`](stdlib/stdlib_math.py) | `math` | Constants, trig, combinatorics, special functions |
| [`stdlib_random.py`](stdlib/stdlib_random.py) | `random` | Random numbers, distributions, sampling, Monte Carlo |
| [`stdlib_pathlib.py`](stdlib/stdlib_pathlib.py) | `pathlib` | Path operations, read/write, glob, vs os.path |
| [`stdlib_hashlib.py`](stdlib/stdlib_hashlib.py) | `hashlib` | SHA-256/MD5/BLAKE2, HMAC, PBKDF2, file integrity |
| [`stdlib_typing.py`](stdlib/stdlib_typing.py) | `typing` | Optional/Union/Literal/Final, Generic, Protocol |
| [`stdlib_argparse.py`](stdlib/stdlib_argparse.py) | `argparse` | CLI arguments, subcommands, custom types |
| [`stdlib_datetime.py`](stdlib/stdlib_datetime.py) | `datetime` | Date/time arithmetic, timezone, age calculation |
| [`stdlib_time.py`](stdlib/stdlib_time.py) | `time` | Timestamps, struct_time, perf_counter, sleep |
| [`stdlib_itertools.py`](stdlib/stdlib_itertools.py) | `itertools` | Infinite iterators, groupby, permutations/combinations |
| [`stdlib_functools.py`](stdlib/stdlib_functools.py) | `functools` | reduce, partial, lru_cache, singledispatch, cached_property |
| [`stdlib_operator.py`](stdlib/stdlib_operator.py) | `operator` | Operator functions, itemgetter/attrgetter/methodcaller |
| [`stdlib_shutil.py`](stdlib/stdlib_shutil.py) | `shutil` | File/directory copy, move, rmtree, archives |
| [`stdlib_glob.py`](stdlib/stdlib_glob.py) | `glob` | Pattern matching, recursive **, vs pathlib vs os.walk |
| [`stdlib_pickle.py`](stdlib/stdlib_pickle.py) | `pickle` | Serialization, custom classes, protocols, safety |
| [`stdlib_os.py`](stdlib/stdlib_os.py) | `os` | Environment, paths, directories, walk, process info |
| [`stdlib_zipfile.py`](stdlib/stdlib_zipfile.py) | `zipfile` | ZIP creation/extraction, in-memory, compression |
| [`stdlib_traceback.py`](stdlib/stdlib_traceback.py) | `traceback` | Stack traces, custom formatting, chained exceptions |
| [`stdlib_urllib.py`](stdlib/stdlib_urllib.py) | `urllib` | URL parsing, encoding, HTTP requests, error handling |
| [`stdlib_webbrowser.py`](stdlib/stdlib_webbrowser.py) | `webbrowser` | Browser detection, open URLs, custom registration |

### 🔴 Data Libraries — NumPy, Pandas, Matplotlib, Seaborn
> Requires `pip install -r requirements.txt` before running.

| File | Library | Description |
|------|---------|-------------|
| [`numpy_1_array_creation.py`](data/numpy_1_array_creation.py) | NumPy | Array creation, dtypes, zeros/ones/full, arange/linspace, random |
| [`numpy_2_indexing_slicing.py`](data/numpy_2_indexing_slicing.py) | NumPy | 1D/2D indexing, fancy indexing, boolean masks, np.where |
| [`numpy_3_reshape_broadcast_math.py`](data/numpy_3_reshape_broadcast_math.py) | NumPy | Reshape/flatten, broadcasting, element-wise ops, matrix math |
| [`numpy_4_sorting_search_sets_stats.py`](data/numpy_4_sorting_search_sets_stats.py) | NumPy | sort/argsort, argmax/min, set operations, statistics |
| [`numpy_5_linalg_random_io.py`](data/numpy_5_linalg_random_io.py) | NumPy | linalg (det/inv/eig/SVD), distributions, file I/O (npy/npz/CSV) |
| [`pandas_1_basics.py`](data/pandas_1_basics.py) | Pandas | Series/DataFrame creation, dtypes, inspection, selection, missing data, strings |
| [`pandas_2_transform_groupby_merge.py`](data/pandas_2_transform_groupby_merge.py) | Pandas | Sorting, GroupBy, merge/join, concat, pivot/melt, time series |
| [`pandas_3_io_cleaning_patterns.py`](data/pandas_3_io_cleaning_patterns.py) | Pandas | CSV/JSON/Excel I/O, apply/map, duplicates, value counts, data cleaning, performance |
| [`matplotlib_1_basic_plots.py`](data/matplotlib_1_basic_plots.py) | Matplotlib | Line, scatter, bar, histogram, pie, error bars, fill_between |
| [`matplotlib_2_subplots_layout_style.py`](data/matplotlib_2_subplots_layout_style.py) | Matplotlib | Subplots, GridSpec, twin axes, custom ticks/annotations, log scale, rcParams, colormaps |
| [`matplotlib_3_statistical_3d_pandas.py`](data/matplotlib_3_statistical_3d_pandas.py) | Matplotlib | Box/violin plots, heatmap, contour, 3D surface/scatter, stacked area, pandas integration |
| [`seaborn_1_statistical_visualization.py`](data/seaborn_1_statistical_visualization.py) | Seaborn | relplot/scatter/line, histplot/KDE/ECDF, box/violin/bar/count/swarm, regplot/lmplot, heatmap/clustermap, pairplot/jointplot, themes/palettes |

### 🌐 Web Scraping
| File | Description |
|------|-------------|
| [`web-scraping_1_extract_news_headlines.py`](web-scraping/web-scraping_1_extract_news_headlines.py) | Extract news headlines with requests + BeautifulSoup |
| [`web-scraping_2_scrape_product_from_ecommerce.py`](web-scraping/web-scraping_2_scrape_product_from_ecommerce.py) | Scrape product data from e-commerce sites |

---

## Repository Structure

```
.
├── LICENSE
├── README.md
├── requirements.txt
├── classes/
│   ├── classes_1_definition.py
│   ├── classes_2_inheritance.py
│   ├── classes_3_encapsulation.py
│   ├── classes_4_polymorphism.py
│   ├── classes_5_methods.py
│   ├── classes_6_magic_methods.py
│   ├── classes_7_dataclasses.py
│   └── classes_8_enum_namedtuple.py
├── control-flow/
│   ├── control-flow_1_if.py
│   ├── control-flow_2_for.py
│   ├── control-flow_3_while.py
│   ├── control-flow_4_break_continue_pass.py
│   ├── control-flow_5_match_case.py
│   ├── control-flow_6_ternary.py
│   ├── control-flow_7_exception_handling.py
│   ├── control-flow_8_with_context.py
│   └── control-flow_9_comprehensions.py
├── functions/
│   ├── functions_1_definition.py
│   ├── functions_2_arguments.py
│   ├── functions_3_lambda.py
│   ├── functions_4_decorators.py
│   ├── functions_5_scope_closure.py
│   ├── functions_6_generators.py
│   ├── functions_7_recursion.py
│   ├── functions_8_builtins.py
│   └── functions_9_higher_order.py
├── input-output/
│   ├── examples/          ← auto-generated by file I/O examples
│   ├── input-output_1_input.py
│   ├── input-output_2_output.py
│   ├── input-output_3_file_io.py
│   ├── input-output_4_argv_argparse.py
│   ├── input-output_5_env_config.py
│   ├── input-output_6_paths_directories.py
│   └── input-output_7_logging.py
├── modules/
│   ├── modules_1_basics.py
│   ├── modules_2_packages.py
│   ├── modules_3_os_sys.py
│   ├── modules_4_collections.py
│   ├── modules_5_itertools.py
│   ├── modules_6_functools.py
│   ├── modules_7_datetime.py
│   ├── modules_8_re.py
│   ├── modules_9_util.py
│   └── shapes_package/
│       ├── __init__.py
│       ├── area.py
│       ├── perimeter.py
│       └── shapes_3d/
│           ├── __init__.py
│           └── volume.py
├── stdlib/
│   ├── stdlib_argparse.py
│   ├── stdlib_datetime.py
│   ├── stdlib_functools.py
│   ├── stdlib_glob.py
│   ├── stdlib_hashlib.py
│   ├── stdlib_itertools.py
│   ├── stdlib_json.py
│   ├── stdlib_math.py
│   ├── stdlib_operator.py
│   ├── stdlib_os.py
│   ├── stdlib_pathlib.py
│   ├── stdlib_pickle.py
│   ├── stdlib_random.py
│   ├── stdlib_shutil.py
│   ├── stdlib_time.py
│   ├── stdlib_traceback.py
│   ├── stdlib_typing.py
│   ├── stdlib_urllib.py
│   ├── stdlib_webbrowser.py
│   └── stdlib_zipfile.py
├── data/
│   ├── matplotlib_1_basic_plots.py
│   ├── matplotlib_2_subplots_layout_style.py
│   ├── matplotlib_3_statistical_3d_pandas.py
│   ├── numpy_1_array_creation.py
│   ├── numpy_2_indexing_slicing.py
│   ├── numpy_3_reshape_broadcast_math.py
│   ├── numpy_4_sorting_search_sets_stats.py
│   ├── numpy_5_linalg_random_io.py
│   ├── pandas_1_basics.py
│   ├── pandas_2_transform_groupby_merge.py
│   ├── pandas_3_io_cleaning_patterns.py
│   └── seaborn_1_statistical_visualization.py
├── variables/
│   ├── var_1_simple.py
│   ├── var_2_impossible.py
│   ├── var_3_no_value.py
│   ├── var_4_integer.py
│   ├── var_5_boolean.py
│   ├── var_6_float.py
│   ├── var_7_string.py
│   ├── var_8_list.py
│   ├── var_9_tuple.py
│   ├── var_10_set.py
│   ├── var_11_dictionary.py
│   └── var_12_bytes.py
└── web-scraping/
    ├── web-scraping_1_extract_news_headlines.py
    └── web-scraping_2_scrape_product_from_ecommerce.py
```

---

## Naming Convention

Files follow the pattern `category_sequencenumber_description.py`:

- **Category directories** — `variables/`, `control-flow/`, `functions/`, `classes/`, `input-output/`, `modules/`, `stdlib/`, `data/`
- **Standard library** — `stdlib_<library>.py` (one file per library)
- **Data libraries** — `<library>_<number>_<topic>.py` (multiple files per library, in `data/`)
- **Comments** — English with inline `# result` comments showing expected output
- **Section separators** — `print("=" * 5, "Section Title", "=" * 5)`
- **Self-contained** — every file runs independently with `python <file>.py`

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new cheat sheet files. PRs are welcome!

---

## License

This project is licensed under the [MIT License](LICENSE).