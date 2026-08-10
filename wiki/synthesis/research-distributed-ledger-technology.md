---
type: synthesis
title: "Research: Distributed Ledger Technology"
domain: blockchain
maturity: established
tags: [research, DLT, blockchain, DAG, Hashgraph, Holochain, Hyperledger, Corda, consensus, enterprise, scalability-trilemma, GDPR, interoperability]
updated: 2026-08-10
created: 2026-08-10
---

# Research: Distributed Ledger Technology

**Research question:** What is the full landscape of distributed ledger technology — its types, architectural trade-offs, enterprise implementations, use cases, and known limitations?

**Research method:** Autonomous web research — 3 initial search passes, 2 successful deep fetches (Coinpaprika architecture overview; Hedera Knowledge Centre), 3 supplementary search passes covering Hyperledger Fabric, R3 Corda, and DLT type comparisons. Sources: Coinpaprika, Hedera, tatum.io, Hyperledger search results, R3 Corda documentation search, CCN education, 101blockchains.

---

## Summary

Distributed Ledger Technology is not a single thing — it is a design space defined by the question of *how multiple mutually distrustful parties can maintain a shared record without a central administrator*. Blockchain is the most famous answer to that question, but it is neither the first nor necessarily the best answer for every context. DAG, Hashgraph, and Holochain each make fundamentally different architectural bets, and the "right" DLT is determined entirely by the constraints of the specific use case.

The single most clarifying insight is the **scalability trilemma**: no DLT simultaneously achieves maximum decentralisation, security, and throughput. Every DLT design, without exception, trades off one against another. Understanding which of the three a given implementation sacrifices is the lens through which all DLT architectural choices become legible.

---

## Core Findings

### 1. "DLT" is a Taxonomy, Not a Technology

The term "distributed ledger technology" is frequently used as a synonym for "blockchain" in non-technical discourse, which is incorrect and misleading. The accurate relationship is:

```
Distributed Ledger Technology (DLT)
├── Blockchain (linear, block-based)
│   ├── Public permissionless (Bitcoin, Ethereum)
│   └── Private permissioned (Hyperledger Fabric, R3 Corda, Besu)
├── DAG (transaction-referencing graph)
│   └── IOTA Tangle, NANO, Avalanche (DAG mempool)
├── Hashgraph (gossip-event DAG + virtual voting)
│   └── Hedera Hashgraph
└── Holochain (agent-centric; no global consensus)
    └── Holochain hApps
```

Each branch makes different assumptions about what "distributed" means, what "consensus" requires, and what the ledger is *for*. Conflating them produces confused architectural decisions.

### 2. Consensus Mechanism Choice Determines Everything

The consensus mechanism is not an implementation detail — it is the fundamental design decision from which throughput, security guarantees, energy profile, validator set size, and finality type all follow:

| Goal | Consensus to choose | Why |
|------|--------------------|----|
| Maximum security, uncensorable | PoW (large network) | Computationally expensive to attack |
| Maximum throughput, enterprise control | PBFT / SmartBFT | Fast, deterministic finality; suits known validators |
| IoT microtransactions, feeless | DAG (Tangle) | No miners; transaction validates prior transactions |
| Absolute BFT in public setting | ABFT (Hashgraph) | Strongest provable guarantee; no voting messages sent |
| No global consensus needed | DHT peer validation (Holochain) | Eliminates the bottleneck entirely |

The critical implication: **there is no "best" consensus mechanism**. A team selecting a consensus mechanism without first specifying their threat model, throughput requirement, and trust assumptions is selecting at random.

### 3. Enterprise Permissioned DLTs Are Not "Decentralised" in the Ideological Sense

Hyperledger Fabric, R3 Corda, and Hyperledger Besu are sometimes called "private blockchains," but this label obscures what they actually are: **distributed databases with Byzantine fault tolerance and cryptographic audit trails**, operated by a consortium of known, legal-identity-verified participants.

They share none of Bitcoin's trustless, permissionless, censorship-resistance properties. What they offer instead is:
- **Immutable audit trails** without a central database owner
- **Multi-party smart contract execution** without trusting a single counterparty's system
- **Privacy** between consortium members (Corda's point-to-point model; Fabric's channels and Private Data Collections)
- **Regulatory compliance** (known participants, reversible under exceptional governance procedures)

