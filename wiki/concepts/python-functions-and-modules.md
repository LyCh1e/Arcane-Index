---
type: concept
title: "Python Functions, Modules & Functional Programming"
domain: programming-fundamentals
complexity: medium
source: "[[sources/INF1002-programming-fundamentals]]"
address: c-000044
created: 2026-05-23
updated: 2026-05-23
tags: [concept, programming-fundamentals, python, functions, recursion, higher-order-functions, lambda, INF1002]
---

# Python Functions, Modules & Functional Programming

Defining and calling functions, controlling scope, organising code into modules, and using Python's functional programming tools: higher-order functions, lambda expressions, and recursion.

---

## Defining Functions

```python
def greet(name):
    """Return a greeting string."""   # docstring
    return f"Hello, {name}!"

result = greet("Alice")   # "Hello, Alice!"
```

- `def` followed by the function name and a parenthesised parameter list.
- The body is indented.
- `return` exits the function and optionally passes back a value. Without `return`, the function returns `None`.

### Docstrings

Triple-quoted strings as the first line of a function (or module) serve as documentation:

```python
def add(a, b):
    """
    Return the sum of a and b.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The sum a + b.
    """
    return a + b
```

Accessible at runtime via `add.__doc__` and used by `help()`.

---

## Parameters and Arguments

### Positional and Keyword Arguments

```python
def power(base, exponent):
    return base ** exponent

power(2, 3)              # positional — base=2, exponent=3
power(exponent=3, base=2)  # keyword — order irrelevant
```

### Default Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")            # "Hello, Alice!"
greet("Bob", "Hi")        # "Hi, Bob!"
```

> Default arguments must come after non-default parameters in the signature.

### `*args` — Variable Positional Arguments

```python
def total(*args):
    return sum(args)      # args is a tuple

total(1, 2, 3)            # 6
total(10, 20)             # 30
```

### `**kwargs` — Variable Keyword Arguments

```python
def describe(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

describe(name="Alice", age=25)
```

`kwargs` is a `dict` inside the function.

---

## Scope

Python uses **LEGB** scope resolution: Local → Enclosing → Global → Built-in.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)     # "local"

    inner()
    print(x)         # "enclosing"

outer()
print(x)             # "global"
```

### `global` Keyword

```python
count = 0

def increment():
    global count
    count += 1    # modifies the global variable
```

Without `global`, assignment inside a function creates a new local variable.

### `nonlocal` Keyword

```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1    # modifies the enclosing function's variable
    inner()
    return x      # 1
```

> Local variables are destroyed when the function exits; globals persist for the lifetime of the programme.

---

## Modules

A **module** is any `.py` file. A **package** is a directory of modules. A **library** is a collection of packages.

### Importing

```python
import math                   # import the whole module
math.sqrt(16)                 # access via dot

import math as m              # alias
m.sqrt(16)

from math import sqrt, pi     # import specific names
sqrt(16)

from math import *            # import everything (not recommended)
```

### Standard Library Highlights

| Module | Purpose |
|---|---|
| `math` | Mathematical functions (`sqrt`, `log`, `floor`) |
| `random` | Random number generation |
| `os` | OS interaction (paths, environment) |
| `sys` | Python runtime (argv, path, exit) |
| `functools` | Higher-order function utilities (`reduce`, `lru_cache`) |
| `copy` | Deep/shallow copy utilities |
| `datetime` | Date and time manipulation |

---

## Higher-Order Functions

A **higher-order function** (HOF) takes a function as an argument or returns one.

### `sorted()`

```python
words = ["banana", "apple", "cherry"]
sorted(words)                         # alphabetical
sorted(words, key=len)                # sort by string length
sorted(words, key=lambda w: w[-1])    # sort by last character
sorted(words, reverse=True)           # descending
```

### `map(func, iterable)`

Applies `func` to every element; returns a **lazy iterator**.

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))   # [2, 4, 6, 8]

# Equivalent list comprehension:
doubled = [x * 2 for x in nums]
```

### `filter(func, iterable)`

Returns elements for which `func` returns truthy; lazy iterator.

```python
evens = list(filter(lambda x: x % 2 == 0, range(10)))
# [0, 2, 4, 6, 8]
```

### `reduce(func, iterable)` — from `functools`

Applies `func` cumulatively, reducing the sequence to a single value.

```python
from functools import reduce

product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])   # 120
# Step-by-step: ((((1*2)*3)*4)*5) = 120
```

---

## Lambda Expressions

Anonymous, single-expression functions:

```python
lambda arg1, arg2: expression
```

```python
square = lambda x: x ** 2
square(5)   # 25

add = lambda a, b: a + b
add(3, 4)   # 7
```

- No `return` keyword — the expression value is returned implicitly.
- Cannot contain statements (no `if`/`for` as statements, only as expressions).
- Primarily used inline with HOFs:

```python
sorted(data, key=lambda item: item["age"])
list(map(lambda x: x.upper(), words))
list(filter(lambda x: x > 0, nums))
```

---

## Recursion

A function that calls **itself** to solve a smaller sub-problem.

### Structure

1. **Base case** — condition that stops recursion (returns a direct value).
2. **Decomposition** — break the problem into a smaller instance of itself.
3. **Composition** — combine the smaller result with the current step.

### Factorial

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case

factorial(5)   # 5 * 4 * 3 * 2 * 1 = 120
```

Call stack for `factorial(3)`:
```
factorial(3) → 3 * factorial(2)
                   → 2 * factorial(1)
                           → 1 * factorial(0)
                                   → 1
```

### Fibonacci

```python
def fib(n):
    if n <= 1:          # base cases: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)

fib(6)   # 8  (sequence: 0,1,1,2,3,5,8)
```

> Naïve Fibonacci is exponential O(2ⁿ) due to repeated sub-problems. Use memoisation (`functools.lru_cache`) for efficiency.

### Recursion vs Iteration

| Aspect | Recursion | Iteration |
|---|---|---|
| Clarity | Often mirrors mathematical definition | Usually more explicit |
| Stack usage | O(depth) stack frames — can hit Python's limit (~1000) | O(1) stack |
| Performance | Function call overhead | Generally faster |
| Use case | Trees, divide-and-conquer, naturally recursive structures | Simple loops and accumulation |

Python's default recursion limit is 1 000; change with `sys.setrecursionlimit(n)`.

---

## Related Pages

- [[concepts/python-fundamentals|Python Fundamentals]] — variables, types, control flow
- [[concepts/python-data-structures-and-io|Python Data Structures & File I/O]] — collections and file I/O
- [[concepts/c-programming-fundamentals|C Programming Fundamentals]] — functions in C (call-by-value, prototypes)
- [[sources/INF1002-programming-fundamentals|INF1002 Source Index]]
