---
address: c-000055
type: concept
status: established
title: "Embedded I/O and Interrupts"
domain: embedded-systems
source: INF2004
complexity: high
tags: [embedded-systems, interrupts, gpio, isr, ivt, polling, inf2004]
---

# Embedded I/O and Interrupts

## Requirements for Embedded Systems

### Requirement Writing Rules

- **"shall"** — mandatory requirement (must be implemented and tested)
- **"should"** — advisory / preferred behaviour (not mandatory)
- Every requirement must be **traceable**: Requirement → Design → Code → Test

### Good Requirement Characteristics

| Property | Meaning |
|----------|---------|
| **Clear** | Unambiguous; only one interpretation |
| **Verifiable** | Can be objectively tested |
| **Traceable** | Linked to a source (user/standard) |
| **Justified** | Rationale exists |
| **Coherent** | No internal contradiction |

### Problematic Requirement Patterns

| Pattern | Example | Problem |
|---------|---------|---------|
| Untraceable | "System shall be good" | Cannot verify or trace to need |
| Untestable | "System shall respond quickly" | No measurable criterion |
| Imprecise | "shall sometimes log data" | Ambiguous frequency |
| No tolerance | "temperature = 25°C" | Misses ±tolerance band |
| Too complex | One req covers 5 behaviours | Fails single-concern rule |
| Implementation-describing | "shall use a linked list" | Constrains design, not behaviour |

### Non-Functional Requirements (NFRs) in Embedded

NFRs are **emergent properties** — they arise from the system as a whole, not from a single component:

- **Performance & timeliness** — response latency, throughput, sampling rate
- **Safety & security** — must not harm people; must resist attack
- **Dependability** — availability, reliability, fault tolerance
- **Resource constraints** — RAM, flash, CPU utilisation, power budget
- **Design & project constraints** — platform, certification standard (e.g. IEC 61508), team size

---

## Interrupt Principles

### What Is an Interrupt?

An interrupt is a hardware or software signal that temporarily suspends the normal execution of a programme to handle a higher-priority event.

**Types of interrupt:**
- **External / hardware** — GPIO pin change, peripheral data-ready signal
- **Internal / software** — timer overflow, arithmetic exception
- **Non-maskable interrupt (NMI)** — cannot be disabled; used for critical safety events

### Interrupt Vector Table (IVT)

The IVT is a fixed memory region (usually at the start of flash) containing *addresses* of handler routines. On ARM Cortex-M:

```
Address 0x00000000  →  Initial Stack Pointer
Address 0x00000004  →  Reset Handler
Address 0x00000008  →  NMI Handler
Address 0x0000000C  →  Hard Fault Handler
...
Address 0x0000004C  →  IRQ0 Handler (first peripheral interrupt)
...
```

### Interrupt Handling Sequence

```
Normal execution
    │
    │  interrupt signal asserted
    ▼
CPU pushes context (PC, SR, registers) → stack
    │
    ▼
CPU reads IVT at interrupt number's offset
    │
    ▼
CPU branches to ISR address
    │
    ▼
ISR executes
    │
    ▼
ISR clears interrupt flag (mandatory, or it re-triggers)
    │
    ▼
ISR executes RETI (return from interrupt)
    │
    ▼
CPU pops context from stack
    │
    ▼
Normal execution resumes
```

### The Stack in Interrupt Context

The **stack** is an area of RAM used as temporary storage. The CPU maintains a **stack pointer (SP)** register pointing to the top of the stack. During an interrupt:
- CPU *pushes* PC, SR, and general-purpose registers onto the stack
- On return, CPU *pops* them back — restoring state exactly

---

## Interrupt Service Routine (ISR) Rules

1. **Keep ISRs short and fast** — they block all lower-priority code while running
2. **Clear the interrupt flag** before exiting — otherwise the ISR fires again immediately
3. **Use global variables** — cannot pass parameters to an ISR; share data via volatilely-declared globals
4. **Never put an infinite loop in an ISR**
5. **Consider re-entrancy** — interrupts are asynchronous; protect shared resources (critical sections, disabling interrupts)
6. **Mask interrupts you do not need** — reduces spurious wake-ups and complexity

### Interrupt Configuration Steps

1. Write the ISR function
2. Populate the IVT with the ISR address
3. Enable the interrupt in the interrupt controller
4. Configure the peripheral's interrupt behaviour (which condition triggers it)
5. Unmask (enable) the specific interrupt

### Edge vs Level Triggering

| Mode | Trigger condition |
|------|------------------|
| **Rising edge** | Signal transitions low → high |
| **Falling edge** | Signal transitions high → low |
| **Level high / low** | Signal is continuously at specified level |

---

## Polling vs Interrupts

**Polling (busy-wait):** The CPU repeatedly checks a peripheral register to see if data is ready.

**Interrupts:** The peripheral asserts a signal when ready; the CPU handles it only then, sleeping otherwise.

### Comparison

| Dimension | Polling | Interrupts |
|-----------|---------|------------|
| CPU utilisation | High — wastes cycles checking | Low — CPU sleeps until needed |
| Latency | Worst-case = polling period | Near-immediate (hardware response `h`) |
| Power consumption | High | Low (sleep between events) |
| Code complexity | Simple | More complex (ISR, shared state) |
| Determinism | Predictable polling cycle | Non-deterministic timing of events |

### Timing Constraints

**Polling constraints** (T = min inter-event time, D = deadline, p = polling period, c = handling CPU time):

```
2c ≤ c + p ≤ D ≤ T
Utilisation: u_polling = c / p
```

**Interrupt constraints** (h = hardware response time):

```
h + c ≤ D ≤ T
Utilisation: u_int = (h + c) / T
```

---

## Digital Communications Protocols

| Protocol | Type | Lines | Key Feature |
|----------|------|-------|-------------|
| **UART** | Asynchronous serial | TX, RX | No clock line; agreed baud rate |
| **SPI** | Synchronous serial | MOSI, MISO, SCLK, CS | Full-duplex; fast; master-slave |
| **I2C** | Synchronous serial | SDA, SCL | Multi-master; 7-bit addresses; 100 kHz / 400 kHz |

---

## Analogue-to-Digital Conversion (ADC)

The ADC converts a continuous analogue voltage into a discrete digital value.

- **Resolution** (bits) — determines the number of discrete levels: 2ⁿ levels for n bits
- **Sampling rate** — how many conversions per second
- **SNR improvement** — oversample and average to reduce noise below ADC quantisation noise
- **Signal conditioning** steps before the ADC: filter → remove DC offset → amplify/attenuate → linearise

**Example (LPS25H pressure sensor, 24-bit ADC):**
```
measure = pressure_hPa × 4096
Sensitivity = 4096 / (2²⁴ − 1) ≈ 0.00024 hPa per LSB
```
