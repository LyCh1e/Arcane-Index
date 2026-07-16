---
type: concept
address: c-000113
title: "Static Code Analysis"
domain: secure-software-development
complexity: high
created: 2026-07-16
updated: 2026-07-16
tags: [concept, SAST, static-analysis, secure-software-development, code-quality, AST, CFG, data-flow, taint-analysis]
related:
  - concepts/security-testing-and-verification
  - examples/ict2216-lab8-static-code-analysis
  - examples/ict2216-lab9-sonarqube
  - sources/ICT2216-lecture-9-static-code-analysis
---

# Static Code Analysis

Static code analysis (also called SAST — Static Application Security Testing) examines source code, bytecode, or binary code for bugs and security vulnerabilities **without executing the programme**. It automates what a skilled human code reviewer would look for — but at far greater scale and coverage.

---

## Why Static Analysis?

Testing finds bugs on paths that tests exercise. Static analysis covers **all paths simultaneously**:

| Testing | Static Analysis |
|---|---|
| Finds bugs on exercised paths only | Can reason about all paths simultaneously |
| Cannot cover uncommon/rare paths | Finds bugs in paths tests never reach |
| Cannot analyse incomplete programmes | Can analyse libraries and modules without a complete executable |
| Cannot detect race conditions reliably | Can model concurrent execution states |
| Fast to run; cheap per test | Can be slow on large codebases |

**Hard-to-test bugs that static analysis targets:**
- Race conditions (thread scheduling is non-deterministic)
- Buffer overflows triggered only on specific input patterns
- Unvalidated inputs reaching evaluation points through uncommon paths

---

## When Does Static Analysis Run?

| Timing | Examples |
|---|---|
| **Before compile-time** | IDE warnings, syntax highlighting, lint checks |
| **At compile-time** | Type checking, compiler warnings (`-Wall` in GCC) |
| **After compile-time** | Load-time bytecode analysis; separate SAST tools in CI/CD pipeline |

---

## The Static Analysis Pipeline

A typical SAST tool processes code through a series of intermediate representations:

```
Source Code
    │
    ▼
Lexical Analysis ──────────▶ Token Stream
    │
    ▼
Parsing ────────────────────▶ Abstract Syntax Tree (AST)
    │
    ▼
Semantic Analysis ──────────▶ Names Database / Symbol Table
    │
    ▼
CFG Construction ───────────▶ Control Flow Graph (CFG)
    │
    ▼
Call Graph Construction ────▶ Call Graph (inter-procedural)
    │
    ▼
Analysis Engine ────────────▶ Findings / Warnings
```

| Representation | Enables |
|---|---|
| **Token Stream** | Pattern matching on syntax tokens |
| **AST** | Syntactic checks, style rules, unused variables |
| **Symbol Table** | Name resolution, type checking, scope analysis |
| **CFG** | Reachability, dead code, interrupt mishandling, missing initialisations |
| **Call Graph** | Inter-procedural analysis, taint tracking across function boundaries |

---

## What Static Analysis Can Detect

| Category | Examples |
|---|---|
| **Input vulnerabilities** | Buffer overflows, unvalidated inputs |
| **Memory errors** | Null dereferences, use-after-free, uninitialised variables |
| **Resource leaks** | Allocated memory / file handles never released |
| **API misuse** | Incorrect usage of security APIs, locking APIs |
| **Injection sinks** | Tainted data reaching SQL, HTML, OS command sinks |
| **Hardcoded credentials** | API keys, passwords, tokens in source |
| **Concurrency bugs** | Race conditions, interrupt mishandling |
| **Dead / unreachable code** | Unused variables, unreachable branches |
| **Evil Regex patterns** | Catastrophic backtracking (ReDoS) |
| **Style violations** | Naming conventions, coding guidelines |

---

## The Spectrum of Static Analysis Power

```
Type Checking ◄──────────────────────────────────────────► Program Verification
(practical, fast)           (SAST tools)               (powerful, impractical)

  Compiler type errors    Coverity, Fortify,           ESC/Java 2, Dafny,
                         Checkmarx, SonarQube,          formal proof systems
                         Bandit, Semgrep
```

- **Left (type checking):** Simple, catches a well-defined class of errors, virtually no false positives
- **Middle (SAST tools):** Heuristic and analysis-based; trade-off between false positive rate and coverage
- **Right (formal verification):** Mathematical proofs; sound and complete but requires expert annotation and enormous effort

---

## 6 Static Analysis Techniques

### 1. Pattern Matching (Simplest)

Checks a sequence of tokens for the presence of specific patterns — no understanding of program semantics.

