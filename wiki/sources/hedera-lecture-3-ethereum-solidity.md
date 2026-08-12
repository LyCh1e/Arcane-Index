---
type: source
title: "Hedera Developer Course — Lecture 3: Ethereum History, EVM & Solidity"
tags: [ethereum, EVM, solidity, smart-contracts, turing-completeness, NFTs, DeFi, gas, sustainability, proof-of-stake, proof-of-work, Vitalik-Buterin, Alan-Turing]
domain: blockchain
source-file: "raw/Blockchain_Lecture3.md"
author: "Hendrik Ebbers (OpenElements / Swirlds Labs / Hedera)"
format: lecture-slides
slides: 95
ingested: 2026-08-12
status: ingested
related-concepts:
  - "[[concepts/ethereum-evm]]"
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/blockchain-technology]]"
  - "[[concepts/bitcoin-history]]"
---

# Hedera Developer Course — Lecture 3: Ethereum History, EVM & Solidity

**Source:** `raw/Blockchain_Lecture3.md`
**Author:** Hendrik Ebbers — OpenElements / Swirlds Labs / Hedera
**Format:** 95 lecture slides (converted from `raw/Blockchain Lecture-3.pdf`)
**Part of:** Three-part Hedera Developer Course (Java + Solidity)

---

## Ethereum History (Slides 1–17)

### Origin

In 2013, **Vitalik Buterin** published the whitepaper *"Ethereum: A Next Generation Smart Contract & Decentralized Application Platform"*. The network launched and began operation in **2015**.

The oft-cited (if slightly tongue-in-cheek) origin story:

> "I happily played World of Warcraft during 2007–2010, but one day Blizzard removed the damage component from my beloved warlock's Siphon Life spell. I cried myself to sleep, and on that day I realised what horrors centralised services can bring." — Vitalik Buterin

The lecture notes this quote is real but "maybe not 100% serious" — presented as a memorable illustration of the centralised-authority problem.

### Ethereum vs Bitcoin

| Dimension | Bitcoin | Ethereum |
|-----------|---------|----------|
| Primary purpose | Platform to trade a digital currency | Platform to do (nearly) anything |
| Key differentiator | Fixed scripting language (non-Turing complete) | Ethereum Virtual Machine (EVM) — Turing complete |
| Native asset | BTC | Ether (ETH) |
| Launched | 2009 | 2015 |

The EVM is what makes Ethereum fundamentally different: it can execute arbitrary code (smart contracts) on the network, not merely validate transfers.

### Ethereum as a Public Ledger

Ethereum is a **public ledger** — a transparent, immutable record accessible to all:

| Property | Description |
|----------|-------------|
| **Transparency** | All transactions are visible to all network participants |
| **Auditability** | Transactions can be easily audited and verified, reducing fraud risk |
| **Accessibility** | Anyone with internet access can view the ledger |

---

## Alan Turing and Turing Completeness (Slides 8–14)

### Alan Turing

| Fact | Detail |
|------|--------|
| Nationality | British |
| Fields | Mathematics, cryptanalysis, computer science |
| Known as | Father of theoretical computer science and artificial intelligence |
| WWII contribution | Broke the German Enigma code at Bletchley Park — significantly contributed to the Allied war effort |

### The Turing Machine (1936)

A theoretical device that manipulates symbols on a strip of tape according to a set of rules. Despite its simplicity, it is capable of implementing any computer algorithm — given endless time and memory. This conceptual framework laid the groundwork for the modern theory of computation and algorithms.

### Turing Completeness

**Definition:** The ability for a computational model to simulate a Turing machine. A Turing-complete programming language is theoretically capable of expressing all tasks accomplishable by computers.

- All modern programming languages are Turing complete
- The EVM is Turing complete — it can execute any algorithm
- The language used to write smart contracts (e.g. Solidity, Vyper) must therefore also be Turing complete

### The Turing Test (1950)

Originally called the **Imitation Game**. Criterion: if a human cannot tell whether a conversational partner is a machine or a human, the machine passes the test. First proposed as a philosophical benchmark for artificial intelligence.

---

## Ethereum Use Cases (Slides 16–17)

