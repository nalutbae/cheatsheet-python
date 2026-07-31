# CheatSheet for Python

This is a repository that collects examples for the purpose of finding and writing Python basics, grammar, and situational snippets.  
Every file is self-contained — copy a snippet, paste it into your editor, and run it directly.

## Categories

### 📦 [variables](variables/) — Variable types and operations
| File | Description |
|------|-------------|
| [`var_1_simple.py`](variables/var_1_simple.py) | Variable declaration, assignment, swap |
| [`var_2_impossible.py`](variables/var_2_impossible.py) | Type constraints and impossible operations |
| [`var_3_no_value.py`](variables/var_3_no_value.py) | None, empty values, falsy types |
| [`var_4.integer.py`](variables/var_4.integer.py) | Integer operations, division, bitwise |
| [`var_5_boolean.py`](variables/var_5_boolean.py) | Boolean operators, comparisons, truthiness |
| [`var_6_float.py`](variables/var_6_float.py) | Float precision, rounding, math operations |
| [`var_7_string.py`](variables/var_7_string.py) | String creation, indexing, escape sequences |
| [`var_8_list.py`](variables/var_8_list.py) | List creation, indexing, slicing, methods |
| [`var_9_tuple.py`](variables/var_9_tuple.py) | Tuple creation, unpacking, immutability |
| [`var_10_set.py`](variables/var_10_set.py) | Set creation, operations, intersection/union |
| [`var_11_dictionary.py`](variables/var_11_dictionary.py) | Dict creation, access, methods, comprehension |
| [`var_12_bytes.py`](variables/var_12_bytes.py) | Bytes/bytearray creation, encoding, decoding |

### 🔀 [control-flow](control-flow/) — Control flow statements
| File | Description |
|------|-------------|
| [`control-flow_1_if.py`](control-flow/control-flow_1_if.py) | if/elif/else, nested if, truthiness, chained comparisons, is vs == |
| [`control-flow_2_for.py`](control-flow/control-flow_2_for.py) | for loop, range, enumerate, zip, dict iteration, break/continue, for-else, walrus operator |
| [`control-flow_3_while.py`](control-flow/control-flow_3_while.py) | while loop, while True, while-else, countdown, Fibonacci, GCD algorithm |
| [`control-flow_4_break_continue_pass.py`](control-flow/control-flow_4_break_continue_pass.py) | break, continue, pass — usage, nested loops, for-else with break, comparison of the three |
| [`control-flow_5_match_case.py`](control-flow/control-flow_5_match_case.py) | match-case (3.10+), literal/OR patterns, variable binding, type matching, list/dict patterns, guards |
| [`control-flow_6_ternary.py`](control-flow/control-flow_6_ternary.py) | Ternary conditional expression, nested ternary, short-circuit evaluation (and/or), default value patterns |
| [`control-flow_7_exception_handling.py`](control-flow/control-flow_7_exception_handling.py) | try/except/else/finally, specific exceptions, custom exceptions, raise/re-raise, assert, exception hierarchy |
| [`control-flow_8_with_context.py`](control-flow/control-flow_8_with_context.py) | with statement, context manager (class & @contextmanager), suppress, redirect_stdout, transaction pattern |
| [`control-flow_9_comprehensions.py`](control-flow/control-flow_9_comprehensions.py) | List/dict/set comprehension, generator expressions, filtering, nesting, conditions, memory comparison |

