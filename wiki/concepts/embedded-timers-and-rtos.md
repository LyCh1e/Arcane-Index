---
address: c-000056
type: concept
title: "Timers, PWM, RTOS, and Finite State Machines"
domain: embedded-systems
source: INF2004
complexity: high
tags: [embedded-systems, timers, pwm, rtos, fsm, scheduling, context-switch, inf2004]
---

# Timers, PWM, RTOS, and Finite State Machines

## Timers and Clocks

### Clock Fundamentals

- Almost all digital circuits are **synchronous** — they operate on a shared clock signal
- A processor has one primary **system clock** (e.g. 48 MHz) generated from an external crystal oscillator or ceramic resonator
- Internal **divider circuits** produce slower clocks: e.g. 24 MHz, 12 MHz, 6 MHz from the master clock
- **Power trade-off**: higher clock frequency → higher current → higher power; unused modules should be gated off to save power

### Real-Time Clock (RTC)

- Driven by a separate **32.768 kHz** watch crystal (= 2¹⁵ Hz)
- 15 divide-by-two stages produce a precise **1 Hz** tick
- The RTC maintains a count of seconds, minutes, hours, and dates
- Often battery-backed to retain time during power loss

### Timer Operation Modes

| Mode | Behaviour |
|------|-----------|
| **Count-down** | Loaded with a start value; counts down to 0 each clock cycle |
| **Count-up** | Starts at 0; counts up to a configured target value |

**On reaching the end-point (0 or target):**
- **One-shot** — stops; raises interrupt once
- **Free-running (wrap-around)** — reloads to maximum and continues
- **Periodic (reload)** — reloads with the same start value and continues

**Example:** 48 MHz system clock → load timer with 48,000 → interrupt fires every **1 ms**

### Watchdog Timer (WDT)

- A dedicated timer that **resets the CPU** when it reaches its target value
- Software must **periodically clear** the WDT counter ("kicking the dog") to prevent reset
- If software crashes and stops clearing, the WDT fires and resets the system
- Essential for **unattended embedded systems** (may be enabled by default after reset — must not forget to service it)

---

## Pulse-Width Modulation (PWM)

PWM simulates an analogue output using a digital GPIO pin by varying the **duty cycle** of a periodic square wave.

**Applications:** motor speed control, LED brightness control, audio amplifiers (Class D), servo positioning.

### Duty Cycle

```
Duty cycle (%) = (period − duty_cycle_count) / period × 100
```

*Example:* `period = 10`, `duty_cycle = 4`, polarity = low:
- Counter: 0 1 2 3 4 | 5 6 7 8 9 10 | …
- Output low when count < 4; high otherwise
- Actual duty cycle ≈ (11 − 5) / 11 ≈ **55%**

### PWM vs Naive Software Toggle

Software loop toggling a GPIO is unreliable — the OS or interrupts will disrupt timing. A hardware PWM counter runs **independently of the CPU** once configured (clock source, duty cycle, polarity).

---

## Embedded Operating System (RTOS)

### Why an Embedded OS?

A bare-metal embedded programme is a single binary. As complexity grows, a **Real-Time Operating System (RTOS)** provides:

- Scheduled execution of multiple concurrent tasks
- Predictable, bounded timing behaviour
- Inter-task communication (queues, semaphores)
- Resource sharing (mutual exclusion)
- Fault tolerance (watchdog integration, bounded memory)

> *An embedded OS that supports construction of real-time systems is called a Real-Time Operating System (RTOS).*

### Kernel Types

| Type | Description | Size | Crash impact |
|------|-------------|------|--------------|
| **Microkernel** | User services and kernel in separate address spaces | Small | Service crash does not crash kernel |
| **Monolithic kernel** | Both in same address space | Large | Any crash crashes the whole system |

Embedded systems typically use a **microkernel** for isolation and small footprint.

### Task Lifecycle