| Use Case | Description |
|----------|-------------|
| **DeFi** | Decentralised Finance — lending, borrowing, trading without intermediaries |
| **NFTs** | Non-Fungible Tokens — unique ownership certificates for digital assets |
| **Supply Chain Management** | Transparent, immutable provenance tracking |
| **Identity Verification** | Self-sovereign identity without centralised identity providers |
| **Voting Systems** | Tamper-evident, transparent on-chain governance |
| **DAOs** | Decentralised Autonomous Organisations — governance by token holders |
| **Gaming / Virtual Worlds** | Ownership of in-game assets (e.g. Axie Infinity) |
| **Real Estate** | Tokenised property ownership and fractional investment |
| **Healthcare** | Patient data consent management and cross-institution record sharing |
| **Legal & Compliance** | Smart contract-enforced legal agreements |
| **IP & Royalties** | Automated royalty distribution to creators |

### NFT Example — Axie Infinity

The lecture uses Axie Infinity as its NFT case study: each Axie is a unique digital creature with traits determined by body parts, ancestor "DNA", colour, and face expression. Axies were trading on OpenSea at prices ranging from $651 to $909+. The lecture also references the **Axie Infinity Ronin bridge hack** (one of the largest DeFi exploits, ~$625M).

---

## Sustainability (Slides 27–36)

### Bitcoin Energy Consumption

Bitcoin's proof-of-work network consumes sufficient electricity to power all tea kettles in the UK for **30 years** (continuous boiling). Reference: Cambridge Bitcoin Electricity Consumption Index (CBECI) — ccaf.io/cbnsi/cbeci.

### Ethereum: The Merge (PoW → PoS)

| Metric | Ethereum 1.0 (Proof of Work) | Ethereum 2.0 (Proof of Stake) |
|--------|------------------------------|-------------------------------|
| Yearly electricity | 22,000,000 TWh | 2,000 MWh |
| Annual CO₂ | 10,000,000 t | 650 t |
| Reduction factor | baseline | ~99.99% reduction in energy; ~99.99% reduction in CO₂ |

The Merge reduced Ethereum's energy consumption by approximately four orders of magnitude.

### Network Energy Comparison

| Network | Yearly electricity |
|---------|--------------------|
| PayPal | 0.28 TWh |
| Netflix | 0.45 TWh |
| YouTube | 12 TWh |
| Bitcoin | 131 TWh |
| **Ethereum (post-Merge)** | **0.0026 TWh** |

Post-Merge Ethereum consumes less electricity than PayPal by two orders of magnitude.

---

## Smart Contracts and the EVM (Slides 37–55)

### Smart Contract Concept

The lecture illustrates smart contracts via a **gambling example**:

- Alice deposits 100 ETH; Bob deposits 100 ETH
- The smart contract holds funds autonomously — no Carol/escrow needed
- The contract automatically pays out 199.99 ETH to the winner based on defined logic
- No human intermediary can intercept funds or alter the outcome

This demonstrates the core value: a smart contract enforces rules exactly as coded, with no ability for any party to override or modify execution once deployed.

### Ethereum as a State Machine

Ethereum is a **distributed state machine**:

```
World State σt  →  [Transaction]  →  World State σt+1
```

The world state is a large data structure containing all accounts and balances, plus machine state. The EVM defines the specific rules for how state changes from block to block.

```
World State
├── Address 1 → Account State 1
├── Address 2 → Account State 2
└── Address 3 → Account State 3
```

### EVM Architecture

| Component | Description |
|-----------|-------------|
| **Program Counter (PC)** | Defines which OpCode executes next; normally incremented by 1 byte; `JUMP` changes it specifically |
| **Stack** | Max 1,024 elements; top element = current call context; familiar via Java stack traces |
| **OpCodes** | Low-level instructions the EVM executes; each has a fixed gas cost |

### EVM OpCodes (Sample)

| Hex | Name | Gas | Operation |
|-----|------|-----|-----------|
| `00` | STOP | 0 | Halt execution |
| `01` | ADD | 3 | `a, b → a + b` (uint256 addition mod 2²⁵⁶) |
| `02` | MUL | 5 | `a, b → a × b` (uint256 multiplication mod 2²⁵⁶) |
| `03` | SUB | 3 | `a, b → a - b` (uint256 subtraction mod 2²⁵⁶) |
| `04` | DIV | 5 | `a, b → a // b` (uint256 integer division) |
| `05` | SDIV | 5 | `a, b → a // b` (int256 signed division) |
| `06` | MOD | 5 | `a, b → a % b` (uint256 modulus) |
| `07` | SMOD | 5 | `a, b → a % b` (int256 signed modulus) |

