---
type: concept
title: "Data Structures Fundamentals"
domain: computer-science
course: INF1008
complexity: high
tags: [adt, arrays, stacks, queues, linked-lists, hash-tables, trees, bst, avl, red-black, b-tree]
updated: 2026-05-11
---

# Data Structures Fundamentals

A data structure is a way of organising data in memory to support efficient operations. The choice of data structure is the first and most consequential algorithmic decision: the right structure turns an O(n²) solution into O(n log n) or even O(1).

## Abstract Data Types (ADTs)

An **ADT** defines a data structure by its **operations and their contracts**, not its implementation. The same ADT (e.g., Stack) can be implemented as an array or a linked list — the ADT hides this choice from the user.

Three things define an ADT:
1. The **data** it stores
2. The **operations** it supports
3. The **preconditions and postconditions** of each operation

## Linear Data Structures

### Arrays

- Fixed-size (static) or resizable (dynamic/ArrayList)
- **O(1) random access** by index
- **O(n) insert/delete** at arbitrary position (shifting required)
- **O(1) append** at end (amortised for dynamic arrays)
- Best when: size is known, random access is frequent, cache locality matters

### Stacks (LIFO)

Last-In, First-Out. Operations:
- `push(x)` — add to top: O(1)
- `pop()` — remove from top: O(1)
- `peek()` — view top without removing: O(1)

Applications: function call stack, undo/redo, expression evaluation (infix → postfix), DFS traversal, bracket matching.

### Queues (FIFO)

First-In, First-Out. Operations:
- `enqueue(x)` — add to rear: O(1)
- `dequeue()` — remove from front: O(1)

Variants:
- **Circular Queue** — fixed-size array with wrap-around; avoids shifting
- **Double-Ended Queue (Deque)** — insert/delete at both ends
- **Priority Queue** — dequeue by priority, not arrival order (see Heaps below)

Applications: BFS traversal, task scheduling, print spooling.

### Linked Lists

Each node contains data + a pointer to the next node. No contiguous memory required.

| Type | Structure | Extra cost |
|------|-----------|-----------|
| **Singly Linked** | node → next | O(n) traversal only |
| **Doubly Linked** | prev ← node → next | O(1) backward traversal |
| **Circular** | tail → head | Loop detection algorithms |

Operations:
- **Insert at head**: O(1)
- **Insert at tail**: O(1) with tail pointer, O(n) without
- **Search**: O(n)
- **Delete by value**: O(n) search + O(1) removal

Best when: frequent insertion/deletion at arbitrary positions, size unknown, no random access needed.

## Priority Queue & Heaps

A **Priority Queue** is an ADT that always returns the element with the highest (or lowest) priority.

A **Binary Heap** is the standard implementation:
- Complete binary tree stored as an array
- **Min-Heap**: parent ≤ children (root is minimum)
- **Max-Heap**: parent ≥ children (root is maximum)

Operations:
- `insert`: O(log n) — add at end, bubble up
- `extract-min/max`: O(log n) — remove root, replace with last, bubble down
- `build-heap` from array: O(n) (not O(n log n) — amortised analysis)

Applications: Dijkstra's algorithm, Prim's MST, Heap Sort, job scheduling.

## Hash Tables

A hash table maps keys to values in O(1) average time using a **hash function**.

### Hash Function Properties

A good hash function is:
- **Deterministic**: same input → same output
- **Uniform**: distributes keys evenly across buckets
- **Fast**: computed in O(1)

### Collision Resolution

Two keys can hash to the same slot (**collision**). Two resolution strategies:

#### Chaining (Closed Addressing)
Each slot holds a linked list of all keys that hash there. Simple and handles high load factors. Worst case: O(n) if all keys hash to one slot.

#### Open Addressing
All entries stored in the table itself. On collision, probe for the next empty slot:
- **Linear probing**: next slot +1, +2, ... (clustering problem)
- **Quadratic probing**: next slot +1², +2², ... (reduces primary clustering)
- **Double hashing**: next slot using a second hash function (best distribution)

### Load Factor

**Load factor** α = n/m (items/slots). Performance degrades as α → 1. Standard practice: resize (rehash) when α > 0.7. Chaining tolerates α > 1; open addressing requires α < 1.

## Tree Structures

### Binary Search Tree (BST)

For every node: left subtree values < node < right subtree values.

| Operation | Average | Worst (degenerate) |
|-----------|---------|-------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

Worst case occurs when the tree is unbalanced (e.g., inserting sorted data creates a linked list). Balanced BSTs solve this.

### AVL Trees

Self-balancing BST (Adelson-Velsky and Landis, 1962). Maintains the **balance factor** (|height(left) - height(right)| ≤ 1) at every node.

Rebalancing via **rotations** (single left, single right, double left-right, double right-left). All operations guaranteed O(log n). Stricter balance than Red-Black trees → faster lookups but slower inserts/deletes. Preferred for read-heavy workloads.

### Red-Black Trees

Self-balancing BST with five invariants:
1. Every node is red or black
2. Root is black
3. Leaves (NIL sentinels) are black
4. Red nodes have black children (no two consecutive reds)
5. All paths from a node to its descendant leaves have the same number of black nodes

All operations O(log n). Less strictly balanced than AVL → faster inserts/deletes. Used in Java's `TreeMap`/`TreeSet`, Linux kernel scheduler, C++ `std::map`.

### B-Trees

Multi-way balanced search tree designed for **disk-resident data**. Each node holds multiple keys and has multiple children (order m means up to m children).

Properties:
- All leaves at the same depth
- Each node (except root) has at least ⌈m/2⌉ children
- A node with k keys has k+1 children

B-Trees minimise disk I/O by maximising data per node (one disk block = one node). Used in filesystem indices, database engines (MySQL InnoDB, PostgreSQL). B+ Trees (all data in leaves, leaves linked) are the standard variant in databases.

## Complexity Comparison Table

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Stack/Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Singly Linked List | O(n) | O(n) | O(1) head | O(1) w/ptr | O(n) |
| Hash Table | N/A | O(1) avg | O(1) avg | O(1) avg | O(n) |
| BST | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg | O(n) |
| AVL / Red-Black | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| B-Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(1) min | O(n) | O(log n) | O(log n) | O(n) |

## See Also

- [[algorithm-complexity]] — formal complexity analysis
- [[sorting-and-searching]] — algorithms that operate on these structures
- [[graph-algorithms]] — graphs as generalisation of trees
- [[INF1008-data-structures-algorithms]] — source course
