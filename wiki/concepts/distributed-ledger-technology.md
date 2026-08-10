---
type: concept
title: "Distributed Ledger Technology (DLT)"
domain: blockchain
maturity: established
tags: [DLT, blockchain, DAG, Hashgraph, Holochain, consensus, Hyperledger, Corda, permissioned, enterprise, decentralisation, IOTA, Hedera]
updated: 2026-08-10
created: 2026-08-10
---

# Distributed Ledger Technology (DLT)

## Core Definition

A **distributed ledger** is a database shared by multiple participants in which each participant maintains and updates a synchronised copy of the data. Unlike a traditional database controlled by a single administrator, no central authority owns the master record — all nodes hold an identical copy and reach agreement via a consensus protocol before any new entry is accepted.

The critical formal relationship: **all blockchains are DLTs, but not all DLTs are blockchains**. Blockchain is one specific implementation of the DLT concept; DAG, Hashgraph, and Holochain are equally valid implementations with different structural trade-offs.

---

## DLT vs. Traditional Databases vs. Blockchain

| Dimension | Traditional Database | Blockchain (DLT subset) | DLT (broader category) |
|-----------|---------------------|------------------------|------------------------|
| **Control** | Single administrator | Decentralised, no owner | Decentralised (degrees vary) |
| **Data structure** | Tables / rows | Linear chain of blocks | Varies by type |
| **Replication** | Optional, centralised | All nodes, full copy | All nodes, full copy |
| **Immutability** | Records can be updated or deleted | Append-only; tampering computationally expensive | Generally append-only; permissioned variants may allow correction |
| **Consensus** | ACID transactions, central authority | PoW / PoS / PBFT (by implementation) | Varies widely |
| **Trust model** | Trust the administrator | Trustless (cryptographic) | Varies |
| **Single point of failure** | Yes | No | No |
| **Performance** | Very high (thousands/ms) | Limited by consensus | Varies by DLT type |

---

## DLT Architecture: Core Components

Regardless of type, all DLTs share the following structural elements:

1. **Nodes** — Each participant runs software that stores the ledger, validates transactions, and communicates with peers. Nodes may be full (hold the complete ledger) or light (hold only block headers / proofs).

2. **Ledger** — The shared, append-only record of all transactions. Each node maintains an identical copy.

3. **Consensus mechanism** — The protocol that ensures all nodes agree on the current state of the ledger without requiring a central arbiter. This is the core technical differentiator between DLT types.

4. **Cryptography** — SHA-256 or equivalent hash functions link records (making tampering detectable), whilst public-key cryptography authenticates participants.

5. **Peer-to-peer (P2P) network** — Nodes communicate directly with neighbours via gossip protocols; there is no central server relaying messages.

6. **Smart contracts / chaincode** — Self-executing logic stored on the ledger that runs deterministically when triggered (present in Ethereum, Hyperledger Fabric, Corda, Hedera, etc.; absent in Bitcoin).

---

## DLT Taxonomy

### 1. Blockchain

The original DLT architecture, introduced by Bitcoin in 2009.

**Data structure:** A linear sequence of cryptographically-linked blocks. Each block contains a batch of transactions, a Merkle root of those transactions, the previous block's hash, and a nonce. Altering any block invalidates every subsequent block.

**Consensus:** Proof of Work (Bitcoin, pre-merge Ethereum), Proof of Stake (post-merge Ethereum, Cardano, Solana), PBFT variants (Hyperledger Fabric, Quorum).

**Key properties:**
- Strong immutability
- Global shared ledger visible to all participants (public) or to authorised participants (permissioned)
- Transaction throughput limited by block size and block time (Bitcoin: ~7 TPS; Ethereum: ~15–30 TPS; Layer 2 solutions: thousands of TPS)
- Sequential block production creates an inherent bottleneck

**Primary use cases:** Cryptocurrency, tokenised assets, NFTs, smart contract platforms, enterprise permissioned ledgers.

---

### 2. Directed Acyclic Graph (DAG)

**Data structure:** A graph in which each new transaction directly references and validates two (or more) prior transactions, rather than waiting to be included in a block. There are no miners, no blocks, and no block reward. The resulting structure is a directed graph with no cycles (hence acyclic).

**Consensus:** Transaction-based approval — each issuer validates two prior transactions before their own is accepted. As the network grows and more transactions validate previous ones, the graph converges on confirmed state.

**Key properties:**
- Feeless (no miner fees)
- Scales with usage: more transactions → more validators → higher throughput
- Eventual rather than immediate finality
- Well-suited to high-frequency, low-value transactions

