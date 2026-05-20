---
type: concept
title: "Computer Architecture Fundamentals"
domain: computer-architecture
source: [[sources/ICT1011-computer-organisation-architecture]]
complexity: medium
updated: 2026-05-13
tags: [concept, computer-architecture, von-neumann, msp430, isa]
status: established
created: 2026-05-13
---

# Computer Architecture Fundamentals

## 1. Architecture vs Organisation

**Computer Architecture** — the attributes visible to the programmer: instruction set, addressing modes, data types, I/O mechanisms.

**Computer Organisation** — the operational units that implement the architecture: control signals, memory technology, bus design. Two computers can share the same architecture (same ISA) but differ in organisation (e.g., different cache implementations).

---

## 2. Von Neumann Architecture

The **stored-program concept**: both instructions and data reside in the same memory. The CPU fetches, decodes, and executes instructions in a repeating cycle.

```
┌──────────┐  Data Bus   ┌──────────────┐
│   CPU    │◄───────────►│    Memory    │
│ (ALU +   │  Address Bus│  (programs + │
│ Control) │────────────►│    data)     │
└──────────┘ Control Bus └──────────────┘
       │                        │
       └──────── I/O Devices ───┘
```

Key property: a **common bus** connects CPU, memory, and I/O — this is both the elegance and the bottleneck (Von Neumann bottleneck: memory bandwidth limits CPU throughput).

**Fetch–Decode–Execute cycle:**
1. Fetch instruction from memory at address in PC
2. Decode the opcode
3. Execute (may read/write memory, update registers)
4. Update PC → repeat

---

## 3. Computer Classes

| Class | Characteristics | Examples |
|-------|----------------|---------|
| Supercomputer | Thousands of processors, massively parallel, scientific HPC | Frontier, Summit |
| Mainframe | High-volume transaction processing, high reliability | IBM z-series |
| Minicomputer | Mid-range, multi-user (historical term) | PDP-11 |
| Microcomputer | Single CPU on chip, desktop/laptop | Intel x86, ARM Cortex-A |
| Embedded/SoC | Application-specific, constrained power/size | MSP430, Arduino, STM32 |

---

## 4. The Three Basic Computer Operations

Every computer operation is one of three types:

| Operation | Description | Example |
|-----------|-------------|---------|
| **Store** | Place data into memory/register | MOV #5, R4 |
| **Transform** | Arithmetic or logical operation | ADD R4, R5 |
| **Transfer** | Move data between locations | MOV R4, R5 or I/O |

---

## 5. Memory Hierarchy

Faster memory is smaller and more expensive. The hierarchy exploits **locality of reference** (temporal: recently used data will be used again; spatial: nearby data will be used).

```
   Speed ▲                         Size ▲
   Cost  ▲                         Cost ▼
         │
  Registers (< 1ns, bytes — on-chip)
         │
   Cache (8–35ns, KB–MB — SRAM)
         │
  Main Memory (20–100ns, GB — DRAM)
         │
 Secondary Memory (5–20ms, TB — HDD/SSD)
```

- **Registers**: inside the CPU, fastest, very few (MSP430 has 16)
- **Cache**: SRAM-based, bridges CPU–main memory speed gap; L1/L2/L3 levels
- **Main Memory (RAM)**: DRAM-based, volatile
- **Secondary Memory**: non-volatile, persistent (HDD, SSD, Flash)

**Volatile vs non-volatile**: RAM loses contents when power is removed; ROM/Flash retains them.

---

## 6. Clock and Reset

**Clock**: a periodic signal that synchronises all CPU operations. All state changes happen on the clock edge. Higher clock frequency → more instructions per second, but also more power consumption and heat.

**Reset**: forces all registers and the Program Counter (PC) to known initial values (PC → 0 in most architectures). Ensures deterministic startup after power-on or watchdog timeout.

---

## 7. The MSP430 Microcontroller

Texas Instruments' **MSP430** is a 16-bit RISC MCU used throughout this module as the teaching platform.

