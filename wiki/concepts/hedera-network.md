---
type: concept
title: "Hedera Network (HBAR)"
domain: blockchain
maturity: established
tags: [Hedera, HBAR, Hashgraph, DLT, DAG, ABFT, consensus, HCS, HTS, HFS, HSCS, governing-council, tokenomics, RWA, CBDC, enterprise, staking, trust-layer]
updated: 2026-08-10
created: 2026-08-10
---

# Hedera Network (HBAR)

## Overview

Hedera is a public distributed ledger built on the **Hashgraph** consensus algorithm — a fundamentally different data structure and consensus mechanism from blockchain. It was created by Dr. Leemon Baird (PhD, Carnegie Mellon) and Mance Harmon (MS Computer Science, UMass), founded in 2018, with the goal of overcoming what they identified as the core limitations of existing blockchains: low throughput, high latency, energy inefficiency, and governance fragility.

Hedera is distinguished from other public DLTs by three features that appear in combination nowhere else: **Asynchronous Byzantine Fault Tolerance (ABFT) consensus**, **governance by an enterprise council** (not miners, validators, or token holders), and **USD-denominated fee stability** that makes cost predictable for enterprise use.

---

## The Hashgraph Consensus Algorithm

### 1. Gossip About Gossip

All nodes in the network continuously exchange information in the following manner:

1. A node selects a random peer and sends it its entire known event history (a "gossip")
2. The receiving node logs not just the data, but the *fact* that it received it and from whom — "gossip about gossip"
3. This creates a **DAG (Directed Acyclic Graph) of events**, where each event records the two prior events it was aware of: its own previous event and the event it received from its gossip partner
4. Information propagates to the entire network in O(log N) rounds — exponentially fast regardless of network size

The result is a shared, append-only DAG representing the complete gossip history of the network.

### 2. Virtual Voting

Classical BFT consensus requires nodes to exchange votes: O(N²) messages per round. Hedera eliminates this entirely via **virtual voting**:

- Because every node has an identical copy of the DAG (from the gossip protocol), each node can independently compute what every other node *would have* voted, given the information they had at each point in time
- No vote messages are transmitted — each node runs the same deterministic computation locally and arrives at identical conclusions
- The result is consensus-level security with zero vote-message overhead

### 3. Asynchronous Byzantine Fault Tolerance (ABFT)

ABFT is the strongest formal security guarantee achievable in distributed systems:

| Security Property | What it means |
|------------------|---------------|
| **Asynchronous** | Security holds even when the network has arbitrary, unbounded delays — no assumptions about timing |
| **Byzantine Fault Tolerant** | The network continues correctly even if up to ⅓ of nodes are actively malicious (not just offline) |
| **Consensus** | All honest nodes reach identical agreement on the order of events |

