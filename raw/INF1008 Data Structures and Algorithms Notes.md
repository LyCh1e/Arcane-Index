---
type: source
folder: wiki/sources
title: INF1008 Data Structures and Algorithms Notes
course: INF1008
status: ingested
updated: 2026-05-09
tags:
  - source
  - dsa
  - algorithms
  - python
  - inf1008
related:
  - "[[data-structures-fundamentals]]"
  - "[[algorithm-complexity]]"
  - "[[algorithm-design-patterns]]"
  - "[[sorting-algorithms]]"
  - "[[search-algorithms]]"
  - "[[trees-and-bst]]"
  - "[[graph-algorithms]]"
  - "[[shortest-path-mst]]"
  - "[[string-algorithms]]"
---

# INF1008 Data Structures and Algorithms — Complete Lecture Notes

> **Singapore Institute of Technology (SIT)**
> Course: INF1008 / ICT1008 Data Structures and Algorithms
> Textbook: *Algorithms* (4th ed.) by Sedgewick & Wayne; *Introduction to Algorithms* (3rd ed.) by CLRS

---

## Table of Contents

1. [Lecture 1a – Introduction](#lecture-1a--introduction)
2. [Lecture 1b – Basic Data Structures](#lecture-1b--basic-data-structures)
3. [Lecture 2 – Analysis of Algorithms](#lecture-2--analysis-of-algorithms)
4. [Lecture 3 – Algorithm Design: Recursion & Greedy](#lecture-3--algorithm-design-recursion--greedy)
5. [Lecture 4 – Algorithm Design: Recursion Trees, Backtracking & Dynamic Programming](#lecture-4--algorithm-design-recursion-trees-backtracking--dynamic-programming)
6. [Lecture 5 – Sorting Algorithms](#lecture-5--sorting-algorithms)
7. [Lecture 6 – Search Algorithms Part 1: Linear Search, Binary Search & Hash Tables](#lecture-6--search-algorithms-part-1-linear-search-binary-search--hash-tables)
8. [Lecture 7 – Search Algorithms Part 2: Binary Search Trees & Balanced Search Trees](#lecture-7--search-algorithms-part-2-binary-search-trees--balanced-search-trees)
9. [Lecture 8 – Graph Algorithms Part 1: DFS, BFS & Topological Sort](#lecture-8--graph-algorithms-part-1-dfs-bfs--topological-sort)
10. [Lecture 9 – Graph Algorithms Part 2: Shortest Paths & Minimum Spanning Trees](#lecture-9--graph-algorithms-part-2-shortest-paths--minimum-spanning-trees)
11. [Lecture 10 – String Algorithms: Brute Force, KMP & Boyer-Moore](#lecture-10--string-algorithms-brute-force-kmp--boyer-moore)

---

## Assessment Weightage

| Component | Weight | Notes |
|-----------|--------|-------|
| Lab | 10% | No tutorial on Week 1 |
| Assignment | 20% | |
| Quiz 1 | 35% | Week 6, Monday |
| Quiz 2 | 35% | Week 13, Monday |

---

## Lecture 1a – Introduction

### Learning Outcomes (First Half)

1. Analyse the order of growth of time and space complexity using Big-Oh notation.
2. Describe and differentiate algorithmic approaches: recursion, divide and conquer, greedy, backtracking, dynamic programming.
3. Evaluate and select appropriate algorithms and data structures for problems such as sorting.
4. Implement algorithms and data structures for solving problems.

### Why Study Algorithms?

> "An algorithm must be seen to be believed." — Knuth

Algorithms have broad, far-reaching impact across many domains:

- **Internet** – Web search, packet routing, distributed file sharing
- **Biology** – Human genome project, protein folding
- **Computers** – Circuit layout, file systems, compilers
- **Computer Graphics** – Movies, video games, virtual reality
- **Security** – Cell phones, e-commerce, voting machines
- **Multimedia** – MP3, JPG, DivX, HDTV, face recognition
- **Social Networks** – Recommendations, news feeds, advertisements
- **Physics** – N-body simulation, particle collision simulation

### Algorithm — Definition & Properties

**Definition:** A finite sequence of rules/instructions for carrying out some calculation or procedure.

**Properties:**

- **Correct** – Must solve the intended problem for all valid inputs; showing incorrectness is easy (find one failing case), but proving correctness is hard (formal or informal methods).
- **Terminates** – Must finish in a finite number of steps.
- **Efficient** – Measured in:
  - **Time** – How many instructions are needed?
  - **Space** – How much storage is needed?
  - (Less commonly: performance, cost, energy consumption)

### Data Structures

- An **organised collection of data**; represents an abstract data type efficiently.
- Allow for **efficient access** by algorithms and use of **minimum storage**.
- Algorithms operate *on* data structures; data structures contain information about system state.
- Choosing the right data structure and algorithm is key to solving a problem well.

---

## Lecture 1b – Basic Data Structures

### Abstract Data Types (ADT)

- A **Data Type** = a set of values + a set of operations on those values.
- An **Abstract Data Type (ADT)** is a data type whose representation/implementation is *hidden* from users.
- ADT vs Primitive Data Type: ADT hides implementation details.

**Why ADT?**
- Supports **encapsulation** in program design.
- Precisely specifies the problem.
- Describes APIs (algorithms and data structures) to be used by clients.

### Arrays

- A **linear data structure** consisting of a fixed number of data items of the **same type**.
- Elements accessed directly via **index** (zero-based).

```
numbers = [12, 23, 4, 0]
numbers[0] == 12
numbers[1] == 23
```

- **Multi-dimensional arrays**: array of arrays; use multiple indices, e.g. `matrix[row][col]`.

**Time Complexity:**
- Access: O(1)
- Search: O(n)
- Insertion/Deletion: O(n) (due to shifting)

### Stacks

- A **linear data structure** following **LIFO (Last-In-First-Out)** / FILO order.

**Operations:**
- `push(value)` – Add value to the top of the stack.
- `pop()` – Remove and return the value on top.
- `peek()` – View the top value without removing it.
- `isEmpty()` – Check if the stack is empty.

**Applications:**
- Expression evaluation and conversion (infix/postfix)
- Function call stack (recursion)
- Undo mechanisms
- Backtracking

**Python Implementation (using list):**
```python
stack = []
stack.append(12)   # push
stack.append(100)
top = stack.pop()  # pop → returns 100
```

**Stack ADT with Linked List:**
- Each node contains data and a pointer to the next node.
- Push: create new node, point it to current top, update top.
- Pop: save top node's data, move top to next, delete old top.

### Queues

- A **linear data structure** following **FIFO (First-In-First-Out)** order.

**Operations:**
- `enqueue(value)` – Add value to the rear.
- `dequeue()` – Remove and return value from the front.
- `peek()` – View the front value.
- `isEmpty()` – Check if the queue is empty.

**Types of Queues:**
- **Simple Queue** – Basic FIFO.
- **Circular Queue** – Front and rear wrap around; avoids wasted space.
- **Priority Queue** – Elements dequeued based on priority.
- **Deque (Double-Ended Queue)** – Insert/delete from both ends.

**Applications:**
- CPU scheduling
- Disk scheduling
- Print spooling
- BFS traversal

**Python Implementation:**
```python
from collections import deque
queue = deque()
queue.append(10)    # enqueue
queue.append(20)
front = queue.popleft()  # dequeue → 10
```

### Linked Lists

A **linked list** is a linear data structure where each element (**node**) contains:
- **Data**
- **Pointer** to the next node (and previous, in doubly linked lists)

**Types:**
- **Singly Linked List** – Each node points to the next only.
- **Doubly Linked List** – Each node has pointers to both next and previous.
- **Circular Linked List** – Last node points back to the first.

**Operations & Complexity:**
| Operation | Singly LL | Array |
|-----------|-----------|-------|
| Access by index | O(n) | O(1) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(n) |
| Insert at tail | O(n) or O(1) with tail pointer | O(1) amortized |
| Delete | O(n) | O(n) |

**Advantages over arrays:**
- Dynamic size (no fixed allocation)
- Efficient insertions/deletions at head

**Disadvantages:**
- No random access (must traverse)
- Extra memory for pointers

**Singly Linked List Node (Python):**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Priority Queue

- Elements are served based on **priority**, not insertion order.
- Implemented using a **heap** (binary heap is most common).

**Heap properties:**
- **Max-Heap**: Parent ≥ children → `peek()` returns max.
- **Min-Heap**: Parent ≤ children → `peek()` returns min.

---

## Lecture 2 – Analysis of Algorithms

### Why Analyse Algorithms?

- To predict **performance** (time and space).
- To compare algorithms and choose the best for a problem.
- To provide **guarantees** on correctness and performance.

### Mathematical Foundations

**Logarithms:**
- Definition: if b^x = n, then log_b(n) = x
- Laws: log(a × b) = log a + log b; log(a/b) = log a − log b; log(a^b) = b log a
- Change of base: log_b(n) = log_c(n) / log_c(b)

**Summation of Series:**
- Arithmetic: 1 + 2 + … + n = n(n+1)/2
- Geometric: a + ar + ar² + … = a(r^n − 1)/(r − 1)

### Empirical Analysis

- Implement and time the algorithm for different input sizes.
- Observe the relationship between input size N and running time T(N).
- Limitation: depends on hardware, implementation, and specific inputs.

**Doubling ratio experiment:**
- Run for N, 2N, 4N, …; observe the ratio of consecutive runtimes.
- If ratio ≈ 2^b, the growth rate is approximately O(N^b).

### Mathematical Models

- Count the number of **basic operations** (comparisons, array accesses, etc.).
- Determine the **dominant term** as N grows large.

### Order of Growth (Big-Oh Notation)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access |
| O(log N) | Logarithmic | Binary search |
| O(N) | Linear | Linear search |
| O(N log N) | Linearithmic | Merge sort |
| O(N²) | Quadratic | Bubble sort, insertion sort |
| O(N³) | Cubic | Matrix multiplication (naïve) |
| O(2^N) | Exponential | Brute-force subset enumeration |

**Formal Definitions:**
- **Big-Oh O(g(n))**: f(n) = O(g(n)) if ∃ constants c > 0, n₀ such that 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀. (Upper bound)
- **Big-Omega Ω(g(n))**: f(n) = Ω(g(n)) if ∃ c > 0, n₀ such that 0 ≤ c·g(n) ≤ f(n) for all n ≥ n₀. (Lower bound)
- **Big-Theta Θ(g(n))**: f(n) = Θ(g(n)) if f(n) = O(g(n)) AND f(n) = Ω(g(n)). (Tight bound)

### Asymptotic Rules

1. **Ignore lower-order terms**: 3n² + 2n + 1 → O(n²)
2. **Ignore constant factors**: 5n → O(n)
3. **Nested loops multiply**: two nested O(n) loops → O(n²)
4. **Sequential statements add**: O(n) + O(n²) → O(n²)

### Theory of Algorithms

- **Best case** – Minimum number of operations for a given input size.
- **Worst case** – Maximum number of operations (most commonly analysed).
- **Average case** – Expected operations over all inputs of size N.

### General Plan for Algorithm Analysis

1. Decide on the input model.
2. Identify the basic operation.
3. Determine the worst, average, and best case.
4. Find the dominant term and express complexity using Big-Oh.

---

## Lecture 3 – Algorithm Design: Recursion & Greedy

### Recursion

**Definition:** Recursion is a method of solving problems by breaking them into smaller subproblems until trivially solvable. A recursive function calls itself.

**Two key parts:**
- **Base case** – The condition under which the function stops calling itself.
- **Recursive case** – The function calls itself with a smaller/simpler input.

**Recurrence relation:** An equation that relates the n-th element to its predecessors.

**Fibonacci Sequence:**
```
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)  for n ≥ 2
→ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …
```

**Factorial:**
```
0! = 1  (base case)
n! = n × (n-1)!  (recursive case)
```

**Python recursive factorial:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Analysis of Recursive Algorithms

- Use a **recurrence relation** to model the time complexity.
- Solve using substitution, recursion trees, or the Master Theorem.

**Example — Fibonacci recurrence:**
T(n) = T(n-1) + T(n-2) + O(1) → exponential O(2^n) without memoisation.

**Common patterns:**
| Recurrence | Solution |
|------------|----------|
| T(n) = T(n-1) + O(1) | O(n) |
| T(n) = T(n/2) + O(1) | O(log n) |
| T(n) = 2T(n/2) + O(n) | O(n log n) |
| T(n) = T(n-1) + O(n) | O(n²) |

### Divide and Conquer

**Strategy:**
1. **Divide** the problem into smaller subproblems.
2. **Conquer** (solve) each subproblem recursively.
3. **Combine** the results.

**Classic examples:** Merge Sort, Quick Sort, Binary Search.

### Greedy Algorithms

**Concept:** Make the locally optimal choice at each step in the hope of finding a global optimum.

**Properties required for greedy to work:**
- **Greedy-choice property** – A global optimum can be arrived at by making locally optimal choices.
- **Optimal substructure** – An optimal solution to the problem contains optimal solutions to subproblems.

**Greedy algorithms do NOT always yield optimal solutions**, but work for many problems.

**Examples of greedy algorithms:**
- Dijkstra's Shortest Path Algorithm
- Kruskal's Minimum Spanning Tree Algorithm
- Prim's Minimum Spanning Tree Algorithm
- Activity Selection / Interval Scheduling
- Huffman Coding

**Activity Selection Problem:**
- Given a set of activities with start and finish times, select the maximum number of non-overlapping activities.
- Greedy rule: always pick the activity with the **earliest finish time**.

**Coin Change (Greedy — works for standard coin systems):**
- Always pick the largest coin ≤ remaining amount.
- Note: greedy does not always work for arbitrary coin denominations.

---

## Lecture 4 – Algorithm Design: Recursion Trees, Backtracking & Dynamic Programming

### Recursion Trees

A **recursion tree** is a visual tool to analyse the time complexity of recursive algorithms.

- Each node represents a subproblem.
- The cost at each level is summed; all levels are totalled.
- Used to derive and verify recurrence solutions.

**Example — Merge Sort T(n) = 2T(n/2) + n:**
- Level 0: n work
- Level 1: 2 × (n/2) = n work
- Level 2: 4 × (n/4) = n work
- … log n levels total → T(n) = O(n log n)

### Master Theorem

For recurrences of the form T(n) = aT(n/b) + f(n):

- **Case 1**: f(n) = O(n^(log_b a - ε)) → T(n) = Θ(n^(log_b a))
- **Case 2**: f(n) = Θ(n^(log_b a)) → T(n) = Θ(n^(log_b a) log n)
- **Case 3**: f(n) = Ω(n^(log_b a + ε)) → T(n) = Θ(f(n))

### Backtracking

**Concept:** Build a solution incrementally; abandon a path (backtrack) as soon as it is determined it cannot lead to a valid solution.

**Key idea:** Explore all potential solutions using a depth-first search approach; prune invalid branches early.

**General template:**
```python
def backtrack(solution, choices):
    if is_complete(solution):
        record(solution)
        return
    for choice in choices:
        if is_valid(solution, choice):
            make(solution, choice)
            backtrack(solution, remaining_choices)
            undo(solution, choice)   # backtrack
```

**Classic problems:**
- **N-Queens Problem** – Place N queens on an N×N board so no two attack each other.
- **Maze Solving** – Find a path from start to end.
- **Sudoku Solver**
- **Subset Sum**
- **Graph Colouring**

**N-Queens approach:**
- Place one queen per row.
- For each row, try each column; check if placement is valid (no conflicts with existing queens).
- Recurse for next row; backtrack if stuck.

### Dynamic Programming (DP)

**Concept:** Solve complex problems by breaking them into overlapping subproblems. Store results to avoid redundant computation.

**Two approaches:**
- **Top-Down (Memoisation):** Recursive approach with caching of results.
- **Bottom-Up (Tabulation):** Iterative approach; fill a table from smallest subproblems upward.

**Conditions for DP:**
- **Optimal substructure** – Optimal solution is built from optimal solutions to subproblems.
- **Overlapping subproblems** – The same subproblems recur many times.

**Difference from Divide and Conquer:** In D&C, subproblems are independent. In DP, subproblems overlap.

**Fibonacci with DP (Bottom-Up):**
```python
def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
Time: O(n), Space: O(n) → compared to O(2^n) for naive recursion.

**Common DP Problems:**
- **0/1 Knapsack** – Select items with max value subject to weight limit.
- **Longest Common Subsequence (LCS)**
- **Coin Change** (minimum coins)
- **Matrix Chain Multiplication**
- **Edit Distance**

**Knapsack (0/1) recurrence:**
```
dp[i][w] = max(dp[i-1][w],  dp[i-1][w - weight[i]] + value[i])
```
where dp[i][w] = max value using first i items with capacity w.

---

## Lecture 5 – Sorting Algorithms

### Overview

Sorting arranges elements in a defined order (ascending or descending). Key metrics: number of **comparisons** and number of **swaps/moves**.

### Bubble Sort

**Algorithm:**
1. Step through the list.
2. Compare adjacent pairs; swap if out of order.
3. Repeat until no swaps are needed.

**Analysis:**
- Number of comparisons: 1 + 2 + … + (n−1) = n(n−1)/2 → **O(n²)**
- Best case (already sorted): O(n) with early termination optimisation.
- Worst case / Average: O(n²)
- In-place: Yes | Stable: Yes

### Selection Sort

**Algorithm:**
1. Find the minimum in the unsorted portion.
2. Swap it to the front of the unsorted portion.
3. Advance the boundary of the sorted portion.
4. Repeat until sorted.

**Analysis:**
- Same number of comparisons as Bubble Sort → **O(n²)**
- Fewer swaps than Bubble Sort → typically faster in practice.
- In-place: Yes | Stable: No (in standard implementation)

### Insertion Sort

**Algorithm:**
1. Start with the second element.
2. Compare it with the elements to its left; shift larger elements right.
3. Insert the element in its correct position.
4. Repeat for each subsequent element.

**Analysis:**
- Best case (sorted input): O(n) comparisons, O(1) swaps.
- Worst case (reverse sorted): O(n²)
- Efficient for **small or nearly sorted** arrays.
- In-place: Yes | Stable: Yes

### Merge Sort

**Algorithm (Divide and Conquer):**
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves.

**Merge operation:** Compare front elements of each half; copy the smaller to the output.

**Analysis:**
- All cases: **O(n log n)**
- Space: O(n) auxiliary
- In-place: No | Stable: Yes

**Recurrence:** T(n) = 2T(n/2) + O(n) → O(n log n)

### Quick Sort

**Algorithm:**
1. Choose a **pivot** element.
2. **Partition**: rearrange so elements < pivot come before it, elements > pivot come after.
3. Recursively sort the sub-arrays on each side of the pivot.

**Pivot selection strategies:**
- First/last element (simple but can be O(n²) on sorted input)
- Median of three
- Random pivot (expected O(n log n))

**Analysis:**
- Best / Average case: **O(n log n)**
- Worst case (already sorted, bad pivot): O(n²)
- In-place: Yes | Stable: No
- Often fastest in practice due to good cache performance.

### Sorting Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |

---

## Lecture 6 – Search Algorithms Part 1: Linear Search, Binary Search & Hash Tables

### Linear Search

**Algorithm:** Scan from left to right; compare each element to the target.

**Analysis:**
- Best case: O(1) (target is first element)
- Worst case: O(n) (target is last or not present)
- Average: O(n/2) → O(n)
- Works on **unsorted** data.

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

### Binary Search

**Prerequisite:** Array must be **sorted**.

**Algorithm:**
1. Set low = 0, high = n−1.
2. Compute mid = (low + high) // 2.
3. If arr[mid] == target → return mid.
4. If arr[mid] < target → low = mid + 1.
5. If arr[mid] > target → high = mid − 1.
6. Repeat until low > high.

**Analysis:**
- Each iteration halves the search space → **O(log n)**
- Worst case: O(log n) | Best case: O(1)

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**Recursive version:** T(n) = T(n/2) + O(1) → O(log n)

### Hash Tables

A **hash table** maps keys to values using a **hash function** that computes an index into an array of buckets.

**Hash Function h(k):**
- Maps key k to an integer index in [0, M−1] where M = table size.
- Should be fast to compute and distribute keys uniformly.

**Ideal properties:**
- Deterministic
- Fast to compute
- Uniform distribution
- Minimises collisions

**Common hash functions:**
- **Division**: h(k) = k mod M
- **Multiplication**: h(k) = floor(M × (k × A mod 1)) where A is a constant
- **String hashing**: polynomial rolling hash

### Collision Resolution

**Collision:** Two keys hash to the same index.

**1. Separate Chaining (Open Hashing):**
- Each bucket holds a linked list of entries.
- Insert: compute hash, append to list at that index.
- Search: compute hash, traverse the list.
- Worst case (all keys in one chain): O(n); average O(1 + α) where α = n/M (load factor).

**2. Open Addressing (Closed Hashing):**
All entries are stored within the table itself.
- **Linear Probing**: if slot h(k) is occupied, try h(k)+1, h(k)+2, …
  - Suffers from **primary clustering**.
- **Quadratic Probing**: try h(k)+1², h(k)+2², h(k)+3², …
  - Reduces primary clustering but has **secondary clustering**.
- **Double Hashing**: use a second hash function to compute step size.
  - `h(k, i) = (h₁(k) + i × h₂(k)) mod M`

**Load Factor α = n/M:**
- Keep α < 0.75 for good performance.
- When α exceeds threshold, **rehash** into a larger table.

**Hash Table Time Complexity:**
| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

**Applications:** Dictionary, symbol tables, caching, database indexing.

---

## Lecture 7 – Search Algorithms Part 2: Binary Search Trees & Balanced Search Trees

### Symbol Table (Dictionary) ADT

Supports:
- `put(key, value)` – Insert or update
- `get(key)` – Retrieve value for key
- `delete(key)` – Remove key-value pair
- `contains(key)` – Check if key exists
- `size()`, `isEmpty()`

### Binary Search Trees (BST)

A **BST** is a binary tree where for every node:
- All keys in the **left subtree** < node's key
- All keys in the **right subtree** > node's key

**Node structure:**
```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
```

**BST Operations:**

**Search:**
- Compare target key to current node.
- If equal → found; if less → go left; if greater → go right.
- O(h) where h = height of tree.

**Insert:**
- Search for the key; insert at the null position where the search terminates.
- O(h)

**Min/Max:**
- **Minimum**: go as far left as possible.
- **Maximum**: go as far right as possible.

**In-order Traversal (Sorted order):** Left → Root → Right

**Deletion:**
Three cases:
1. Node has **no children** → simply remove it.
2. Node has **one child** → replace node with its child.
3. Node has **two children** → replace with **in-order successor** (smallest in right subtree), then delete the successor.

**BST Complexity:**
| Operation | Average | Worst (skewed tree) |
|-----------|---------|---------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

The worst case occurs when elements are inserted in sorted order (tree becomes a linked list).

### Balanced Search Trees

To guarantee O(log n) for all operations, we need a **balanced** BST where height is always O(log n).

### AVL Trees

- A **self-balancing BST** where the heights of the two child subtrees differ by at most 1 (**balance factor ∈ {−1, 0, 1}**).
- Named after Adelson-Velsky and Landis (1962).

**Balance Factor = height(left subtree) − height(right subtree)**

**Rotations (to restore balance):**
- **Right Rotation (LL case):** Left-heavy tree; rotate root right.
- **Left Rotation (RR case):** Right-heavy tree; rotate root left.
- **Left-Right Rotation (LR case):** Left-rotate left child, then right-rotate root.
- **Right-Left Rotation (RL case):** Right-rotate right child, then left-rotate root.

**Complexity:** O(log n) guaranteed for all operations.

### Red-Black Trees

A BST with one extra bit per node: **colour** (red or black).

**Properties:**
1. Every node is red or black.
2. The root is black.
3. Every null leaf is black.
4. If a node is red, both its children are black (no two consecutive reds).
5. All paths from any node to its descendant null leaves have the same number of black nodes (**black-height**).

- Height is at most **2 log(n+1)** → O(log n) operations.
- Used in Java's TreeMap, C++ std::map.

### 2-3 Trees

- Each internal node has either **2 or 3 children**.
- All leaves are at the same level (perfectly balanced).
- Guaranteed O(log n) for search, insert, delete.

### B-Trees

- Generalisation of 2-3 trees; nodes can have **many children** (order M).
- Used in databases and file systems where data is stored on disk.
- Each node contains between ⌈M/2⌉ and M children.

---

## Lecture 8 – Graph Algorithms Part 1: DFS, BFS & Topological Sort

### Graph Terminology

A **graph** G = (V, E) consists of:
- **V** – Set of vertices (nodes)
- **E** – Set of edges (connections)

**Types:**
- **Undirected graph** – Edges have no direction; (u,v) = (v,u).
- **Directed graph (DiGraph)** – Edges have direction; (u,v) ≠ (v,u).
  - **In-degree**: number of edges entering a vertex.
  - **Out-degree**: number of edges leaving a vertex.
- **Weighted graph** – Edges have associated weights/costs.

**Other terms:**
- **Path** – Sequence of vertices connected by edges.
- **Cycle** – Path that starts and ends at the same vertex.
- **Connected graph** – Every vertex is reachable from every other.
- **DAG** – Directed Acyclic Graph (no directed cycles).
- **Sparse graph** – Few edges (E << V²); **Dense graph** – Many edges.

### Graph Representations

**1. Adjacency Matrix:**
- V × V matrix; `matrix[u][v] = 1` (or weight) if edge (u,v) exists.
- Space: O(V²)
- Edge check: O(1); finding all neighbours: O(V)
- Better for dense graphs.

**2. Adjacency List:**
- Array of lists; `adj[u]` contains all neighbours of u.
- Space: O(V + E)
- Edge check: O(degree(u)); finding all neighbours: O(degree(u))
- Better for sparse graphs (most real-world graphs).

### Depth-First Search (DFS)

**Idea:** Explore as deep as possible before backtracking.

**Algorithm (recursive):**
```python
def dfs(graph, v, visited):
    visited[v] = True
    for neighbour in graph[v]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited)
```

**Properties:**
- Uses a **stack** (implicit call stack or explicit).
- Time: O(V + E)
- Space: O(V)

**Applications:**
- Cycle detection
- Topological sort
- Finding connected components
- Solving mazes / puzzles
- Finding strongly connected components (Kosaraju's, Tarjan's)

**DFS Tree edge types (directed graph):**
- **Tree edge**: edge to an unvisited node.
- **Back edge**: edge to an ancestor (indicates a cycle).
- **Forward edge**: edge to a descendant already visited.
- **Cross edge**: edge to a node in a different DFS tree.

### Breadth-First Search (BFS)

**Idea:** Explore all neighbours at the current depth before moving deeper.

**Algorithm (iterative):**
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
```

**Properties:**
- Uses a **queue** (FIFO).
- Time: O(V + E)
- Space: O(V)
- Finds the **shortest path** (fewest edges) from source to all vertices in an unweighted graph.

**BFS Properties:**
- Queue always contains ≥ 0 vertices at distance k, followed by ≥ 0 at distance k+1.
- Examines vertices in increasing distance order from source.

**Applications:**
- Shortest path in unweighted graphs
- Web crawling
- Social network friend suggestions
- Finding all nodes within distance k

### DFS vs BFS

| Feature | DFS | BFS |
|---------|-----|-----|
| Data structure | Stack | Queue |
| Time | O(V+E) | O(V+E) |
| Space | O(V) | O(V) |
| Shortest path | No | Yes (unweighted) |
| Use for | Cycle detection, Topo sort | Shortest path, Level order |

### In-Order, Pre-Order, Post-Order Traversal (Trees)

**Pre-order:** Root → Left → Right
**In-order:** Left → Root → Right (gives sorted order for BST)
**Post-order:** Left → Right → Root

These are special cases of DFS on trees.

### Topological Sort

**Definition:** A linear ordering of vertices in a DAG such that for every directed edge (u → v), u comes before v.

**Condition:** Only possible if the graph is a **DAG** (no directed cycles).

**Application examples:**
- Build system dependencies
- Course prerequisites
- Task scheduling

**Algorithm (DFS-based):**
1. Run DFS on the graph.
2. After all recursive calls for a vertex return, add that vertex to the front of the result list (post-order).
3. The result is the topological order (reverse post-order).

```python
def topo_dfs(graph, v, visited, result):
    visited[v] = True
    for neighbour in graph[v]:
        if not visited[neighbour]:
            topo_dfs(graph, neighbour, visited, result)
    result.insert(0, v)  # prepend (reverse post-order)
```

**Complexity:** O(V + E)

---

## Lecture 9 – Graph Algorithms Part 2: Shortest Paths & Minimum Spanning Trees

### Minimum Spanning Tree (MST)

**Problem:** Given a connected, undirected graph with positive edge weights, find a spanning tree with minimum total edge weight.

**Spanning Tree:** A subgraph T that is:
- Connected
- Acyclic
- Includes all vertices (V nodes, V−1 edges)

**Applications:**
- Network design (roads, cables, power lines)
- Cluster analysis
- Circuit layout
- Wireless sensor networks
- Cancer research (nuclei arrangement)

**Assumptions:**
- Graph is connected.
- Edge weights are distinct (if not, MST may not be unique).
- If not connected → compute MST for each connected component (Minimum Spanning Forest).

### Prim's Algorithm

**Strategy (Greedy):**
1. Start with any vertex (e.g., vertex 0).
2. Grow the MST one vertex at a time.
3. Always add the minimum-weight edge that connects a vertex inside the MST to a vertex outside.
4. Repeat until all vertices are included (V−1 edges added).

**Implementation using Priority Queue:**
- Maintain a priority queue of edges with one endpoint in the MST.
- Delete-min to get the cheapest crossing edge.
- Add the new vertex and insert its edges into the PQ.

**Time Complexity:**
- With binary heap: O(E log V)
- With Fibonacci heap: O(E + V log V)

### Kruskal's Algorithm

**Strategy (Greedy):**
1. Sort all edges by weight.
2. Add edges one by one in order of increasing weight.
3. Skip an edge if it creates a cycle (both endpoints already connected).
4. Stop when V−1 edges have been added.

**Cycle detection using Union-Find (Disjoint Set):**
- Maintain a set for each connected component.
- If both endpoints are in the same set → adding the edge creates a cycle → skip.
- Otherwise → add edge and merge the two sets.

**Time Complexity:**
| Operation | Frequency | Time per op |
|-----------|-----------|-------------|
| Build priority queue | 1 | E |
| Delete-min | E | log E |
| Union | V | log V |
| Connected check | E | log V |
Overall: **O(E log E)**

### Prim's vs Kruskal's

| | Prim's | Kruskal's |
|-|--------|-----------|
| Strategy | Grow from a vertex | Add cheapest edge globally |
| Data structure | Priority Queue | Sorted edges + Union-Find |
| Better for | Dense graphs | Sparse graphs |
| Complexity | O(E log V) | O(E log E) |

### Shortest Path Problem

**Problem:** Given a weighted directed graph, find the shortest (minimum weight) path from source s to all other vertices.

**Applications:**
- Map navigation / GPS routing
- Network routing protocols (OSPF, BGP, RIP)
- PERT/CPM project management
- Robot navigation
- Arbitrage in currency exchange

**Key data structures:**
- `distTo[v]` – Length of shortest known path from s to v (initialised to ∞, 0 for source).
- `edgeTo[v]` – Last edge on the shortest known path to v.

**Edge Relaxation:**
For edge e = v → w with weight w_e:
```
if distTo[v] + w_e < distTo[w]:
    distTo[w] = distTo[v] + w_e
    edgeTo[w] = e
```

### Dijkstra's Algorithm

**Condition:** Edge weights must be **non-negative**.

**Algorithm:**
1. Set distTo[s] = 0, all others = ∞.
2. Use a priority queue (min-heap) ordered by distTo.
3. Extract the vertex v with the minimum distTo.
4. Relax all edges leaving v.
5. Repeat until all vertices are settled.

**Example (trace):**

For the demo graph (source = 0):
- Initially: distTo = [0, ∞, ∞, ∞, ∞, ∞, ∞, ∞]
- After marking 0: update neighbours 1 (dist=5), 4 (dist=9), 7 (dist=8)
- After marking 1: update 2 (dist=17), 3 (dist=20)
- After marking 7: update 2 (dist=15), 5 (dist=14)
- After marking 4: update 5 (dist=13), 6 (dist=29)
- After marking 5: update 2 (dist=14), 6 (dist=26)
- After marking 2: update 3 (dist=17), 6 (dist=25)
- Final: distTo = [0, 5, 14, 17, 9, 13, 25, 8]

**Complexity (with binary heap PQ):**
- V insert + V delete-min + E decrease-key operations
- **O(E log V)**

**Note:** Dijkstra does NOT work with negative edge weights.

### Bellman-Ford Algorithm

**Handles:** Graphs with **negative edge weights** (but no negative cycles).

**Algorithm:**
1. Set distTo[s] = 0, all others = ∞.
2. Repeat V−1 times:
   - Relax every edge in the graph.
3. (Optional) Check for negative cycles: if any distTo[v] changes in the V-th pass, a negative cycle exists.

**Negative Cycle:** A directed cycle whose total weight is negative. No shortest path exists if a negative cycle is reachable from s.

**Complexity:** O(V × E) = O(VE)

### Shortest Path Summary

| Algorithm | Restriction | Complexity |
|-----------|-------------|------------|
| Dijkstra (binary heap PQ) | No negative weights | O(E log V) |
| Bellman-Ford | No negative cycles | O(VE) |

---

## Lecture 10 – String Algorithms: Brute Force, KMP & Boyer-Moore

### String Searching / Pattern Matching

**Problem:** Given a text string T (length n) and a pattern string P (length m), find all occurrences of P in T.

**Applications:**
- Text editors (find/replace)
- Search engines
- Bioinformatics (DNA sequence matching)
- Intrusion detection

### Brute Force (Naive) Search

**Algorithm:**
1. Try to match P at every position in T (from 0 to n−m).
2. At each position, compare characters of P with T left to right.
3. On mismatch, slide P one position right and restart.

```python
def brute_force(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            print(f"Match at index {i}")
```

**Complexity:**
- Worst case: **O(nm)** — e.g., T = "AAAA…A", P = "AAA…AB"
- Best case: O(n)

### Knuth-Morris-Pratt (KMP) Algorithm

**Key idea:** When a mismatch occurs, use information about the pattern's own structure to avoid redundant comparisons. Never back up in the text.

**Failure Function (also called prefix function or partial match table):**
- `fail[j]` = length of the longest proper prefix of P[0..j] that is also a suffix.
- Used to determine where to resume matching after a mismatch.

**Building the failure function:**
```python
def build_fail(pattern):
    m = len(pattern)
    fail = [0] * m
    k = 0
    for j in range(1, m):
        while k > 0 and pattern[k] != pattern[j]:
            k = fail[k - 1]
        if pattern[k] == pattern[j]:
            k += 1
        fail[j] = k
    return fail
```

**KMP search:**
```python
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    fail = build_fail(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            print(f"Match at index {i - m + 1}")
            j = fail[j - 1]
```

**Complexity:**
- Preprocessing: O(m)
- Searching: O(n)
- **Total: O(n + m)**

### Boyer-Moore Algorithm

**Key ideas:** Two heuristics that allow skipping large portions of the text.

**1. Bad Character Rule:**
- When a mismatch occurs at text position i (matching pattern position j), look at the mismatched text character c.
- Find the rightmost occurrence of c in P[0..j-1].
- Shift P so that occurrence aligns with c in T.
- If c does not appear in P, shift P past position i.

**2. Good Suffix Rule:**
- When a mismatch occurs after matching suffix P[j+1..m-1] = T[i+1..i+m-1-j]:
- Find the rightmost copy of this suffix in P that is preceded by a different character.
- Shift P to align that copy with the matched suffix in T.

**Searching direction:** Boyer-Moore compares right-to-left within the pattern (while sliding left-to-right).

**Complexity:**
- Preprocessing: O(m + |Σ|) where |Σ| = alphabet size
- Searching:
  - Best case: **O(n/m)** (very fast in practice)
  - Worst case: O(nm) but rare; O(n) with full Good Suffix rule
  - Average case: **O(n)** — widely regarded as the fastest in practice for large alphabets

### Algorithm Comparison

| Algorithm | Preprocessing | Searching | Total | Backtrack in text? |
|-----------|--------------|-----------|-------|-------------------|
| Brute Force | None | O(nm) | O(nm) | Yes |
| KMP | O(m) | O(n) | O(n + m) | No |
| Boyer-Moore | O(m + \|Σ\|) | O(n/m) best | O(n + m) avg | No |

**When to use:**
- **Brute Force** – Small patterns/texts; simple implementation needed.
- **KMP** – Large texts; need guaranteed linear time; small alphabets.
- **Boyer-Moore** – Large alphabets (e.g., English text); need fastest average-case performance.

---

## Quick Reference: Complexity Summary

### Data Structures

| Data Structure | Access | Search | Insert | Delete |
|---------------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Hash Table | — | O(1) avg | O(1) avg | O(1) avg |
| BST | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg |
| AVL / Red-Black | O(log n) | O(log n) | O(log n) | O(log n) |

*at head for singly linked list

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |

### Graph Algorithms

| Algorithm | Complexity | Use case |
|-----------|------------|----------|
| DFS | O(V + E) | Cycle detection, Topo sort |
| BFS | O(V + E) | Shortest path (unweighted) |
| Dijkstra | O(E log V) | Shortest path (non-negative weights) |
| Bellman-Ford | O(VE) | Shortest path (negative weights) |
| Prim's MST | O(E log V) | Minimum spanning tree |
| Kruskal's MST | O(E log E) | Minimum spanning tree |

### String Algorithms

| Algorithm | Preprocessing | Search | Best for |
|-----------|--------------|--------|----------|
| Brute Force | O(1) | O(nm) | Simple / small |
| KMP | O(m) | O(n) | Small alphabets |
| Boyer-Moore | O(m + \|Σ\|) | O(n/m) avg | Large alphabets |

---

*End of INF1008 Data Structures and Algorithms Notes*
