---
type: concept
title: "C Pointers, Memory & Data Structures"
domain: programming-fundamentals
complexity: high
source: "[[sources/INF1002-programming-fundamentals]]"
address: c-000046
created: 2026-05-23
updated: 2026-05-23
tags: [concept, programming-fundamentals, c, pointers, memory-allocation, linked-lists, structs, file-io, INF1002]
---

# C Pointers, Memory & Data Structures

Pointer variables, pointer arithmetic, dynamic memory allocation, structs, typedef, linked lists, and file I/O in C.

---

## Pointer Basics

A **pointer** is a variable whose value is a memory address.

```c
int x = 42;
int *ptr;         // declare a pointer to int (the * is part of the type)
ptr = &x;         // & = address-of operator; ptr now holds x's address

printf("%p\n", ptr);    // print the address (hex)
printf("%d\n", *ptr);   // * = dereference operator; prints 42
*ptr = 99;              // modify x through the pointer; x is now 99
```

| Operator | Name | Effect |
|---|---|---|
| `&var` | Address-of | Returns the address of `var` |
| `*ptr` | Dereference | Accesses the value at the address stored in `ptr` |

### Null Pointer

```c
int *ptr = NULL;    // pointer that points to nothing
if (ptr == NULL) { /* safe to check before dereferencing */ }
```

Never dereference a `NULL` pointer — it causes a segmentation fault.

---

## Pointer Arithmetic

Arithmetic on pointers moves by multiples of `sizeof` the pointed-to type.

```c
int arr[] = {10, 20, 30, 40};
int *p = arr;           // p points to arr[0]

p++;                    // p now points to arr[1] (moves 4 bytes for int)
*(p + 2)                // arr[3] = 40

// Array indexing and pointer arithmetic are equivalent:
arr[i]  ≡  *(arr + i)  ≡  *(p + i)  (when p == arr)
```

- Subtracting two pointers of the same type gives the number of elements between them.
- Comparisons (`<`, `>`, `==`) between pointers to the same array are valid.

### Arrays and Pointers

```c
int b[] = {1, 2, 3, 4};
int *bPtr = b;          // array name decays to pointer to first element

bPtr[3]      // 4  — pointer subscript
*(bPtr + 3)  // 4  — equivalent
*(b + 3)     // 4  — array name used as pointer
```

> `b` (array name) is a **constant** pointer — you cannot do `b++`. `bPtr` is a variable pointer.

---

## Pointers to Pointers

```c
int x = 10;
int *ptr = &x;
int **ptrToPtr = &ptr;   // pointer to a pointer

**ptrToPtr   // 10  — double dereference reaches x
```

Used in dynamic 2D array allocation and for out-parameters that return pointer values.

---

## Call-by-Reference via Pointers

Because C passes by value, modifying a caller's variable requires passing its address:

```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int x = 5, y = 10;
swap(&x, &y);    // x=10, y=5 after the call
```

Pattern: caller passes `&var`; function receives `int *ptr`; modifies via `*ptr = value`.

---

## Dynamic Memory Allocation

Stack-allocated arrays require a size known at compile time. `malloc`/`calloc` allocate on the **heap** at runtime.

### `malloc` — Memory Allocate

```c
#include <stdlib.h>

int n = 5;
int *arr = (int *) malloc(n * sizeof(int));

if (arr == NULL) {
    fprintf(stderr, "malloc failed\n");
    exit(1);
}

arr[0] = 42;    // use like a normal array
free(arr);      // release memory when done
arr = NULL;     // good practice to avoid dangling pointer
```

- Returns `void *`; cast to the required pointer type.
- Returns `NULL` on allocation failure — always check.
- Memory is **uninitialised** (may contain garbage).

### `calloc` — Contiguous Allocate (zero-initialised)

```c
int *arr = (int *) calloc(n, sizeof(int));
// All elements set to 0
```

### `realloc` — Resize an Allocation

```c
arr = (int *) realloc(arr, new_size * sizeof(int));
```

### `free` — Release Memory

```c
free(ptr);
```

- Every `malloc`/`calloc` must be matched by exactly one `free`.
- **Memory leak**: allocated memory never freed — the programme's memory usage grows unboundedly.
- **Double-free** and **use-after-free** are undefined behaviour.

---

## Structs

A `struct` groups related variables of different types under one name.

```c
struct Student {
    char name[50];
    int  age;
    float gpa;
};

struct Student s1;               // declare a Student variable
s1.age = 21;                     // dot operator for member access
strcpy(s1.name, "Alice");
s1.gpa = 3.8f;
```

### Pointer to Struct — Arrow Operator

