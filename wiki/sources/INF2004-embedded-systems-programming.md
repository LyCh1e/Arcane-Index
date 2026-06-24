---
address: c-000053
type: source
status: established
title: "INF2004 Embedded Systems Programming"
course: INF2004
domain: embedded-systems
date_ingested: 2026-05-23
tags: [source, embedded-systems, inf2004]
---

# INF2004 Embedded Systems Programming

Singapore Institute of Technology — module covering embedded software design and development on the Raspberry Pi Pico (RP2040).

## Module Structure

| Week | Topic | Slides |
|------|-------|--------|
| W0 | Module overview; Raspberry Pi Pico platform | — |
| W1 | Introduction to Embedded Systems | — |
| W2 | Requirements for Embedded Systems | — |
| W3/W4 | Interrupt Principles | 21 |
| W3/W4 | Timer & PWM | 18 |
| W5.1 | Embedded Operating System (RTOS) | 28 |
| W5.2 | Finite State Machine | 6 |
| W6.1 | Testing | 28 |
| W6.2 | Sensor Fusion | 41 |
| W8 | Optimisations | 20 |
| W10 | Edge Computing & TinyML | 21 |

## Concept Pages

| Concept | Address |
|---------|---------|
| [[concepts/embedded-systems-fundamentals\|Embedded Systems Fundamentals]] | c-000054 |
| [[concepts/embedded-io-and-interrupts\|Embedded I/O and Interrupts]] | c-000055 |
| [[concepts/embedded-timers-and-rtos\|Timers, PWM, RTOS, and FSM]] | c-000056 |
| [[concepts/embedded-testing-and-optimisation\|Embedded Testing and Optimisation]] | c-000057 |
| [[concepts/embedded-sensor-fusion-and-edge\|Sensor Fusion and Edge Computing]] | c-000058 |

## Cross-References to Existing Concepts

| Concept | Relevance |
|---------|-----------|
| [[concepts/c-programming-fundamentals\|C Programming Fundamentals]] | Embedded systems are predominantly programmed in C |
| [[concepts/c-pointers-memory-and-data-structures\|C Pointers, Memory & Data Structures]] | Pointer-heavy embedded code; manual memory management |
| [[concepts/os-processes-and-threads\|OS Fundamentals, Processes, and Threads]] | RTOS parallels general OS process model |
| [[concepts/cpu-scheduling-and-synchronisation\|CPU Scheduling and Synchronisation]] | Embedded scheduling algorithms (RMS, EDF, LST) |
| [[concepts/sdlc-models\|SDLC Models]] | V-Model is the dominant SDLC for embedded |
| [[concepts/software-testing-fundamentals\|Software Testing Fundamentals]] | Unit/integration/system testing with hardware-specific constraints |

## Key Hardware Platform

**Raspberry Pi Pico** — RP2040 dual-core ARM Cortex-M0+ @ 133 MHz, 264 KB SRAM, 2 MB flash, 30 GPIO, 2× UART, 2× SPI, 2× I2C, 16× PWM, ADC, PIO state machines.
