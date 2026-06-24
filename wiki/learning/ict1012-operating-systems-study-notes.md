---
type: learning
status: established
title: "ICT1012 Operating Systems — Exam Study Notes"
domain: operating-systems
source: "[[sources/ICT1012-operating-systems|ICT1012 Source]]"
complexity: high
updated: 2026-05-14
tags: [learning, operating-systems, exam-prep, processes, scheduling, synchronisation, memory, deadlocks]
---

# ICT1012 Operating Systems — Exam Study Notes

Dense Q&A and definition cards for exam preparation. Covers processes, scheduling, synchronisation, memory management, and deadlocks.

---

## 1. Processes and the PCB

> [!question]- What are the five process states and their transitions?
> **New** → (admitted) → **Ready** → (scheduler dispatch) → **Running**
> **Running** → (I/O or event wait) → **Waiting** → (I/O done) → **Ready**
> **Running** → (interrupt) → **Ready**
> **Running** → (exit) → **Terminated**
> A sixth state, **Waiting Swapped**, exists when the OS swaps out a waiting process to free memory.

> [!question]- What fields does the Process Control Block (PCB) store?
> - **Process state** (new / ready / running / waiting / terminated)
> - **Process ID (PID)** and parent PID
> - **Programme counter** — address of the next instruction
> - **CPU registers** — all register contents at the time of a context switch
> - **CPU scheduling information** — priority, pointer to scheduling queue
> - **Memory management information** — page tables, segment tables, base/limit registers
> - **Accounting information** — CPU time used, time limits, job numbers
> - **I/O status** — open file list, allocated devices
> - **IPC structures** — shared memory regions, message queue handles

> [!question]- What is a context switch and why is it overhead?
> A **context switch** saves the state of the currently running process into its PCB and loads the state of the next process from its PCB. No useful work is performed during this period — it is pure overhead. Duration depends on hardware support (register count, special instructions).

> [!question]- Distinguish the three types of scheduler.
> | Scheduler | Frequency | Role |
> |-----------|-----------|------|
> | **Long-term** (job) | Seconds / minutes | Admits processes to the ready queue; controls degree of multiprogramming; balances CPU-bound vs I/O-bound mix |
> | **Medium-term** | On memory pressure | Swaps processes to/from disk; temporarily reduces multiprogramming |
> | **Short-term** (CPU) | Every few milliseconds | Selects which ready process runs next; must be extremely fast |

---

## 2. CPU Scheduling Algorithms

> [!question]- FCFS: explain the convoy effect with a numeric example.
> **First-Come, First-Served** is a non-preemptive FIFO queue.
> **Convoy effect**: a long CPU-bound process blocks many short I/O-bound processes behind it.
> *Example*: P1=3 ms, P2=3 ms, P3=24 ms.
> - Order P1→P2→P3: avg waiting = (0+3+6)/3 = **3 ms**
> - Order P3→P2→P1: avg waiting = (0+24+27)/3 = **17 ms**
> Arrival order dramatically affects performance.

> [!question]- SJF: what is exponential averaging and why is it used?
> **Shortest-Job-First** needs to predict the next CPU burst. Actual burst lengths are unknown, so the OS estimates using **exponential averaging**:
> ```
> τ(n+1) = α · t(n) + (1 − α) · τ(n)
> ```
> - `t(n)` = actual nth burst; `τ(n)` = predicted nth burst; `α` = weight (commonly 0.5)
> - `α = 0` → ignore all recent history (use only initial estimate)
> - `α = 1` → use only the most recent actual burst
> At α = 0.5, recent and historical bursts contribute equally.
> **SRTF** (preemptive SJF) preempts the current process if a new arrival has a shorter remaining burst.
> SJF is **optimal for minimising average waiting time** but can cause **starvation** of long jobs.

> [!question]- Round Robin: how do you calculate maximum waiting time?
> Each of **n** processes in the ready queue receives up to **q** ms of CPU time, then is preempted.
> Maximum waiting time for any process = **(n − 1) × q** ms.
> - q too large → degenerates to FCFS
> - q too small → context switch overhead dominates
> RR gives better response time than SJF but typically higher average turnaround time.

> [!question]- Priority scheduling: what is starvation and how is it solved?
> **Starvation**: low-priority processes may wait indefinitely if high-priority processes keep arriving.
> **Solution — ageing**: gradually increase the priority of processes that have been waiting a long time, ensuring every process eventually runs.

