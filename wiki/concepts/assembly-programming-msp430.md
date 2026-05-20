---
type: concept
title: "Assembly Programming (MSP430)"
domain: computer-architecture
source: [[sources/ICT1011-computer-organisation-architecture]]
complexity: high
updated: 2026-05-13
tags: [concept, computer-architecture, msp430, assembly, modular-programming]
status: established
created: 2026-05-13
---

# Assembly Programming (MSP430)

Covers assembly language syntax, the full MSP430 instruction set, emulated (pseudo) instructions, and modular programming with the call stack.

---

## 1. Assembly Language Syntax

Each assembly statement has four columns:

```
label:    mnemonic    operand(s)    ; comment
LOOP:     ADD         R4, R5        ; R5 = R5 + R4
          JNZ         LOOP          ; repeat while R5 ≠ 0
```

| Column | Required? | Notes |
|--------|-----------|-------|
| Label | Optional | Identifies address for jumps/branches; followed by `:` |
| Mnemonic | Required | Instruction or directive name |
| Operand(s) | Instruction-dependent | Format I: `src, dst`; Format II: `dst`; Format III: `offset` |
| Comment | Optional | Begins with `;` — ignored by assembler |

---

## 2. Assembler Directives

Directives control the assembler; they produce no executable machine code (except memory-initialising ones).

### Section Control

| Directive | Purpose |
|-----------|---------|
| `.text` | Subsequent code goes into the code (ROM) section |
| `.data` | Subsequent data goes into the initialised data section |
| `.sect "name"` | User-defined named section |
| `.bss symbol, size` | Reserve `size` bytes of uninitialised RAM (zero-filled) |
| `.usect "name", size` | User-defined uninitialised section |

### Memory Initialisation

| Directive | Purpose |
|-----------|---------|
| `.byte val[, val…]` | Place one or more bytes at current location |
| `.word val[, val…]` | Place one or more 16-bit words at current location |
| `.string "text"` | Place ASCII bytes + null terminator |
| `.space N` | Reserve N bytes (uninitialised) |

### Symbol Control

| Directive | Purpose |
|-----------|---------|
| `.equ symbol, value` | Define a constant (no memory allocated) |
| `.set symbol, value` | Same as `.equ` (reassignable) |

### Library / Linking

| Directive | Purpose |
|-----------|---------|
| `.global symbol` | Make symbol visible outside this file |
| `.ref symbol` | Reference a symbol defined in another file |
| `.def symbol` | Define symbol as exported |
| `.end` | Marks end of source file |

---

## 3. Two-Pass Assembly

The assembler makes two passes over the source file to resolve forward references (labels used before they are defined):

| Pass | Action |
|------|--------|
| **Pass 1** | Scan all labels → build the **symbol table** (maps each label to its address) |
| **Pass 2** | Generate **machine code** using the symbol table to fill in all address references |

```
Source: JMP DONE    ; DONE not yet seen → unknown in Pass 1
        ADD R4, R5
DONE:   NOP

Pass 1: symbol table → DONE = address 0x4404 (for example)
Pass 2: JMP DONE → JMP 0x4404 (encodes as Format III jump offset)
```

---

## 4. Executable Instructions

### 4.1 Data Transfer

| Instruction | Operation | Flags |
|-------------|-----------|-------|
| `MOV src, dst` | dst ← src | None affected |
| `SWPB dst` | Swap bytes of dst (8-bit halves) | None |
| `SXT dst` | Sign-extend byte to word | N, Z |

> `MOV` is the workhorse — it does not affect any flags, unlike `ADD`.

### 4.2 Arithmetic

| Instruction | Operation | Notes |
|-------------|-----------|-------|
| `ADD src, dst` | dst ← dst + src | Sets N, Z, C, V |
| `ADDC src, dst` | dst ← dst + src + C | Add with carry (multi-precision) |
| `SUB src, dst` | dst ← dst − src | Implemented as ADD + ~src + 1 |
| `SUBC src, dst` | dst ← dst − src − ~C | Subtract with borrow |
| `DADD src, dst` | BCD add with carry | Decimal arithmetic |

### 4.3 Logical / Bitwise

| Instruction | Operation | Typical Use |
|-------------|-----------|------------|
| `AND src, dst` | dst ← dst AND src | Mask / clear bits |
| `BIS src, dst` | dst ← dst OR src | Set bits (Bit Set) |
| `XOR src, dst` | dst ← dst XOR src | Toggle bits |
| `BIC src, dst` | dst ← dst AND ~src | Clear specific bits (Bit Clear) |

### 4.4 Rotation / Shift

| Instruction | Operation | Notes |
|-------------|-----------|-------|
| `RRC dst` | Rotate right through carry | LSB → C; old C → MSB |
| `RLC dst` | Rotate left through carry | MSB → C; old C → LSB |
| `RRA dst` | Arithmetic right shift | MSB preserved (sign fill) |

### 4.5 Comparison

| Instruction | Operation | Notes |
|-------------|-----------|-------|
| `CMP src, dst` | dst − src | Sets flags only, no result written |
| `BIT src, dst` | dst AND src | Sets flags only (bit test) |

### 4.6 Control Flow — Jump Instructions

