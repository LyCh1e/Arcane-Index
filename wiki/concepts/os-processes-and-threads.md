---
type: concept
title: "OS Fundamentals, Processes, and Threads"
domain: operating-systems
source: [[sources/ICT1012-operating-systems]]
complexity: high
updated: 2026-05-13
tags: [concept, operating-systems, processes, threads, ipc, system-calls]
---

# OS Fundamentals, Processes, and Threads

Covers the OS definition and role, system calls and privilege modes, OS design approaches, process model, process communication, and threads.

---

## 1. What is an Operating System?

An OS is a programme that acts as an **intermediary** between users and hardware. Its roles:

| Role | Description |
|------|-------------|
| **Hardware abstraction** | Provides uniform APIs for CPU, memory, I/O devices |
| **Resource allocator** | Decides between conflicting requests (e.g., two processes needing the CPU) |
| **Synchronisation provider** | Prevents race conditions between concurrent applications |
| **Communication provider** | Offers pipes, shared memory, message passing |
| **Protection & security** | Prevents unauthorised access between processes |

**Kernel**: the one programme running at all times. Everything else is either a system programme (ships with the OS) or an application programme.

**Bootstrap**: a programme stored in ROM/firmware that loads and starts the OS kernel on power-up.

---

## 2. Computer System Organisation

- CPU and device controllers share a **common bus** connected to main memory
- Each device controller has a **local buffer**; the CPU moves data between buffers and main memory
- Device controllers use **interrupts** to notify the CPU of completion
- **Device drivers** provide a uniform interface to device controllers

### DMA (Direct Memory Access)

For high-speed devices, the device controller transfers **entire blocks** directly to/from main memory without CPU intervention per byte. Only **one interrupt per block** is generated.

### Interrupt Cycle

```
Fetch → Execute → Check interrupts
               ↓ (interrupt pending + enabled)
         Save context (registers + PC → stack)
         Jump to ISR (interrupt vector table)
         RETI → restore context
```

---

## 3. System Calls

A **system call** is the programming interface to OS services. Typically written in C/C++, invoked via a specific interrupt or `syscall` instruction.

### Mechanism

- **Old x86**: `int 0x80` (Linux) or `int 0x2E` (Windows) — CPU jumps to handler via interrupt table, then checks register for call number
- **Modern**: `syscall` instruction — CPU jumps directly to specific handler; RAX = call number, RCX/RDX/R8… = arguments

### APIs

Programs access system calls via high-level **Application Programming Interfaces (APIs)**: Win32 (Windows), POSIX (Unix/Linux/macOS), Java API (JVM).

### Parameter Passing Methods

1. **Registers** — simplest, limited by number of registers
2. **Memory block** — address of a parameter block passed in a register (Linux, Solaris)
3. **Stack** — parameters pushed by programme, popped by OS; unlimited number of arguments

### Privilege Modes

System calls can execute **privileged ISA instructions** that user mode cannot:
- Load/store descriptor tables (LGDT, LIDT)
- Modify control registers (MOV CRx)
- Halt processor (HLT)
- Virtualisation (VMRUN)

The CPU uses a **Current Privilege Level (CPL)** bit in the CS register. During a system call, CPL → 0 (kernel); on return, CPL → 1 (user).

---

## 4. OS Design Approaches

| Approach | Description | Examples |
|----------|-------------|---------|
| **Layered** | Each layer uses only services from layers below | Linux, macOS, Windows |
| **Modular** | Loadable kernel modules; each module talks via known interfaces; flexible | Linux, Solaris, Windows |
| **Microkernel** | Minimal kernel; most services run in user space; communicate via message passing; more reliable/secure but slower | Mach (basis of Darwin/macOS) |
| **Monolithic** | Everything in kernel space; fast; common on UNIX | Linux kernel |
| **Hybrid** | Microkernel + extensions in user space | Windows NT, macOS Darwin (Mach + BSD) |

---

## 5. Process Concept

A **process** is a programme in execution. A programme (passive, on disk) becomes a process when loaded into memory.

### Process Memory Layout

```
High address
  Stack     ← grows downward (function params, return addrs, local vars)
  ↓    ↑
  Heap      ← grows upward (malloc/new — dynamic allocation)
  BSS       ← uninitialised global and static variables
  Data      ← initialised global and static variables
  Text      ← compiled programme code (read-only)
Low address
```

Stack and heap grow towards each other — meeting causes stack overflow or allocation failure.

### Process States

```
                    ┌──────────┐
                    │   new    │
                    └────┬─────┘
                  admitted│
                    ┌────▼─────┐    scheduler dispatch    ┌──────────┐
          ┌────────►│  ready   │──────────────────────────►│ running  │
          │         └─────▲────┘                          └────┬─────┘
          │         interrupt│     ◄──────────────────────────  │
          │                  │            I/O or event wait     │
    I/O done         ┌───────┴─────┐◄─────────────────────────  │
                     │   waiting   │                             │
                     └─────────────┘                      ┌─────▼────┐
                                                           │terminated│
                                                           └──────────┘
```

Also: **waiting swapped** — process was swapped out whilst waiting for I/O.

### Process Control Block (PCB)

The OS maintains one PCB per process, containing:
- Process state, process ID (PID)
- Programme counter, CPU registers
- CPU scheduling information (priority, queue pointers)
- Memory management information
- Accounting information (CPU used, time limits)
- I/O status (devices allocated, open files)
- IPC structures (shared memory areas, message queues)

### Schedulers