### 🛠 [functions](functions/) — Functions and functional programming
| File | Description |
|------|-------------|
| [`functions_1_definition.py`](functions/functions_1_definition.py) | Function definition, parameters, return values, docstrings, type hints, first-class functions |
| [`functions_2_arguments.py`](functions/functions_2_arguments.py) | Positional/keyword args, defaults, *args/**kwargs, unpacking, positional-only (/), keyword-only (*), full signature |
| [`functions_3_lambda.py`](functions/functions_3_lambda.py) | Lambda expressions, map/filter/reduce, sorted key, dict values, closure gotcha (capture by reference) |
| [`functions_4_decorators.py`](functions/functions_4_decorators.py) | Decorator basics, @wraps, decorator with arguments, stacking, timing/debug/auth/memoize decorators, class-based decorator |
| [`functions_5_scope_closure.py`](functions/functions_5_scope_closure.py) | LEGB rule, local/global/nonlocal scope, closures, state maintenance (counter/accumulator), scope resolution order |
| [`functions_6_generators.py`](functions/functions_6_generators.py) | yield/next, send/throw/close, yield from, Fibonacci/prime generators, chunk generator, memory comparison with itertools |
| [`functions_7_recursion.py`](functions/functions_7_recursion.py) | Factorial/Fibonacci, nested list flatten/sum/depth, string reverse/palindrome, binary tree traversal, memoization (lru_cache/manual), tail recursion vs iteration |
| [`functions_8_builtins.py`](functions/functions_8_builtins.py) | Type conversion, math (abs/round/min/max/sum/pow/divmod), iterables (enumerate/zip/map/filter/sorted/any/all), string (chr/ord/format), type checking (isinstance/hasattr), eval/exec |
| [`functions_9_higher_order.py`](functions/functions_9_higher_order.py) | First-class functions, map/filter/reduce, sorted key, function composition (compose/pipe), functools.partial, currying |

### 🏛️ [classes](classes/) — Classes and object-oriented programming
| File | Description |
|------|-------------|
| [`classes_1_definition.py`](classes/classes_1_definition.py) | Class definition, __init__, self, instance/class attributes, instance methods, __str__/__repr__, dynamic attributes |
| [`classes_2_inheritance.py`](classes/classes_2_inheritance.py) | Inheritance, super(), method overriding, isinstance/issubclass, multiple inheritance, MRO, abstract base classes (ABC), mixins |
| [`classes_3_encapsulation.py`](classes/classes_3_encapsulation.py) | Public/protected/private attributes, name mangling, @property (getter/setter/deleter), computed properties, __slots__ |
| [`classes_4_polymorphism.py`](classes/classes_4_polymorphism.py) | Polymorphism, duck typing, operator overloading (+, -, *, /, ==, <, >), common dunder methods, __call__, context manager with __enter__/__exit__ |
| [`classes_5_methods.py`](classes/classes_5_methods.py) | Instance methods, @classmethod (alternative constructors), @staticmethod (utility functions), from_string/from_dict/from_json patterns, tracking instances |
| [`classes_6_magic_methods.py`](classes/classes_6_magic_methods.py) | __new__/__init__/__del__, __str__/__repr__/__format__, comparison (__eq__/__lt__/@total_ordering), container protocol (__len__/__getitem__/__contains__/__iter__), Fraction class, type conversion |
| [`classes_7_dataclasses.py`](classes/classes_7_dataclasses.py) | @dataclass basics, default values, field(), frozen dataclass, inheritance, order=True, __post_init__, asdict/astuple/replace, computed fields |
| [`classes_8_enum_namedtuple.py`](classes/classes_8_enum_namedtuple.py) | Enum, IntEnum, auto(), Flag/IntFlag (bitwise), NamedTuple, functional syntax, Enum vs dataclass vs NamedTuple comparison |

### 📦 [modules](modules/) — Modules, packages, and standard library
| File | Description |
|------|-------------|
| [`modules_1_basics.py`](modules/modules_1_basics.py) | Module basics, import styles, module attributes, custom module import, conditional import, __all__, reload |
| [`modules_2_packages.py`](modules/modules_2_packages.py) | Package structure, __init__.py, import styles for packages, sys.path, relative imports, nested packages |
| [`modules_3_os_sys.py`](modules/modules_3_os_sys.py) | os (environment, paths, directories, walk), sys (argv, version, path, modules), pathlib (Path, glob, read/write) |
| [`modules_4_collections.py`](modules/modules_4_collections.py) | Counter, defaultdict, OrderedDict, deque (appendleft/popleft/rotate/maxlen), namedtuple, ChainMap |
| [`modules_5_itertools.py`](modules/modules_5_itertools.py) | count/cycle/repeat, accumulate, chain, compress/filterfalse/takewhile/dropwhile, groupby, islice, permutations/combinations/product, zip_longest, starmap |
| [`modules_6_functools.py`](modules/modules_6_functools.py) | reduce, partial, lru_cache, @wraps, @total_ordering, @singledispatch, @cached_property |
| [`modules_7_datetime.py`](modules/modules_7_datetime.py) | date, time, datetime, timedelta, timezone, strftime/strptime, date arithmetic, age calculation, timezone conversion |
| [`modules_8_re.py`](modules/modules_8_re.py) | Pattern matching, character classes, quantifiers, anchors, groups, findall/finditer/sub, split, compile, common patterns (email, URL, phone) |
| [`modules_9_util.py`](modules/modules_9_util.py) | Utility module imported by modules_1_basics.py (add, multiply, greet, Calculator, __all__, if __name__) |

📦 [modules/shapes_package/](modules/shapes_package/) — Sample package for modules_2_packages.py
| File | Description |
|------|-------------|
| [`__init__.py`](modules/shapes_package/__init__.py) | Package init: exports area and perimeter modules |
| [`area.py`](modules/shapes_package/area.py) | Area calculations: circle, rectangle, triangle, square, trapezoid |
| [`perimeter.py`](modules/shapes_package/perimeter.py) | Perimeter calculations: circle, rectangle, square, triangle |
| [`shapes_3d/__init__.py`](modules/shapes_package/shapes_3d/__init__.py) | Subpackage init: exports volume module |
| [`shapes_3d/volume.py`](modules/shapes_package/shapes_3d/volume.py) | Volume calculations: sphere, cube, cuboid, cylinder, cone |

### 📡 [input-output](input-output/) — Input, output, and I/O operations
| File | Description |
|------|-------------|
| [`input-output_1_input.py`](input-output/input-output_1_input.py) | input(), type conversion, multi-value input, validation, sentinel loop, getpass, interactive menu |
| [`input-output_2_output.py`](input-output/input-output_2_output.py) | print() (sep/end/file), f-strings (format spec, alignment, debug), str.format(), %-formatting, ljust/rjust/center/zfill, pprint, table output |
| [`input-output_3_file_io.py`](input-output/input-output_3_file_io.py) | File open/write/read/append modes, readline/readlines, binary I/O, seek/tell, CSV (reader/writer/DictReader), JSON (dump/load), os.path & pathlib |
| [`input-output_4_argv_argparse.py`](input-output/input-output_4_argv_argparse.py) | sys.argv, argparse (positional/optional args, defaults, type, choices, nargs, mutually exclusive groups, subcommands), redirect_stdout/stderr |
| [`input-output_5_env_config.py`](input-output/input-output_5_env_config.py) | Environment variables (os.getenv/environ), type conversion helpers, INI config (configparser), TOML config (tomllib), JSON config |
| [`input-output_6_paths_directories.py`](input-output/input-output_6_paths_directories.py) | os.path (join/split/abspath/exists/isfile/isdir), pathlib (Path/Slash operator/glob/read_text/write_text/stat), shutil (copy/move/rmtree), tempfile |
| [`input-output_7_logging.py`](input-output/input-output_7_logging.py) | Log levels, formatters, file+console handlers, logger hierarchy, RotatingFileHandler, TimedRotatingFileHandler, custom formatter, dictConfig |

### 📚 [stdlib](stdlib/) — Standard library (one file per library)
| File | Description |
|------|-------------|
| [`stdlib_json.py`](stdlib/stdlib_json.py) | JSON serialization/deserialization, dumps/loads, dump/load files, custom objects, error handling |
| [`stdlib_math.py`](stdlib/stdlib_math.py) | Math constants, rounding, power/log, trigonometric, combinatorial (comb/perm/gcd/lcm), special functions (erf/gamma), floating-point utilities |
| [`stdlib_random.py`](stdlib/stdlib_random.py) | Random numbers, seed, choice/choices/sample, shuffle, distributions (gauss/uniform/triangular), practical examples (password, color, Monte Carlo) |
| [`stdlib_pathlib.py`](stdlib/stdlib_pathlib.py) | Path creation/properties, read/write files, directory operations, glob/rglob, path vs os.path comparison, temporary files |
| [`stdlib_hashlib.py`](stdlib/stdlib_hashlib.py) | SHA-256/MD5/SHA-1/BLAKE2 hashing, incremental hashing, HMAC, password hashing with salt, PBKDF2, file integrity verification |
| [`stdlib_typing.py`](stdlib/stdlib_typing.py) | Type hints, Optional/Union/Literal/Final, Callable, TypeVar, Generic, TypedDict, Protocol, TypeAlias, overload |
| [`stdlib_argparse.py`](stdlib/stdlib_argparse.py) | Positional/optional arguments, types, nargs, subcommands, mutually exclusive groups, custom type conversion, complete CLI example |
| [`stdlib_datetime.py`](stdlib/stdlib_datetime.py) | date/time/datetime, timedelta arithmetic, timezone handling, strftime/strptime, age calculation, business day logic |
| [`stdlib_functools.py`](stdlib/stdlib_functools.py) | reduce, partial, @lru_cache, @wraps, @total_ordering, @singledispatch, @cached_property, practical patterns |
| [`stdlib_glob.py`](stdlib/stdlib_glob.py) | glob/iglob patterns, recursive **, character ranges [abc], glob.escape, glob vs pathlib vs os.walk comparison |
| [`stdlib_hashlib.py`](stdlib/stdlib_hashlib.py) | SHA-256/MD5/SHA-1/BLAKE2 hashing, incremental hashing, HMAC, password hashing with salt, PBKDF2, file integrity verification |
| [`stdlib_itertools.py`](stdlib/stdlib_itertools.py) | count/cycle/repeat, accumulate, chain, compress/filterfalse/takewhile/dropwhile, groupby, islice, permutations/combinations/product, zip_longest |
| [`stdlib_json.py`](stdlib/stdlib_json.py) | JSON serialization/deserialization, dumps/loads, dump/load files, custom objects, error handling |
| [`stdlib_math.py`](stdlib/stdlib_math.py) | Math constants, rounding, power/log, trigonometric, combinatorial (comb/perm/gcd/lcm), special functions (erf/gamma), floating-point utilities |
| [`stdlib_operator.py`](stdlib/stdlib_operator.py) | Arithmetic/comparison/logical operators as functions, itemgetter/attrgetter/methodcaller, functional patterns with reduce/sort/groupby |
| [`stdlib_os.py`](stdlib/stdlib_os.py) | Environment variables, path operations (join/split/abspath), file/directory existence, stat, directory creation/removal, os.walk, process/system info |
| [`stdlib_pathlib.py`](stdlib/stdlib_pathlib.py) | Path creation/properties, read/write files, directory operations, glob/rglob, path vs os.path comparison, temporary files |
| [`stdlib_pickle.py`](stdlib/stdlib_pickle.py) | Object serialization/deserialization, file I/O, custom classes, __getstate__/__setstate__, protocols, caching pattern, safety warnings |
| [`stdlib_random.py`](stdlib/stdlib_random.py) | Random numbers, seed, choice/choices/sample, shuffle, distributions (gauss/uniform/triangular), practical examples (password, color, Monte Carlo) |
| [`stdlib_shutil.py`](stdlib/stdlib_shutil.py) | File/directory copy (copy/copytree), move, rmtree, disk_usage, which, make_archive/unpack_archive, copystat |
| [`stdlib_time.py`](stdlib/stdlib_time.py) | Timestamps, struct_time, formatting/parsing (strftime/strptime), sleep, perf_counter/monotonic/process_time, timezone info, Timer context manager |
| [`stdlib_traceback.py`](stdlib/stdlib_traceback.py) | format_exc/extract_tb/extract_stack, custom error formatting, walking traceback frames, chained exceptions, logging integration, ExceptionReporter |
| [`stdlib_typing.py`](stdlib/stdlib_typing.py) | Type hints, Optional/Union/Literal/Final, Callable, TypeVar, Generic, TypedDict, Protocol, TypeAlias, overload |
| [`stdlib_urllib.py`](stdlib/stdlib_urllib.py) | URL parsing (urlparse), construction (urlunparse), encoding (quote/unquote), query strings (parse_qs/urlencode), HTTP requests (urlopen), error handling |
| [`stdlib_webbrowser.py`](stdlib/stdlib_webbrowser.py) | Browser detection, open/open_new/open_new_tab, specific browser controllers, custom browser registration, search URL builder |
| [`stdlib_zipfile.py`](stdlib/stdlib_zipfile.py) | ZIP creation/reading/extraction, writestr, compression methods, ZipInfo, password-protected archives, in-memory ZIP, integrity check, directory backup |

### 🌐 [web-scraping](web-scraping/) — Web scraping examples
| File | Description |
|------|-------------|
| [`web-scraping_1_extract_news_headlines.py`](web-scraping/web-scraping_1_extract_news_headlines.py) | Extract news headlines with requests + BeautifulSoup |
| [`web-scraping_2_scrape_product_from_ecommerce.py`](web-scraping/web-scraping_2_scrape_product_from_ecommerce.py) | Scrape product data from e-commerce sites |

## Repository Structure

```
.
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
├── variables/
│   ├── var_1_simple.py
│   ├── var_2_impossible.py
│   ├── var_3_no_value.py
│   ├── var_4.integer.py
│   ├── var_5_boolean.py
│   ├── var_6_float.py
│   ├── var_7_string.py
│   ├── var_8_list.py
│   ├── var_9_tuple.py
│   ├── var_10_set.py
│   ├── var_11_dictionary.py
│   └── var_12_bytes.py
├── web-scraping/
│   ├── web-scraping_1_extract_news_headlines.py
│   └── web-scraping_2_scrape_product_from_ecommerce.py
├── requirements.txt
└── README.md
```

## Naming Convention

Files follow the pattern `category_sequance_description.py`:

- **category** — folder name (e.g. `control-flow`, `functions`, `input-output`)
- **sequance** — zero-padded sequence number (e.g. `1`, `2`, … `12`)
- **description** — short topic name in snake_case (e.g. `if`, `for`, `lambda`)

## Contributions

Contributions through PR are always welcome.