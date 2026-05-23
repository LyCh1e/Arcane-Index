---
type: area
title: "Programming Fundamentals"
domain: programming-fundamentals
address: c-000047
created: 2026-05-23
updated: 2026-05-23
tags: [area, programming-fundamentals, python, c, INF1002]
---

# Programming Fundamentals

Introductory programming covering two paradigms: Python (scripting and functional) and C (procedural and systems-level). This domain corresponds to SIT's INF1002 module.

---

## Domain Overview

Programming fundamentals bridges the gap between no programming knowledge and competency in two languages with contrasting design philosophies:

- **Python** — high-level, dynamically typed, garbage-collected, interpreted. Prioritises readability and rapid development.
- **C** — low-level, statically typed, manually memory-managed, compiled. Prioritises performance and close-to-hardware control.

Together they teach: what a variable actually is in memory, how functions work at the call stack level, how data structures are laid out, and how files are accessed — concepts that transfer to every subsequent language.

---

## Concept Pages

| Page | Language | Topics |
|---|---|---|
| [[concepts/python-fundamentals\|Python Fundamentals]] | Python | Variables, types, operators, control flow, I/O, f-strings |
| [[concepts/python-data-structures-and-io\|Python Data Structures & File I/O]] | Python | Strings, lists, tuples, dicts, comprehensions, file I/O |
| [[concepts/python-functions-and-modules\|Python Functions, Modules & Functional Programming]] | Python | Functions, scope, modules, HOFs, lambda, recursion |
| [[concepts/c-programming-fundamentals\|C Programming Fundamentals]] | C | Compilation, data types, printf/scanf, control flow, arrays, strings |
| [[concepts/c-pointers-memory-and-data-structures\|C Pointers, Memory & Data Structures]] | C | Pointers, dynamic memory, structs, linked lists, file I/O |

---

## Source

| Source | Type |
|---|---|
| [[sources/INF1002-programming-fundamentals\|INF1002 Programming Fundamentals]] | Course notes (SIT) |

---

## Key Contrasts Between Python and C

| Concept | Python | C |
|---|---|---|
| Variable declaration | Implicit (`x = 1`) | Explicit (`int x = 1;`) |
| Type system | Dynamic | Static |
| Memory | Automatic (GC) | Manual (`malloc`/`free`) |
| String | Immutable `str` object | Mutable `char[]` with `'\0'` sentinel |
| Array bounds | List grows dynamically | Fixed; no bounds check |
| Functions | First-class objects | Not first-class (no lambdas pre-C11) |
| Pointers | Hidden (references) | Explicit (`int *ptr`) |
| File I/O | `open()` / context manager | `FILE *` / `fopen`/`fclose` |

---

## Cross-Domain Connections

| Domain | Connection |
|---|---|
| [[areas/computer-science\|Computer Science]] | Linked lists, recursion, and algorithmic thinking taught here extend to [[concepts/data-structures-fundamentals\|Data Structures]] and [[concepts/algorithm-complexity\|Algorithm Complexity]] |
| [[areas/operating-systems\|Operating Systems]] | C is the language of OS internals; pointers and memory layout connect to [[concepts/memory-and-virtual-memory\|Virtual Memory]] and [[concepts/os-processes-and-threads\|Processes & Threads]] |
| [[areas/computer-architecture\|Computer Architecture]] | The compilation pipeline (C → assembly → machine code) connects to [[concepts/assembly-programming-msp430\|Assembly Programming]] |
| [[areas/software-engineering\|Software Engineering]] | Python functions, modules, and HOFs are prerequisites for [[concepts/python-functions-and-modules\|functional patterns]] used in data science and scripting |
