---
type: concept
title: "Ethereum and the EVM"
domain: blockchain
complexity: high
tags: [ethereum, EVM, smart-contracts, Turing-complete, gas, OpCodes, state-machine, Vitalik-Buterin, Alan-Turing, proof-of-stake, proof-of-work, sustainability, NFT, DeFi, DAOs]
created: 2026-08-12
updated: 2026-08-12
status: established
related:
  - "[[concepts/blockchain-technology]]"
  - "[[concepts/solidity-fundamentals]]"
  - "[[concepts/bitcoin-history]]"
  - "[[concepts/cryptographic-hash-functions]]"
  - "[[concepts/hedera-network]]"
---

# Ethereum and the EVM

Ethereum is the second-generation blockchain platform that transformed distributed ledgers from a single-purpose currency system into a **general-purpose programmable infrastructure**. Its central innovation — the Ethereum Virtual Machine (EVM) — enables arbitrary code execution on a decentralised network, a capability Bitcoin's scripting language was explicitly designed to prevent.

---

## History

### Origin

| Event | Detail |
|-------|--------|
| **2013** | Vitalik Buterin publishes the Ethereum whitepaper: *"Ethereum: A Next Generation Smart Contract & Decentralized Application Platform"* |
| **2015** | Ethereum mainnet launches; the EVM begins executing smart contracts |
| **2022** | "The Merge" — Ethereum transitions from Proof of Work to Proof of Stake, reducing energy consumption by ~99.99% |

### The Founding Motivation

Buterin's frequently cited motivation is the experience of a **World of Warcraft Siphon Life spell nerf** by Blizzard in 2010:

> "I cried myself to sleep, and on that day I realised what horrors centralised services can bring."

This is presented in the Hedera Developer Course as a real quote but "maybe not 100% serious" — a memorable framing of the core blockchain argument: centralised authorities can arbitrarily change the rules, and users have no recourse. A smart contract, once deployed, cannot be altered by any party.

### Ethereum vs Bitcoin

| Dimension | Bitcoin | Ethereum |
|-----------|---------|----------|
| Design goal | Digital currency | General-purpose programmable platform |
| Scripting | Intentionally limited (non-Turing complete) | Turing-complete EVM |
| Native asset | BTC | Ether (ETH) |
| Consensus (current) | Proof of Work | Proof of Stake (post-Merge, 2022) |
| Smart contracts | Rudimentary (Bitcoin Script) | Full-featured (Solidity, Vyper, Yul, Fe) |
| State model | UTXO (Unspent Transaction Outputs) | Account-based (persistent balance + state) |

---

## Turing Completeness

### Alan Turing (1912–1954)

| Contribution | Detail |
|-------------|--------|
| **Turing Machine (1936)** | Theoretical device that manipulates symbols on a tape by a set of rules; capable of implementing any algorithm given unlimited time and memory; foundational to computation theory |
| **Enigma code-breaking** | WWII — Turing led the mathematical effort at Bletchley Park to break the German Enigma cipher, significantly shortening the war |
| **Turing Test (1950)** | The "Imitation Game" — if a human cannot distinguish a machine's responses from a human's, the machine is considered to exhibit intelligent behaviour |
| **Turing completeness** | A computational system that can simulate a Turing machine; capable of expressing any algorithm |

### Why Turing Completeness Matters for Ethereum

Bitcoin's scripting language is **intentionally non-Turing complete** — it cannot express loops or arbitrary computation. This is a security choice: it is easy to reason about whether a Bitcoin script will terminate and what it will cost.

The EVM is **Turing complete** — it can execute any algorithm. This makes it a general-purpose programmable platform, but introduces the **halting problem**: it is mathematically impossible to determine in advance whether an arbitrary programme will ever terminate. Ethereum's solution is **gas**: every operation has a cost, and every transaction specifies a maximum gas limit. If execution would exceed the limit, it is aborted. Gas transforms an undecidable problem into a bounded one.

---

## Ethereum as a Distributed State Machine