```c
struct Student *ps = &s1;
ps->age = 22;         // equivalent to (*ps).age = 22
```

### Struct Initialisation

```c
struct Student s2 = {"Bob", 20, 3.5f};    // positional
```

---

## `typedef`

Creates a type alias to avoid repeating `struct`:

```c
typedef struct {
    char name[50];
    int  age;
} Student;

Student s1;             // no longer need 'struct Student'
Student s2 = {"Carol", 19};
```

---

## Linked Lists

A **linked list** is a dynamic data structure made of nodes where each node holds data and a pointer to the next node.

### Node Definition

```c
typedef struct node_struct {
    int data;
    struct node_struct *next;   // self-referential — must use struct tag, not typedef alias
} Node;
```

### Head Pointer

```c
Node *head = NULL;    // empty list
```

### Search

```c
Node *search(Node *head, int target) {
    Node *temp = head;
    while (temp != NULL) {
        if (temp->data == target) return temp;
        temp = temp->next;
    }
    return NULL;    // not found
}
```

### Insert at Head

```c
void insert_head(Node **head, int val) {
    Node *new = (Node *) malloc(sizeof(Node));
    new->data = val;
    new->next = *head;
    *head = new;
}
```

> Note: `head` is passed as `Node **` so the function can update the caller's `head` pointer.

### Delete a Node

```c
void delete_node(Node **head, int val) {
    Node *prev = NULL, *curr = *head;
    while (curr != NULL && curr->data != val) {
        prev = curr;
        curr = curr->next;
    }
    if (curr == NULL) return;     // not found
    if (prev == NULL)
        *head = curr->next;       // deleting head node
    else
        prev->next = curr->next;  // bypass the node
    free(curr);
}
```

### Traversal / Print

```c
void print_list(Node *head) {
    for (Node *temp = head; temp != NULL; temp = temp->next)
        printf("%d → ", temp->data);
    printf("NULL\n");
}
```

### Free Entire List

```c
void free_list(Node *head) {
    Node *temp;
    while (head != NULL) {
        temp = head->next;
        free(head);
        head = temp;
    }
}
```

---

## File I/O in C

C file I/O uses a `FILE *` pointer obtained from `fopen`.

### Open and Close

```c
FILE *f = fopen("data.txt", "w");
if (f == NULL) {
    perror("fopen");    // print system error message
    exit(1);
}
// ... do work ...
fclose(f);
```

### File Modes

| Mode | Description |
|---|---|
| `"r"` | Read; file must exist |
| `"w"` | Write; create or truncate |
| `"a"` | Append; create or append |
| `"r+"` | Read and write |
| `"rb"` / `"wb"` | Binary read/write |

### Text I/O

```c
fprintf(f, "Name: %s, Score: %d\n", name, score);   // like printf to file
fscanf(f, "%s %d", name, &score);                    // like scanf from file
fgets(line, sizeof(line), f);                         // read a line
fputs(line, f);                                       // write a string
```

### Binary I/O

```c
// Write n elements of size bytes each from buffer
fwrite(buffer, sizeof(element), n, f);

// Read into buffer
size_t read_count = fread(buffer, sizeof(element), n, f);
```

### Random Access

```c
fseek(f, offset, whence);
// whence: SEEK_SET (from start), SEEK_CUR (from current), SEEK_END (from end)

fseek(f, 0, SEEK_SET);    // rewind to start
fseek(f, -sizeof(int), SEEK_END);   // position just before last int

long pos = ftell(f);      // get current position
rewind(f);                // equivalent to fseek(f, 0, SEEK_SET)
```

---

## Memory Layout Summary

```
High address
┌──────────────┐
│   Stack      │  Local variables, function call frames (grows downward)
├──────────────┤
│     ↓        │
│              │
│     ↑        │
├──────────────┤
│   Heap       │  malloc/calloc allocations (grows upward)
├──────────────┤
│   BSS        │  Uninitialised global/static variables
├──────────────┤
│   Data       │  Initialised global/static variables
├──────────────┤
│   Text       │  Programme code (read-only)
Low address
```

---

## Related Pages

- [[concepts/c-programming-fundamentals|C Programming Fundamentals]] — data types, control flow, arrays, strings
- [[concepts/data-structures-fundamentals|Data Structures Fundamentals]] — linked lists from an algorithmic perspective
- [[concepts/memory-and-virtual-memory|Memory Management and Virtual Memory]] — OS view of heap/stack
- [[concepts/python-data-structures-and-io|Python Data Structures & File I/O]] — Python counterpart
- [[sources/INF1002-programming-fundamentals|INF1002 Source Index]]