The decision to use Hyperledger Fabric vs. a conventional database is a **governance and trust decision**, not a technical one: *do the parties trust a single administrator, or do they each want to run a node and verify transactions independently?*

### 4. R3 Corda's Point-to-Point Model Is the Correct Mental Model for Financial Markets

Most DLTs broadcast every transaction to the entire network and use consensus to establish a canonical ordering. This is sensible for a public cryptocurrency but commercially absurd for institutional finance: Barclays does not want HSBC to see its trades in real time.

Corda's architecture inverts the broadcast assumption: **transactions are shared only between counterparties and the notary**. Consensus is reduced to a minimal operation — uniqueness verification by the notary — rather than a network-wide agreement round. The result is:
- Strong transaction privacy by construction (not bolted on)
- Fast finality (notary signature replaces network-wide consensus)
- A trust model that matches how financial contracts actually work (bilateral agreements)

This is why Corda has been adopted for serious financial infrastructure (Fnality, DTCC, We.Trade) where no other DLT has achieved production deployment at comparable scale.

### 5. The GDPR Tension Is Unresolved and Structural

The immutability that makes DLT valuable for audit trails is precisely the property that conflicts with the GDPR right to erasure (Article 17). This is not a technical bug that a better DLT implementation will fix — it is a **structural conflict between legal right and cryptographic property**.

The currently authoritative guidance (EDPB Guidelines 02/2025, consistent with the 2019 Working Party opinion) is:
- Store personal data **off-chain** in a traditional, deletable database
- Anchor only a **cryptographic hash** (SHA-256) on-chain
- Deletion of off-chain data renders the hash useless as a data record, satisfying the right to erasure in practice if not in principle

This is a pragmatic compromise. It does not resolve the philosophical tension, and the legal status of "is an on-chain hash personal data?" remains genuinely contested in case law across EU member states.

---

## Architecture Decision Framework

For any project considering a DLT:

```
Do you need a shared, tamper-evident record between 
multiple mutually distrustful parties?
│
├─ NO → Use a conventional database. DLT adds cost with no benefit.
│
└─ YES
    │
    ├─ Are the parties known, legally identified, and regulated?
    │   │
    │   ├─ YES → Permissioned DLT
    │   │         ├─ Financial markets, bilateral contracts → R3 Corda
    │   │         ├─ Multi-party supply chain / consortium → Hyperledger Fabric
    │   │         └─ Ethereum-compatible + enterprise → Hyperledger Besu
    │   │
    │   └─ NO → Public DLT
    │             ├─ Censorship-resistant value transfer → Bitcoin
    │             ├─ Smart contracts, DeFi, NFTs → Ethereum
    │             ├─ High-throughput enterprise dApps → Hedera Hashgraph
    │             └─ IoT / feeless microtransactions → IOTA Tangle
    │
    └─ Do you need global ordering of all transactions?
        ├─ YES → Blockchain or Hashgraph
        └─ NO → Consider Holochain (if agent-centric is sufficient)
```

---

## Cross-Domain Connections

### DLT ↔ Bitcoin History

Bitcoin is the production validation of the blockchain subset of DLT. Seventeen years of continuous operation, zero successful protocol-level attacks, and a market cap exceeding $1 trillion make it the most empirically tested distributed system in existence. Every theoretical claim about blockchain immutability and decentralisation has a real-world stress test in Bitcoin's history. See [[concepts/bitcoin-history]].

### DLT ↔ Blockchain Microcredentials

