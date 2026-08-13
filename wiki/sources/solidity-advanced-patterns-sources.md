---
type: source
title: "Solidity Advanced Patterns — Multi-Source Ingest"
fetched: 2026-08-12
domain: blockchain
tags: [solidity, smart-contracts, delegatecall, inheritance, libraries, using-for, imports, patterns]
quality: primary — official language specification + curated examples
related:
  - "[[concepts/solidity-advanced-patterns]]"
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/solidity-security]]"
---

# Source: Solidity Advanced Patterns — Multi-Source Ingest

**Fetched:** 2026-08-12

Eight reference pages covering advanced Solidity language features and code organisation. Grouped into one source index because all eight pages address the same curriculum topic (Solidity code reuse, inter-contract communication, and file organisation).

---

## Sources

| URL | Topic | Access method | Quality |
|-----|-------|--------------|---------|
| https://solidity-by-example.org/delegatecall/ | `delegatecall` | GitHub raw (`.sol` source file) | ★★★★★ |
| https://solidity-by-example.org/calling-contract/ | Calling contracts | GitHub raw (`.sol` source file) | ★★★★★ |
| https://docs.soliditylang.org/en/v0.8.23/contracts.html#inheritance | Inheritance | GitHub RST (`ethereum/solidity` v0.8.23) | ★★★★★ |
| https://docs.soliditylang.org/en/v0.8.23/contracts.html#using-for | `using for` | GitHub RST (`ethereum/solidity` v0.8.23) | ★★★★★ |
| https://docs.soliditylang.org/en/v0.8.23/contracts.html#libraries | Libraries | GitHub RST (`ethereum/solidity` v0.8.23) | ★★★★★ |
| https://docs.soliditylang.org/en/v0.8.23/solidity-by-example.html#modular-contracts | Modular contracts | GitHub RST (`ethereum/solidity` v0.8.23) | ★★★★★ |
| https://docs.soliditylang.org/en/v0.8.23/layout-of-source-files.html#importing-other-source-files | Imports | GitHub RST (`ethereum/solidity` v0.8.23) | ★★★★★ |
| https://remix-ide.readthedocs.io/en/latest/import.html#import-from-a-github-url | Remix GitHub imports | HTTPS (200 OK) | ★★★★☆ |

**Access notes:**
- `docs.soliditylang.org` returns HTTP 403 to automated clients. Content fetched from the `ethereum/solidity` GitHub repository (`raw.githubusercontent.com`) using the `v0.8.23` tag. Language semantics are identical to v0.8.36 for all topics covered here.
- `solidity-by-example.org` pages use client-side rendering (Svelte); the markdown index files contain template placeholders. Actual Solidity source files fetched directly from the `solidity-by-example/solidity-by-example.github.io` GitHub repository.

---

## Key Concepts Extracted

### Calling Contracts

Three patterns for inter-contract calls:
1. Pass a typed reference (`Callee _callee`) as a function parameter — compiler validates the ABI.
2. Cast an `address` to the contract type: `Callee callee = Callee(_addr);`.
3. Send Ether with a call using `{value: msg.value}` — target function must be `payable`.

Low-level `.call(abi.encodeWithSignature(...))` bypasses compile-time checks — only use when ABI is unknown at compile time.

### `delegatecall`

- Runs target contract's code in the **caller's storage context**.
- `msg.sender` and `msg.value` retain the caller's context, not the original EOA's.
- Storage layout (slot order) between caller and callee **must match exactly**.
- Foundation of the upgradeable proxy pattern and Solidity's library mechanism.

### Inheritance

- `virtual` = can be overridden; `override` = does override.
- Multiple inheritance resolved via **C3 linearisation** — list bases most base-like first.
- State variable shadowing is a **compiler error**.
- Visibility can only move from `external` → `public`; mutability can only become stricter.
- Constructor args: supply in the `is` list (constant) or in the derived constructor (dynamic).

### Libraries

- No state variables, no Ether, no inheritance, no `selfdestruct`.
- `internal` functions: inlined via `JUMP` — no separate deployment needed.
- `public`/`external` functions: called via `DELEGATECALL` — requires deployment and address linking.
- Call protection: compiler inserts an `ADDRESS` opcode guard that reverts if a state-modifying library function is called via regular `CALL`.

### `using for`

- `using LibraryName for TypeName` — attaches all non-private library functions as member methods.
- `using {f, g} for TypeName` — attaches specific free functions.
- `global` keyword at file level extends attachment to all importing files.
- First parameter of each function is treated as `self` (must be implicitly convertible to the target type).
- Can define custom operators (`+`, `-`, `*`, etc.) for user-defined value types.

### Imports

| Form | Syntax |
|------|--------|
| Simple (avoid) | `import "filename";` |
| Namespace | `import * as Name from "filename";` |
| Alias | `import "filename" as Name;` |
| Selective | `import {Foo, Bar as Baz} from "filename";` |

Remix accepts full GitHub URLs; always pin a release tag.

### Modular Contracts

Separate invariant logic into a library; the contract shell delegates to it via `using for`. Result: every call path shares one auditable function.

---

## Wiki Pages Generated from This Source

- [[concepts/solidity-advanced-patterns]] — new page covering all eight topics in depth with full code examples