### Gas

When creating a transaction, a **gas limit** must be specified — the maximum gas the transaction may consume. If execution exceeds the limit, it is aborted:

```
transaction failed pre-check with the status `INSUFFICIENT_GAS`
```

Gas serves two purposes: it prevents infinite loops (the halting problem: a Turing-complete system cannot determine in advance whether a programme halts) and it fairly prices computation and storage on the shared network.

---

## Solidity Introduction (Slides 56–72)

### EVM Languages

| Language | Extension | Notes |
|----------|-----------|-------|
| Solidity | `.sol` | Most popular; JavaScript/C++–influenced |
| Vyper | `.vy` | Python-influenced; security-focused |
| YUL / YUL+ | `.yul` | Intermediate language; close to opcodes |
| FE | `.fe` | Experimental; Rust-influenced |

All compile to EVM bytecode for deployment.

### Compilation

```bash
# Install locally (brew, npm, or binary)
solc --bin -o build/contracts contracts/hello_world.sol
#         ^output format ^output dir  ^input file

# Or via Docker (no local install needed)
docker run -v $(pwd)/contracts:/contracts ethereum/solc:stable \
  -o /contracts/output --bin
```

### Hello World

```solidity
pragma solidity ^0.8.20;

contract HelloWorld {
    string public greet = "Hello World!";
}
```

### Coin Contract (Full Annotated Example)

```solidity
pragma solidity >= 0.7.0;       // version pragma — compiler version constraint

contract Coin {
    address public minter;                          // state variable — persists on-chain
    mapping (address => uint) public balances;      // map: address → token balance

    event Sent(address from, address to, uint amount);  // event — emitted to log

    constructor() {                                 // runs once on deployment
        minter = msg.sender;                        // deployer becomes the minter
    }

    function mint(address receiver, uint amount) public {
        require(msg.sender == minter);              // only the minter can mint
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        require(amount <= balances[msg.sender]);    // guard: sufficient balance
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);    // emit the event
    }
}
```

This contract introduces all the core Solidity constructs:

| Construct | Keyword / Example | Purpose |
|-----------|-------------------|---------|
| Version pragma | `pragma solidity >= 0.7.0` | Constrains the compiler version |
| Contract | `contract Coin { }` | Top-level container; equivalent to a class |
| State variable | `address public minter` | Persistent on-chain storage |
| Mapping | `mapping (address => uint)` | Hash map from key type to value type |
| Event | `event Sent(...)` | Emitted to the EVM log; cheap storage for off-chain consumers |
| Constructor | `constructor()` | Runs once at deployment |
| Function | `function mint(...) public` | Callable method |
| `require` | `require(condition)` | Reverts if false — precondition guard |
| `msg.sender` | Global | Address of the account that called the function |
| `emit` | `emit Sent(...)` | Fires the event |

---

## Solidity Part 2 — Deployment and Language Reference (Slides 73–95)

### Smart Contract Deployment Lifecycle

```
1. Write the contract in Solidity
         ↓
2. Compile with solc → binary (.bin)
         ↓
3. Deploy to the ledger → unique contract address returned
         ↓
   Constructor executes (owner = msg.sender)
         ↓
   One persistent instance lives at that address forever
```

Key points:
- Each deployment creates a **new independent instance** with a unique address
- Deploying the same `.sol` file three times produces three separate contracts at three different addresses
- The contract instance is a **singleton** — there will only ever be one instance at that address on that network
- The instance **holds state** — its storage variables persist between function calls

### Solidity Language Reference

#### Functions

```solidity
contract MyContract {
    // basic function with visibility
    function hello() public { }

    // function with parameters
    function hello(int amount) public { }
    function calculate(int a, int b) public { }

    // function with return type
    function getCount() public returns (int) { }
    function isActive() public returns (bool) { }
}
```

Visibility modifiers: `public` (callable by anyone), `private` (only within the contract); `internal` and `external` covered in later slides.

#### Value Types