The verifiable credential systems built on DLT (W3C VC 2.0, OpenBadges 3.0, EBSI) use blockchain or Ethereum as a trust anchor. The architectural choice between on-chain and off-chain credential storage is the GDPR tension in concrete form. The DLT choice (did:ethr on Ethereum, did:ion on Bitcoin, did:ebsi on EBSI's Besu instance) determines longevity, revocation capability, and regulatory exposure. See [[concepts/blockchain-microcredentials]].

### DLT ↔ Prompt Injection and AI Agents

Agentic AI systems are beginning to interact with DLT infrastructure — querying on-chain data, executing smart contracts via tool calls, and managing wallet operations. This creates a new attack surface: **an adversarial prompt that induces an AI agent to execute a malicious smart contract transaction or sign an unintended message**. The irreversibility of DLT transactions makes this threat materially more severe than most prompt injection scenarios — there is no "undo" for a signed blockchain transaction. See [[concepts/prompt-injection]].

### DLT ↔ Social Engineering

The dominant attack vector against DLT systems is not technical — it is social. The majority of cryptocurrency theft occurs via:
- **Phishing** for seed phrases or private keys
- **SIM swapping** to compromise exchange accounts
- **Fake support staff** convincing victims to "connect their wallet" to malicious sites
- **Deepfake CFO calls** authorising wire transfers to attacker-controlled wallets

Bitcoin's protocol has had zero successful cryptographic attacks since 2010. Its *users* have lost billions. The security model of a DLT is only as strong as its custody and authentication layer — and that layer runs on human psychology. See [[concepts/social-engineering]].

### DLT ↔ Privacy and Data Protection

Bitcoin's pseudonymity model is widely misunderstood. Every transaction is permanently public. Chain analysis (Chainalysis, Elliptic) can de-anonymise a significant proportion of transactions by clustering addresses and correlating with exchange KYC data. Public DLTs create permanent, irrevocable records that are difficult to reconcile with data minimisation and purpose limitation principles under GDPR. Permissioned DLTs (Corda, Fabric) offer stronger privacy controls, but introduce centralisation trade-offs.

---

## Open Questions

1. **Will the scalability trilemma be solved, or merely managed?** Layer 2 solutions (Lightning, rollups, state channels) push throughput dramatically without sacrificing base-layer security — but they reintroduce trusted intermediaries at the L2 layer. Is this genuinely solving the trilemma or relocating it?

2. **Will Corda's point-to-point model become the template for financial market infrastructure?** The Fnality and DTCC deployments are the most significant real-world tests. If they succeed at scale, Corda's privacy model may become the de facto standard for regulated financial DLT.

3. **What happens to Hyperledger Fabric deployments (e.g., TradeLens) that were discontinued despite technical success?** TradeLens was technically functional but commercially failed due to competitor adoption reluctance. Is the governance problem of consortium DLTs more intractable than the technical problem?

4. **Can IOTA's Tangle achieve its machine-economy ambitions without a coordinator?** IOTA 2.0 (Shimmer) aimed to remove the centralised coordinator that bootstrapped the Tangle's security. The success of this transition determines whether DAG DLT can genuinely claim decentralisation.

5. **How will quantum computing affect DLT security?** SHA-256 and ECDSA (used in Bitcoin, Ethereum, and most DLTs) are theoretically vulnerable to sufficiently powerful quantum computers. Post-quantum cryptographic migration for live distributed ledgers with billions of UTXOs is an unsolved engineering challenge.

---

## Source Pages

- [Coinpaprika — What is Distributed Ledger Technology and How It Works](https://coinpaprika.com/education/what-is-distributed-ledger-technology-dlt-and-how-it-works/)
- [Hedera — What is Distributed Ledger Technology](https://hedera.com/learning/distributed-ledger-technologies/what-is-distributed-ledger-technology)
- [tatum.io — DAG vs Blockchains vs Hashgraphs: A Deep Technical Comparison](https://tatum.io/blog/dag-vs-blockchains-vs-hashgraphs-a-deep-technical-comparison)
- [GeeksforGeeks — Hyperledger Fabric Component Design](https://www.geeksforgeeks.org/hyperledger-fabric-component-design/)
- [xoriant.com — Understanding Corda Architecture](https://www.xoriant.com/blog/corda-architecture-explained)
- [101blockchains.com — Corda Blockchain](https://101blockchains.com/corda-blockchain/)
- [R3 Developer Platform — Notaries in Corda Next-Gen Architecture](https://developer.r3.com/blog/notaries-in-corda-next-gen-architecture/)

**Primary concept page:** [[concepts/distributed-ledger-technology]]
