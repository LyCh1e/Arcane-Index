---
type: concept
title: "I/O Interfacing and Memory Systems"
domain: computer-architecture
source: [[sources/ICT1011-computer-organisation-architecture]]
complexity: high
updated: 2026-05-13
tags: [concept, computer-architecture, io, serial-communication, memory, sram, dram, paging, msp430]
status: established
created: 2026-05-13
---

# I/O Interfacing and Memory Systems

Covers I/O interfacing techniques (serial/parallel, polled/interrupt, Bluetooth), secondary memory (HDD, RAID), primary memory (bus, SRAM, DRAM, ROM/Flash), and memory management (swapping, partitioning, paging).

---

## 1. I/O Interfacing Concepts

### 1.1 Parallel vs Serial

| | Parallel | Serial |
|--|---------|--------|
| Data path | Multiple bits simultaneously | One bit at a time |
| Speed | Fast | Slower per bit, but simpler wiring |
| Wiring | Many wires (one per bit) | One or two wires |
| Typical use | Internal buses, printer port (legacy) | UART, USB, SPI, I²C, Bluetooth |

### 1.2 Duplex Modes

| Mode | Description |
|------|-------------|
| **Simplex** | One direction only (transmit or receive) |
| **Half-duplex** | Both directions, but not simultaneously (one at a time) |
| **Full-duplex** | Both directions simultaneously (two independent channels) |

### 1.3 Asynchronous Serial Communication Format

Asynchronous serial does not use a shared clock. Timing is recovered from the data stream using a known **baud rate**.

```
Idle    Start    D0  D1  D2  D3  D4  D5  D6  D7   Parity  Stop
─────── ──┐      ┌───┐   ┌───┐            ┌───┐           ┌────
MARK(1) │ │      │ 0 │   │ 1 │            │ 1 │   [P]     │  1
        │ └──────┘   └───┘   └───...───────┘   └───────────┘
        SPACE(0) LSB first
```

| Field | Value |
|-------|-------|
| Start bit | Logic 0 (Space) — signals start of frame |
| Data bits | 7 or 8 bits, LSB transmitted first |
| Parity bit | Optional — Odd, Even, or None |
| Stop bit(s) | Logic 1 (Mark) — 1 or 2 bits |

**Baud rate** = bits per second (including framing bits). `1/T` where T is bit period.

> Data rate (payload bps) < baud rate because start/stop bits are overhead.

**RS-232**: standard for DTE (Data Terminal Equipment, e.g., PC) ↔ DCE (Data Circuit-terminating Equipment, e.g., modem) serial communication. Voltage levels: Mark = −3 to −15 V; Space = +3 to +15 V (inverted logic compared to TTL).

---

## 2. Memory-Mapped I/O vs Isolated I/O

| | Memory-Mapped I/O | Isolated I/O |
|--|------------------|-------------|
| Address space | Peripherals share the same address space as memory | Peripherals have a separate I/O address space |
| Instructions | Normal memory instructions (MOV) | Special IN/OUT instructions |
| Advantage | Orthogonal — any addressing mode works | Does not "consume" memory addresses |
| Used by | MSP430, ARM | Intel x86 (legacy) |
| MSP430 | 0x0000–0x09FF reserved for peripherals | — |

---

## 3. Polled I/O vs Interrupt-Driven I/O

### 3.1 Polled (Busy-Wait) I/O

The CPU continuously checks a status flag in a loop until the device is ready.

```asm
poll_loop:
    BIT  #READY_FLAG, P1IN    ; test device ready bit
    JZ   poll_loop             ; not ready — loop
    MOV  P1IN, R4              ; ready — read data
```

**Pros**: simple to implement.  
**Cons**: CPU is fully occupied during the wait; cannot do other work.

### 3.2 Interrupt-Driven I/O

The device raises an **Interrupt Request (IRQ)** when ready. The CPU:
1. Completes the current instruction
2. Pushes PC and SR onto the stack
3. Jumps to the **Interrupt Service Routine (ISR)** address in the interrupt vector table
4. Executes the ISR
5. Executes `RETI` — pops SR and PC, resuming the interrupted programme

**Pros**: CPU is free to run other code between I/O events; efficient for slow or sporadic devices.  
**Cons**: More complex (ISR must be written; shared state must be protected).

---

## 4. Bluetooth

| Parameter | Value |
|-----------|-------|
| Frequency band | 2402–2480 MHz (2.4 GHz ISM band) |
| Channels | 79 channels × 1 MHz spacing |
| Hopping | FHSS (Frequency-Hopping Spread Spectrum), 1600 hops/second |
| Access method | TDD-TDMA (Time Division Duplex) |
| Piconet | 1 master + up to 7 active slave devices |
| Scatternet | Multiple overlapping piconets sharing the band |
| BLE | Bluetooth Low Energy — reduced power, shorter bursts, optimised for IoT sensors |