```
startup
  │
  ▼
READY ─────── run ──────► RUNNING
  ▲                          │
  │ placed in queue           │ blocked (waiting for
  │                           │ semaphore / timer / I/O)
  └── ◄── resource available ◄── BLOCKED
                          │
                          │ task exits / deleted
                          ▼
                      TERMINATED
```

| State | Description |
|-------|-------------|
| **Ready** | Eligible to run; awaiting CPU assignment |
| **Running** | Currently executing on the CPU (only one task at a time) |
| **Blocked** | Waiting for an event (semaphore, timer, I/O completion) |
| **Terminated** | Explicitly deleted |

### Task vs Function

| | Function | Task |
|-|----------|------|
| Lifecycle | Executes once, returns | Loops indefinitely |
| Blocking | Does not block | Blocks on signals/semaphores |
| Triggering | Called explicitly | Unblocked by another task posting a signal |

### Task Control Block (TCB)

The RTOS maintains a **TCB** for each task containing:
- Program counter (current instruction pointer)
- Stack pointer
- Task priority and state
- Scheduling information
- Task name / ID

TCBs are typically managed as a **linked list** (ready queue and blocked queue).

### Context Switch

When the scheduler moves execution from one task to another:
1. Save the current task's context (registers, PC, SP) onto its **stack**
2. Load the next task's context from its stack
3. Resume execution at the saved PC of the new task

Interrupts are usually **disabled** during a context switch to prevent corruption. Minimising context-switch time is critical for real-time performance.

---

## Scheduling Algorithms

### Round Robin (Time Slicing)

- Each task receives an equal **time slice**
- A fixed-rate clock interrupt triggers the scheduler
- Task executes until it completes or its time slice expires; context is saved if not finished
- Simple and fair; does not account for priority

### Pre-emptive Priority

- Each task has a **priority level**
- A higher-priority task can immediately pre-empt a running lower-priority task when it becomes ready
- Priorities may be **fixed** or **dynamic**

### Fixed-Priority Algorithms

| Algorithm | Principle |
|-----------|-----------|
| **Rate Monotonic Scheduling (RMS)** | Shorter period → higher priority (statically assigned) |
| **Deadline Monotonic Scheduling (DMS)** | Shorter deadline → higher priority |

### Dynamic-Priority Algorithms

| Algorithm | Principle |
|-----------|-----------|
| **Earliest Deadline First (EDF)** | Task with the nearest deadline runs next |
| **Least Slack Time (LST)** | Task with the smallest slack (deadline − remaining execution − current time) runs next |

---

## Finite State Machine (FSM)

An FSM is a **computational model** that describes a system as a finite set of states, with transitions between states triggered by inputs.

### Components

| Component | Description |
|-----------|-------------|
| **States** | Discrete conditions the system can be in |
| **Transitions** | Moves from one state to another on a condition/input |
| **Inputs** | Events or signals that drive transitions |
| **Outputs** | Actions taken on entry/exit/transition |

### State Diagram

Circles represent states; arrows represent transitions labelled with triggering inputs. A button/LED example:

```
States: 00, 01, 10, 11 (LED2 LED1 encoding)
Inputs: BTN1, BTN2

00 ──BTN1──► 01
01 ──BTN1──► 10
01 ──BTN2──► 10
10 ──BTN2──► 11
11 ──BTN1──► 00
11 ──BTN2──► 00
```

### State Table

A tabular representation listing **current state + input → next state + output**:

| Current State | Input | Next State |
|---------------|-------|-----------|
| 00 | BTN1 | 01 |
| 00 | BTN2 | 00 (no change) |
| 01 | BTN1 | 10 |
| 01 | BTN2 | 10 |
| 10 | BTN1 | 10 (no change) |
| 10 | BTN2 | 11 |
| 11 | BTN1 | 00 |
| 11 | BTN2 | 00 |

### FSM in Embedded Practice

FSMs are the standard pattern for implementing embedded control logic: traffic lights, communication protocol handlers, motor controllers, button debouncing. They produce **deterministic, auditable behaviour** directly mapped to requirements.