**Performance:** DAG networks report sustained throughput of tens of thousands of TPS under load.

**Primary implementation:** IOTA (the Tangle) — designed specifically for machine-to-machine IoT microtransactions. Each IoT device both submits and validates transactions, replacing the miner role.

**Limitations:**
- Security assumptions change at low network load (few transactions → fewer validators)
- Finality is probabilistic, not absolute
- Less mature tooling and smart contract support than blockchain

---

### 3. Hashgraph

**Inventor:** Leemon Baird (Swirlds Inc.). The algorithm is patented, which limits its use to the Hedera Hashgraph network.

**Data structure:** A DAG of "gossip events" — records of information exchanges between nodes, not of transactions directly. The data structure records *who told whom what, and when*.

**Consensus:** "Gossip about gossip" + virtual voting via Asynchronous Byzantine Fault Tolerance (ABFT).
- Each node randomly selects neighbours and shares its complete event history ("gossip")
- Nodes log which information they received from whom (gossip *about* gossip)
- Using only this shared graph, each node can independently compute what a vote would have been, without actually sending votes — a process called *virtual voting*
- Result: ABFT-grade finality (the strongest achievable — secure even if up to one-third of nodes are actively malicious) without a single vote message being transmitted

**Key properties:**
- Claimed throughput: 250,000+ TPS (Hedera claims 10,000+ confirmed TPS in production)
- ABFT consensus: strongest formal security guarantee of any DLT type
- Fair ordering: timestamps are consensus-derived, preventing transaction reordering by individual nodes
- Patented — only available via Hedera Governing Council (39 global enterprises including Google, IBM, Boeing, Deutsche Telekom)

**Primary implementation:** Hedera Hashgraph — used for enterprise payments, tokenisation, and consensus service (verifiable timestamps for any data).

**Limitations:**
- Patent lock-in prevents open-source forks
- Governance is centralised in the Governing Council, contradicting pure decentralisation
- Smaller developer ecosystem than Ethereum or Hyperledger

---

### 4. Holochain

**Architecture:** Agent-centric, not ledger-centric. Rather than all nodes maintaining a single shared state, each participant runs their own local **source chain** (a personal hash chain of their actions). There is no global consensus and no globally shared ledger.

**Consensus model:** Replaced entirely by peer validation and a distributed hash table (DHT). When an agent takes an action, the resulting entry is stored in a shared DHT and validated by a random subset of peers. Rules are enforced by the application's DNA (the code defining valid actions), not by network-wide consensus.

**Key properties:**
- No global bottleneck — throughput scales per agent, independently
- No mining, no validators, no staking
- Every application runs in its own isolated execution context ("hApp")
- Radically different trust model: validity enforced at time of storage by DHT neighbours

**Primary use case:** Decentralised social applications, data sovereignty applications, peer-to-peer marketplaces where global consensus is unnecessary.

**Limitations:**
- Not suited to use cases requiring global ordering (financial settlement, currency issuance)
- Small ecosystem; significantly less production deployment than other types
- The absence of global consensus makes cross-application interoperability complex

---

### 5. Other Notable Architectures

| Architecture | Mechanism | Distinguishing Feature | Primary Platform |
|-------------|-----------|----------------------|-----------------|
| **Tempo (Radix)** | Logical clocks + sharded validator sets | Sharded ledger with deterministic conflict resolution | Radix DLT |
| **Block-DAG (Phantom/GhostDAG)** | DAG of blocks, not individual transactions | Maintains block structure while allowing parallel block production | Kaspa |
| **Tangle (IOTA 2.0)** | Tokenised Proof of Work + Committee | Self-governing, feeless, no coordinator | IOTA 2.0 / Shimmer |

---

## Consensus Mechanism Reference