| Mnemonic | Condition | Meaning |
|----------|-----------|---------|
| `JEQ` / `JZ` | Z = 1 | Jump if equal / zero |
| `JNE` / `JNZ` | Z = 0 | Jump if not equal / not zero |
| `JC` | C = 1 | Jump if carry (unsigned ≥) |
| `JNC` | C = 0 | Jump if no carry (unsigned <) |
| `JN` | N = 1 | Jump if negative |
| `JGE` | N ⊕ V = 0 | Jump if greater or equal (signed) |
| `JL` | N ⊕ V = 1 | Jump if less (signed) |
| `JMP` | Always | Unconditional jump |

All jumps use a **10-bit signed offset** added to the PC after fetch. Range: −512 to +511 words (±1 KB).

### 4.7 Stack and Subroutine

| Instruction | Operation |
|-------------|-----------|
| `PUSH src` | SP ← SP − 2; Mem[SP] ← src |
| `CALL dst` | SP ← SP − 2; Mem[SP] ← PC+2; PC ← dst |
| `RETI` | Pop SR then PC from stack (interrupt return) |

---

## 5. Emulated (Pseudo) Instructions

Emulated instructions are convenience mnemonics that the assembler translates into one or two core instructions. They introduce no new opcodes.

| Emulated | Translates To | Effect |
|----------|--------------|--------|
| `NOP` | `MOV R3, R3` | No operation |
| `CLR dst` | `MOV #0, dst` | Clear to zero |
| `INC dst` | `ADD #1, dst` | Increment |
| `DEC dst` | `ADD #-1, dst` | Decrement |
| `INV dst` | `XOR #-1, dst` | Bitwise invert |
| `TST dst` | `CMP #0, dst` | Test (sets flags) |
| `SETC` | `BIS #1, SR` | Set carry flag |
| `CLRC` | `BIC #1, SR` | Clear carry flag |
| `SETZ` | `BIS #2, SR` | Set zero flag |
| `CLRZ` | `BIC #2, SR` | Clear zero flag |
| `SETN` | `BIS #4, SR` | Set negative flag |
| `CLRN` | `BIC #4, SR` | Clear negative flag |
| `EINT` | `BIS #8, SR` | Enable interrupts (GIE=1) |
| `DINT` | `BIC #8, SR` | Disable interrupts (GIE=0) |
| `RET` | `MOV @SP+, PC` | Return from subroutine |
| `BR dst` | `MOV dst, PC` | Branch (wide jump, any address) |
| `POP dst` | `MOV @SP+, dst` | Pop from stack |

---

## 6. Modular Programming

### 6.1 The Stack

The MSP430 stack grows **downward** (towards lower addresses). SP always points to the last-pushed value (top of stack).

```
Push:  SP ← SP − 2;  Mem[SP] ← value    (pre-decrement)
Pop:   value ← Mem[SP];  SP ← SP + 2    (post-increment)
```

### 6.2 CALL and RET

```
CALL subroutine:
    1. SP ← SP − 2
    2. Mem[SP] ← PC + 2   (return address = address of next instruction)
    3. PC ← subroutine address

RET (= MOV @SP+, PC):
    1. PC ← Mem[SP]
    2. SP ← SP + 2
```

> `CALL` and `RET` are exact inverses. The return address is always the instruction immediately after the `CALL`.

### 6.3 Parameter Passing Methods

Three strategies, each with trade-offs:

| Method | Mechanism | Pros | Cons |
|--------|-----------|------|------|
| **Registers** | Place args in R4, R5, … before CALL | Fast, no memory access | Limited to number of registers; registers tied up |
| **Memory block** | Place args in a fixed memory block; pass address | Can pass many args | Not re-entrant; no recursion |
| **Stack** | PUSH args before CALL; function reads from SP+offset | Fully general, supports recursion | Slower; must manage offsets carefully |

**Pass by value**: a copy of the data is passed. The callee cannot modify the caller's original.

**Pass by reference**: the address of the data is passed. The callee can read and write the original.

### 6.4 Stack Frame and Local Variables

To allocate local variables inside a subroutine, decrement SP by the required bytes at function entry and restore it at exit:

```asm
my_func:
    PUSH    R4              ; save callee-saved registers
    SUB     #4, SP          ; reserve 4 bytes for 2 local words

    ; local var at 0(SP), next at 2(SP)
    MOV     #0, 0(SP)
    MOV     #1, 2(SP)

    ; ... function body ...

    ADD     #4, SP          ; deallocate locals
    POP     R4              ; restore register
    RET
```

Stack frame layout (typical, grows downward):

```
Higher address  ──────────────────
                  caller's data
                  ...
                  argument N
                  argument 1
                  return address   ← pushed by CALL
                  saved registers  ← pushed by callee
                  local variables  ← SP decremented by callee
Lower address   ──────────────────  ← SP
```

---

## See Also

- [[concepts/computer-architecture-fundamentals|Computer Architecture Fundamentals]] — Von Neumann, MSP430 registers, ISA formats, addressing modes
- [[concepts/io-and-memory-systems|I/O Interfacing and Memory Systems]] — I/O techniques, memory technologies, paging
- [[sources/ICT1011-computer-organisation-architecture|ICT1011 Source Page]]