FHSS hops rapidly between channels, making Bluetooth resistant to narrowband interference and reducing the probability of colliding with other 2.4 GHz devices (Wi-Fi, microwave ovens).

---

## 5. Secondary Memory — Hard Disk Drive (HDD)

### 5.1 Physical Structure

| Component | Description |
|-----------|-------------|
| **Platter** | Rotating magnetic disk; both surfaces used |
| **Track** | Concentric ring on a platter surface |
| **Cylinder** | Set of all tracks at the same radius across all platters |
| **Sector** | Smallest addressable unit on a track (typically 512 B or 4 KB) |
| **Read/Write head** | One per platter surface; floats nanometres above the surface |

### 5.2 Access Time Formula

```
Total access time = Ts + Tr + Tt

Ts  = seek time (head moves to correct track)
Tr  = rotational delay (average = 0.5 / RPS)
Tt  = transfer time = N / (RPS × DT × DS)
     where N  = number of bits to transfer
           RPS = rotations per second
           DT  = tracks per disk surface (used for density)
           DS  = sectors per track
```

### 5.3 RAID

| Level | Technique | Benefit | Drawback |
|-------|-----------|---------|---------|
| **RAID 0** | Striping — data split across N drives | Performance (parallel reads/writes) | No redundancy; any single drive failure = total loss |
| **RAID 1** | Mirroring — identical copy on each drive | Fault tolerance (survives one drive failure) | 50% storage efficiency |
| **RAID 10** | Stripe of mirrors (RAID 1 + RAID 0) | Performance + fault tolerance | Requires ≥ 4 drives; 50% efficiency |

---

## 6. Primary Memory — Bus Interconnect

Three buses connect the CPU to memory and peripherals:

| Bus | Width | Carries |
|-----|-------|---------|
| **Data bus** | Width = bits per transfer (e.g., 16-bit for MSP430) | Data values |
| **Address bus** | Width = log₂(max addressable memory) | Memory addresses |
| **Control bus** | Varies | Read/Write signal, interrupt request, clock, reset, bus grant |

### 6.1 Synchronous Bus Transfers

All transfers clocked by a shared bus clock. Simpler to implement and test. All devices must operate at the same clock rate — inflexible for mixing slow and fast devices.

**Synchronous Read:**
1. CPU places address on address bus
2. CPU asserts Read on control bus
3. After fixed clock cycles (access time), memory places data on data bus
4. CPU latches data; releases address/control buses

**Synchronous Write:**
1. CPU places address on address bus
2. CPU places data on data bus
3. CPU asserts Write on control bus
4. Memory latches data after fixed clock period

### 6.2 Asynchronous Bus Transfers

Uses a **handshake** protocol (ReadReq / DataReady / Ack). No shared clock required — flexible for devices operating at different speeds. Each device signals when it is ready; the bus waits.

**Trade-off**: synchronous is simpler; asynchronous is flexible but more complex and can be slowed by a slow device holding the bus.

### 6.3 Memory Performance

| Metric | Definition |
|--------|-----------|
| **Access time (latency)** | Time from address placed on bus until data is available |
| **Memory cycle time** | Access time + any additional time before the next access can begin |
| **Transfer rate** | 1 / memory cycle time for RAM; TN = TA + (N/R) for sequential devices |

---

## 7. Primary Memory — Technologies

### 7.1 RAM Overview

Random Access Memory: both reads and writes, any address, in any order. **Volatile** — data lost on power-off.

| | SRAM | DRAM |
|--|------|------|
| Cell structure | Cross-connected inverters (latch) + 2 transistors | 1 transistor + 1 capacitor |
| Stability | Holds data without refresh | Must be refreshed periodically (charge leaks) |
| Speed | Fast (few ns) | Slower |
| Density | Lower (more transistors per bit) | Higher (smaller cell) |
| Cost | Higher | Lower |
| Typical use | Cache (L1/L2/L3) | Main memory |

**SRAM operation**: Word Line selects a row; Bit Lines carry the value. The latch holds the state as long as power is supplied.

**DRAM operation**: 
- **Write**: drive bit line; row access (Word Line) charges/discharges capacitor
- **Read**: Word Line activated; sense amplifiers on bit lines detect charge level. Reading also refreshes the row.
- **Refresh**: must periodically activate each row to restore charge before it decays below threshold.

### 7.2 ROM and Flash

**ROM** (Read-Only Memory): contents written at manufacture. Single transistor per cell; write-once.

