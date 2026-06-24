---
type: area
status: established
title: "Operating Systems"
domain: operating-systems
source: [[sources/ICT1012-operating-systems]]
updated: 2026-05-14
tags: [area, operating-systems]
---

# Operating Systems

**Source**: ICT1012 — Dr. David Sanan & Assoc. Prof. Shang-Wei Lin, SIT. Textbook: Silberschatz et al., *Operating System Concepts* (10th Ed.)

---

## What I Know

The OS is the layer between hardware and applications. It provides process management, memory management, file systems, and synchronisation primitives. ICT1012 covers the full OS stack across 10 chapters.

**Core model**: everything ultimately runs as a process (or thread); the OS kernel arbitrates access to shared resources (CPU, memory, files, devices) and prevents conflicts.

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/os-processes-and-threads\|OS Fundamentals & Processes]] | OS roles, system calls, privilege modes, process states/PCB, IPC, threads |
| [[concepts/cpu-scheduling-and-synchronisation\|CPU Scheduling & Synchronisation]] | FCFS/SJF/RR/CFS algorithms, race conditions, mutex, semaphores |
| [[concepts/file-systems\|File Systems]] | Allocation methods (contiguous/linked/indexed), directory structures, inode |
| [[concepts/memory-and-virtual-memory\|Memory & Virtual Memory]] | Paging, TLB, demand paging, page replacement, thrashing |
| [[concepts/deadlocks\|Deadlocks]] | 4 conditions, Banker's algorithm, detection, recovery |

---

## Key Ideas

- **Process ≠ programme**: a programme is static; a process is a running instance with its own PCB, stack, heap, and address space
- **Scheduling tradeoff**: optimising for throughput (SJF) conflicts with fairness (RR); real systems use multilevel feedback queues or CFS
- **Synchronisation hierarchy**: test_and_set → mutex lock → semaphore → monitor (each adds abstraction over the previous)
- **Paging bridges ICT1011 and ICT1012**: ICT1011 establishes the hardware mechanism; ICT1012 adds the OS policy layer (TLB, demand paging, page replacement)
- **Thrashing diagnosis**: if CPU utilisation drops while paging activity spikes, the working set exceeds available frames — suspend a process

---

## Cross-Domain Connections

- [[synthesis/ict1011-ict1012-architecture-bridge|Hardware Paging → OS Virtual Memory]] — how ICT1011 paging mechanism becomes ICT1012 virtual memory policy
- [[concepts/io-and-memory-systems|I/O & Memory Systems]] (ICT1011) — hardware SRAM/DRAM/TLB that OS manages
- [[concepts/deadlocks|Deadlocks]] ↔ [[concepts/cpu-scheduling-and-synchronisation|Synchronisation]] — semaphore misuse causes deadlock

---

## Study Notes

[[learning/ict1012-operating-systems-study-notes|ICT1012 Study Notes]] — exam-prep flashcard summaries
