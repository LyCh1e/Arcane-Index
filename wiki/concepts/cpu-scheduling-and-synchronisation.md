---
type: concept
title: "CPU Scheduling and Synchronisation"
domain: operating-systems
source: [[sources/ICT1012-operating-systems]]
complexity: high
updated: 2026-05-13
tags: [concept, operating-systems, scheduling, synchronisation, semaphores, mutex, critical-section]
---

# CPU Scheduling and Synchronisation

Covers CPU scheduling algorithms and the mechanisms for preventing race conditions in concurrent processes and threads.

---

## 1. CPU Scheduling — Basic Concepts

Processes alternate between **CPU bursts** (computation) and **I/O bursts** (waiting for device):

- **I/O-bound** process: many short CPU bursts
- **CPU-bound** process: few, long CPU bursts

The short-term (CPU) scheduler selects from the **ready queue** and allocates the CPU.

**Dispatcher**: the module that actually performs the context switch, switches to user mode, and jumps to the correct location. **Dispatch latency** = time to stop one process and start another.

### Preemptive vs Non-preemptive

- **Non-preemptive**: CPU held until process terminates or blocks (cases 1 and 2 below)
- **Preemptive**: CPU can be taken away (cases 3 and 4 below)

Scheduling decisions occur when a process:
1. Switches running → waiting (non-preemptive)
2. Terminates (non-preemptive)
3. Switches running → ready (preemptive)
4. Switches waiting → ready (preemptive)

---

## 2. Scheduling Criteria

| Criterion | Goal | Description |
|-----------|------|-------------|
| CPU utilisation | Maximise | Keep CPU as busy as possible |
| Throughput | Maximise | Processes completed per time unit |
| Turnaround time | Minimise | Submission → completion |
| Waiting time | Minimise | Time spent in ready queue |
| Response time | Minimise | Request submitted → first response produced |

---

## 3. Scheduling Algorithms

### 3.1 FCFS — First-Come, First-Served

Simple FIFO queue. Non-preemptive.

**Convoy effect**: a long CPU-bound process holds up many short I/O-bound processes behind it → poor average waiting time.

| Example (P1=3, P2=3, P3=24) | Order P1,P2,P3 | Order P3,P2,P1 |
|------------------------------|----------------|----------------|
| Avg waiting time | (0+3+6)/3 = **3** | (0+24+27)/3 = **17** |

### 3.2 SJF — Shortest-Job-First

Associates each process with its estimated next CPU burst. Optimal for minimum average waiting time.

- **Non-preemptive SJF**: once started, runs to completion
- **Preemptive SJF (SRTF — Shortest-Remaining-Time-First)**: new arrival with shorter remaining burst preempts current process

**Estimating burst length** (exponential averaging):
```
τ(n+1) = α · t(n) + (1 − α) · τ(n)

where t(n)  = actual nth CPU burst
      τ(n)  = predicted nth burst
      α     = weight (commonly 0.5)
```
- α = 0: ignore recent history; α = 1: only last burst matters

### 3.3 Priority Scheduling

Each process has a priority (integer; smaller = higher priority). CPU allocated to highest-priority process.

- **Problem**: **starvation** — low-priority processes may never execute
- **Solution**: **ageing** — gradually increase the priority of long-waiting processes

### 3.4 Round Robin (RR)

Each process gets a time **quantum** q (typically 10–100 ms), then is preempted and added to the end of the ready queue.

- n processes in ready queue: each gets CPU in chunks of at most q, waiting ≤ (n−1)q
- q large → degenerates to FCFS; q too small → overhead from context switching dominates
- Better response time than SJF; typically higher average turnaround time

### 3.5 Multilevel Queue

Ready queue split into separate sub-queues (e.g., foreground interactive = RR; background batch = FCFS). Processes permanently assigned to a queue. Queues scheduled by fixed priority or time slice.

### 3.6 Multilevel Feedback Queue

Like Multilevel Queue, but **processes can move between queues** (ageing). Defined by: number of queues, per-queue scheduling algorithm, promotion/demotion rules.

**Example** (3 queues):
- Q0: RR, quantum 8 ms
- Q1: RR, quantum 16 ms
- Q2: FCFS
- New job → Q0; if not done in 8 ms → Q1; if not done in 16 ms → Q2

### 3.7 Algorithm Comparison

| Algorithm | Starvation? | Preemptive? | Good for |
|-----------|------------|------------|---------|
| FCFS | No | No | Simple, batch |
| SJF | Possible (long jobs) | No | Minimum avg wait |
| SRTF | Possible | Yes | Short jobs |
| Priority | Possible | Optional | Real-time |
| Round Robin | No | Yes | Time-sharing, fairness |
| Multilevel Feedback | Possible | Yes | General-purpose |

### 3.8 Real-Time Scheduling

- **Soft real-time**: no guarantee on when critical process will be scheduled
- **Hard real-time**: task *must* complete by its deadline

**Rate Monotonic Scheduling**: static priorities based on period — shorter period = higher priority. Optimal among static-priority algorithms. CPU utilisation bound: n(2^(1/n) − 1) → ~69% for large n.

### 3.9 Linux CFS (Completely Fair Scheduler, kernel 2.6.23+)

- Based on **virtual runtime** (`vruntime`) per task
- Default priority task: vruntime = actual runtime
- Lower priority: vruntime grows faster; higher priority: slower
- Scheduler always runs task with **lowest vruntime**
- Nice value: −20 (highest priority) to +19 (lowest) → maps to global priorities 100–139

