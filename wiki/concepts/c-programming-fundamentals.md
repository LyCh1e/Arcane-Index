---
type: concept
title: "C Programming Fundamentals"
domain: programming-fundamentals
complexity: high
source: "[[sources/INF1002-programming-fundamentals]]"
address: c-000045
created: 2026-05-23
updated: 2026-05-23
tags: [concept, programming-fundamentals, c, compilation, arrays, strings, INF1002]
---

# C Programming Fundamentals

Introduction to C: its history, the compilation pipeline, data types, I/O, control flow, functions, arrays, and strings.

---

## Brief History

- **BCPL → B → C**: Dennis Ritchie developed C at Bell Labs (1972–73) as a systems programming language.
- C was used to rewrite Unix (previously in assembly), making it portable.
- Standardised as **C89/ANSI C** (1989), then **C99** (1999), adding `//` comments, `<stdbool.h>`, variable-length arrays, and more.
- C underpins operating systems, embedded systems, compilers, and is the basis of C++, Java, and many other languages.

---

## C vs Python at a Glance

| Dimension | C | Python |
|---|---|---|
| Execution model | Compiled to machine code | Interpreted |
| Typing | Static — declared at compile time | Dynamic — inferred at runtime |
| Variable declaration | Required (`int x;`) | Not required (`x = 1`) |
| Block delimiters | `{ }` braces | Indentation |
| Statement terminator | `;` semicolon | Newline |
| Entry point | `main()` function | Top-level script |
| Memory management | Manual (`malloc`/`free`) | Automatic (garbage collection) |
| Null sentinel | `'\0'` in char arrays | `None` |

---

## Compilation Pipeline

```
Source (.c)  →  Preprocessor  →  Compiler  →  Assembler  →  Linker  →  Executable
```

| Stage | Action |
|---|---|
| **Preprocessor** | Expands `#include`, `#define`, conditional compilation directives |
| **Compiler** | Translates C to assembly; performs type checking and optimisation |
| **Assembler** | Converts assembly to object code (`.o`) |
| **Linker** | Combines object files and library code into a single executable |
| **Loader** | Loads the executable into memory for the OS to run |

### Preprocessor Directives

```c
#include <stdio.h>        // system header (searched in system paths)
#include "myheader.h"     // user header (searched in current directory first)

#define PI 3.14159        // symbolic constant — text substitution before compile
#define MAX(a,b) ((a)>(b)?(a):(b))   // macro (use with caution)
```

---

## Basic Programme Structure

```c
#include <stdio.h>

int main(void) {
    printf("Hello, world!\n");
    return 0;   // 0 signals success to the OS
}
```

- Every C programme must have a `main()` function.
- `return 0` from `main` indicates success; non-zero indicates an error.

---

## Data Types and Size

| Type | Format Specifier | Typical Size | Range |
|---|---|---|---|
| `int` | `%d` | 4 bytes | −2 147 483 648 to 2 147 483 647 |
| `long` | `%ld` | 4–8 bytes | Platform-dependent |
| `float` | `%f` | 4 bytes | ~6–7 significant digits |
| `double` | `%lf` / `%.10f` | 8 bytes | ~15–16 significant digits |
| `char` | `%c` | 1 byte | 0–255 (ASCII) |
| `char[]` / string | `%s` | — | NUL-terminated |

> Sizes are platform-dependent. Use `sizeof(type)` to inspect at runtime.

### Variable Declaration and Initialisation

```c
int age;             // declared but uninitialised (undefined value)
int age = 25;        // declared and initialised
float pi = 3.14f;
char initial = 'A';
```

---

## printf and scanf

### `printf` — Formatted Output

```c
printf(format_string, arg1, arg2, ...);

printf("Name: %s, Age: %d\n", name, age);
printf("%10.2f\n", price);      // right-align in field width 10, 2 d.p.
printf("%-10s|\n", "left");     // left-align (- flag)
printf("%+d\n", 42);            // show sign (+42)
printf("%05d\n", 7);            // zero-pad to width 5 → 00007
```

**Format specifier anatomy**: `%[flags][width][.precision]type`

### `scanf` — Formatted Input

```c
int n;
scanf("%d", &n);         // & is the address-of operator — scanf needs the address

float f;
scanf("%f", &f);

char word[50];
scanf("%49s", word);     // strings: no & (array name is already a pointer)
                         // field width 49 prevents buffer overflow
```

> `scanf` skips leading whitespace for numeric types but not for `%c`.

---

## Control Flow

### `if / else if / else`

```c
if (x > 0) {
    printf("positive\n");
} else if (x == 0) {
    printf("zero\n");
} else {
    printf("negative\n");
}
```

