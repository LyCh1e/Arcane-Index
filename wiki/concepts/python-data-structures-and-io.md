---
type: concept
status: established
title: "Python Data Structures & File I/O"
domain: programming-fundamentals
complexity: medium
source: "[[sources/INF1002-programming-fundamentals]]"
address: c-000043
created: 2026-05-23
updated: 2026-05-23
tags: [concept, programming-fundamentals, python, data-structures, file-io, INF1002]
---

# Python Data Structures & File I/O

Python's built-in collection types — strings, lists, tuples, and dictionaries — plus list comprehensions and file I/O.

---

## Strings

Strings are **immutable** sequences of Unicode characters.

```python
s = "hello"
s[0]          # 'h'
s[-1]         # 'o'  (negative indexing from end)
len(s)        # 5
"ell" in s    # True
```

### Slicing

```python
s[start:end:step]   # end is exclusive
s[1:4]              # 'ell'
s[::2]              # 'hlo'  (every other character)
s[::-1]             # 'olleh'  (reverse)
```

### Common String Methods

| Method | Description | Example |
|---|---|---|
| `s.lower()` | Lowercase copy | `"Hi".lower()` → `"hi"` |
| `s.upper()` | Uppercase copy | `"hi".upper()` → `"HI"` |
| `s.strip()` | Remove leading/trailing whitespace | `" hi ".strip()` → `"hi"` |
| `s.split(sep)` | Split into list | `"a,b".split(",")` → `["a","b"]` |
| `s.join(lst)` | Join list into string | `",".join(["a","b"])` → `"a,b"` |
| `s.find(sub)` | Index of first match, or -1 | `"hello".find("ll")` → `2` |
| `s.replace(old, new)` | Replace occurrences | `"abc".replace("b","x")` → `"axc"` |
| `s.startswith(p)` | Boolean prefix check | `"hi".startswith("h")` → `True` |
| `s.endswith(p)` | Boolean suffix check | `"hi".endswith("i")` → `True` |
| `s.count(sub)` | Count non-overlapping occurrences | `"banana".count("a")` → `3` |

Immutability means methods return **new** strings — the original is unchanged.

---

## Lists

Lists are **mutable**, ordered sequences. Elements can be of mixed type.

```python
lst = [1, "two", 3.0, True]
lst[0]          # 1
lst[-1]         # True
len(lst)        # 4
```

### Mutation Methods

| Method | Description |
|---|---|
| `lst.append(x)` | Add `x` to end |
| `lst.insert(i, x)` | Insert `x` at index `i` |
| `lst.remove(x)` | Remove first occurrence of `x` |
| `del lst[i]` | Delete element at index `i` |
| `lst.pop(i)` | Remove and return element at index `i` (default: last) |
| `lst.sort()` | In-place sort |
| `lst.reverse()` | In-place reverse |
| `lst.extend(other)` | Append all elements of `other` |

### Shallow vs Deep Copy

```python
import copy

a = [[1, 2], [3, 4]]

# Assignment — same object, no copy
b = a           # b is a; b[0].append(9) modifies a too

# Shallow copy — new list, but nested objects are shared
c = a.copy()    # or list(a) or a[:]
# c is a new list, but c[0] is the same object as a[0]

# Deep copy — fully independent
d = copy.deepcopy(a)
# d[0] is a new object; modifying d[0] does NOT affect a[0]
```

> **Rule**: use `deepcopy` whenever the list contains mutable elements (e.g., nested lists) and you need genuine independence.

---

## Tuples

Tuples are **immutable**, ordered sequences. Typically used for fixed collections (e.g., coordinates, RGB values).

```python
t = (10, 20, 30)
t[0]            # 10
len(t)          # 3
x, y, z = t    # unpacking
```

- Parentheses are optional: `t = 1, 2, 3` creates a tuple.
- Single-element tuple requires trailing comma: `t = (42,)`.
- Tuples can be used as dictionary keys (lists cannot, because lists are unhashable).

---

## Dictionaries

Dictionaries store **key-value pairs**. Keys must be immutable (str, int, tuple). Values can be anything.

```python
d = {"name": "Alice", "age": 25}
d["name"]          # "Alice"
d["city"] = "SG"   # add new key
del d["age"]       # remove key

"name" in d        # True (checks keys)
len(d)             # number of key-value pairs
```

### Iteration

```python
for key in d:
    print(key, d[key])

for key in d.keys():    pass
for val in d.values():  pass
for k, v in d.items():  pass
```

### Useful Methods

| Method | Description |
|---|---|
| `d.get(key, default)` | Return value or default if key absent |
| `d.pop(key)` | Remove and return value |
| `d.update(other)` | Merge `other` into `d` |
| `d.setdefault(key, val)` | Insert key with val if key absent, then return its value |

---

## List Comprehensions

A concise way to build lists from iterables.

```python
# Basic form
squares = [x**2 for x in range(10)]

# With filter
evens = [x for x in range(20) if x % 2 == 0]

# Nested
pairs = [(x, y) for x in [1,2] for y in [3,4]]

# With transformation
words = ["hello", "world"]
upper = [w.upper() for w in words]
```

**General form**: `[expression for member in iterable (if condition)]`

Equivalent to a `for` loop with `append`, but more readable and slightly faster.

---

## File I/O

### Opening and Closing

```python
f = open("data.txt", "r", encoding="utf-8")
# ... do work ...
f.close()   # must close to flush and release OS handle
```

### File Modes

| Mode | Description |
|---|---|
| `"r"` | Read (default); file must exist |
| `"w"` | Write; creates or truncates |
| `"a"` | Append; creates or appends |
| `"r+"` | Read and write; file must exist |
| `"w+"` | Read and write; truncates |
| `"b"` | Binary mode (append to above: `"rb"`, `"wb"`) |

### Reading

```python
content = f.read()           # entire file as one string
line    = f.readline()       # one line including '\n'
lines   = f.readlines()      # list of all lines

# Idiomatic — iterate line by line (memory-efficient)
for line in f:
    print(line.strip())
```

### Writing

```python
f.write("Hello\n")           # write string; returns characters written
f.writelines(["a\n","b\n"])  # write sequence of strings (no auto newlines)
```

### The `with` Statement (Context Manager)

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# f is automatically closed here, even if an exception occurs
```

Benefits of `with`:
1. **Automatic close** — no need to call `f.close()`.
2. **Exception safety** — file is closed even if the body raises an error.
3. **Scope clarity** — `f` is only valid inside the `with` block.

### Practical Patterns

```python
# Read all lines, strip whitespace
with open("names.txt") as f:
    names = [line.strip() for line in f]

# Write list to file
with open("out.txt", "w") as f:
    for name in names:
        f.write(name + "\n")
```

---

## Related Pages

- [[concepts/python-fundamentals|Python Fundamentals]] — variables, types, control flow
- [[concepts/python-functions-and-modules|Python Functions, Modules & Functional Programming]] — functions, scope, HOFs
- [[concepts/c-pointers-memory-and-data-structures|C Pointers, Memory & Data Structures]] — C file I/O counterpart
- [[sources/INF1002-programming-fundamentals|INF1002 Source Index]]