---

## 4. Synchronisation — Race Conditions

When multiple processes/threads access shared data concurrently and the result depends on the order of execution → **race condition**.

**Example** (`counter++` and `counter--` are not atomic):
```
Producer: register1 = counter   {5}
Producer: register1 += 1         {6}
Consumer: register2 = counter   {5}   ← reads stale value
Consumer: register2 -= 1         {4}
Producer: counter = register1   {6}   ← writes 6
Consumer: counter = register2   {4}   ← overwrites with 4 ← WRONG
```

---

## 5. Critical Section Problem

A **critical section** is a code segment where shared resources are accessed. Requirements for a correct solution:

| Property | Meaning |
|----------|---------|
| **Mutual exclusion** | If process Pi is in its critical section, no other process can be in theirs |
| **Progress** | If no process is in its critical section, the selection of who enters next cannot be postponed indefinitely |
| **Bounded waiting** | A bound must exist on how many times other processes can enter before a waiting process is admitted |

---

## 6. Hardware Synchronisation

### 6.1 test_and_set

```c
boolean test_and_set(boolean *target) {
    boolean rv = *target;
    *target = true;   // atomically set to true
    return rv;        // return old value
}

// Usage:
do {
    while (test_and_set(&lock));  // spin until lock was false
    /* critical section */
    lock = false;
} while (true);
```

- Lock = false → test_and_set returns false (enter critical section) and sets lock to true
- Lock = true → test_and_set returns true (keep spinning)
- **Problem**: always writes to memory → cache invalidation overhead

### 6.2 compare_and_swap

```c
int compare_and_swap(int *value, int expected, int new_value) {
    int temp = *value;
    if (*value == expected) *value = new_value;  // only updates if still expected
    return temp;
}

// Usage:
do {
    while (compare_and_swap(&lock, 0, 1) != 0);  // enter if lock == 0
    /* critical section */
    lock = 0;
} while (true);
```

More efficient than test_and_set — only writes if the value matches expectation, reducing cache invalidation.

---

## 7. Mutex Locks

Higher-level abstraction over hardware primitives:

```c
acquire(&lock);    // spin until available (spinlock)
/* critical section */
release(&lock);
```

- **Spinlock**: CPU busy-waits — wasteful but fast for short critical sections on multicore
- **Sleep-based**: put thread to sleep instead of spinning — slower but frees CPU

```c
void acquire(int *lock) { while(test_and_set(lock)); }
void release(int *lock) { *lock = false; }
```

---

## 8. Semaphores

A semaphore S is an integer representing the count of available resources. Two atomic operations:

```c
wait(S)   { while (S == 0) /* block */; S--; }
signal(S) { S++; }
```

In practice, processes **block** (sleep) rather than busy-wait when S = 0. The semaphore maintains a waiting queue; `signal()` wakes one blocked process.

### Types

| Type | Range | Use |
|------|-------|-----|
| **Binary semaphore** | 0 or 1 | Equivalent to mutex lock (without spinlock) |
| **Counting semaphore** | 0 to N | Manage N instances of a resource |

### Synchronisation Pattern

To ensure S1 executes before S2:
```c
// Initialize synch = 0
P1: S1; signal(synch);
P2: wait(synch); S2;
```

### Bounded-Buffer Solution

```
mutex = 1     (mutual exclusion for buffer access)
not_empty = 0 (count of filled slots; consumer waits here)
not_full = n  (count of empty slots; producer waits here)

Producer:                     Consumer:
  wait(not_full)               wait(not_empty)
  wait(mutex)                  wait(mutex)
  /* add to buffer */          /* remove from buffer */
  signal(mutex)                signal(mutex)
  signal(not_empty)            signal(not_full)
```

### Problems with Semaphores

| Mistake | Effect |
|---------|--------|
| `signal(mutex)` before `wait(mutex)` at exit | Multiple processes enter critical section |
| `wait(mutex)` instead of `signal(mutex)` at exit | Eventually deadlocks — no one can enter |
| Omit both | No mutual exclusion |

**Deadlock**: P0 holds S, waits for Q; P1 holds Q, waits for S → circular wait → neither proceeds.

**Starvation**: process permanently blocked in semaphore queue.

**Priority inversion**: low-priority process holds resource needed by high-priority process.
- Solution: **priority-inheritance protocol** — low-priority process temporarily inherits the higher priority.

---

## Summary

```
Scheduling: FCFS (convoy) → SJF/SRTF (optimal, needs prediction) →
            Priority (starvation → aging) → RR (fair, time-sharing) →
            Multilevel Feedback (adaptive, general-purpose) → CFS (Linux)

Synchronisation: Race condition → Critical section (ME + Progress + Bounded)
  → Hardware: test_and_set / compare_and_swap
  → Mutex lock (spinlock or sleep)
  → Semaphore (binary = mutex; counting = resource pool)
  → Classic: Bounded-buffer uses mutex + not_empty + not_full
```

## See Also

- [[concepts/os-processes-and-threads|OS Fundamentals, Processes, and Threads]] — process states, PCB, schedulers
- [[concepts/deadlocks|Deadlocks]] — when semaphore misuse leads to circular waiting
- [[sources/ICT1012-operating-systems|ICT1012 Source Page]]