**What it finds:**
- Hardcoded API keys, secrets, magic numbers
- Dangerous function calls (e.g., `gets()`, `strcpy()` in C)
- Evil Regex patterns (catastrophic backtracking — ReDoS)
- Style violations

**Example — flagging hardcoded credentials:**
```python
api_key = 'WwIZp6ihFqaHV841eb2BxbRt50iAj1EZx1laj'   # flagged
aws_key = '294D78743194D244AF48C6757A7FF1E71CC51'    # flagged
```

**Limitation:** No understanding of data flow — cannot tell if the string is actually used as a credential.

---

### 2. Data Flow Analysis

Tracks how data moves through the programme — which variables are assigned, where they are used, and whether they reach unsafe evaluation points.

**Key concepts:**

| Term | Definition |
|---|---|
| **Basic Block** | A consecutive sequence of instructions where control enters at the start and exits at the end with no internal branches |
| **Definition point** | Where a value is assigned to a variable |
| **Reference point** | Where a variable's value is read |
| **Evaluation point** | Where a value is executed or output (e.g., SQL query, HTML render, OS command) |

**Taint Analysis** (the most important data flow technique for security):

```
Definition Point  →  Reference Point(s)  →  Evaluation Point
(HTTP parameter)     (variable uses)         (SQL query / innerHTML)
   [TAINTED]                                  [FLAGGED if still tainted]
```

Untrusted input is marked "tainted" at entry. If it reaches an evaluation point without sanitisation or escaping, it is flagged as a potential injection vulnerability.

**Example — missing initialisation (data flow):**

```c
// Correct: both branches set c
if (b) { c = 5; } else { c = 6; }

// Wrong: else branch sets d, not c — c unset on one path
if (b) { c = 5; } else { d = 6; }   // ← c may be uninitialised
```

---

### 3. Control Flow Analysis

Builds a **Control Flow Graph (CFG)** of the programme:
- **Nodes** = basic blocks
- **Directed edges** = possible jumps between blocks
- **Entry block** = first executed; **Exit block** = last executed

The CFG enables analysis of which paths reach which code.

**Example — interrupt mishandling (Linux kernel driver):**

```c
save_flags(flags);
cli();                        // ← interrupts DISABLED
if ((bh = sh->buffer_pool) == NULL)
    return NULL;              // ← exits with interrupts STILL DISABLED (bug!)
sh->buffer_pool = bh->b_next;
restore_flags(flags);         // ← only reached on non-null path
```

Control flow analysis tracks interrupt state as `{enabled, disabled}` across all CFG paths. The early-return path has state `disabled` at the exit block — flagged as a bug.

**False positives in control flow:**
```c
if (condition_A) { cli(); }
if (condition_B) { restore_flags(flags); }
```
If the tool cannot determine that `condition_A` and `condition_B` are correlated, it may conservatively flag the second `if` as a potential "restore without disable" — a **false positive**.

---

### 4. Abstract Interpretation

**Abstract interpretation** performs a **partial execution** of the programme using an abstract domain — a simplified model of values that captures the properties of interest without computing exact values.

**Key property — soundness:**
- The analysis may **overestimate** possible behaviours (can produce false positives)
- It never **underestimates** — if the tool says "no error of type X here," there genuinely are none (no false negatives for the checked property)

**Example — division by zero:**

```python
def f(x, y):
    return x / y
```

Abstract interpretation: "A division by zero **may** occur here" (if `y` could be 0 on any call path). This is conservative — a false positive if the caller always passes `y ≠ 0`. But sound — if the tool says "no division by zero possible," it cannot occur on any path.

**Application:** Inside compilers (safety checks for optimisations) and for certification of safety-critical software.

---

### 5. Model Checking

**Model checking** verifies whether a model of the programme satisfies a formal property expressed in logic.

**Properties it can verify:**
- "Method A never calls Method C directly" — architectural invariant
- "Every method that acquires a lock eventually releases it" — liveness property
- "No path leads to privilege escalation" — security property

**Logics used:**

| Logic | Purpose |
|---|---|
| **Temporal logic** | Properties over sequences of states ("eventually," "always," "until") |
| **Hoare logic** | Preconditions and postconditions for individual functions |

**Not limited to software** — model checking applies to hardware, network protocols, and state machines.

---

### 6. Theorem Proving (Most Powerful)

**Theorem proving** mathematically proves that annotated properties hold across all possible executions.