### `switch / case`

```c
switch (grade) {
    case 'A':
        printf("Excellent\n");
        break;          // without break, execution falls through to next case
    case 'B':
        printf("Good\n");
        break;
    default:
        printf("Other\n");
}
```

- Operates on integer types and `char` (not strings or floats).
- `break` is required to prevent fall-through.
- `default` is the catch-all (equivalent to `else`).

### `for` Loop

```c
for (int i = 0; i < 10; i++) {
    printf("%d\n", i);
}
// init; condition; increment — any part can be omitted
```

### `while` Loop

```c
int i = 0;
while (i < 10) {
    printf("%d\n", i);
    i++;
}
```

### `do-while` Loop

Executes the body **at least once** before checking the condition — Python has no equivalent.

```c
int choice;
do {
    printf("Enter 1–3: ");
    scanf("%d", &choice);
} while (choice < 1 || choice > 3);
```

---

## Functions

### Declaration, Definition, and Call

```c
// Prototype (declaration) — placed before main or in header file
int add(int a, int b);

// Definition
int add(int a, int b) {
    return a + b;
}

// Call
int result = add(3, 4);
```

Prototypes allow the compiler to validate function calls before the definition appears.

### Call-by-Value

C passes arguments **by value** — a copy is made. The original variable is unaffected.

```c
void double_it(int x) {
    x *= 2;        // modifies the local copy only
}

int n = 5;
double_it(n);
// n is still 5
```

To modify the original, pass a pointer (see [[concepts/c-pointers-memory-and-data-structures|C Pointers, Memory & Data Structures]]).

### Return Types

```c
void print_hello(void) {   // void: no return value
    printf("Hello\n");
}

int square(int n) {
    return n * n;
}
```

### Scope

| Scope | Where Declared | Lifetime |
|---|---|---|
| **File (global)** | Outside all functions | Entire programme |
| **Block (local)** | Inside `{ }` | Until closing `}` |
| **Function parameter** | Function signature | During function execution |

---

## Arrays

Fixed-size, contiguous sequence of elements of the same type.

```c
int scores[5];                    // uninitialized 5-element array
int scores[5] = {90, 85, 78, 92, 88};   // initialised
int scores[] = {90, 85, 78};     // size inferred from initialiser
```

- **0-indexed**: `scores[0]` is the first element, `scores[4]` is the last of a 5-element array.
- **No bounds checking**: accessing `scores[10]` is undefined behaviour.
- Array name without `[]` is a pointer to the first element.

### 2D Arrays

```c
int matrix[2][3] = {{1,2,3},{4,5,6}};
matrix[1][2]   // 6  (row 1, column 2)
```

### Passing Arrays to Functions

```c
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

print_array(scores, 5);
```

Arrays decay to pointers when passed — the size information is lost and must be passed separately.

---

## Strings in C

A C string is a **`char` array terminated by the null character `'\0'`**.

```c
char name[] = "blue";        // {'b','l','u','e','\0'} — 5 bytes
char name[10] = "blue";      // 10-byte buffer, partially filled
```

### String I/O

```c
printf("%s\n", name);           // print string
scanf("%9s", word);             // read up to 9 chars (leaves room for '\0')
fgets(line, sizeof(line), stdin);  // safer: reads line including '\n'
puts(name);                     // print string + newline
```

> Use `fgets` rather than `gets` (which has no bounds check and is deprecated).

### `<string.h>` Functions

| Function | Description |
|---|---|
| `strlen(s)` | Length of `s` (not counting `'\0'`) |
| `strcpy(dest, src)` | Copy `src` into `dest` |
| `strncpy(dest, src, n)` | Copy at most `n` chars (safer) |
| `strcmp(s1, s2)` | Compare: 0 if equal, <0 if s1 < s2, >0 if s1 > s2 |
| `strcat(dest, src)` | Append `src` to `dest` |
| `strchr(s, c)` | Pointer to first occurrence of char `c` in `s` |
| `sprintf(buf, fmt, ...)` | Print formatted string into a buffer |

### `<stdlib.h>` — String Conversion

```c
int n = atoi("42");      // string → int
long l = atol("123456"); // string → long
double d = atof("3.14"); // string → double
```

---

## Related Pages

- [[concepts/python-fundamentals|Python Fundamentals]] — interpreted counterpart
- [[concepts/c-pointers-memory-and-data-structures|C Pointers, Memory & Data Structures]] — pointers, dynamic memory, structs, linked lists, file I/O
- [[concepts/os-processes-and-threads|OS Fundamentals, Processes, and Threads]] — C is the language of OS internals
- [[sources/INF1002-programming-fundamentals|INF1002 Source Index]]