Ethereum is not merely a ledger — it is a **distributed state machine**:

```
World State σt  →  [Transaction]  →  World State σt+1
```

The **world state** is a large data structure containing:
- All account addresses and their balances
- Smart contract code and storage
- The machine state of any executing contract

The EVM defines the rules for valid state transitions. Every full node executes the same transactions independently and arrives at the identical next state — this is what makes the system trustless and verifiable.

### Account Model

```
World State
├── Address 1 → Account State 1  (balance, nonce, code, storage)
├── Address 2 → Account State 2
└── Address 3 → Account State 3  (contract: has code + storage)
```

Two account types:
- **Externally Owned Accounts (EOAs)** — controlled by a private key; no code; initiate transactions
- **Contract Accounts** — controlled by code; have storage; cannot initiate transactions (only respond to calls)

---

## The Ethereum Virtual Machine

### Architecture

| Component | Description |
|-----------|-------------|
| **Program Counter (PC)** | Tracks the next OpCode to execute; normally increments by 1 byte; `JUMP` and `JUMPI` alter it conditionally |
| **Stack** | LIFO data structure; max 1,024 elements; each element is 256 bits (32 bytes); all arithmetic and logic operates on the stack |
| **Memory** | Byte-addressable, volatile (reset per call); cheaper than storage |
| **Storage** | Persistent key-value store per contract (256-bit key → 256-bit value); the most expensive resource |
| **Call Data** | Read-only input data passed by the caller to the function |

### OpCodes

The EVM is a **stack-based virtual machine**: OpCodes pop operands from the stack and push results back. Each has a fixed **gas cost** that reflects its computational or storage burden.

| Hex | Name | Gas | Operation |
|-----|------|-----|-----------|
| `00` | STOP | 0 | Halt execution |
| `01` | ADD | 3 | `a, b → a + b` (uint256 mod 2²⁵⁶) |
| `02` | MUL | 5 | `a, b → a × b` (uint256 mod 2²⁵⁶) |
| `03` | SUB | 3 | `a, b → a − b` (uint256 mod 2²⁵⁶) |
| `04` | DIV | 5 | `a, b → a // b` (uint256 integer division) |
| `05` | SDIV | 5 | `a, b → a // b` (int256 signed division) |
| `06` | MOD | 5 | `a, b → a % b` (uint256 modulus) |
| `07` | SMOD | 5 | `a, b → a % b` (int256 signed modulus) |

Storage operations (`SSTORE`, `SLOAD`) cost hundreds to thousands of gas — reflecting that persistent state is the scarcest resource on a global shared ledger.

### Gas

```
Transaction cost = gas_used × gas_price
gas_price is denominated in gwei (10⁻⁹ ETH)
```

| Property | Detail |
|----------|--------|
| Gas limit | Set by the caller — maximum gas the transaction may consume |
| Gas used | Actual sum of OpCode costs during execution |
| Over-limit | Transaction aborted with `INSUFFICIENT_GAS`; state is reverted; gas already consumed is not refunded |
| Unused gas | Returned to the caller |
| Purpose | (1) Prevents infinite loops by bounding all computation; (2) Prices computation and storage fairly across the shared network |

### Smart Contract Execution Languages

| Language | Extension | Characteristics |
|----------|-----------|-----------------|
| **Solidity** | `.sol` | Most widely used; JavaScript/C++–influenced; object-oriented |
| **Vyper** | `.vy` | Python-influenced; security-focused; no inheritance, no modifiers (reduces attack surface) |
| **YUL / YUL+** | `.yul` | Intermediate assembly-like language; used in optimisation and formal verification |
| **FE** | `.fe` | Experimental; Rust-influenced; strong type safety |

All compile to EVM bytecode via the Solidity compiler (`solc`) or equivalent.

---

## Ethereum Use Cases

