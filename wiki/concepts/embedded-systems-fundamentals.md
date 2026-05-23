---
address: c-000054
type: concept
title: "Embedded Systems Fundamentals"
domain: embedded-systems
source: INF2004
complexity: high
tags: [embedded-systems, real-time, microcontroller, build-pipeline, inf2004]
---

# Embedded Systems Fundamentals

## Definition

An **embedded system** is a computing system designed for a *dedicated task* within a larger device or system. Key properties:

- **Sensor–actuator coupling** — reads inputs from the physical world, drives outputs
- **Real-time operation** — must respond within bounded time constraints
- **Limited resources** — constrained CPU, RAM, flash, and power budget
- **Microcontroller-based** — typically a single-chip solution (MCU)

> "Embedded systems are computers that are submerged in a device, controlling it" — Prof. Ian McLoughlin, SIT

---

## Real-Time Taxonomy

| Class | Definition | Consequence of Missed Deadline |
|-------|-----------|-------------------------------|
| **Hard real-time** | Deadline is absolute; late = wrong | System failure, safety hazard |
| **Soft real-time** | Deadline is preferred; occasional miss tolerable | Degraded quality |
| **Non real-time** | No timing constraints | No constraint |

*Examples*: Airbag controller = hard; video stream buffer = soft; desktop OS = non.

---

## Hardware Taxonomy

| Device | Description | Typical Use |
|--------|-------------|-------------|
| **µC (Microcontroller)** | CPU + RAM + flash + peripherals on one chip | Most embedded products |
| **SoC (System-on-Chip)** | µC + specialised hardware blocks (DSP, GPU, radio) | Smartphones, IoT gateways |
| **ASIC** | Application-Specific IC — fixed silicon logic | High-volume, fixed function |
| **µP (Microprocessor)** | CPU only; needs external memory & peripherals | General-purpose computing |
| **DSP** | Optimised for digital signal processing (MACs) | Audio, comms, radar |
| **FPGA** | Field-Programmable Gate Array — reconfigurable logic | Prototyping, acceleration |
| **GPU** | Massively parallel floating-point | ML training, graphics |
| **NPU** | Neural Processing Unit | On-device ML inference |

---

## Edge–Fog–Cloud Architecture

```
Sensors / Actuators
    │
    ▼
[Edge Layer]  — µCs, embedded nodes (billions of devices)
    │  local inference, real-time control
    ▼
[Fog Layer]   — gateways, local servers (millions of devices)
    │  aggregation, short-term storage
    ▼
[Cloud Layer] — data centres (thousands of servers)
               long-term analytics, model training
```

---

## Embedded vs General-Purpose Software

| Dimension | Embedded | General-Purpose |
|-----------|----------|-----------------|
| Resources | Constrained (KB of RAM) | Abundant (GB of RAM) |
| OS | Bare-metal or RTOS | Full OS (Linux, Windows) |
| Deployment | Fixed target hardware | Heterogeneous hardware |
| Testing | HIL, hardware-in-the-loop | Simulation, mocking |
| Language | C, Assembly | C/C++, Python, Java, etc. |
| Update cycle | Rare; safety-critical approval | Frequent |
| Failure cost | Potentially catastrophic | Usually recoverable |

---

## Build Pipeline

```
Source (.c / .h)
    │
    ▼ compiler (e.g. arm-none-eabi-gcc)
Object file (.o)
    │
    ▼ assembler (for .s files)
Object file (.o)
    │
    ▼ linker + linker script (.ld) + C libraries (.a)
ELF / .axf executable
    │
    ▼ objcopy / uf2conv
Binary / .uf2 image → flash to MCU
```

**Cross-compilation** — toolchain runs on a host (e.g. x86 Windows) but generates code for the target ISA (e.g. ARM Cortex-M0+). Distinct from *native compilation* (host = target).

### SDK / Bootloader / Compiler

- **SDK** — vendor-provided headers and libraries abstracting hardware registers (e.g. Pico SDK wraps RP2040 peripherals)
- **Bootloader** — small resident ROM program that receives a new image and writes it to flash
- **Compiler** — translates C to target machine code; the Pico SDK uses `arm-none-eabi-gcc`

---

## Startup Code (`crt0.s`)

Before `main()` runs, the startup assembly routine performs:

1. Disable all interrupts
2. Copy initialised data segment from flash → RAM
3. Zero-initialise BSS segment (uninitialised globals)
4. Initialise stack pointer
5. Initialise heap
6. Enable interrupts
7. Call `main()`

---

## V-Model SDLC for Embedded

```
Requirements ────────────────────────► Acceptance Testing
  System Design ──────────────────► System Testing
    Architecture Design ─────────► Integration Testing
      Module Design ─────────────► Unit Testing
                 Implementation
```

Each left-side artefact has a *direct test counterpart* on the right. **Traceability** is mandatory: every requirement must trace through design → code → test.

---

## Embedded Failure Case Studies

### Therac-25 (1985–1987)
- Medical radiation machine — race condition between operator commands
- Software ran correctly in isolation but failed under specific rapid input sequences (Heisenbug)
- **Root cause**: Removed hardware safety interlocks and replaced with software-only checks; concurrent access to shared variable without synchronisation
- **Lesson**: Never replace independent hardware safety mechanisms with software alone

### Ariane 5 (1996)
- European Space Agency rocket — first flight, self-destructed after 37 seconds
- 64-bit floating-point value (horizontal velocity `BH`) cast to 16-bit integer caused overflow
- Code was *correct* for Ariane 4 but reused without re-validation on the faster Ariane 5
- **Root cause**: `(float)H_O / 65536.0` exceeded 16-bit signed range; unhandled exception halted the inertial reference system
- **Lesson**: Re-validate all reused software when hardware parameters change

### Toyota (2009–2011)
- Unintended acceleration in Camry; linked to "spaghetti code" in engine control unit
- 11,000+ global variables, unreachable code, stack overflow risk, single-point failure
- **Root cause**: No MISRA-C compliance, inadequate task separation, insufficient testing
- **Lesson**: Safety-critical embedded software requires coding standards (MISRA-C), static analysis, and formal verification

---

## Key Terms

| Term | Definition |
|------|-----------|
| MCU | Microcontroller Unit — single-chip computer |
| HIL | Hardware-in-the-Loop testing |
| BSS | Block Started by Symbol — uninitialised data segment |
| MISRA-C | Motor Industry Software Reliability Association C coding standard |
| Cross-compilation | Generating code for a different target architecture |