- Requires **formal specifications** written as annotations in the source (e.g., JML for Java, Dafny, ESC/Java 2)
- The tool **proves** the annotated properties hold — not just checks heuristically
- **Sound and complete** for the specified properties (no false positives or negatives within scope)
- **Labor-intensive** — writing and maintaining formal specifications is expensive
- **Practical use:** Safety-critical systems only — avionics, medical devices, cryptographic protocol implementations, operating system kernels

---

## False Positives vs. False Negatives

| Term | Definition | Risk |
|---|---|---|
| **False positive** | Tool complains about a non-error | "Alert fatigue" — developers ignore the tool |
| **False negative** | Tool misses a real error | Invisible; real vulnerability ships to production |

There is an inherent **trade-off**: reducing false negatives (higher coverage) typically increases false positives, and vice versa. The right balance depends on the use case.

> **Alert fatigue is a real failure mode.** If a tool generates too many false positives, developers suppress all warnings without investigation — defeating the purpose of the tool.

---

## Abstract Interpretation vs. Model Checking vs. Theorem Proving

| Technique | Soundness | False Positives | False Negatives | Effort | Scale |
|---|---|---|---|---|---|
| Pattern Matching | No | Yes | Yes | Low | Any |
| Data Flow | Partial | Yes | Some | Low-medium | Industrial |
| Control Flow | Partial | Yes | Some | Low-medium | Industrial |
| Abstract Interpretation | Sound | Yes | No (for checked prop.) | Medium | Industrial |
| Model Checking | Sound | Yes | No | High | Medium |
| Theorem Proving | Sound + Complete | No | No | Very high | Small / critical |

---

## Criteria for a Successful Static Analysis Tool

1. **Acceptable false positive rate** — too many false positives cause developers to suppress all warnings without investigation
2. **Not too many warnings** — overwhelming output drives users away from the tool
3. **Good error reporting** — each finding must include context, the trace leading to the error, and a clear explanation
4. **Bugs should be easy to fix** — the tool should identify the root cause, not just the symptom
5. **Teachable / adjustable** — developers must be able to:
   - **Suppress false positives** with justification annotations
   - **Add design intent** (assertions, contracts) to help the tool reason more precisely

---

## Limitations

### The Heap Challenge

The heap is a **dynamic structure** that changes at runtime:
- Most static tools **disregard the heap** or model it coarsely
- **False positives:** Tool flags heap operations as unsafe when they are safe at runtime
- **False negatives:** Tool misses heap-based vulnerabilities (use-after-free, null pointer dereference through dynamically allocated structures)

### Other Limitations

- Cannot reason about **external inputs** or runtime environment (OS, network, hardware state)
- Cannot detect **logical flaws** that require business-domain understanding
- Cannot detect all security issues — a human security review remains necessary for high-assurance systems

---

## Static Analysis Tools Reference

| Tool | Language / Platform | Focus |
|---|---|---|
| **Coverity** | C, C++, Java | Deep bug finding including security flaws |
| **Fortify (HP/Micro Focus)** | C/C++, Java, Python, and more | Enterprise security SAST |
| **Checkmarx** | Multi-language | Cloud SAST with CI/CD integration |
| **Veracode** | Multi-language | SAST + SCA (Software Composition Analysis) |
| **SonarQube** | Multi-language | Code quality and security; integrates with CI/CD |
| **Semgrep** | Multi-language | Lightweight pattern-based; easy custom rules |
| **Bandit** | Python | Security-focused; OWASP rules |
| **ESLint + security plugins** | JavaScript / TypeScript | Lint + security checks |
| **CodeQL** | Multi-language | Semantic analysis; GitHub Advanced Security |
| **FindBugs / SpotBugs** | Java | Bug pattern detection |
| **CheckStyle** | Java | Style and convention checking |
| **ESC/Java 2** | Java | Extended static checking with formal annotations |

Labs covered in ICT2216: ESLint + SARIF (Lab 8), CodeQL (Lab 8), SonarQube (Lab 9).

---

## Circular Initialisation — Abstract Interpretation Example

```java
class A { static int a = B.b + 1; }
class B { static int b = A.a + 1; }
```

Abstract interpretation using a domain that distinguishes **undefined** from **defined** values detects that one class must read the other's field before it is initialised — a **circular static initialisation** bug that causes unpredictable values at runtime.

---

## See Also

- [[concepts/security-testing-and-verification]] — testing pyramid, ASVS, WSTG, penetration testing methodologies
- [[examples/ict2216-lab8-static-code-analysis]] — ESLint + SARIF + CodeQL in practice
- [[examples/ict2216-lab9-sonarqube]] — SonarQube setup and dashboard
- [[sources/ICT2216-lecture-9-static-code-analysis]] — source page with case studies