| Domain | Example Applications |
|--------|---------------------|
| **DeFi (Decentralised Finance)** | Uniswap (DEX), Aave (lending), MakerDAO (stablecoin DAI) |
| **NFTs** | Unique digital ownership — art, gaming assets (Axie Infinity), collectibles |
| **Supply Chain** | Immutable provenance from manufacturer to retailer |
| **Identity** | Self-sovereign identity; verifiable credentials |
| **Voting** | Tamper-evident on-chain governance and DAO voting |
| **DAOs** | Token-holder governance of protocols and treasuries |
| **Gaming** | True ownership of in-game assets; play-to-earn economies |
| **Real Estate** | Tokenised property; fractional ownership |
| **Healthcare** | Patient consent management; cross-institution records |
| **Legal & Compliance** | Self-executing legal agreements; escrow |
| **IP & Royalties** | Automated royalty splits on every resale |

### NFT Case Study: Axie Infinity

The lecture uses Axie Infinity as a concrete NFT example. Each Axie is a unique digital creature — its properties (body parts, "DNA" inherited from ancestors, colour, facial expression) are encoded as token metadata. NFTs like Axies were trading at $651–$909+ on OpenSea.

The **Axie Infinity Ronin bridge hack** is referenced — one of the largest DeFi exploits, in which the bridge securing cross-chain transfers was compromised, resulting in a ~$625 million loss.

---

## Sustainability — PoW vs PoS

### Bitcoin Energy Use

Bitcoin's proof-of-work network consumes electricity equivalent to powering **all UK tea kettles continuously for 30 years** (Cambridge Bitcoin Electricity Consumption Index — CBECI).

### Ethereum: The Merge (September 2022)

| Metric | Ethereum 1.0 (Proof of Work) | Ethereum 2.0 (Proof of Stake) | Reduction |
|--------|------------------------------|-------------------------------|-----------|
| Yearly electricity | ~22,000,000 TWh | ~2,000 MWh | ~99.9999% |
| Annual CO₂ | ~10,000,000 t | ~650 t | ~99.994% |

Proof of Stake replaced energy-intensive mining with **validator staking** (32 ETH stake required per validator). Validators are chosen pseudo-randomly weighted by stake, not by hash power.

### Cross-Network Comparison

| Network | Yearly electricity (TWh) |
|---------|--------------------------|
| PayPal | 0.28 |
| Netflix | 0.45 |
| YouTube | 12 |
| Bitcoin | 131 |
| **Ethereum (post-Merge)** | **0.0026** |

Post-Merge Ethereum consumes approximately 100× less electricity than PayPal.

---

## Ethereum as a Public Ledger

| Property | Description |
|----------|-------------|
| **Transparency** | All transactions visible to all network participants — anyone can inspect any account balance, contract code, or transaction history |
| **Auditability** | Easy to audit and verify transactions; reduces fraud risk at the protocol level |
| **Immutability** | Once confirmed, transactions cannot be altered or deleted |
| **Accessibility** | Anyone with internet access can read the ledger, submit transactions, or deploy contracts |

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/blockchain-technology]] | Ethereum is a public permissionless blockchain; overlaps on consensus (PoS section), smart contracts overview, account model, Layer 2 scaling; this page adds EVM internals, OpCode detail, and sustainability data |
| [[concepts/solidity-fundamentals]] | Solidity is the primary language for writing EVM smart contracts; compilation and deployment lifecycle documented there |
| [[concepts/bitcoin-history]] | Bitcoin and Ethereum are the two dominant blockchain platforms; Bitcoin = digital gold / currency platform; Ethereum = programmable platform; Ethereum's PoW energy vs Bitcoin's PoW energy discussed in sustainability section |
| [[concepts/cryptographic-hash-functions]] | Ethereum uses Keccak-256 (SHA-3 family) for block hashing, address derivation, and EVM `KECCAK256` opcode |
| [[concepts/hedera-network]] | Hedera supports the EVM via HSCS — the Hedera Smart Contract Service runs a Besu EVM instance; Solidity contracts deploy identically on Hedera as on Ethereum mainnet |
| [[sources/hedera-lecture-3-ethereum-solidity]] | Source lecture for this concept page |