> [!question]- Multilevel Feedback Queue: how does it differ from Multilevel Queue?
> In a **Multilevel Queue**, processes are permanently assigned to a queue (e.g., foreground = RR; background = FCFS).
> In a **Multilevel Feedback Queue**, processes **move between queues** based on behaviour:
> - New jobs enter the highest-priority queue (shortest quantum)
> - Jobs that do not complete within their quantum are demoted
> - Long-waiting jobs are promoted (ageing)
> This makes it the most general-purpose algorithm.

---

## 3. Critical Section and Hardware Synchronisation

> [!question]- State the three requirements for a correct critical-section solution.
> 1. **Mutual exclusion** — if process Pᵢ is in its critical section, no other process may be in theirs simultaneously
> 2. **Progress** — if no process is in its critical section and some processes wish to enter, the selection cannot be postponed indefinitely
> 3. **Bounded waiting** — a bound must exist on how many times other processes can enter before a waiting process is admitted (prevents starvation)

> [!question]- How does test_and_set work? What is its weakness?
> ```c
> boolean test_and_set(boolean *target) {
>     boolean rv = *target;
>     *target = true;   // atomically set to true
>     return rv;        // return old value
> }
> // Usage: while (test_and_set(&lock));  // spin until lock was false
> ```
> If `lock` is false, `test_and_set` returns false (process enters critical section) and sets lock to true.
> **Weakness**: always writes to the lock variable — even when the lock is already held — causing **cache invalidation** on every spin across all cores.

> [!question]- How does compare_and_swap differ from test_and_set? Why is it preferred?
> ```c
> int compare_and_swap(int *value, int expected, int new_value) {
>     int temp = *value;
>     if (*value == expected) *value = new_value;
>     return temp;
> }
> // Usage: while (compare_and_swap(&lock, 0, 1) != 0);
> ```
> CAS **only writes if the current value matches the expected value**. When the lock is already held, spinning threads read the value without writing it → **no cache-line invalidation** → lower bus traffic on multicore systems.

---

## 4. Semaphores and the Bounded-Buffer Problem

> [!question]- What are the two semaphore operations and what do they do?
> `wait(S)`: if S > 0, decrement S; otherwise block the calling process on the semaphore's queue.
> `signal(S)`: increment S; if any process is blocked, wake one.
> Both operations are **atomic** — the OS guarantees they execute without interruption.
> - **Binary semaphore**: S ∈ {0, 1} — equivalent to a mutex lock
> - **Counting semaphore**: S ∈ 0..N — manages a pool of N identical resources

> [!question]- Describe the bounded-buffer semaphore solution. Name the three semaphores and their roles.
> ```
> mutex    = 1   → mutual exclusion for buffer access
> not_empty = 0  → count of filled slots (consumer blocks here when 0)
> not_full  = n  → count of empty slots (producer blocks here when 0)
>
> Producer:              Consumer:
>   wait(not_full)         wait(not_empty)
>   wait(mutex)            wait(mutex)
>   /* add item */         /* remove item */
>   signal(mutex)          signal(mutex)
>   signal(not_empty)      signal(not_full)
> ```
> The ordering matters: always acquire `mutex` **after** the counting semaphore to avoid deadlock.

> [!question]- What common semaphore mistakes cause deadlock or mutual-exclusion failure?
> | Mistake | Effect |
> |---------|--------|
> | `signal(mutex)` before `wait(mutex)` at exit | Multiple processes enter the critical section simultaneously |
> | `wait(mutex)` again instead of `signal(mutex)` at exit | Deadlock — mutex never released |
> | Omitting both signal and wait | No mutual exclusion whatsoever |

---

## 5. Memory Management — Paging and the TLB

> [!question]- How does paging translate a logical address to a physical address?
> The logical address is split into a **page number (p)** and a **page offset (d)**.
> `p` indexes the **page table** to obtain the **frame number (f)**.
> The physical address = `[f | d]`.
> Page size is always a power of 2; if logical space = 2ᵐ and page size = 2ⁿ, then p uses (m−n) bits and d uses n bits.
> Paging **eliminates external fragmentation** but introduces **internal fragmentation** (average ½ page wasted per process).

> [!question]- TLB: state the EAT formula and work a numeric example.
> The **Translation Look-aside Buffer** is a small associative cache of recent page→frame mappings.
> ```
> EAT = hit_ratio × memory_access + (1 − hit_ratio) × 2 × memory_access
> ```
> The factor of 2 in the miss path accounts for: (1) reading the page table from memory, then (2) reading the actual data.
> *Worked example*: hit ratio = 99%, memory access = 10 ns.
> EAT = 0.99 × 10 + 0.01 × 20 = 9.9 + 0.2 = **10.1 ns** — only 1% overhead.
> TLBs store **ASIDs** (Address Space IDs) so multiple processes' entries coexist without flushing on every context switch.

---

