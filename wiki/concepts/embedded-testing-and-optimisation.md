---
address: c-000057
type: concept
title: "Embedded Testing and Optimisation"
domain: embedded-systems
source: INF2004
complexity: high
tags: [embedded-systems, testing, traceability, v-model, optimisation, power, memory, inf2004]
---

# Embedded Testing and Optimisation

## Traceability in Embedded Testing

**Traceability** ensures every requirement maps to a design element, a code artefact, and a test case — and vice versa.

### Traceability Chain

```
Requirement (R1)
    │
    ▼ High-Level Design (HLD)  → Diagram/block reference
    │
    ▼ Low-Level Design (LLD)   → Function specification
    │
    ▼ Implementation            → Source file, function name
    │
    ▼ Test Case (T1.x)         → Pass/fail criteria, method
```

**Example:**
```
R1: "System shall log temperature every 5 minutes to flash memory."
  HLD: Logger Module (Fig 2, Block D1.2)
  LLD: log_temp_data() — D1.2.1
  Code: logger.c::log_temp_data(), triggered by timer ISR every 300 s
  Test T1.3: Run 15 min; read flash; expect 3 valid entries.
```

### Traceability Anti-Patterns

| Anti-Pattern | Problem |
|---|---|
| Tests not linked to requirements | Cannot confirm system meets specification |
| Requirements without tests | Unverified behaviour |
| Missing design elements | Gap between requirements and code |
| Gold plating | Features built without a traceable requirement |

### Traceability Best Practices

- Give every design item a unique ID (e.g. `D1.2.1`)
- Use the V-Model to link left-side artefacts to right-side tests
- Check for gold plating (extra features without a requirement)
- Trace change impact: modifying a requirement ripples to design, code, and tests
- Use auto-generated IDs — manual re-numbering breaks references

---

## Embedded Testing Strategy

### The Cost of Late Bug Discovery

```
Bugs caught here:    Unit Test  →  Integration  →  System  →  Field
Relative cost:          1×            10×           100×      1000×+
```

> *"Product-level tests should never find a software bug. If they do, your process is broken."*

Aim for fewer than 5% of bugs discovered at system test. A bug found in system test represents a **process failure**, not just a code fault.

### V-Model Testing Levels

| Level | Tests Against | Scope |
|-------|--------------|-------|
| **Unit Testing** | Module Design / LLD | Single function or module |
| **Integration Testing** | HLD / System Design | Interfaces between modules |
| **System Testing** | System Requirements | Entire system on real hardware |
| **Acceptance Testing** | User / Product Requirements | Customer sign-off |

---

## Unit Testing

**Goal:** Verify each module or function in isolation, before integration.

### Good Practices

- Test one module or function at a time using low-level interfaces
- Combine **white-box** (internal paths) and **black-box** (functional outputs)
- Best place to catch **boundary bugs** (cheapest to fix here)

### Common Mistakes

- Testing only "happy paths" — ignore error conditions
- Only doing system testing — bugs found are expensive
- Forgetting missing/exception cases (NULL, NaN, overflow)

### White-Box vs Black-Box

| Dimension | White-Box | Black-Box |
|-----------|-----------|-----------|
| Knowledge | Internal code structure known | Treats module as opaque |
| Approach | Test code paths, branches, loops | Test inputs → outputs |
| Goal | High code coverage | Validate all requirements |
| Finds | Hidden logic errors | Missing or wrong features |
| Misses | Unimplemented requirements | Internal logic errors |
| Embedded use | Firmware, control loops, safety checks | System I/O, sensor features |

### Coverage Strategies

| Strategy | What to Cover |
|----------|--------------|
| **Boundary** | Min/max values, counter rollover, time boundary crossings |
| **Exceptional** | NULL, NaN, Inf, undefined inputs, leap year, invalid ranges |
| **Justify** | Trace each test to a design element; define strategy for boundary and exception coverage |

**Coverage caveats:**
- 100% coverage ≠ fully tested (tests may not check correctness)
- All tests passing ≠ bug-free (test oracle may be wrong)
- Hard-to-reach error handlers may lower coverage; document why they exist

---

## Integration Testing

**Goal:** Validate that modules work correctly *together* — focus on interfaces, not internal logic.

- Drive tests from System Design (SD) and High-Level Design (HLD)
- Assume unit tests have already vetted individual components
- Test valid, invalid, and boundary inputs at each interface
- Cover timing and sequencing behaviours
- Check intermediate side effects, not just final output

### Anti-Patterns

- Skipping straight to system test
- No traceability from integration test to HLD
- Declaring "pass" based only on overall function (ignoring interface contracts)

