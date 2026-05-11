---
type: source-index
title: "INF1008 Data Structures & Algorithms"
course: INF1008
institution: SIT
raw: "raw/INF1008 Data Structures and Algorithms Notes.md"
domain: computer-science
topics: [data-structures, algorithms, complexity, sorting, graphs, dynamic-programming]
ingested: 2026-05-11
---

# INF1008 — Data Structures & Algorithms

DSA is the foundational course for writing efficient programs. It covers how data is organised in memory and how algorithms exploit that organisation to solve problems within predictable time and space bounds. Every subsequent course in the programme builds on the intuitions developed here.

## Course Overview

The course progresses from complexity analysis → fundamental data structures → sorting/searching → graph algorithms → advanced algorithm design paradigms (dynamic programming, backtracking, string matching).

## Key Topics

### Complexity Analysis

Big-Oh notation is the language of algorithmic efficiency. The course covers formal definitions of O, Ω, and Θ, common complexity classes (O(1) through O(2^n)), asymptotic rules, and the Master Theorem for divide-and-conquer recurrences. See [[algorithm-complexity]].

### Data Structures

Each data structure is studied as an **Abstract Data Type (ADT)** — defined by its operations and their contracts, not its implementation:

- **Arrays** — random access O(1), insertion O(n)
- **Stacks** (LIFO) — push/pop O(1), expression evaluation
- **Queues** (FIFO) — enqueue/dequeue O(1), BFS scaffolding
- **Linked Lists** — singly, doubly, circular; O(1) insert at head
- **Hash Tables** — O(1) average lookup, collision resolution
- **Trees** — BST, AVL, Red-Black, B-Tree — O(log n) operations
- **Priority Queues / Heaps** — O(log n) insert/extract-min

See [[data-structures-fundamentals]] for the full breakdown including complexity comparison tables.

### Sorting & Searching

The course examines six sorting algorithms against three axes — time complexity, space, and stability:

| Algorithm | Best | Avg | Worst | Stable? |
|-----------|------|-----|-------|---------|
| Bubble | O(n) | O(n²) | O(n²) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | No |
| Insertion | O(n) | O(n²) | O(n²) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | No |

Binary search, linear search, and hash-based search are compared in [[sorting-and-searching]], which also covers KMP and Boyer-Moore string matching.

### Graph Algorithms

Graphs model relationships. The course covers:
- **Traversal**: DFS (stack-based, O(V+E)), BFS (queue-based, O(V+E))
- **Topological Sort** (DAGs only, DFS-based)
- **MST**: Prim's (greedy, dense graphs) and Kruskal's (union-find, sparse graphs)
- **Shortest Paths**: Dijkstra (non-negative weights, O(E log V)) and Bellman-Ford (handles negative weights, O(VE))

See [[graph-algorithms]].

### Advanced Paradigms

- **Dynamic Programming** — overlapping subproblems + optimal substructure; memoisation vs tabulation
- **Backtracking** — systematic exhaustive search with pruning
- **String Algorithms** — Brute Force O(nm), KMP O(n+m), Boyer-Moore (sublinear average)

## Concept Pages

| Concept | Description |
|---------|-------------|
| [[algorithm-complexity]] | Big-Oh, Master Theorem, recurrence solving |
| [[data-structures-fundamentals]] | ADTs, trees, hash tables, complexity table |
| [[sorting-and-searching]] | All sorting/searching algorithms with when-to-use guide |
| [[graph-algorithms]] | DFS/BFS, MST, shortest paths |

## Related Courses

- [[INF1009-object-oriented-programming]] — Java/C++ implementations of these ADTs
- [[INF2007-mobile-app-development]] — Kotlin collections, coroutines use graph-like dependency scheduling
