---
type: source
title: "ICT1012 Operating Systems"
course: ICT1012
domain: operating-systems
ingested: 2026-05-13
tags: [source, operating-systems, processes, scheduling, synchronisation, memory, file-systems, deadlocks]
---

# ICT1012 Operating Systems

## Source Details

| Field | Value |
|-------|-------|
| File | `raw/ICT1012 Operating Systems Notes.md` |
| Format | Compiled lecture notes from all slides — 10 chapters, ~7,856 lines |
| Authors | Dr. David Sanan & Assoc. Prof. Shang-Wei Lin (Singapore Institute of Technology) |
| Textbook | A. Silberschatz, P. Galvin, G. Gagne, *Operating System Concepts* (10th Ed.), Wiley, 2019 |
| Assessment | Labs 30%, Assignment 35%, Exam 35% |

## Chapter Map

| Chapter | Title | Key Topics |
|---------|-------|-----------|
| 1 | Introduction to OSes | OS role, hardware abstraction, interrupts, DMA, bootstrap, kernel |
| 2 | System Calls | Syscall mechanism, privilege modes, APIs (POSIX/Win32), OS design (layered/modular/microkernel/monolithic) |
| 3 | Processes | Process concept, states, PCB, memory layout, schedulers, IPC (shared memory + message passing) |
| 4 | Threads & Concurrency | Thread vs process, user/kernel threads, models (1:1, M:1, M:M), Pthreads, threading issues |
| 5 | CPU Scheduling | Criteria, FCFS, SJF/SRTF, Priority, RR, Multilevel Queue, Multilevel Feedback Queue, CFS, Real-Time |
| 6 | Synchronisation | Race conditions, critical section, test_and_set, compare_and_swap, mutex, semaphores, bounded-buffer |
| 7 | File Systems Interface | File concept, access methods, directory structures, Unix permissions |
| 7b | File System Implementation | Layered FS, FCB/inode, allocation methods (contiguous/linked/indexed), free-space management |
| 8 | Main Memory | Address binding, MMU, paging, TLB, page table structures |
| 9 | Virtual Memory | Demand paging, page replacement algorithms, frame allocation, thrashing, working set |
| 10 | Deadlocks | 4 conditions, resource allocation graph, prevention, avoidance (Banker's), detection, recovery |

## Concept Pages Created

| Page | Chapters Covered |
|------|-----------------|
| [[concepts/os-processes-and-threads\|OS Fundamentals, Processes, and Threads]] | 1, 2, 3, 4 |
| [[concepts/cpu-scheduling-and-synchronisation\|CPU Scheduling and Synchronisation]] | 5, 6 |
| [[concepts/file-systems\|File Systems (Interface and Implementation)]] | 7, 7b |
| [[concepts/memory-and-virtual-memory\|Memory Management and Virtual Memory]] | 8, 9 |
| [[concepts/deadlocks\|Deadlocks]] | 10 |

## Relationship to ICT1011

ICT1011 (Computer Organisation) ends with memory management (swapping, partitioning, paging at the hardware level). ICT1012 (Operating Systems) picks up exactly there — Chapter 8 revisits paging from the OS perspective (TLB, page table structures) and Chapter 9 extends it to virtual memory and demand paging. This module is the direct continuation of ICT1011.