| Mechanism | Used In | Energy | TPS Range | Fault Tolerance | Key Trade-off |
|-----------|---------|--------|-----------|-----------------|---------------|
| **Proof of Work (PoW)** | Bitcoin, Monero, Litecoin | Very high | 3–30 | 50% attacker resistance | Security at extreme energy cost |
| **Proof of Stake (PoS)** | Ethereum, Cardano, Solana | Very low | 15–65,000 | Depends on stake distribution | Capital at risk, not computation |
| **Delegated PoS (DPoS)** | EOS, Tron, BitShares | Very low | Thousands | Delegate collusion risk | Speed at cost of decentralisation |
| **PBFT / variants** | Hyperledger Fabric, Stellar | Low | Hundreds–thousands | Works up to ⅓ Byzantine nodes | Only suits small, known validator sets |
| **Raft** | Hyperledger Fabric (crash-tolerant) | Very low | High | Crash failures only; no Byzantine | Simpler but weaker than PBFT |
| **SmartBFT** | Hyperledger Fabric 3.0 | Low | High | ⅓ Byzantine tolerance | Production-grade BFT for enterprise |
| **ABFT (Hashgraph)** | Hedera | Low | 250,000+ claimed | ⅓ Byzantine tolerance (strongest) | Patented; closed governance |
| **DAG approval** | IOTA Tangle | Very low | Tens of thousands | Coordinator-dependent (IOTA 1.x) | Feeless but eventual finality |
| **DHT peer validation** | Holochain | Very low | Scales per agent | Assumes majority honest per DHT neighbourhood | No global ordering |

---

## Permission Models

DLTs are categorised along two independent axes, yielding four permission profiles:

```
                    PERMISSIONLESS         PERMISSIONED
                  ┌─────────────────┬─────────────────────┐
    PUBLIC        │  Bitcoin         │  Rare (contradictory │
  (anyone can     │  Ethereum        │  by design)          │
   read/submit)   │  Hedera          │                      │
                  ├─────────────────┼─────────────────────┤
    PRIVATE       │  Rare (obscures  │  Hyperledger Fabric  │
  (restricted     │  the point of   │  R3 Corda            │
   read access)   │  public DLT)    │  Quorum / Besu       │
                  └─────────────────┴─────────────────────┘
```

- **Public permissionless** — anyone can read the ledger, submit transactions, and participate in consensus. Maximum decentralisation. Use: censorship-resistant value transfer, open smart contract platforms.
- **Private permissioned** — only approved entities can join, transact, and validate. Consensus is fast (PBFT-class). Use: enterprise consortia, regulated financial markets, supply chain networks.

---

## Enterprise Permissioned DLT Platforms

### Hyperledger Fabric

Maintained by the Linux Foundation under the LF Decentralised Trust umbrella. The leading enterprise permissioned blockchain platform.

**Architecture:** Modular execute-order-validate pipeline:
1. **Execute** — Client submits transaction proposal to endorsing peers, who simulate chaincode execution and return signed responses
2. **Order** — Orderer nodes sequence the endorsed transactions into blocks via the consensus protocol (no transaction execution at this stage)
3. **Validate** — All committing peers validate the ordered block against endorsement policies and write to the ledger

**Key components:**

| Component | Role |
|-----------|------|
| **Peer nodes** | Store the ledger; execute and endorse transactions; anchor peers facilitate inter-organisation discovery |
| **Orderer nodes** | Provide consensus and block production; do not hold ledger state |
| **Channels** | Private sub-ledgers within a single Fabric network; only channel members see channel transactions; multiple channels can share infrastructure |
| **Chaincode** | Smart contracts written in Go, Java, or Node.js; deployed per-channel; define business logic and access control |
| **Membership Services Provider (MSP)** | PKI-based identity management; issues digital certificates to all participants; enables role-based access control |

**Consensus (Fabric 3.0, March 2024):**
- **SmartBFT** (recommended for production) — Byzantine Fault Tolerant; tolerates up to ⅓ malicious orderer nodes
- **Raft** — Crash Fault Tolerant; simpler; does not handle actively malicious nodes
- **Solo** — Single orderer; testing only

**Privacy:** Channels provide transaction isolation between organisations. Private Data Collections (PDCs) allow subsets of channel members to share data that is not written to the shared channel ledger — only a hash of the private data is recorded on-chain.

**Performance:** Fabric is optimised for throughput over absolute decentralisation — benchmarks range from hundreds to several thousand TPS depending on chaincode complexity, endorsement policy, and hardware. The execute-order-validate pipeline allows chaincode to run in parallel before ordering, improving throughput over single-bottleneck designs.

**Real-world deployments:**
- **TradeLens** (Maersk / IBM) — global shipping documentation (discontinued 2022 due to adoption challenges)
- **Food Trust** (IBM / Walmart) — food supply chain traceability; active
- **We.Trade** — European trade finance consortium; banks including HSBC, Deutsche Bank, Rabobank
- **Pharma supply chain** — MediLedger network for drug traceability

---

### R3 Corda

Developed by the R3 consortium (founded 2014, with 200+ member financial institutions). Corda is **not a traditional blockchain** — transactions are not grouped into blocks, and there is no globally shared ledger.

