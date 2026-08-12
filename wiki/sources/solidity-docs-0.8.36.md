---
type: source
title: "Solidity Language Documentation v0.8.36"
source: https://docs.soliditylang.org/en/v0.8.36/
fetched: 2026-08-12
domain: blockchain
tags: [solidity, smart-contracts, EVM, types, security, patterns, reference]
quality: primary — official language specification
related:
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/solidity-security]]"
  - "[[concepts/ethereum-evm]]"
---

# Source: Solidity Language Documentation v0.8.36

**URL:** https://docs.soliditylang.org/en/v0.8.36/  
**Type:** Official language specification  
**Fetched:** 2026-08-12  
**Content fetched from:** GitHub source (`ethereum/solidity` repository, v0.8.26 RST files) plus introduction page

---

## What This Source Covers

The official Solidity reference documentation, version 0.8.x. Covers the complete language from introductory contracts through the full type system, control structures, error handling, security considerations, common patterns, and the ABI/cheatsheet reference.

---

## Table of Contents (Major Sections)

| Section | Key topics |
|---------|-----------|
| Introduction to Smart Contracts | SimpleStorage, Coin/Subcurrency examples; Blockchain basics; EVM accounts, transactions, gas, storage/memory/stack |
| Types | Value types (bool, int/uint, address, bytes, enum, UDVT, function types, literals); Reference types (arrays, structs, mappings); data locations |
| Expressions & Control Structures | if/while/for/do, internal vs external calls, CREATE2, destructuring, scoping, `unchecked`, error handling |
| Contracts | Visibility, state variables, functions, modifiers, events, custom errors, inheritance, abstract contracts, interfaces, libraries, `using for` |
| Inline Assembly | Yul language, low-level EVM access |
| Cheatsheet | Block/transaction globals, address members, ABI encoding, type information, modifiers |
| Security Considerations | Reentrancy, gas limits, `tx.origin`, integer overflow, mapping deletion, checks-effects-interactions |
| Common Patterns | Withdrawal pattern, access restriction, state machine |
| 0.8.x Breaking Changes | Overflow revert by default, ABI coder v2 default, `byte` type removed, address literals non-payable, Panic vs invalid opcode |

---

## Key Concepts Extracted

### Smart Contract Fundamentals

- A **contract** is code residing at a blockchain address, containing state variables (persistent storage) and functions.
- Two account types on Ethereum: **External Accounts** (key-pair controlled) and **Contract Accounts** (code controlled). Both share 20-byte address space.
- **EVM**: Completely isolated sandbox. No network/filesystem/process access. Restricted inter-contract communication.

### Blockchain & Transaction Model

- Transactions represent globally shared database modifications requiring network consensus. They are atomic — all-or-nothing.
- **Gas**: Each EVM instruction costs gas. Out-of-gas triggers revert (state rolled back). Block gas limit caps total computation per block.
- **Storage** (persistent, expensive `SSTORE`) / **Memory** (fresh per call, linear) / **Stack** (max 1024 × 256-bit elements, only top 16 accessible).

### 0.8.x Breaking Changes (from 0.7.x)

| Change | Detail |
|--------|--------|
| Overflow/underflow | **Reverts by default**. Use `unchecked { }` for wrapping behaviour |
| ABI coder v2 | Default; stricter input validation; use `pragma abicoder v1` for old behaviour |
| `**` associativity | `a**b**c` now parses as `a**(b**c)` (right-associative) |
| `assert` failures | Now use `Panic(uint256)` revert opcode (not `invalid`); costs less gas |
| `byte` alias | Removed; use `bytes1` |
| Address literals | Have type `address` (not `address payable`); use `payable(addr)` to convert |
| Explicit conversions | Only one change of sign/width/category allowed per conversion |
| `tx.origin` / `msg.sender` | Now `address` type (not `address payable`) |

### Type System Highlights

**Value types** (copied on assignment):
- `bool`, `int8`…`int256`, `uint8`…`uint256`, `address`, `address payable`, `bytes1`…`bytes32`, `enum`, user-defined value types (UDVT), function types
- Integers: checked arithmetic by default; `type(T).min` / `type(T).max` for bounds
- `fixed`/`ufixed`: partially supported — avoid in production

**Reference types** (require data location annotation):
- `T[]` dynamic arrays, `T[k]` fixed arrays, `bytes`, `string`, `struct`, `mapping`
- Data locations: `storage` (persistent), `memory` (call-scoped copy), `calldata` (non-modifiable parameter area, most gas-efficient for read-only)

**Data location assignment rules**:
- Storage ↔ Memory/Calldata: always independent copy
- Memory → Memory: creates a reference (shared)
- Storage → local storage variable: reference (not copy)

### Error Handling Full Reference

| Mechanism | Error type | Gas behaviour | Use case |
|-----------|-----------|---------------|----------|
| `require(cond)` | `Error(string)` | Refunds unused gas | Input/precondition checks |
| `require(cond, "msg")` | `Error(string)` | Refunds unused gas | With human-readable reason |
| `revert CustomError(...)` | Custom error | Refunds unused gas | Structured error data, cheaper than strings |
| `assert(cond)` | `Panic(uint256)` | Refunds unused gas (v0.8+) | Internal invariants |
| `try / catch` | — | — | External call error recovery |

**Panic codes**: `0x01` assert, `0x11` overflow, `0x12` div-by-zero, `0x21` invalid enum, `0x31` pop empty array, `0x32` out-of-bounds, `0x41` too much memory, `0x51` zero internal function call.

### Security: Key Patterns

1. **Checks-Effects-Interactions**: validate → modify state → call external. Prevents reentrancy.
2. **Withdrawal pattern**: never push funds; let users pull. Isolates failure.
3. **Access restriction**: `modifier onlyOwner { require(msg.sender == owner); _; }` — composable, readable.
4. **State machine**: enum stages + `atStage(s)` modifier + `timedTransitions` modifier.
5. **`tx.origin` ban**: always use `msg.sender` for authentication.

### Global Variables (Cheatsheet)

**Block**: `block.number`, `block.timestamp`, `block.chainid`, `block.coinbase`, `block.gaslimit`, `block.basefee`, `block.prevrandao`, `blockhash(n)`  
**Transaction**: `msg.sender`, `msg.value`, `msg.data`, `msg.sig`, `tx.origin`, `tx.gasprice`, `gasleft()`  
**Crypto**: `keccak256()`, `sha256()`, `ripemd160()`, `ecrecover(hash, v, r, s)`, `addmod()`, `mulmod()`  
**ABI**: `abi.encode()`, `abi.encodePacked()`, `abi.encodeWithSelector()`, `abi.encodeWithSignature()`, `abi.encodeCall()`, `abi.decode()`  
**Contract**: `this`, `super`, `selfdestruct(payable)`, `type(C).name`, `type(C).creationCode`, `type(T).min/max`

---

## Source Quality Assessment

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Authority | ★★★★★ | Official Ethereum Foundation / Solidity core team documentation |
| Accuracy | ★★★★★ | Normative reference for compiler behaviour |
| Depth | ★★★★★ | Complete language specification |
| Freshness | ★★★★★ | v0.8.36 (fetched 2026-08-12) |
| Applicability | ★★★★★ | Directly applicable to Hedera HSCS (Besu EVM) |

---

## Wiki Pages Generated / Updated from This Source

- [[concepts/solidity-fundamentals]] — expanded with full type system, data locations, Panic codes, try/catch, common patterns, global variables cheatsheet, 0.8.x changes
- [[concepts/solidity-security]] — new page: security pitfalls and patterns