| Type | Write mechanism | Erase mechanism |
|------|----------------|----------------|
| **ROM** | At manufacture (mask-programmed) | Cannot be erased |
| **PROM** | One-time — burn fuses with high current pulse | Cannot be erased |
| **EPROM** | Inject charge to turn on floating-gate transistor | UV light (erases entire chip) |
| **EEPROM** | Electrical charge injection (individual bytes) | Electrical (individual bytes) |
| **Flash** | Electrical (like EEPROM) | Electrical, but in **blocks** (not individual bytes) |

Flash key properties:
- Higher density and lower cost than EEPROM
- Write requires read-erase-write of the entire block
- Widely used in SSDs, USB drives, mobile phones, digital cameras
- MSP430 stores programme code in Flash (non-volatile, survives power-off)

---

## 8. Memory Management

Memory management is the operating system's responsibility. Its goal is to support **multi-programming** — running multiple processes efficiently while keeping them isolated.

### 8.1 Uni-Program vs Multi-Program

| | Uni-program | Multi-program |
|--|------------|--------------|
| Concurrent processes | 1 | Many |
| CPU utilisation | Low (idle during I/O waits) | High (another process runs while one waits) |
| Memory | OS + one user programme | OS + multiple user programmes |

### 8.2 Swapping

When main memory is full, the OS moves a blocked process out to **secondary storage** (intermediate queue) and loads a ready process in. This is an I/O operation and has a cost.

```
Long-term queue (disk) → [swap in] → Main memory → [swap out] → Intermediate queue (disk)
```

### 8.3 Partitioning

Dividing main memory into regions for each process.

**Fixed Partitioning**:
- Memory divided into fixed-size regions at system start
- Process assigned to smallest region that fits (**best fit**)
- Problem: **internal fragmentation** — unused space inside a too-large partition

**Dynamic Partitioning**:
- Each process gets exactly the memory it needs
- Problem: **external fragmentation** — over time, many small gaps (holes) appear between processes; individually too small to use
- Solutions:
  - **Coalescing**: merge adjacent free holes into one larger hole
  - **Compaction**: periodically move all processes to one end of memory, consolidating all free space into one block

### 8.4 Paging

Paging eliminates external fragmentation entirely by allowing non-contiguous allocation.

| Term | Definition |
|------|-----------|
| **Page** | Fixed-size chunk of a process's logical (virtual) address space |
| **Frame / Page frame** | Fixed-size chunk of physical memory (same size as a page) |
| **Page table** | Per-process mapping: page number → frame number |

**Key property**: a process's pages do not need to occupy contiguous frames. The OS maintains a **free frame list** and assigns any available frames.

**Address translation**:

```
Logical address:   [ page number (n−m bits) | page offset (m bits) ]
                              │
                    Index into page table
                              │
                         frame number
                              │
Physical address:  [ frame number | page offset (m bits) ]
```

Example: 16-bit logical address, 10-bit page offset → 1024 bytes/page, 64 pages (6-bit page number).

```
Logical: Page 1, Offset 30  →  Page table[1] = Frame 13  →  Physical: Frame 13, Offset 30
```

**Benefits of paging**:
- No external fragmentation (any frame can hold any page)
- Processes can be larger than any single contiguous free block
- Enables virtual memory (pages can be swapped to disk on demand)

**Relocation**: because a process may be loaded into different frames on each swap-in, programmes use **logical addresses**. The **Memory Management Unit (MMU)** translates logical → physical at runtime.

---

## Summary

```
I/O Techniques
├── Parallel / Serial
├── Simplex / Half-duplex / Full-duplex
├── Async serial: start + data + parity + stop; baud rate
├── Memory-mapped vs isolated I/O
├── Polled (busy-wait) vs Interrupt-driven
└── Bluetooth: FHSS, piconet, BLE

Secondary Memory
├── HDD: platters → tracks → cylinders → sectors
├── Access time: Ts + Tr + Tt
└── RAID: 0 (stripe), 1 (mirror), 10 (stripe+mirror)

Primary Memory
├── Bus: data / address / control
├── Synchronous (clocked) vs Asynchronous (handshake)
├── SRAM: latch, fast → cache
├── DRAM: capacitor, refresh, high density → main memory
└── ROM/Flash: non-volatile; Flash in blocks

Memory Management
├── Swapping: disk ↔ main memory
├── Fixed partition → internal fragmentation
├── Dynamic partition → external fragmentation → coalesce/compact
└── Paging: pages + frames + page table → no external fragmentation
```

## See Also

- [[concepts/computer-architecture-fundamentals|Computer Architecture Fundamentals]] — Von Neumann, MSP430, ISA
- [[concepts/assembly-programming-msp430|Assembly Programming (MSP430)]] — assembly, instructions, modular programming
- [[sources/ICT1011-computer-organisation-architecture|ICT1011 Source Page]]