- **Word size**: 16 bits
- **Instruction set**: 27 core instructions (RISC philosophy: few, orthogonal instructions)
- **Addressing modes**: 7
- **Registers**: 16 × 16-bit

### 7.1 Registers

| Register | Name | Role |
|----------|------|------|
| R0 | PC — Program Counter | Address of next instruction to fetch |
| R1 | SP — Stack Pointer | Top of stack (pre-decrement push, post-increment pop) |
| R2 | SR / CG1 — Status Register | Condition flags: N (negative), Z (zero), C (carry), V (overflow); also GIE (global interrupt enable) and low-power mode bits |
| R3 | CG2 — Constant Generator | Hard-wired constants (0, 1, 2, −1, 4, 8) — saves instruction bytes |
| R4–R15 | General-Purpose Registers | Available for data, address calculations, parameter passing |

### 7.2 Status Register (SR) Flags

| Flag | Set When |
|------|---------|
| N (Negative) | Result's MSB is 1 (signed negative) |
| Z (Zero) | Result is 0 |
| C (Carry) | Unsigned overflow / borrow-out of MSB |
| V (oVerflow) | Signed overflow (sign of result is wrong) |

### 7.3 Memory Map

| Address Range | Contents |
|--------------|---------|
| 0x0000 – 0x01FF | 8-bit peripheral registers |
| 0x0200 – 0x09FF | 16-bit peripheral registers |
| 0x2400 | Start of RAM |
| 0x4400 | Start of Flash (program code) |
| 0xFF80 – 0xFFFF | Interrupt vector table |

**Little-endian**: the low byte of a 16-bit word is stored at the lower (even) address; the high byte at the higher (odd) address.

---

## 8. Instruction Set Architecture (ISA) — MSP430

### 8.1 Instruction Formats

| Format | Operands | Bits | Usage |
|--------|----------|------|-------|
| Format I | Double operand (src + dst) | 16-bit | MOV, ADD, SUB, AND, XOR, … |
| Format II | Single operand (dst only) | 16-bit | RRC, SWPB, RRA, SXT, PUSH, CALL, RETI |
| Format III | Jump (10-bit signed offset + condition) | 16-bit | JEQ/JZ, JNE/JNZ, JC, JNC, JN, JGE, JL, JMP |

Jump offset is relative to PC (after fetch). Range: ±512 words.

### 8.2 Addressing Modes

| Mode | Syntax | Description |
|------|--------|-------------|
| Register | `Rn` | Operand is content of register Rn |
| Indexed | `x(Rn)` | EA = Rn + 16-bit offset x (stored in next word) |
| Indirect Register | `@Rn` | EA = content of Rn (no increment) |
| Indirect Auto-increment | `@Rn+` | EA = Rn, then Rn += 1 or 2 (byte/word) |
| Symbolic (PC-relative) | `label` | EA = PC + offset (operand in next word) |
| Absolute | `&label` | EA = absolute address (operand in next word) |
| Immediate | `#n` | Operand is literal n (stored in next word) |

> Immediate mode uses `@PC+` internally — the PC is the source register and auto-increments past the constant.

---

## Summary Diagram

```
Computer Architecture
       │
 ┌─────┴──────┐
 │ Von Neumann │  ← stored-program concept, common bus
 └─────┬──────┘
       │
 ┌─────┴───────┐
 │  ISA Layer  │  ← instruction set, registers, addressing, formats
 └─────┬───────┘
       │
 ┌─────┴────────────┐
 │  MSP430 RISC MCU │  ← 16-bit, 27 instructions, 7 modes, 16 registers
 └──────────────────┘
```

## See Also

- [[concepts/assembly-programming-msp430|Assembly Programming (MSP430)]] — assembly syntax, instructions, modular programming
- [[concepts/io-and-memory-systems|I/O Interfacing and Memory Systems]] — I/O techniques, SRAM/DRAM, ROM/Flash, memory management
- [[sources/ICT1011-computer-organisation-architecture|ICT1011 Source Page]]