| Type | Notes |
|------|-------|
| `bool` | `true` / `false` |
| `int` / `uint` | Signed / unsigned; sized variants: `int8`, `int16`, … `int256`; default `int` = `int256` |
| Fixed-point numbers | `&` (partially supported; use with caution) |
| `address` | 20-byte Ethereum address; supports `.transfer()`, `.call()` |
| Byte arrays (fixed) | `bytes1` … `bytes32` |
| Byte arrays (dynamic) | `bytes` |
| `enum` | User-defined enumeration |

#### Reference Types

| Type | Description |
|------|-------------|
| `array` | Fixed-size or dynamic-size list |
| `mapping` | Hash map: `mapping(KeyType => ValueType)` |
| `struct` | Custom composite type |

#### Control Structures

```solidity
if (condition) { } else { }
while (condition) { }
do { } while (condition);
for (uint i = 0; i < n; i++) { }
break;
continue;
return value;
```

#### Error Handling

| Mechanism | Behaviour |
|-----------|-----------|
| `require(condition, "message")` | Reverts state if condition is false; used for input validation and access control |
| `revert("message")` | Unconditionally revert with a message |
| `try / catch` | Handle errors from external calls and contract creation |
| State-reverting | All state changes in a failed transaction are rolled back atomically |

#### Modifiers

```solidity
modifier onlyOwner() {
    require(msg.sender == owner);
    _;   // placeholder — the modified function body runs here
}

function adminAction() public onlyOwner {
    // only owner can call this
}
```

Modifiers are reusable precondition blocks applied to functions.

#### Advanced Patterns (Slides 94–95)

| Pattern | Resource |
|---------|----------|
| Delegate call | solidity-by-example.org/delegatecall |
| Calling other contracts | solidity-by-example.org/calling-contract |
| Inheritance | Solidity docs — `contracts.html#inheritance` |
| `using for` (structs) | Solidity docs — `contracts.html#using-for` |
| Libraries | Solidity docs — `contracts.html#libraries` |
| Import (local) | `import "./MyContract.sol";` |
| Import (Remix from GitHub) | `import "https://github.com/.../Contract.sol";` |

---

## Hands-On Exercises (Slides 55, 72)

| Exercise | Topic |
|----------|-------|
| Explain why gas is important | Gas as a metering mechanism; prevents halting problem; prices computation fairly |
| Benefit of a VM | Portability — identical execution on all nodes regardless of host OS; sandboxing |
| EVM vs JVM differences | EVM is deterministic + metered (gas); JVM has no gas and allows non-deterministic I/O; EVM stack is 1,024 elements max |
| Create a "Hello World" smart contract | `pragma solidity ^0.8.20; contract HelloWorld { string public greet = "Hello World!"; }` |
| Compile the contract without errors | `solc --bin -o build/contracts contracts/hello_world.sol` |

---

## Source Quality Assessment

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Technical accuracy | High | Ethereum history, EVM mechanics, and Solidity syntax align with official documentation |
| Currency | Medium | Solidity version examples use `^0.8.20` — current and relevant; sustainability data is pre-Merge era (2022 timeframe) for Ethereum 1.0 comparison |
| Bias | Low | Neutral introduction to Ethereum; critique of centralised services is balanced by the WoW disclaimer |
| Depth | Medium | Introductory to intermediate — covers EVM concepts and basic Solidity; advanced patterns referenced via external links |
| Practical value | High | Solidity hands-on exercises directly build toward the course's smart contract development track |

---

## Key Concepts Introduced

- [[concepts/ethereum-evm]] — Ethereum history, EVM architecture (state machine, OpCodes, gas, stack), Turing completeness, sustainability
- [[concepts/solidity-fundamentals]] — Solidity syntax, types, compilation, deployment lifecycle, contract structure
- [[concepts/blockchain-technology]] — Smart contracts and the EVM already covered at overview level; this lecture adds OpCode detail and sustainability data

---

## Related Pages

- [[sources/hedera-lecture-1-bitcoin-wallets]] — Lecture 1: Bitcoin history, wallets, digital currency taxonomy
- [[sources/hedera-lecture-2-blockchain-hashing]] — Lecture 2: block anatomy, hash chaining, cryptographic hash functions, Java blockchain
- [[concepts/ethereum-evm]] — Ethereum architecture, Turing completeness, EVM internals, sustainability
- [[concepts/solidity-fundamentals]] — Solidity language reference (full syntax, types, deployment, modifiers)
- [[concepts/blockchain-technology]] — Broader blockchain architecture, consensus mechanisms, UTXO vs account model
