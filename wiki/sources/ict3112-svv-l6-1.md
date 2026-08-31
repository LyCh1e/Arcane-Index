---
type: source
title: "ICT3112 SVV — Lecture 6.1: Blackbox Testing — Equivalence Partitioning and Boundary Value Analysis"
source_file: "raw/ICT3112 Software Verification and Validation - L6_1_Blackbox_Testing_EquivalencePartitioning_and_BoundaryValueAnalysis.md"
domain: software-verification-validation
tags: [ict3112, svv, blackbox-testing, equivalence-partitioning, boundary-value-analysis]
created: 2026-08-31
---

# Source Index — ICT3112 SVV Lecture 6.1: Equivalence Partitioning and Boundary Value Analysis

Course: **ICT3112 Software Verification and Validation** — Ryan Fraser Kirwan

---

## Equivalence Partitioning (EP)

### Purpose

Designed to **minimise the number of test cases** while still covering a large amount of system requirements.

### Mechanism

- All test inputs are divided into groups called **Equivalence Partitions**
- Test inputs include: human inputs, interface inputs (API parameters), hardware inputs, etc.
- Each partition is expected to be processed by the system in a **similar way** → equivalent results expected
- Testing one member of a partition is equivalent to testing any other member

### Example 1a — Integer 0 to 100

```
Invalid 1  |  Valid  |  Invalid 2
  < 0      |  0–100  |   > 100
```

Partitions:
- **Valid**: e.g., +90, +10
- **Invalid**: e.g., +110, −10

Can be split as two invalid partitions (below 0 and above 100) for more precision.

### Example 2 — Binary Search in Unsorted Array of 10 Positive Integers < 99

Partitions:
- **Inputs where precondition = true and element is an array member** (e.g., 12)
- **Inputs where precondition = true and element is not an array member** (e.g., 95)
- **Inputs where precondition = false** (e.g., −19, 150, 1000)

### Advantages / Disadvantages

| Advantages | Disadvantages |
|-----------|--------------|
| Usually easy to analyse | Excludes some inputs |
| Applicable for all test levels | No rule to choose the specific input within a partition |
| Minimises test cases while covering many requirements | Very limited focus |
| Can be used to partition both inputs and outputs | No guarantee that all elements of a partition are treated the same way |

---

## Boundary Value Analysis (BVA)

### Purpose

Design test cases based on **boundary value inputs** — assumes testing at boundaries is likely to yield defects.

**Complements EP**: BVA selects the max and min values of partitions as boundary values.

### Mechanism

- Select input values at, and just beyond, the boundaries of Equivalence Partitions
- Cover both valid and invalid boundaries
- Consider both input and output boundaries

### Example 1 — Integer 0 to 100

| Boundary | Value | Type |
|----------|-------|------|
| Low valid | 0 | Valid |
| High valid | 100 | Valid |
| Just below low | −1 | Invalid |
| Just above high | 101 | Invalid |

Extended (3-value boundary): test 0, 1, 99, 100 (low/low+1 and high−1/high).

**Also consider input representation**: if the system expects 3-digit format (leading zeros):
- Valid: enter 1 digit → system adds 2 leading zeros
- Valid: enter 3 digits
- Invalid: enter 4 digits → system rejects
- Invalid: enter null → system rejects

### Example 2 — Binary Search in Array

BVA for the same 10-element unsorted array:
- `precondition = true`, e.g., 0, 98 (first and last valid values)
- `precondition = true`, element is the 1st array member: 45
- `precondition = true`, element is the last array member: 50
- `precondition = true`, element is not a member: 95
- `precondition = false`: −1, 99

### Example 3 — String Input: First Name (1–10 CAPITAL letters)

| Boundary | Test Value | Reason |
|----------|-----------|--------|
| Valid, lower size | "G" (1 char) | Lower boundary of string length |
| Valid, lower ASCII | "A" (ASCII 65) | Lower boundary of capital letter range |
| Valid, upper size | "BORDERNAME" (10 chars) | Upper boundary of string length |
| Valid, upper ASCII | "Z" (ASCII 90) | Upper boundary of capital letter range |
| Invalid, lower ASCII | "@" (ASCII 64) | Just below 'A' |
| Invalid, lower null | null / empty | No input |
| Invalid, upper size | "FAKEBIGNAME" (11 chars) | Just above upper length |
| Invalid, upper ASCII | "[" (ASCII 91) | Just above 'Z' |

**Note**: Separate test cases for ASCII boundary and size boundary — combining them would make it unclear which boundary caused a failure.

### Example 4 — Date Input (dd/mm/yyyy, start date)

Assumptions: no date older than 120 years; date can be in the future but not beyond today + 31 days.

| Parameter | Valid Low | Valid High | Invalid Low | Invalid High |
|-----------|-----------|-----------|-------------|-------------|
| **dd** | 1 | #days_in_month (28/29/30/31) | 0 | #days_in_month + 1 |
| **mm** | 1 | 12 | 0 | 13 |
| **yyyy** | today − 120 years | today + 31 days | today − 121 years | today + 32 days |

*(Don't forget leap years!)*

### Example 5 — Time Input (HH:MM, 24-hour clock)

| Parameter | Valid Low | Valid High | Invalid Low | Invalid High |
|-----------|-----------|-----------|-------------|-------------|
| **hh** | 00 | 23 | −01 | 24 |
| **mm** | 00 | 59 | −01 | 60 |

---

## General BVA Process

| Rule | Description |
|------|------------|
| **1** | For a range of values: create valid tests at each end; invalid tests just beyond each end. Also consider output conditions. |
| **2** | For values without a specified range: use min and max of values, plus one below and beyond. |
| **3** | For sets of values: test each value in the set, and the set's size. For files: test first and last records. |
| **4** | For any other extreme input or output conditions: test each of them. |

**Output condition example**: billing system must not exceed 6,000,000 subscribers in a report.
- Valid outputs: 0 and 6,000,000
- Invalid outputs: −1 and 6,000,001

### Advantages / Disadvantages

| Advantages | Disadvantages |
|-----------|--------------|
| Applicable for all test levels | Excludes some inputs |
| Can expose potential UI / user input problems | Does not consider dependencies between combinations of input values |
| Very clear guidelines for determining tests | |
| Capable of identifying a high number of defects | |

---

## Linked Concepts

- [[concepts/blackbox-testing-techniques]] — comprehensive blackbox reference
- [[concepts/test-design-techniques]] — EP and BVA overview (age example, coverage comparison)