| Scheduler | Invocation | Purpose |
|-----------|-----------|---------|
| **Long-term** (job) | Infrequently (seconds/minutes) | Selects which processes enter the ready queue; controls degree of multiprogramming; balances CPU-bound vs I/O-bound |
| **Medium-term** | When memory pressure rises | Swaps processes out to disk and back; reduces multiprogramming temporarily |
| **Short-term** (CPU) | Very frequently (ms) | Selects which ready process runs next; must be fast |

**Context switch**: saving and restoring process state when switching the CPU between processes — overhead with no productive work.

---

## 6. Process Creation and Termination (UNIX)

```c
pid = fork();      // create child (duplicate of parent)
                   // fork returns 0 to child, child's PID to parent
exec("/bin/ls");   // replace process memory with new programme
wait(NULL);        // parent waits for child to terminate
exit(0);           // child terminates, notifies parent
```

- **Process tree**: processes form a parent–child hierarchy; Linux root is `systemd` (PID 1)
- **Zombie**: child terminated, parent hasn't called `wait()` — PCB kept until parent reads exit status
- **Orphan**: parent terminated before child — in Linux, orphans are adopted by `init`/`systemd`

---

## 7. Interprocess Communication (IPC)

Cooperating processes need to share data. Two mechanisms:

### 7.1 Shared Memory

Processes map the same physical memory into their address space. Fast — no kernel involvement after setup.

| System Call | Purpose |
|-------------|---------|
| `mmap()` + `MAP_SHARED` | Create shared memory region |
| `shm_open()` / `shm_unlink()` | POSIX shared memory objects |
| `ftruncate()` | Set size of shared memory |
| `munmap()` | Release mapping |

### 7.2 Message Passing

Processes communicate without shared variables. The OS provides `send(message)` and `receive(message)`.

| System Call | Purpose |
|-------------|---------|
| `mq_open()` | Create/open message queue |
| `mq_send()` / `mq_receive()` | Send / receive |
| `mq_close()` / `mq_unlink()` | Close / destroy |

**Synchronisation modes**:
- **Blocking** (synchronous): sender blocks until message is received; receiver blocks until message available (rendezvous)
- **Non-blocking** (asynchronous): sender continues immediately; receiver gets message or null

**Buffer capacity**:
| Capacity | Sender behaviour |
|----------|-----------------|
| Zero | Both must synchronise (rendezvous) |
| Bounded (n) | Sender waits if full; receiver waits if empty |
| Unbounded | Sender never waits |

---

## 8. Threads

A **thread** is the basic unit of CPU utilisation. Threads within a process share code, data, and files but have their own registers and stack.

### Why Threads?

| Benefit | Explanation |
|---------|-------------|
| **Economy** | Thread creation cheaper than process creation; context switch cheaper than process switch |
| **Resource sharing** | Threads share the same address space — no need for IPC for internal parallelism |
| **Scalability** | Threads can run in parallel on multiple cores |
| **Responsiveness** | UI thread stays responsive while background thread does work |

### Concurrency vs Parallelism

- **Concurrency**: multiple tasks making progress on a single core (interleaved by scheduler)
- **Parallelism**: multiple tasks running simultaneously on multiple cores

### User Threads vs Kernel Threads

| | User Threads | Kernel Threads |
|--|-------------|---------------|
| Management | Thread library (user space) | OS kernel |
| Examples | POSIX Pthreads (user-level) | Windows threads, Linux tasks |
| Mapping | Must be mapped to kernel threads | Each is a schedulable unit |

### Threading Models

| Model | Description | Drawback |
|-------|-------------|---------|
| **Many-to-One** | Many user threads → 1 kernel thread | One blocking call blocks all; no parallelism |
| **One-to-One** | Each user thread → 1 kernel thread | Most common (Linux, Windows); overhead creating kernel threads |
| **Many-to-Many** | Many user threads → many kernel threads | Flexible; OS can create enough kernel threads |
| **Two-Level** | M:M plus ability to bind a user thread to a specific kernel thread | — |

### Pthreads API (POSIX)

```c
pthread_create(&tid, &attr, runner, argv[1]);  // create thread
pthread_join(tid, NULL);                        // wait for thread
pthread_exit(0);                                // terminate self
pthread_cancel(tid);                            // request cancellation
pthread_detach(tid);                            // release resources after exit
```

### Threading Issues

| Issue | Detail |
|-------|--------|
| `fork()` semantics | Does it duplicate all threads or only the calling thread? Some UNIXes have two versions |
| Signal handling | Where to deliver signal in multithreaded process? (per-thread, all threads, or specific thread) |
| Thread cancellation | Asynchronous (immediate) vs deferred (check at cancellation points) |
| Thread-Local Storage (TLS) | Per-thread data visible across function calls; unlike local variables |
| Thread safety | Thread-safe (reentrant/atomic), conditionally safe, or unsafe |

### Linux Threads

Linux uses `clone()` system call instead of `fork()` — allows sharing of address space, file descriptors, signal handlers. Linux calls threads **tasks**; `task_struct` points to shared or unique data structures.

---

## See Also

- [[concepts/cpu-scheduling-and-synchronisation|CPU Scheduling and Synchronisation]] — scheduling algorithms, race conditions, semaphores
- [[concepts/memory-and-virtual-memory|Memory Management and Virtual Memory]] — paging, TLB, demand paging
- [[concepts/io-and-memory-systems|I/O Interfacing and Memory Systems]] (ICT1011) — hardware-level I/O and memory
- [[sources/ICT1012-operating-systems|ICT1012 Source Page]]