## 6. Virtual Memory and Demand Paging

> [!question]- State the six steps of page fault handling in order.
> 1. Reference to an invalid page causes a **trap** to the OS (page fault interrupt)
> 2. OS checks its internal table: if the reference is truly invalid → terminate process; if valid but not resident → continue
> 3. OS finds a **free frame** (or selects a victim via a replacement algorithm)
> 4. OS schedules a **disk read** to load the required page into the free frame
> 5. OS updates the **page table**: set the valid bit to `v`, record the frame number
> 6. OS **restarts the faulting instruction** — the process continues as if no fault occurred

> [!question]- Compare the three main page replacement algorithms.
> | Algorithm | Mechanism | Anomaly / Note |
> |-----------|-----------|----------------|
> | **FIFO** | Evict the oldest page (arrival order) | **Belady's anomaly** — adding more frames can *increase* page faults |
> | **OPT** | Evict the page not needed for the longest time in future | Optimal (minimum faults); requires future knowledge — benchmark only |
> | **LRU** | Evict the page least recently used | No Belady's anomaly; good in practice; needs hardware support (counter or linked list) |
> **LRU approximations** (hardware reference bit):
> - **Second-chance (clock)**: if ref bit = 1, clear and skip; if ref bit = 0, evict
> - **Enhanced second-chance**: use (reference, modify) pairs; prefer (0,0) — not used, not dirty

> [!question]- What is thrashing and how does the working-set model prevent it?
> **Thrashing**: a process spends more time servicing page faults than executing because it lacks enough frames to hold its active pages.
> **Cause**: total size of all process localities exceeds available physical memory.
> **Working-set model**: WSSᵢ(Δ) = set of pages referenced in the last Δ accesses (the locality).
> **D = Σ WSSᵢ** ≈ total frames currently needed.
> **Policy**: if D > total frames, suspend one process until D ≤ total frames.
> - Δ too small → misses the current locality
> - Δ too large → spans multiple localities

---

## 7. Deadlocks

> [!question]- State the four necessary conditions for deadlock.
> All four must hold **simultaneously**:
> 1. **Mutual exclusion** — at least one resource held in non-shareable mode
> 2. **Hold and wait** — a process holds at least one resource while waiting for additional ones held by others
> 3. **No preemption** — resources cannot be forcibly taken; they must be voluntarily released
> 4. **Circular wait** — a cycle exists: P₀ waits for a resource held by P₁, …, Pₙ waits for a resource held by P₀

> [!question]- Banker's Algorithm: state the safety algorithm steps.
> Initialise `Work = Available`; `Finish[i] = false` for all i.
> ```
> Loop:
>   Find i where: Finish[i] == false  AND  Need[i] ≤ Work
>   If found:
>     Work = Work + Allocation[i]   (process finishes, returns resources)
>     Finish[i] = true
>   Else if all Finish[i] == true → state is SAFE
>   Else → state is UNSAFE (deadlock possible)
> ```
> Time complexity: **O(m × n²)** where m = resource types, n = processes.
> A **safe state** guarantees that a safe sequence exists — an ordering in which every process can eventually obtain all the resources it needs.

> [!question]- How does deadlock prevention differ from deadlock avoidance?
> **Prevention** statically removes one of the four necessary conditions from the system design.
> - Most practical: impose a **total ordering** on resource types and require processes to request in increasing order (eliminates circular wait)
>
> **Avoidance** dynamically inspects each resource request and refuses it if granting would leave the system in an **unsafe state** (Banker's algorithm).
> - Requires processes to declare their **maximum** resource needs in advance

> [!question]- How is deadlock detected using a wait-for graph?
> For single-instance resources: derive the wait-for graph by removing resource nodes from the resource-allocation graph. An **edge P → Q** means P waits for Q to release a resource. A **cycle in the wait-for graph = deadlock**. Cycle detection runs in **O(n²)** where n = number of processes.

---

## Quick Reference

| Topic | Formula / Rule |
|-------|----------------|
| SJF prediction | τ(n+1) = α·t(n) + (1−α)·τ(n) |
| RR max wait | (n − 1) × q ms |
| TLB EAT | h × m + (1−h) × 2m |
| Page fault EAT | (1−p) × m + p × (fault overhead) |
| Working-set demand | D = Σ WSSᵢ |
| Banker's safety | O(m × n²) |

## See Also

- [[concepts/os-processes-and-threads|Processes and Threads]]
- [[concepts/cpu-scheduling-and-synchronisation|CPU Scheduling and Synchronisation]]
- [[concepts/memory-and-virtual-memory|Memory and Virtual Memory]]
- [[concepts/deadlocks|Deadlocks]]
