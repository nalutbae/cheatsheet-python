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

### 🌐 [web-scraping](web-scraping/) — Web scraping examples
| File | Description |
|------|-------------|
| [`web-scraping_1_extract_news_headlines.py`](web-scraping/web-scraping_1_extract_news_headlines.py) | Extract news headlines with requests + BeautifulSoup |
| [`web-scraping_2_scrape_product_from_ecommerce.py`](web-scraping/web-scraping_2_scrape_product_from_ecommerce.py) | Scrape product data from e-commerce sites |

## Repository Structure

```
.
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