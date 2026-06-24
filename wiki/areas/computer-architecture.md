---
type: area
status: established
title: "Computer Architecture"
domain: computer-architecture
source: [[sources/ICT1011-computer-organisation-architecture]]
updated: 2026-05-15
tags: [area, computer-architecture]
---

# Computer Architecture

**Source**: ICT1011 — Computer Organisation & Architecture, SIT.

---

## What I Know

How physical hardware is organised and how it executes instructions. ICT1011 covers the Von Neumann model, the MSP430 instruction set, the memory hierarchy, and I/O systems — establishing the hardware foundation on which operating systems and software run.

---

## Concept Pages

| Page | What It Covers |
|------|---------------|
| [[concepts/computer-architecture-fundamentals\|Computer Architecture Fundamentals]] | Von Neumann model, fetch-decode-execute cycle, CPU registers, ALU, clock cycles, CPI, MIPS; MSP430 register set (R0–R15), addressing modes, instruction formats |
| [[concepts/assembly-programming-msp430\|Assembly Programming (MSP430)]] | MSP430 instruction set (MOV/ADD/SUB/CMP/JMP family), byte vs word operations, stack (PUSH/POP/CALL/RET), subroutine conventions, interrupt vectors, low-power modes |
| [[concepts/io-and-memory-systems\|I/O & Memory Systems]] | Memory hierarchy (registers→cache→RAM→disk), locality of reference, cache mapping (direct/associative/set-associative), cache eviction policies, memory-mapped I/O vs port-mapped I/O, DMA, interrupts vs polling |

---

## Key Ideas

- **Von Neumann bottleneck**: a single shared bus for data and instructions forces sequential fetch-execute; modern CPUs mitigate this with caches, pipelines, and out-of-order execution
- **MSP430 addressing modes**: Register, Indexed (offset + register), Symbolic (PC-relative), Absolute, Indirect, Indirect Auto-increment — the auto-increment mode is the MSP430's efficient substitute for a separate PUSH instruction
- **Cache hit rate dominates performance**: a 1% miss increase from 95% to 96% hit rate has enormous speed impact because a cache miss triggers a full RAM access (~100× slower than L1 cache)
- **Interrupts vs polling**: interrupts are efficient for infrequent, unpredictable events (CPU does useful work between events); polling wastes cycles but has lower latency for high-frequency events
- **DMA offloads the CPU**: DMA controller transfers data directly between I/O device and RAM; CPU only handles start and end interrupts, not every byte

---

## Cross-Domain Connections

- [[synthesis/ict1011-ict1012-architecture-bridge|Computer Architecture → OS]] — the hardware primitives ICT1011 establishes (registers, page tables, interrupts) are exactly the mechanisms ICT1012 exploits for scheduling, virtual memory, and process isolation
- [[concepts/os-processes-and-threads|Processes & Threads]] — context switching saves and restores the CPU register set defined in ICT1011
- [[concepts/memory-and-virtual-memory|Virtual Memory]] — the physical memory model and address bus from ICT1011 is what virtual memory maps onto
- [[concepts/algorithm-complexity|Algorithm Complexity]] — hardware performance (cache, pipeline) determines the constant factors hidden inside Big-Oh notation