**Core design principle:** In financial markets, a bank does not want its competitors to see its transaction data. Corda's architecture enforces the principle that *only the counterparties to a transaction, plus a notary, ever see that transaction*.

**Key primitives:**

| Primitive | Description |
|-----------|-------------|
| **State** | An immutable shared fact (analogous to a UTXO). States are consumed and produced by transactions. |
| **Transaction** | Proposes to consume one or more input states and produce one or more output states. Must satisfy the contract code attached to each state. |
| **Contract** | Immutable code that validates the legality of transitions between states. Applied deterministically. |
| **Flow** | The orchestration of a multi-party transaction: collecting signatures, verifying counterparty states, and invoking the notary. Flows are asynchronous and restartable. |
| **Notary** | Provides **uniqueness consensus** — prevents double-spending by attesting that no input state has been previously consumed. Does not validate business logic; only checks uniqueness. |
| **Vault** | Each node's private database of all states it currently holds or has held. Only states relevant to that node are stored locally. |
| **CorDapp** | A Corda Distributed Application — the application layer defining states, contracts, and flows for a specific business process. |

**Consensus model:** Uniqueness is provided by the notary. Validity is checked locally by each counterparty using the contract code. There is no network-wide consensus round — Corda achieves finality via bilateral agreement plus notary signing, making it far faster than block-based consensus for two-party transactions.

**Privacy:** The strongest privacy model of any major DLT — data is shared point-to-point between counterparties. A bank's transactions are never broadcast to the network. This is a fundamental departure from blockchain's global-broadcast model.

**Real-world deployments:**
- **Fnality International** — settlement system for major central banks; backed by UBS, Barclays, Santander, CIBC
- **DTCC** — US securities post-trade infrastructure pilot
- **Marco Polo** — trade finance network
- **Harmonia** — interoperability protocol (R3 + Adhara, a Hyperledger Lab) bridging Corda to other DLTs

---

### Hyperledger Besu

An Ethereum-compatible enterprise client maintained by LF Decentralised Trust. Runs the same Ethereum Virtual Machine (EVM) and supports Solidity smart contracts, but adds:
- Permissioning at node and account level
- Pluggable consensus: IBFT 2.0, QBFT (PBFT variants), Clique (PoA)
- Private transactions (Tessera-based)
- Monitoring and operational tooling

Used by ConsenSys Quorum (now Quorum / GoQuorum), Ethereum Enterprise Alliance members, and CBDC pilots including the Banque de France's experiments.

---

## Use Cases by Sector

| Sector | DLT Application | DLT Type Preferred | Real-World Example |
|--------|----------------|-------------------|-------------------|
| **Finance / Capital Markets** | Cross-border settlement, securities tokenisation, wCBDCs | Permissioned (Corda, Fabric, Besu) | Fnality, DTCC, Broadridge |
| **Supply Chain** | Provenance tracking, environmental certification, food safety | Permissioned (Fabric) or public (Ethereum) | IBM Food Trust, GS1 Digital Link |
| **Healthcare** | Drug traceability, clinical trial data, patient record sharing | Permissioned (Fabric, Corda) | MediLedger, Chronicled |
| **Energy** | Peer-to-peer energy trading, renewable certificate tracking | Public or consortium | Power Ledger, WePower |
| **Government / Public Sector** | Land registries, identity, voting | Permissioned or national blockchain | Sweden Lantmäteriet (land), Estonia X-Road |
| **IoT / Machine Economy** | Feeless machine payments, sensor data provenance | DAG (IOTA Tangle) | IOTA Tangle for Bosch, smart cities |
| **Digital Identity** | Verifiable credentials, DIDs, self-sovereign identity | Public + permissioned (Ethereum, EBSI) | EBSI (EU), Microsoft ION |
| **Intellectual Property** | Timestamped proof of creation, royalty tracking | Public (Ethereum, Bitcoin) | OpenSea, Verisart |

---

## Advantages

| Benefit | Mechanism | Practical Impact |
|---------|-----------|-----------------|
| **Transparency** | Shared ledger visibility | Faster audits; automated dispute resolution |
| **Security** | Cryptographic linking + distribution | No single-node breach compromises the record |
| **Immutability** | Append-only with cryptographic chaining | Stronger compliance evidence; tamper detection |
| **Cost reduction** | Eliminates reconciliation between separate databases | Lower back-office operational costs in finance |
| **Resilience** | Multi-node replication | No single point of failure; high availability |
| **Programmability** | Smart contracts / chaincode | Automation of complex multi-party business logic |
| **Disintermediation** | Peer-to-peer settlement | Faster, cheaper cross-border transactions |

