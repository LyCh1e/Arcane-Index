---
type: source
status: established
title: "ICT1011 Computer Organisation and Architecture"
course: ICT1011
domain: computer-architecture
ingested: 2026-05-13
tags: [source, computer-architecture, msp430, assembly, memory-management]
---

# ICT1011 Computer Organisation and Architecture

## Source Details

| Field | Value |
|-------|-------|
| File | `raw/ICT1011 Computer Organisation Architecture Notes.md` |
| Format | OCR'd slide deck — 10 chapters, ~15,297 lines |
| Authors | Steven Wong & Xin Lou (Singapore Institute of Technology, ©2024) |
| Module | ICT1011 — Computer Organisation and Architecture |
| Assessment | Lab quizzes 30%, Team Project 20%, Quizzes 20%, Exam 30% |

## Chapter Map

| Chapter | Title | Key Topics |
|---------|-------|-----------|
| 0 | Module Overview | Computer architecture vs organisation, module structure |
| 1 | Fundamentals of Computing | Von Neumann, computer classes, 3 operations, memory hierarchy |
| 3 | Instruction Set Architecture | MSP430 registers, memory map, addressing modes, instruction formats |
| 4 | Assembly Language | Syntax, directives, 2-pass assembly |
| 5 | Executable Instructions | MOV, arithmetic, logical, control flow, emulated instructions |
| 6 | Modular Programming | CALL/RET, stack, parameter passing, local variables |
| 7 | I/O Interfacing | Serial/parallel comms, RS-232, polled/interrupt I/O, Bluetooth |
| 8 | Secondary Memory | HDD structure, RAID 0/1/10 |
| 9 | Primary Memory Subsystems | Bus interconnect, SRAM, DRAM, ROM/Flash |
| 10 | Memory Management | Swapping, partitioning, paging |

## Concept Pages Created

| Page | Chapters Covered |
|------|-----------------|
| [[concepts/computer-architecture-fundamentals\|Computer Architecture Fundamentals]] | 0, 1, 3 |
| [[concepts/assembly-programming-msp430\|Assembly Programming (MSP430)]] | 4, 5, 6 |
| [[concepts/io-and-memory-systems\|I/O Interfacing and Memory Systems]] | 7, 8, 9, 10 |

## Key Themes

The module uses the **MSP430 16-bit RISC microcontroller** as a concrete vehicle for all architecture and assembly topics. The pedagogical arc runs: what a computer is → how instructions are encoded → how to write assembly → how the CPU communicates with the outside world → how memory is organised.

The final chapter (10) on Memory Management bridges into Operating Systems (ICT1007), deliberately ending with paging as the conceptual handover.