PBFT and Raft (used in Hyperledger Fabric) are Byzantine Fault Tolerant but not fully asynchronous — they assume bounded message delays. PoW and PoS provide probabilistic finality (Bitcoin's "6-block confirmation" is ~99.9997%, not mathematical certainty). ABFT provides **mathematical, deterministic finality** without timing assumptions — the strongest provable guarantee.

### 4. Fair Ordering

Hashgraph derives consensus timestamps via the **median** of the timestamps assigned by each node when it first receives an event. Because the median requires collusion by over ⅓ of nodes to manipulate, no single node or small coalition can alter the ordering of transactions. This prevents **front-running** — a major problem on Ethereum where miners/validators can reorder transactions in their mempool for profit (MEV).

### 5. Performance Summary

| Metric | Value |
|--------|-------|
| **Claimed max TPS** | 250,000+ (theoretical) |
| **Confirmed production TPS** | 10,000+ |
| **Finality time** | 3–7 seconds |
| **Daily transactions** | ~500,000 (2025 average) |
| **Total accounts** | 9.26 million (October 2025) |
| **Energy per transaction** | ~0.000003 kWh (negligible vs. Bitcoin's ~700 kWh) |
| **Transaction fee (transfer)** | $0.0001 USD |

---

## Network Architecture

Hedera's network comprises three layers:

```
┌─────────────────────────────────────────────────────┐
│              APPLICATION LAYER                      │
│  DeFi protocols · NFT platforms · dApps · AI agents │
├─────────────────────────────────────────────────────┤
│              SERVICES LAYER                         │
│  HCS · HTS · HFS · HSCS (Besu EVM)                 │
│  Mirror Nodes · REST API · JSON-RPC relay           │
├─────────────────────────────────────────────────────┤
│              CONSENSUS LAYER                        │
│  Hedera public network nodes (council-operated)     │
│  Hashgraph consensus: gossip + virtual voting        │
│  ABFT finality · Fair ordering · USD fee schedules  │
└─────────────────────────────────────────────────────┘
```

**Main nodes** — operated by Governing Council members. Currently permissioned; permissionless node operation is on the public roadmap.

**Mirror nodes** — read-only nodes that replicate the ledger for querying. Publicly accessible; used by explorers, wallets, analytics platforms. Do not participate in consensus.

**JSON-RPC relay** — exposes an Ethereum-compatible JSON-RPC interface so that MetaMask, Hardhat, Ethers.js, and other Ethereum tooling works with Hedera without modification.

---

## Native Services

Hedera exposes four distinct services at the protocol level. Unlike Ethereum (where all functionality must be implemented via smart contracts), Hedera bakes common primitives directly into the protocol, achieving lower cost and higher throughput for standard operations.

### Hedera Consensus Service (HCS)

**Purpose:** Decentralised, ordered, verifiable event log — "timestamping as a service."

**How it works:**
- Developers create a **topic** on the ledger
- Applications publish arbitrary byte-string messages to the topic
- Hedera applies consensus ordering and timestamps each message
- The ledger returns a record containing: consensus timestamp, sequence number, running hash of all previous messages

**Fee structure:**
| Operation | Cost |
|-----------|------|
| Create topic | $0.01 |
| Update topic | $0.00022 |
| Submit message | $0.0001 |

**Use cases:** Supply chain event ordering, multiplayer game state consensus, audit logging, cross-application coordination, verifiable AI agent action logs.

**Developer value:** Any application that needs a globally trusted, tamper-evident sequence of events — without running its own consensus infrastructure — can use HCS as a service.

---

### Hedera Token Service (HTS)

**Purpose:** Native token creation and management — no smart contract required.

**How it works:** Tokens are first-class primitives on the Hedera ledger. Creating a token is a protocol-level transaction, not a contract deployment. All token accounts must explicitly *associate* with a token before receiving it (preventing spam).

**Supported token types:**
- **Fungible tokens** — equivalent to ERC-20 but native (no Solidity, no gas)
- **Non-fungible tokens (NFTs)** — equivalent to ERC-721 but native; serial numbers assigned at mint

**Built-in compliance controls (unique to HTS):**
| Control | Effect |
|---------|--------|
| **KYC flag** | Account must pass KYC check before it can transact with the token |
| **Freeze** | Suspend a specific account's ability to transact with the token |
| **Pause** | Pause all transfers of the token across the entire network |
| **Wipe** | Remove tokens from a specific account (requires wipe key) |
| **Supply control** | Mint or burn tokens (up to max supply cap) |

**Custom fee schedules:** Token creators can define automatic royalties (fixed fee, fractional fee, or royalty fee on NFT transfers), enabling built-in revenue sharing without smart contracts.

**Atomic swaps:** HTS supports atomic multi-token swaps in a single transaction — multiple token types and HBAR can be exchanged atomically, with all transfers succeeding or all failing.

**Performance:** Up to 10,000 TPS for token transfers; $0.0001 per transfer.

**Smart contract integration:** The HTS System Contract (precompile at address `0x167`) exposes HTS operations to Solidity smart contracts, enabling DeFi protocols to interact with native tokens using standard Solidity interfaces.

**HTS vs ERC-20/ERC-721:**
| Dimension | HTS (Native) | ERC-20 / ERC-721 (Ethereum) |
|-----------|-------------|---------------------------|
| Deployment | Protocol transaction, no code | Smart contract deployment required |
| Gas | Fixed USD fee | Variable gas price |
| Compliance controls | Built-in (KYC, freeze, pause, wipe) | Must code manually or use standards |
| Front-running risk | None (fair ordering) | High (MEV) |
| Custom fees | Built-in royalty / fee schedules | Must code in contract |
| Upgrade path | Token admin key | Proxy patterns, migration |

---

### Hedera File Service (HFS)

**Purpose:** Decentralised file storage on the ledger.

**Architecture:**
- Files stored across network nodes using Merkle trees and Merkle DAGs
- Append-only by default; files expire after a configurable duration
- Transaction size limit: 4 KB per operation; larger files are built via sequential append transactions

**GDPR compliance:** HFS provides a **proof-of-deletion** mechanism — when a file expires or is deleted, the network records the deletion. This is significant because most DLTs cannot delete data. HFS makes erasure provable, addressing the GDPR right-to-erasure tension that plagues immutable blockchain storage.

**Fee structure:**
| Operation | Cost |
|-----------|------|
| Create file | $0.05 |
| Update file | $0.05 |
| Append file | ~$0.05 |
| Delete file | $0.007 |

**Use cases:** GDPR-compliant document storage, immutable record anchoring, smart contract bytecode hosting, configuration storage for dApps.

---

### Hedera Smart Contract Service (HSCS)

**Purpose:** Ethereum-compatible smart contracts on Hedera's network.

**EVM:** Uses Besu EVM — the same EVM implementation used by Hyperledger Besu for enterprise Ethereum. Hedera has customised it for performance and fee-model integration.

**Developer experience:** Existing Solidity contracts deploy on Hedera with no or minimal changes. MetaMask, Hardhat, Ethers.js, Foundry, and standard Ethereum development tooling all work via Hedera's JSON-RPC relay.

**Performance:**
- 15 million gas per second throughput
- Rapid finality via Hashgraph consensus (3–7 seconds, not 12-second block times)
- Predictable, low fees ($0.05 per contract call vs. Ethereum's variable gas)

**HTS integration:** Smart contracts interact with native HTS tokens via the `0x167` precompile, enabling DeFi protocols (DEXs, lending protocols) to use native tokens without wrapping them.

**Fee structure:**
| Operation | Cost |
|-----------|------|
| Contract creation | $1.00 |
| Contract call | $0.05 |
| Contract update | $0.026 |

---

## Governing Council

### Structure

Hedera is governed by the **Hedera Council** (formerly Hedera Governing Council), a body of up to **39 enterprise organisations** from diverse industries and geographies. In September 2024, Hedera transferred all source code governance to the **Linux Foundation**, making the protocol itself vendor-neutral while the Council retains governance of network policy and treasury.

**Key governance rules:**
- Equal voting rights — no single member can outvote the rest
- Term limits — members rotate to prevent entrenchment
- Geographic and industry diversity is a stated requirement for council composition
- The Council controls: protocol upgrades, treasury allocation, node operator approvals, fee schedules

### Current Members (as of mid-2026)

| Sector | Members |
|--------|---------|
| **Technology** | Google, IBM, Dell, Wipro, Tata Communications, Hitachi, ServiceNow |
| **Finance** | Nomura, Shinhan Bank, Standard Bank, BitGo, Australian Payments Plus |
| **Legal / Professional** | Dentons, DLA Piper |
| **Energy** | EDF, Repsol, Blockchain for Energy (B4E) |
| **Telecoms** | Deutsche Telekom, Zain |
| **Retail / Consumer** | Mondelēz, Avery Dennison, Magalu, LG, Ubisoft |
| **Logistics / Supply Chain** | FedEx, Arrow Electronics |
| **Academia** | IIT Madras, LSE (London School of Economics) |
| **Capital Markets / Exchange** | NSE (Nairobi Securities Exchange), McLaren Racing |
| **Fintech / Blockchain** | Chainlink Labs, Swirlds (Hashgraph inventor) |
| **Other** | Aberdeen, Accenture |

### 2025 Governance Restructuring

- **HBAR Foundation → Hedera Foundation**: sharper focus on tokenisation, DeFi, AI, community innovation (ecosystem growth arm)
- **Hedera Governing Council → Hedera Council**: clarified separation — Foundation drives ecosystem; Council preserves network decentralisation and stability
- **New membership tiers**: Strategic Partnership and Community Partnership tiers added alongside full Council membership
- **HEAT**: Hedera Enterprise Adoption Team launched to accelerate proof-of-concept-to-production delivery for enterprises

### The Centralisation Critique

The Council model is a deliberate trade-off. Critics argue:
- Only approved entities run consensus nodes — this is **not decentralised** by the Bitcoin/Ethereum definition
- The Council controls protocol upgrades and treasury — concentrated power
- Swirlds (Leemon Baird's company) held the Hashgraph IP on a licensing basis until the Council purchased and open-sourced it under Apache 2.0 in 2022 — historical dependency

Hedera's counter-argument:
- The 39-member council spanning 20+ industries and multiple continents is **collusion-proof in practice** — what do Google and FedEx and IIT Madras and Shinhan Bank all agree on?
- Term limits and equal voting rights prevent entrenchment of any single interest
- Known, legally accountable entities as node operators is a **feature for regulated enterprise use** — you cannot sue a miner
- Permissionless node operation is on the roadmap, with governance retained by the Council

---

## HBAR Tokenomics

### Supply

| Parameter | Value |
|-----------|-------|
| **Maximum supply** | 50,000,000,000 HBAR (50 billion) |
| **Inflation** | None — no new tokens ever created |
| **Minting event** | All tokens minted at network genesis (2018) |
| **Release schedule** | Gradual treasury distribution over ~15 years from genesis |
| **Circulating supply** | ~84.8% released as of 2025 |

### Allocation Categories

| Category | Purpose |
|----------|---------|
| **Initial Development** | Hashgraph IP licensing and early deployment (ended 2022 after IP purchase by Council) |
| **Purchase Agreements** | SAFTs and Token Purchase Agreements for early investors |
| **Network Governance** | Founder, executive, and employee compensation; council operations |
| **Ecosystem Development** | HBAR Foundation / Hedera Foundation grants, developer incentives |
| **Unallocated** | Reserved; released by Council governance votes |

**December 2024 ecosystem allocation:** The Council allocated **7 billion HBAR** (14% of total supply) specifically for ecosystem expansion:
- 3.5 billion transferred by February 2025
- Remaining disbursements tied to measurable milestones in DeFi, RWA tokenisation, enterprise adoption, and developer tooling

**October 2025:** 250 million HBAR allocated to staking reward pool.

### Fee Model

Hedera fees are **denominated in USD** and converted to HBAR at time of execution using real-time exchange rates. This ensures:
- Enterprise cost predictability regardless of HBAR price volatility
- Fees remain stable and low ($0.0001 per transaction) in USD terms even if HBAR appreciates significantly

Fees are **not burned**. They are distributed:
- A portion to node operators (bandwidth, compute, consensus participation)
- A portion to the treasury (network sustainability)

### Staking

| Parameter | Value |
|-----------|-------|
| **Model** | Proxy staking (delegate to nodes) |
| **Custodial** | Non-custodial — stake never leaves your account |
| **Slashing** | None |
| **APY** | ~6.5% (2025; funded from treasury, not new issuance) |
| **Reward source** | Fixed treasury distribution, not inflation |

Staking in Hedera does not determine consensus weight at the node level in the traditional PoS sense — HBAR assigned to a node signals economic weight and earns rewards, but consensus is driven by the Hashgraph algorithm independent of stake.

---

## Real-World Deployments

| Year | Organisation | Use Case | Detail |
|------|-------------|----------|--------|
| 2021 | UK NHS / Everyware | COVID-19 vaccine cold-chain | Tamper-proof temperature monitoring records via HCS |
| 2021 | Shinhan Bank + Standard Bank | Cross-border remittance | Low-cost, seconds-finality international settlement |
| 2022–23 | Meeco | Verifiable credentials / DID | Users control identity data using Hedera-anchored VCs |
| 2023 | Archax + Ownera | HSBC bond tokenisation | Tokenised bond assets on HTS for faster settlement |
| 2025 (Mar) | UNDP / Guardian | Carbon registry | Carbon project issuances auditable on Hedera; open-source methodology libraries |
| 2025 | Lloyds Banking Group + Aberdeen | Tokenised UK gilts | Settled tokenised gilts and MMF units as collateral in FX trades |
| 2025 | Australian Digital Dollar | Stablecoin | AUD stablecoin launched on Hedera using Stablecoin Studio |
| 2025 | Swarm | Tokenised securities | Compliant tokenised stocks (AAPL, TSLA) and gold |
| 2025 | StegX | Real estate tokenisation | $100M+ in institutional real estate tokenised using jurisdiction-aware standards |
| 2025 | Reserve Bank of Australia (Project Acacia) | Wholesale CBDC pilot | Hedera selected for wCBDC issuance exploration |
| 2025 | Wyoming FRNT | State stable token | Hedera listed as candidate for first US state-issued stable token |
| 2025 | Bank of England / BIS | RTGS synchronisation | Hedera selected (alongside one other L1) for money and RTGS system exploration |
| 2025 | Georgia Ministry of Justice | National land registry | Exploring national real estate registry migration to Hedera |
| 2025 | EQTY Lab / NVIDIA Blackwell | Verifiable AI compute | Hedera anchoring immutable AI audit logs for NVIDIA GPU compute verification |

---

## 2025 Strategic Developments

### AI Studio

Open-source toolkit enabling developers to build **AI agents with verifiable backends on Hedera**. Uses HCS to create tamper-proof, ordered audit logs of agent actions — each step an AI agent takes is anchored on the ledger with a consensus timestamp, enabling post-hoc audit and regulatory review.

Hedera joined the **Decentralised AI Society** in 2025 to shape standards for transparent, ethical AI infrastructure.

### HashSphere

Launched March 2025. A **private, permissioned hybrid network layer** that connects seamlessly to the public Hedera network and other EVM ecosystems. Enables enterprises operating in regulated environments (banking, healthcare, government) to maintain private transaction privacy while anchoring to Hedera's public consensus for auditability and interoperability.

### Asset Tokenisation Studio

Enhanced with:
- **ERC-3643 (T-REX protocol)** — the on-chain identity and compliance standard for regulated security tokens
- **ERC-1400** — permissioned security token standard
- Recognised as "Top Financial Innovation" by *Global Finance Magazine* (2025)

### Cross-Chain Interoperability

**Axelar Network integration** links Hedera to **60+ blockchains** including Arbitrum, Solana, and XRPL — enabling assets and messages to move between Hedera and the broader multi-chain ecosystem.

**Canonical WETH** integrated via Stargate and SaucerSwap (Hedera's leading DEX).

### Security

**Blockaid partnership** (August 2025): real-time threat detection for Hedera transactions and smart contracts, equivalent to the threat screening deployed on Ethereum by MetaMask and Coinbase.

---

## Ecosystem

| Category | Notable Projects |
|----------|-----------------|
| **DEX / DeFi** | SaucerSwap (leading DEX), HeliSwap, Bonzo Finance (lending) |
| **NFTs** | Hashinals, Dead Pixels Ghost Club, Turtle Moon |
| **Stablecoins** | Australian Digital Dollar (AUD), USDC on Hedera |
| **RWA** | StegX (real estate), Swarm (securities), Archax (bonds) |
| **Identity** | Meeco, Calaxy, Hashport |
| **Developer Tools** | HashScan (explorer), Hedera Developer Playground, Contract Builder |
| **Infrastructure** | Dfns (institutional wallets), Blockaid (security), Axelar (bridges) |
| **AI** | AI Studio, EQTY Lab (Verifiable Compute) |

**Developer events:** HederaCon 2025 (Denver, 400+ attendees), Hello Future Hackathon 2.0, Hashathon Nairobi, Hedera Agents Hackathon.

---

## Competitive Comparison

| Dimension | Hedera (HBAR) | Ethereum | Solana | Bitcoin |
|-----------|--------------|----------|--------|---------|
| **Consensus** | ABFT Hashgraph | PoS (Gasper) | PoH + PoS | PoW |
| **Data structure** | DAG of gossip events | Blockchain | Blockchain | Blockchain |
| **TPS** | 10,000+ (production) | 15–30 (L1) | 2,000–4,000 | ~7 |
| **Finality** | 3–7 sec (absolute) | ~12 min (probabilistic → justified) | ~0.4 sec (probabilistic) | ~60 min (6 confirmations) |
| **Security guarantee** | ABFT (strongest) | BFT (probabilistic) | BFT (optimistic) | 51% attack resistance |
| **Fees** | $0.0001 (USD-fixed) | Variable gas | Variable (low) | Variable (can spike) |
| **Governance** | Enterprise council | Token holder voting (EIP process) | Solana Labs / Foundation | IETF-style rough consensus |
| **Node permissioning** | Permissioned (roadmap: open) | Permissionless | Permissionless | Permissionless |
| **Smart contracts** | Solidity / Besu EVM | Solidity / EVM | Rust / SVM | Limited (Taproot/Script) |
| **Native token primitive** | Yes (HTS, no contract) | No (ERC-20 requires contract) | No (SPL via program) | No |
| **Energy per tx** | ~0.000003 kWh | ~0.03 kWh (post-merge) | ~0.0003 kWh | ~700 kWh |
| **Front-running protection** | Fair ordering (built-in) | None (MEV endemic) | Partial | Partial |

---

## Risks and Criticisms

| Risk | Detail |
|------|--------|
| **Centralised node operation** | Only Council-approved entities run nodes; permissionless participation is a roadmap promise, not yet reality |
| **Council governance power** | 39 enterprises control protocol upgrades, treasury, and fee schedules — significant centralised authority |
| **Historical IP dependency** | Swirlds held Hashgraph patent until 2022; Council purchased IP and open-sourced under Apache 2.0, but the history exists |
| **Ecosystem maturity gap** | DeFi TVL and developer ecosystem are significantly smaller than Ethereum's |
| **HBAR price volatility** | Despite USD-denominated fees, HBAR itself is volatile; staking APY and treasury value fluctuate |
| **TPS claim vs. reality** | 250,000 TPS is theoretical; ~500,000 transactions/day (≈5.8 avg TPS) is far from either the theoretical or the 10,000+ claimed production peak |
| **Quantum vulnerability** | Like all current DLTs, Hedera's cryptography (ECDSA) is theoretically vulnerable to sufficiently powerful quantum computers |
| **Smaller validator set** | Fewer node operators means a narrower set of potential Byzantine failures, but also less decentralisation in practice |

---

## Network Environments

| Environment | Purpose | Notes |
|-------------|---------|-------|
| **MainNet** | Live production network | Real HBAR; transactions cost real money |
| **TestNet** | Free development and testing | 10,000 HBAR/day via faucet (`docs.hedera.com/guides/testnet/testnet-access`) |
| **PreviewNet** | Preview upcoming protocol changes | Unstable by design — for core contributors and early adopters |
| **LocalNode** | Fully isolated local Docker network | Open source; `github.com/hashgraph/hedera-local-node` |

Use **TestNet** for all course exercises and development work. Never test on MainNet.

---

## Java SDK — Smart Contract Deployment (HAPI)

HAPI (Hedera API) provides SDKs for multiple languages. The Java SDK:

```xml
<dependency>
    <groupId>com.hedera.hashgraph</groupId>
    <artifactId>sdk</artifactId>
    <version>2.17.0</version>
</dependency>
```

(GitHub: `hashgraph/hedera-sdk-java` → migrating to `org.hiero:hiero-sdk-java` post Hiero rebrand)

### Getting Started (Testnet)

```java
AccountId myAccountId = AccountId.fromString(Dotenv.load().get("MY_ACCOUNT_ID"));
PrivateKey myPrivateKey = PrivateKey.fromString(Dotenv.load().get("MY_PRIVATE_KEY"));

Client client = Client.forTestnet();
client.setOperator(myAccountId, myPrivateKey);
client.setDefaultMaxTransactionFee(new Hbar(100));
client.setMaxQueryPayment(new Hbar(50));
```

### Smart Contract Deployment — Four Steps

```
Compile Solidity → Upload bytecode (FileId) → Create contract (ContractId) → Call functions
```

**Step 1 — Upload bytecode to Hedera File Service:**

```java
byte[] bytecode = readCompiledContract();   // result of solc --bin
FileCreateTransaction fileCreateTx = new FileCreateTransaction()
    .setContents(bytecode);
FileId fileId = fileCreateTx.execute(client)
                             .getReceipt(client)
                             .fileId;
```

**Step 2 — Instantiate the contract:**

```java
ContractCreateTransaction contractTx = new ContractCreateTransaction()
    .setBytecodeFileId(fileId)
    .setGas(100_000);   // set max gas cost — reverts if exceeded
ContractId contractId = contractTx.execute(client)
                                   .getReceipt(client)
                                   .contractId;
```

**Alternative one-step shortcut (`ContractCreateFlow`):**

```java
ContractId contractId = new ContractCreateFlow()
    .setBytecode(bytecodeInHex)
    .setGas(1_000_000)
    .execute(client)
    .getReceipt(client)
    .contractId;
```

**Step 3 — Call a read-only function (query, no state change):**

```java
ContractFunctionResult result = new ContractCallQuery()
    .setGas(100_000)
    .setContractId(contractId)
    .setFunction("greet")
    .execute(client);
```

**Step 4 — Call a state-changing function (transaction):**

```java
new ContractExecuteTransaction()
    .setContractId(contractId)
    .setGas(100_000)
    .setFunction("vote",
        new ContractFunctionParameters().addUint256(proposalIndex))
    .execute(client);
```

### Transaction Fields (Apply to Any Transaction)

```java
Transaction<?> tx = new AccountCreateTransaction()
    .setKey(key)
    .setInitialBalance(Hbar.fromTinybars(1000))
    .setMaxTransactionFee(new Hbar(2))   // caps fee; reverts if exceeded
    .setTransactionMemo("memo");
```

### web3j (Alternative — Ethereum-Compatible Java Library)

`web3j` was designed for Ethereum but works with Hedera via EVM compatibility:
- Java wrapper generation from ABI + bytecode (`web3j generate`)
- Maven plugin for automated code generation
- API compatible with Hedera HSCS because it speaks standard JSON-RPC

Useful when code must be portable across Ethereum and Hedera, or when the team prefers generated type-safe wrappers over the HAPI SDK's fluent builder pattern.

---

## Developer SDK

### Package Name — Hiero Rebrand

In September 2024, Hedera transferred its source code to the **Linux Foundation Decentralised Trust** project under the **Hiero** umbrella. The JavaScript/TypeScript SDK was republished under a new package name:

| Old | New | Status |
|---|---|---|
| `@hashgraph/sdk` | `@hiero-ledger/sdk` | `@hashgraph/sdk` still available but new projects should use the Hiero package |

The API surface is identical. The Java SDK follows the same pattern: `com.hedera.hashgraph:sdk` → `org.hiero:hiero-sdk-java`.

---

### Core Imports (JavaScript / Node.js)

```javascript
const {
  AccountId,
  PrivateKey,
  Client,
  TransferTransaction,
  Hbar,
  AccountCreateTransaction,
} = require("@hiero-ledger/sdk");
```

---

### Client Initialisation

```javascript
const client = Client.forTestnet();  // or Client.forMainnet()
client.setOperator(
  AccountId.fromString(process.env.HEDERA_ACCOUNT_ID),
  PrivateKey.fromStringECDSA(process.env.HEDERA_PRIVATE_KEY)
);
```

`setOperator` designates the default **fee payer** and **auto-signer**. Every transaction executed via this client is automatically signed by the operator's key on `.execute()`. The operator is debited the Hedera network fee (denominated in USD, converted to HBAR at execution time); other accounts are debited only the explicit amounts stated in the transaction.

---

### ECDSA Account Creation with EVM Alias

```javascript
const privateKey = PrivateKey.generateECDSA();
const publicKey  = privateKey.publicKey;

const tx = new AccountCreateTransaction()
  .setECDSAKeyWithAlias(publicKey)   // derives 0x EVM alias from the ECDSA key
  .setInitialBalance(new Hbar(10));

const response  = await tx.execute(client);
const receipt   = await response.getReceipt(client);
const accountId = receipt.accountId; // 0.0.XXXXX Hedera-native ID
```

`setECDSAKeyWithAlias` creates a Hedera account with an **EVM alias** (an Ethereum-style `0x...` address) derived from the ECDSA public key. The account is accessible via both:

- **Native Hedera API** — using the `0.0.XXXXX` account ID
- **EVM-compatible tools** (MetaMask, Ethers.js, Hardhat) — using the derived `0x` alias

Alternative: `.setKeyWithoutAlias(publicKey)` creates an account whose EVM address is derived from the account ID, not the public key — not fully EVM-compatible.

### Key Types — ED25519 vs ECDSA

| | ED25519 | ECDSA (secp256k1) |
|--|---------|------------------|
| `generate` | `PrivateKey.generateED25519()` | `PrivateKey.generateECDSA()` |
| `fromString` | `PrivateKey.fromStringED25519(str)` | `PrivateKey.fromStringECDSA(str)` |
| EVM alias | Not supported | Yes — via `setECDSAKeyWithAlias` |
| Use case | Hedera-native accounts, operators | EVM-compatible accounts (MetaMask, Hardhat) |
| Signature size | Smaller / faster | Standard Ethereum (secp256k1) |

**Rule:** Operator accounts (the Testnet account created via the faucet) typically use ED25519. New accounts intended for EVM smart contract interaction should use ECDSA with `setECDSAKeyWithAlias`.

---

### The `freezeWith` + `sign` Transaction Pattern

Hedera transactions are **immutable once frozen**. The signing flow for a non-operator sender is:

```javascript
let tx = new TransferTransaction()
  .addHbarTransfer(senderAccountId, new Hbar(-amount))  // debit
  .addHbarTransfer(receiverAccountId, new Hbar(amount)) // credit
  .freezeWith(client);   // 1. lock transaction bytes (node, valid duration, tx ID)

tx = await tx.sign(senderPrivateKey); // 2. attach sender's authorisation signature

const response = await tx.execute(client); // 3. operator auto-signs as fee payer
```

| Step | What it does | Required for |
|---|---|---|
| `.freezeWith(client)` | Fixes the transaction bytes. Nothing may change after this. | Any transaction requiring explicit signing |
| `.sign(privateKey)` | Attaches a signature from a specific key. Returns a new object — must reassign. | Non-operator accounts (the `from` account on a debit) |
| `.execute(client)` | Submits to network; operator key auto-signs here. | All transactions |

**Operator exemption:** If the operator account is the sender, no `.sign()` call is needed — the SDK signs on `.execute()` automatically. This is why an `operator` object can be constructed with `privateKey: null` when the client is already configured with the operator key.

---

### Transaction Receipt and ID

```javascript
const response = await tx.execute(client);
const receipt  = await response.getReceipt(client);

receipt.status.toString();   // "SUCCESS" | "INSUFFICIENT_PAYER_BALANCE" | ...
receipt.accountId;           // populated for AccountCreateTransaction
response.transactionId.toString();
// format: "0.0.XXXXX@1234567890.000000000"
//          payer     Unix seconds  nanoseconds
```

The transaction ID format is globally unique: it encodes the **payer account** and the **consensus timestamp** (nanosecond precision). This ID can be used to retrieve full transaction details from the mirror node REST API or from **HashScan**:

```
https://hashscan.io/testnet/transaction/<txId>
https://hashscan.io/mainnet/transaction/<txId>
```

---

### Key `Hbar` Denomination Notes

```javascript
new Hbar(1)          // 1 HBAR = 100,000,000 tinybar
new Hbar(0.5)        // 0.5 HBAR — decimal supported
Hbar.fromTinybars(100000000) // equivalent to new Hbar(1)
```

`TransferTransaction.addHbarTransfer` expects a signed `Hbar` value:
- Negative → debit (funds leave the account)
- Positive → credit (funds arrive at the account)

The sum of all `addHbarTransfer` amounts in a transaction must equal zero; the network enforces this as a validity requirement.

---

### Mirror Node REST API

Mirror Nodes are read-only data services that index Hedera's ledger history and expose it via a REST API. They run separately from the consensus nodes and propagate asynchronously — typically a few seconds behind consensus.

```
Testnet base URL: https://testnet.mirrornode.hedera.com/api/v1/
MainNet base URL: https://mainnet.mirrornode.hedera.com/api/v1/
```

**Key endpoints:**

| Endpoint | Returns |
|----------|---------|
| `GET /accounts/{idOrAddress}` | Account info — `evm_address`, `balance`, `key` |
| `GET /transactions/{transactionId}` | Full transaction record, status, fees |
| `GET /contracts/{idOrAddress}` | Contract bytecode, ABI, storage |
| `GET /tokens/{tokenId}` | Token metadata (name, symbol, decimals, supply) |

**Querying EVM address after account creation:**

```javascript
// Wait for Mirror Node propagation before querying
await new Promise((resolve) => setTimeout(resolve, 5000));

const mirrorResponse = await fetch(
  `https://testnet.mirrornode.hedera.com/api/v1/accounts/${accountId.toString()}`
);
if (mirrorResponse.ok) {
  const mirrorData = await mirrorResponse.json();
  const evmAddress = mirrorData.evm_address; // "0x..." — only populated for ECDSA alias accounts
}
```

**Production retry pattern** (Mirror Node may not have propagated yet):

```javascript
async function fetchWithRetry(url, retries = 5, delayMs = 2000) {
  for (let i = 0; i < retries; i++) {
    const res = await fetch(url);
    if (res.ok) return res.json();
    await new Promise(r => setTimeout(r, delayMs * (i + 1)));
  }
  throw new Error(`Mirror Node fetch failed after ${retries} attempts`);
}
```

**Why derive EVM address from Mirror Node?** When `setECDSAKeyWithAlias` is used, the EVM address equals `keccak256(publicKey)[12:]` — which you can compute off-chain. Querying the Mirror Node is a confirmation step, not strictly required. For accounts created with `setKeyWithoutAlias`, the Mirror Node is the only way to retrieve the EVM address (it is derived from the account ID, not the key).

---

### HTS SDK — Token Creation (JavaScript)

#### Basic Token (Immutable — no admin or supply keys)

```javascript
const txTokenCreate = await new TokenCreateTransaction()
  .setTokenName("Your Token Name")
  .setTokenSymbol("F")
  .setTokenType(TokenType.FungibleCommon)  // or TokenType.NonFungibleUnique for NFTs
  .setTreasuryAccountId(MY_ACCOUNT_ID)     // receives all initial supply
  .setInitialSupply(5000)
  .freezeWith(client);

const signedTxTokenCreate   = await txTokenCreate.sign(MY_PRIVATE_KEY);
const txTokenCreateResponse = await signedTxTokenCreate.execute(client);
const receiptTokenCreateTx  = await txTokenCreateResponse.getReceipt(client);
const tokenId               = receiptTokenCreateTx.tokenId;
```

**Why treasury must sign:** The treasury receives the initial supply. The network requires the treasury's explicit authorisation to prevent tokens being forced into an account.

**No admin/supply keys = immutable token.** The token name, symbol, and supply cannot change after creation.

#### Advanced Token (Mutable — with admin and supply keys)

```javascript
const txTokenCreate = await new TokenCreateTransaction()
  .setTokenName("Your Token Name")
  .setTokenSymbol("F")
  .setTokenType(TokenType.FungibleCommon)
  .setTreasuryAccountId(MY_ACCOUNT_ID)
  .setAdminKey(MY_PRIVATE_KEY.publicKey)   // enables TokenUpdateTransaction
  .setSupplyKey(MY_PRIVATE_KEY.publicKey)  // enables TokenMintTransaction / TokenBurnTransaction
  .setInitialSupply(5000)
  .freezeWith(client);
```

#### Token Key Reference

| Key | Set with | Enables |
|-----|----------|---------|
| `adminKey` | `.setAdminKey(pubKey)` | `TokenUpdateTransaction` — rename, change keys |
| `supplyKey` | `.setSupplyKey(pubKey)` | `TokenMintTransaction` / `TokenBurnTransaction` |
| `freezeKey` | `.setFreezeKey(pubKey)` | Freeze individual accounts |
| `kycKey` | `.setKycKey(pubKey)` | KYC-gate accounts before they can transact |
| `wipeKey` | `.setWipeKey(pubKey)` | Forcibly remove tokens from an account |
| `pauseKey` | `.setPauseKey(pubKey)` | Pause all transfers globally |

Keys not set at creation time cannot be added later unless `adminKey` is already set.

---

### HCS SDK — Topic Creation and Messaging (JavaScript)

```javascript
// Bare topic — no access controls
const txCreateTopic = new TopicCreateTransaction();

const txCreateTopicResponse = await txCreateTopic.execute(client);
const receiptCreateTopicTx  = await txCreateTopicResponse.getReceipt(client);
const topicId               = receiptCreateTopicTx.topicId.toString(); // "0.0.XXXXX"
```

**With access controls:**
```javascript
const txCreateTopic = new TopicCreateTransaction()
  .setTopicMemo("My application event log")
  .setSubmitKey(submitPublicKey)   // only this key may publish messages
  .setAdminKey(adminPublicKey);    // only this key may update or delete the topic
```

**Publishing a message:**
```javascript
await new TopicMessageSubmitTransaction()
  .setTopicId(topicId)
  .setMessage("{ \"event\": \"user_login\", \"userId\": 42 }")
  .execute(client);
```

**Subscribing (mirror node stream):**
```javascript
new TopicMessageQuery()
  .setTopicId(topicId)
  .subscribe(client, (message) => {
    console.log(message.contents.toString());
    console.log("Consensus timestamp:", message.consensusTimestamp.toString());
    console.log("Sequence number    :", message.sequenceNumber.toString());
  });
```

Each message is given a **consensus timestamp** and **sequence number** — tamper-evident because the ledger records a running hash of all prior messages.

---

### Batch Transaction SDK — HIP-551 (JavaScript)

`BatchTransaction` executes multiple inner transactions atomically: either all succeed, or all are rolled back.

#### The `batchify()` Pattern

`tx.batchify(client, batchPublicKey)` converts a transaction into an inner-transaction payload. The `batchPublicKey` is the key that will sign the outer `BatchTransaction`.

**Critical:** Each inner transaction still requires all of its own signers. `batchify` does not satisfy existing signing requirements.

```javascript
const batchKey       = PrivateKey.generateECDSA();
const batchPublicKey = batchKey.publicKey;

// Step 1: batchify each inner tx, then sign it
const txA = await new TransferTransaction()
  .addHbarTransfer(MY_ACCOUNT_ID, new Hbar(-1))
  .addHbarTransfer(receiverAccountId, new Hbar(1))
  .batchify(client, batchPublicKey);
const signedTxA = await txA.sign(MY_PRIVATE_KEY);

// Step 2: assemble the batch and sign with batchKey
const batchTx = await new BatchTransaction()
  .addInnerTransaction(signedTxA)
  // .addInnerTransaction(signedTxB) ...
  .freezeWith(client)
  .sign(batchKey);

const txResponse = await batchTx.execute(client);
const receipt    = await txResponse.getReceipt(client);
const txId       = txResponse.transactionId.toString();

// Inner tx IDs are accessible:
const innerTxIds = batchTx.innerTransactionIds;
```

#### Counterfactual Account ID Derivation

For ECDSA accounts created with `setECDSAKeyWithAlias`, the Hedera account ID can be derived from the public key **before** the account is created. This allows batching account creation with operations that reference the new account:

```javascript
const recipientAccountId = recipientAccountPublicKey.toAccountId(0, 0);
// shard=0, realm=0 → standard Testnet/MainNet
// Now use recipientAccountId in subsequent inner transactions within the same batch
```

#### HashScan URL Formats

| Transaction type | URL path | ID format |
|-----------------|----------|-----------|
| Standard | `/testnet/transaction/{txId}` | `0.0.XXXXX@seconds.nanos` |
| Batch | `/testnet/transactionsById/{txId}` | `0.0.XXXXX-seconds-nanos` (hyphens) |

```javascript
// Convert standard txId to batch URL format
const [entityId, timestamp] = txId.split('@');
const [seconds, nanos]      = timestamp.split('.');
const formattedTxId         = `${entityId}-${seconds}-${nanos}`;
// → https://hashscan.io/testnet/transactionsById/${formattedTxId}
```

#### TokenAirdropTransaction vs TransferTransaction

`TokenAirdropTransaction` (HIP-904) transfers tokens to accounts that have **not** yet associated with the token. `TransferTransaction.addTokenTransfer` requires prior `TokenAssociateTransaction` from the recipient.

```javascript
// HIP-904 — no prior token association needed
const txTokenAirdrop = new TokenAirdropTransaction()
  .addTokenTransfer(tokenId, MY_ACCOUNT_ID, -1000)     // debit sender
  .addTokenTransfer(tokenId, recipientAccountId, 1000); // credit recipient (no pre-association)
```

See [[examples/hedera-hts-hcs-batch-js]] for a full worked example covering all five operations.

---

## Key Statistics at a Glance

- **Total HBAR supply:** 50 billion (fixed, no inflation)
- **Circulating supply:** ~84.8% (as of 2025)
- **Total accounts:** 9.26 million (October 2025)
- **Daily transactions:** ~500,000 average
- **Finality time:** 3–7 seconds
- **Transaction cost:** $0.0001 (crypto transfer)
- **Staking APY:** ~6.5% (treasury-funded, no slashing)
- **Council members:** 30+ (cap: 39)
- **Source code licence:** Apache 2.0 (since 2022, via Linux Foundation)
- **Smart contract EVM:** Besu EVM, 15M gas/second
- **Token service TPS:** 10,000+

---

## Related Pages

- [[concepts/distributed-ledger-technology]] — DLT taxonomy; Hedera's position as a Hashgraph-class DLT; comparison with blockchain, DAG, and Holochain
- [[concepts/blockchain-microcredentials]] — verifiable credentials anchored to public DLTs including Hedera (did:hedera)
- [[concepts/bitcoin-history]] — historical context for why Hedera was designed as a response to blockchain limitations
- [[concepts/prompt-injection]] — Hedera's AI Studio and agentic AI use cases create new prompt injection / irreversible transaction attack surfaces
- [[examples/hedera-local-ledger-js]] — working JavaScript example combining a local SHA-256 hash-chained ledger with real Hedera Testnet transactions (`@hiero-ledger/sdk`)
- [[examples/hedera-account-creation-js]] — account creation with ECDSA key, EVM alias, and Mirror Node REST API query
- [[examples/hedera-hts-hcs-batch-js]] — HBAR transfer, HTS token creation (basic and advanced), HCS topic creation, batch transaction (HIP-551) with batchify pattern
- [[examples/hedera-lecture4-voting-contract]] — Poll V1 and V2 Solidity contracts with full HAPI Java deployment code
- [[concepts/token-standards-erc20-erc721]] — ERC-20 and ERC-721 standards, stablecoin taxonomy, HTS vs ERC comparison