---

## Limitations and Challenges

### Scalability Trilemma
The "blockchain trilemma" (attributed to Vitalik Buterin) holds that any DLT can achieve at most two of three properties simultaneously:
- **Decentralisation** — many independent validators
- **Security** — resistant to attack
- **Scalability** — high throughput, low latency

Most solutions sacrifice some decentralisation (permissioned systems) or security (delegated consensus) to achieve scale.

### Energy Consumption
Proof of Work systems consume enormous electricity (Bitcoin: ~120–150 TWh/year at peak). PoS, PBFT, and DAG systems are dramatically more efficient. Ethereum's 2022 switch to PoS reduced energy consumption by over 99.9%.

### GDPR Tension
Public ledgers record data permanently. The GDPR right to erasure (Article 17) conflicts with DLT immutability. The EDPB Guidelines 02/2025 and earlier Working Party opinions recommend: store personal data off-chain; anchor only a SHA-256 hash on-chain. See [[concepts/blockchain-microcredentials]] for the credential-specific treatment.

### 51% Attack
Any PoW network where a single actor controls more than 50% of hash rate can rewrite recent transaction history and double-spend. Smaller networks (Ethereum Classic, Bitcoin Gold) have suffered successful 51% attacks. ABFT systems (Hashgraph) and PBFT systems (Fabric) are mathematically immune to this attack vector.

### Interoperability
Most DLT platforms use incompatible protocols and data standards. Moving value or data between a Corda network and a Fabric network requires a bridge or interoperability protocol (e.g., Harmonia, Weave, Polkadot parachains). No universal standard has emerged.

### Implementation Complexity
Integrating a DLT into existing enterprise infrastructure requires significant technical expertise, governance design, and legal frameworks. Adoption bottlenecks are frequently organisational rather than technical.

### Irreversibility Risk
Confirmed transactions are extremely difficult to reverse. Operational errors (wrong address, wrong amount) can result in permanent loss of funds or data with no recourse.

---

## DLT Type Comparison Summary

| Property | Blockchain | DAG | Hashgraph | Holochain |
|----------|-----------|-----|-----------|-----------|
| **Data structure** | Linear blocks | Transaction graph | Gossip event DAG | Per-agent source chains |
| **Global consensus** | Yes | Eventual | Yes (ABFT) | No |
| **Finality** | Probabilistic → Absolute (PoS) | Eventual | Absolute (ABFT) | Per-application |
| **TPS (typical)** | 7–65,000 | Tens of thousands | 10,000+ (Hedera production) | Unlimited (per agent) |
| **Energy** | High (PoW) / Low (PoS/PBFT) | Very low | Low | Very low |
| **Transaction fees** | Yes (usually) | None (DAG) | Very low | None |
| **Smart contracts** | Yes (most platforms) | Limited | Yes (Hedera Smart Contract) | Application DNA |
| **Privacy** | Public or permissioned | Public (IOTA) | Public permissionless | Per-hApp |
| **Maturity** | High | Medium | Medium | Low |
| **Open source** | Yes | Yes | Algorithm patented | Yes |
| **Best suited for** | Currency, DeFi, enterprise | IoT, microtransactions | Enterprise, high-throughput | Social apps, data sovereignty |

---

## Key Statistics

- **Bitcoin TPS:** ~7 on-chain (Lightning Network enables millions of off-chain payments)
- **Ethereum TPS:** ~15–30 on-chain; ~2,000–4,000 with Layer 2 rollups
- **Hedera:** 10,000+ confirmed TPS in production; 250,000+ claimed theoretical
- **IOTA Tangle:** Tens of thousands of TPS; feeless
- **Hyperledger Fabric:** Hundreds to several thousand TPS depending on configuration
- **Ethereum PoS energy reduction vs PoW:** >99.9% (The Merge, September 2022)
- **EU MiCA:** Fully applied December 30, 2024
- **Global crypto market cap (as at article research date):** ~$2.3 trillion

---

## Related Pages

- [[concepts/bitcoin-history]] — the existence proof of DLT in the wild, 17 years of uninterrupted operation
- [[concepts/blockchain-microcredentials]] — DLT applied to verifiable credential systems; GDPR tension; on-chain vs. off-chain architecture
- [[concepts/prompt-injection]] — agentic AI systems increasingly interact with DLT; cross-domain attack surface
- [[concepts/social-engineering]] — social engineering is the primary attack vector against DLT custody (exchange hacks, SIM swaps, phishing for seed phrases)