---

## System Testing

**Goal:** Validate the entire system as a whole in its intended environment, against requirements.

- Test with **real hardware**: sensors, actuators, power supplies
- Driven by requirements and user scenarios
- Confirms end-to-end functionality, performance, usability, and safety
- Include **off-nominal** conditions: faults, noise, invalid inputs, power glitches

### Anti-Patterns

- Testing only the "happy path"
- Ignoring hardware–software interaction (timing, electrical noise, power supply variation)
- Skipping environmental tests (temperature, voltage, EMI)

---

## Embedded Optimisation

### Optimisation Triangle

Three competing resources — optimising one often costs another:

```
     Power
     /   \
    /     \
Performance—Memory
```

*"Sometimes they co-exist: less code (less memory) → fewer cache misses → better performance."*

---

## Power Optimisation

### Power Fundamentals

```
P_total = P_dynamic + P_static
P_dynamic = C × V² × f   (proportional to frequency)
P_static  = leakage current × voltage (harder to control)
```

### Techniques

| Technique | Mechanism |
|-----------|-----------|
| **Clock scaling** | Reduce f_clk → lower current → lower power (energy per operation unchanged) |
| **Voltage scaling** | Lower V → lower P quadratically; must lower f proportionally |
| **Turn off peripherals** | Disable clock to unused modules (most effective technique) |
| **Interrupt over polling** | CPU sleeps between events; only wakes on interrupt |
| **Time-based processing** | Wake at known intervals, process data, sleep again |

### Low-Power Coding Practices

- Use `unsigned` data types where possible (avoid sign-extension overhead)
- Use pointers to access structures (avoids copying)
- Use `static const` for arrays/structs (avoids run-time copying from flash)
- **Avoid floating-point operations** (costly on MCUs without FPU)
- Write count-down `for` loops (compare to zero is cheaper)
- Keep ISRs short

---

## Performance Optimisation

### Compiler Optimisation Levels

| Level | Behaviour |
|-------|-----------|
| **-O0** | No optimisation; variables on stack for debugger access |
| **-O1** | Basic optimisation |
| **-O2** | Standard optimisation |
| **-O3** | Maximum optimisation; may increase code size |
| **-Os** | Optimise for size |

Higher optimisation → longer compile time; may make debugging harder.

### C Optimisation Techniques

| Technique | Description |
|-----------|-------------|
| **Right data types** | Use 16-bit types if 32-bit precision not needed (avoids multi-instruction operations) |
| **Register-based calling** | Pass arguments via registers when count ≤ register count |
| **Hardware loops** | Zero-overhead loop mechanism in DSPs; avoids decrement-and-branch |
| **Assembly inlining** | Use `__asm` for performance-critical hotspots |
| **Common sub-expression elimination** | Extract repeated expressions into a temporary variable |
| **Loop unrolling** | Duplicate loop body to reduce branch/check overhead; enables vectorisation |
| **Vendor libraries** | Use vendor-optimised routines (FFT, AES, CMSIS-DSP) written in assembly |

**Loop unrolling example:**
```c
// Original
for (int i = 0; i < 3; i++) { color_map[n + i] = i; }

// Unrolled
int i = 0;
color_map[n + i] = i; i++;
color_map[n + i] = i; i++;
color_map[n + i] = i;
```

---

## Memory Optimisation

### Code Size

- Target ISA matters: 32-bit arithmetic on a 16-bit platform generates extra instructions → larger code
- Use **Thumb / Thumb-2** instruction set on ARM for 16-bit encoding of common instructions
- Select appropriate data types: `short int` (16-bit) vs `int` (32-bit) saves flash and RAM

### Data Structures

- Choose data structures appropriate to access patterns: sequential access → array (cache-friendly); insertion/deletion → linked list
- Cache locality matters even on small MCUs with instruction caches

---

## Top 10 Risks of Poor Embedded Quality

Escalating consequence of a bug surviving to each stage:

| # | Stage | Consequence |
|---|-------|------------|
| 1 | Fails unit test | Immediate rework |
| 2 | Found in peer review | Dents confidence |
| 3 | Fails integration/system test | Delays, debugging cost |
| 4 | Fails acceptance testing | Customer trust lost |
| 5 | Field problem report | Support costs |
| 6 | Customer escalation | Critical downtime |
| 7 | Emergency patch in hostile conditions | Risky remote update |
| 8 | Public exposure | Negative press |
| 9 | Legal & regulatory trouble | Lawsuits, certification loss |
| 10 | Safety/catastrophic failure | Human injury, mission loss |
