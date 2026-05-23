---
type: concept
title: "Python Fundamentals"
domain: programming-fundamentals
complexity: medium
source: "[[sources/INF1002-programming-fundamentals]]"
address: c-000042
created: 2026-05-23
updated: 2026-05-23
tags: [concept, programming-fundamentals, python, variables, control-flow, INF1002]
---

# Python Fundamentals

Core building blocks of Python programming: how values are stored, what operations can be performed on them, and how execution flow is directed.

---

## Interpreted vs Compiled Languages

| Dimension | Python (Interpreted) | C (Compiled) |
|---|---|---|
| Execution | Line-by-line via interpreter | Translated to machine code first |
| Error detection | At runtime | At compile time |
| Portability | Runs anywhere Python is installed | Platform-specific binary |
| Speed | Slower (interpretation overhead) | Faster (native machine code) |
| Typing | Dynamic — type bound to value | Static — type bound to variable |

---

## Variables and Assignment

A variable is a name bound to a value in memory.

```python
name = value          # assignment
x = 42
greeting = "hello"
pi = 3.14159
```

- **Naming convention**: `snake_case` per PEP 8.
- `id(x)` — returns the memory address of the object `x` is bound to.
- `type(x)` — returns the type of the object.
- Dynamic typing: a variable can be rebound to a value of a different type.

### Built-in Scalar Types

| Type | Example | Notes |
|---|---|---|
| `int` | `42`, `-7` | Arbitrary precision |
| `float` | `3.14`, `-0.5` | IEEE 754 double |
| `bool` | `True`, `False` | Subclass of `int` (True == 1, False == 0) |
| `str` | `"hello"` | Immutable Unicode sequence |
| `NoneType` | `None` | Singleton — represents absence of value |

### Collection Types (overview)

| Type | Example | Mutable? |
|---|---|---|
| `list` | `[1, 2, 3]` | Yes |
| `tuple` | `(1, 2, 3)` | No |
| `set` | `{1, 2, 3}` | Yes |
| `dict` | `{"a": 1}` | Yes |

---

## Type Casting

Explicit conversion between types:

```python
int("42")        # → 42    (truncates floats: int(3.9) → 3)
float("3.14")    # → 3.14
str(99)          # → "99"
bool(0)          # → False (falsy: 0, 0.0, "", None, [], {})
```

> `int()` truncates towards zero — it does **not** round.

---

## Arithmetic Operators

| Operator | Operation | Example | Result |
|---|---|---|---|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `3 - 2` | `1` |
| `*` | Multiplication | `3 * 2` | `6` |
| `/` | True division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Modulo | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

**Augmented assignment**: `x += 1`, `x -= 1`, `x *= 2`, etc.

**Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=` — return `bool`.

**Logical operators**: `and`, `or`, `not`.

---

## Console I/O

### Input

```python
name = input("Enter your name: ")   # always returns str
age  = int(input("Enter age: "))    # cast manually if numeric needed
```

### Output

```python
print("Hello, world!")
print(x, y, sep=", ", end="\n")    # sep default ", end default "\n"
```

### f-Strings (Python 3.6+)

Embed expressions directly inside string literals:

```python
name = "Alice"
score = 95.5
print(f"Hello, {name}!")
print(f"Score: {score:.2f}")          # 2 decimal places → 95.50
print(f"{'right':>10}")               # right-align in field of width 10
print(f"{value:08.3f}")               # zero-pad, width 8, 3 decimal places
```

**Format spec** inside `{}`: `{value:[fill][align][sign][width][.precision][type]}`

| Spec part | Example | Meaning |
|---|---|---|
| `>10` | `f"{'hi':>10}"` | Right-align in width 10 |
| `<10` | `f"{'hi':<10}"` | Left-align in width 10 |
| `.2f` | `f"{3.14:.2f}"` | Float with 2 decimal places |
| `08.3f` | `f"{pi:08.3f}"` | Width 8, zero-padded, 3 d.p. |
| `d` | `f"{42:d}"` | Integer |

---

## Control Flow

### Conditional — `if / elif / else`

```python
x = 10
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
```

Conditions evaluate truthiness. Blocks are delimited by **indentation** (4 spaces per PEP 8).

### Structural Pattern Matching — `match / case` (Python 3.10+)

```python
command = "quit"
match command:
    case "quit":
        print("Quitting")
    case "help":
        print("Help menu")
    case _:             # wildcard — matches anything
        print("Unknown command")
```

### `while` Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop pattern:
while True:
    user_in = input("> ")
    if user_in == "exit":
        break
```

### `for` Loop

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for char in "hello":        # iterate over any sequence
    print(char)

for i in range(2, 10, 2):  # start=2, stop=10, step=2 → 2,4,6,8
    print(i)
```

`range(stop)`, `range(start, stop)`, `range(start, stop, step)` — returns a lazy range object.

### Loop Control

| Statement | Effect |
|---|---|
| `break` | Exit the innermost loop immediately |
| `continue` | Skip to the next iteration |
| `pass` | No-op placeholder (syntactically required empty block) |

---

## PEP 8 Conventions (Key Rules)

| Rule | Example |
|---|---|
| Variable/function names | `snake_case` |
| Constants | `UPPER_SNAKE_CASE` |
| Classes | `PascalCase` |
| Indentation | 4 spaces (no tabs) |
| Max line length | 79 characters |
| Two blank lines before top-level functions/classes | — |

---

## Related Pages

- [[concepts/python-data-structures-and-io|Python Data Structures & File I/O]] — strings, lists, tuples, dicts, comprehensions, file I/O
- [[concepts/python-functions-and-modules|Python Functions, Modules & Functional Programming]] — functions, scope, HOFs, lambda, recursion
- [[concepts/c-programming-fundamentals|C Programming Fundamentals]] — compiled counterpart
- [[sources/INF1002-programming-fundamentals|INF1002 Source Index]]
