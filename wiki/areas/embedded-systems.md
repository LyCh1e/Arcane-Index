---
address: c-000059
type: area
status: established
title: "Embedded Systems"
domain: embedded-systems
tags: [area, embedded-systems, rtos, real-time, microcontroller]
---

# Embedded Systems

Domain overview for embedded systems engineering — the discipline of designing software for resource-constrained, real-time, hardware-coupled computing devices.

## What Is Embedded Systems Engineering?

Embedded systems engineering spans the full lifecycle of software that runs on microcontrollers and dedicated computing hardware: from requirements and architecture through to low-level C programming, hardware-aware testing, and deployment optimisation.

Unlike general-purpose software, embedded systems:
- Operate within strict **resource budgets** (RAM, flash, CPU cycles, power)
- Must meet **real-time constraints** — hard, soft, or non
- Are **hardware-coupled** — software directly controls physical sensors and actuators
- Are often **safety-critical** — a software fault can cause physical harm

---

## Concept Pages

| Concept | Complexity | Key Topics |
|---------|-----------|------------|
| [[concepts/embedded-systems-fundamentals\|Embedded Systems Fundamentals]] | high | ES definition, real-time taxonomy, hardware taxonomy, build pipeline, startup code, V-Model, case studies |
| [[concepts/embedded-io-and-interrupts\|Embedded I/O and Interrupts]] | high | Requirements writing, IVT, ISR, stack, polling vs interrupts, timing constraints, ADC, digital comms |
| [[concepts/embedded-timers-and-rtos\|Timers, PWM, RTOS, and FSM]] | high | RTC, WDT, PWM duty cycle, RTOS task lifecycle, context switch, scheduling algorithms, FSM |
| [[concepts/embedded-testing-and-optimisation\|Embedded Testing and Optimisation]] | high | Traceability, V-model testing, unit/integration/system tests, white/black box, power/performance/memory optimisation |
| [[concepts/embedded-sensor-fusion-and-edge\|Sensor Fusion and Edge Computing]] | high | Sensor fundamentals, signal conditioning, preprocessing, complementary filter, sensor fusion taxonomy, TinyML |

---

## Source

| Source | Type | Date |
|--------|------|------|
| [[sources/INF2004-embedded-systems-programming\|INF2004 Embedded Systems Programming]] | course | 2026-05-23 |

---

## Cross-Domain Connections

```
C Programming ────────────────────────────────► Embedded Systems
  (pointers, structs, memory management)         (bare-metal firmware, ISRs, device drivers)

Computer Architecture ────────────────────────► Embedded Systems
  (ISA, registers, memory map, interrupts)       (IVT, startup code, peripheral registers)

Operating Systems ────────────────────────────► Embedded Systems
  (process states, scheduling, context switch)   (RTOS task model, pre-emptive priority)

Machine Learning ─────────────────────────────► Embedded Systems
  (model training, quantisation, CNNs)           (TinyML, on-device inference, Edge Impulse)

Computer Networks ────────────────────────────► Embedded Systems
  (IoT protocols, edge-fog-cloud, wireless)      (IoT gateway, sensor nodes, MQTT)

Software Testing ─────────────────────────────► Embedded Systems
  (unit, integration, system tests)              (HIL testing, traceability, V-model)
```

---

## Platform Reference: Raspberry Pi Pico (RP2040)

| Spec | Value |
|------|-------|
| Processor | Dual-core ARM Cortex-M0+ |
| Clock | Up to 133 MHz |
| SRAM | 264 KB |
| Flash | 2 MB (external) |
| GPIO | 30 pins |
| UART | 2 |
| SPI | 2 |
| I2C | 2 |
| PWM | 16 channels |
| ADC | 4 channels (12-bit) |
| Programmable I/O | 8 PIO state machines |
| SDK | Pico SDK (C/C++) |

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| MCU | Microcontroller Unit — single-chip CPU + RAM + flash + peripherals |
| RTOS | Real-Time Operating System — OS designed for bounded, predictable timing |
| ISR | Interrupt Service Routine — handler function invoked on interrupt |
| IVT | Interrupt Vector Table — memory region mapping interrupt numbers to ISR addresses |
| WDT | Watchdog Timer — hardware reset on software hang |
| PWM | Pulse-Width Modulation — variable duty cycle for analogue simulation |
| FSM | Finite State Machine — state-driven control model |
| ADC | Analogue-to-Digital Converter |
| TinyML | Deploying ML inference on resource-constrained embedded devices |
| HIL | Hardware-in-the-Loop — testing with real hardware in the control loop |
| MISRA-C | Safety-critical C coding standard used in automotive and aerospace |
