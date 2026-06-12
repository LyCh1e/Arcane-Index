---
type: synthesis
title: "Research: Blockchain Technology"
created: 2026-06-12
updated: 2026-06-12
tags: [research, blockchain, cryptography, DeFi, consensus, security, scalability, CBDC]
status: complete
rounds: 3
searches: 9
sources_fetched: 7
pages_created: 8
related:
  - "[[concepts/blockchain-technology]]"
  - "[[sources/hacken-smart-contract-vulnerabilities-2025]]"
  - "[[sources/atlantic-council-cbdc-tracker-2026]]"
  - "[[sources/chainalysis-crypto-crime-report-2025]]"
  - "[[sources/layer2-scaling-comparison-2025]]"
  - "[[entities/satoshi-nakamoto]]"
  - "[[entities/vitalik-buterin]]"
  - "[[entities/nick-szabo]]"
sources:
  - "[[sources/hacken-smart-contract-vulnerabilities-2025]]"
  - "[[sources/atlantic-council-cbdc-tracker-2026]]"
  - "[[sources/chainalysis-crypto-crime-report-2025]]"
  - "[[sources/layer2-scaling-comparison-2025]]"
---

# Research: Blockchain Technology

## Overview

Blockchain is a distributed, append-only ledger using cryptographic hashing to make records tamper-evident and consensus mechanisms to achieve agreement among mutually distrusting parties. The field has bifurcated into two tracks: **public, permissionless chains** (Bitcoin, Ethereum) optimised for trustlessness; and **permissioned, consortium chains** (Hyperledger Fabric, R3 Corda) optimised for enterprise throughput and compliance. As of 2026, both tracks are in production use, and a third track — **CBDCs** — is in active government deployment, representing state-controlled money on permissioned ledgers.

---

## Key Findings

### 1. The Security Landscape is Shifting — From Protocol Bugs to Key Theft
(Source: [[sources/chainalysis-crypto-crime-report-2025]])

- **Total crypto theft 2025**: >$3.4 billion
- **Bybit exchange hack**: $1.5B (44 % of annual total); attributed to DPRK / Lazarus Group
- **DPRK total 2025**: ≥$2.02 billion stolen — a single nation-state dominates global crypto theft
- **DeFi losses improving**: $2.62B peak (2022) → $534M (2024) → $680M (2025)
- Median loss per DeFi incident fell **75 %** (2022–2025), from $6M to $1.5M — genuine protocol security progress
- **Attack vector shift**: Smart contract bugs (2022 dominant) → Protocol logic exploits (89.1 % of 2025 DeFi losses) → Private key / personal wallet compromise growing fastest (7.3 % → 44 % of total stolen value)

> **Implication**: The biggest losses are no longer in on-chain protocol bugs but in off-chain key management failures. The weakest link has moved from code to people.

### 2. Smart Contract Vulnerabilities — Known, Preventable, Still Exploited
(Source: [[sources/hacken-smart-contract-vulnerabilities-2025]])

- Q1 2026 alone: 44 incidents, **$482M** losses (dramatic escalation from Q1 2024's $45M)
- Top 3 loss-generating vulnerabilities: **Flash loans** ($181M Beanstalk alone), **Reentrancy** ($80M Rari Capital), **Oracle manipulation** ($15.6M Inverse Finance)
- MEV bots extracted **>$1 billion** since June 2020 via front-running
- **All top 10 vulnerabilities have known mitigations** — the problem is audit coverage and developer awareness, not unknown attack classes

### 3. Layer 2 Scaling is Maturing Rapidly
(Source: [[sources/layer2-scaling-comparison-2025]])

| L2 Type | Lead Project | TVL | TPS | Finality |
|---|---|---|---|---|
| Optimistic Rollup | Arbitrum | $15B+ | 2,000–4,000 | 7-day dispute |
| ZK Rollup | zkSync Era | (total $6.27B) | 2,000–20,000 | Instant |
| Sidechain | Polygon PoS | $5B+ | 7,000+ | Own consensus |
| State Channels | Lightning Network | — | ∞ off-chain | Instant |

- Arbitrum alone hosts **500+ applications** — L2 has crossed from research to production
- ZK rollups are closing the gap: STARKs are additionally **quantum-resistant** (no trusted setup required)
- Cross-rollup interoperability protocols are the next frontier (2025–2026), enabling asset movement between L2s without L1 bridging

### 4. CBDCs: 146 Countries Exploring, Only 3 Launched, China Dominant
(Source: [[sources/atlantic-council-cbdc-tracker-2026]])

- **146 countries** (98 % of global GDP) exploring a CBDC — up from 35 in 2020
- **Only 3 retail CBDCs fully launched**: Bahamas (Sand Dollar), Jamaica (JAM-DEX), Nigeria (eNaira)
- Adoption even in launched countries remains limited; Nigeria eNaira driven by government airdrops, not organic use
- **China's e-CNY**: 3.4 billion transactions; 16.7 trillion RMB cumulative; expanding cross-border via mBridge ($55.49B volume, 2,500× growth since 2022 pilot)
- **EU**: 2026 issuance decision pending after October 2025 preparation phase conclusion
- **USA**: GENIUS Act (July 2025) **bans** a Federal Reserve retail CBDC; pivots to stablecoin regulation instead
- BRICS alignment: 9 of 11 BRICS members in active CBDC pilots — geopolitical dimension of digital currency is significant

### 5. Post-Quantum Migration is Urgent but Not Yet Crisis
(Source: thequantumspace.org PQC Standards, 2025)

- NIST finalised post-quantum suite (2024): **CRYSTALS-Dilithium** (FIPS 204 / ML-DSA), FALCON, SPHINCS+ for signatures; CRYSTALS-Kyber for key encapsulation
- **Critical migration window**: Europe identifies 2026–2030 as the period for hybrid deployment
- Current blockchain ECDSA is **vulnerable to Shor's algorithm** on sufficiently large quantum computers (projected "next decade" for "millions of logical qubits")
- SHA-256 is **safe** — Grover's halves effective security from 256 → 128 bits, still computationally infeasible
- Dilithium signatures are **~40–70× larger** than ECC (2.4–4.6 KB vs 64 bytes) — significant impact on block size and transaction fees
- Polkadot's Web3 Foundation published a Dilithium migration roadmap in 2025; StarkNet STARKs are inherently quantum-resistant
- **Migration strategy**: Hybrid cryptography (ECC + PQC in parallel) allows staged transition without hard forks

### 6. Real-World Asset Tokenisation is Growing Rapidly
- Tokenised RWA market (excluding stablecoins): **$32 billion** on-chain by May 2026
- Including stablecoins (the largest tokenised RWA): **>$300 billion**
- Standard Chartered projects **$30 trillion** market by 2034
- 57 % of institutional investors interested in tokenised assets; 72 % plan investment by 2026
- Key asset classes: US Treasuries (largest share), real estate, private credit, commodities

---

## Key Entities

- [[entities/satoshi-nakamoto]]: Pseudonymous Bitcoin inventor; whitepaper (2008) solved Byzantine Generals Problem for digital cash without trusted parties
- [[entities/vitalik-buterin]]: Ethereum founder; coined Blockchain Trilemma; led PoW→PoS Merge; proposed rollup-centric "Endgame" vision
- [[entities/nick-szabo]]: Originated smart contract concept (1994) and Bit Gold (1998) — direct Bitcoin predecessor
- **Chainalysis**: Leading blockchain analytics firm; primary source for on-chain crime attribution data
- **Hacken**: Security audit firm; publishes authoritative smart contract vulnerability research
- **Atlantic Council GeoEconomics Center**: Maintains the definitive CBDC tracker
- **NIST**: Published FIPS 203/204/205 post-quantum cryptography standards (2024)
- **Lazarus Group / TraderTraitor** (DPRK): Nation-state threat actor; stole ≥$2.02B in 2025

---

## Key Concepts

- [[concepts/blockchain-technology]]: Full technical reference — block anatomy, consensus, smart contracts, security, scalability
- **Blockchain Trilemma**: Decentralisation × Security × Scalability — cannot maximise all three simultaneously
- **MEV (Maximal Extractable Value)**: Value extracted by miners/validators by reordering, inserting, or censoring transactions; >$1B extracted via front-running since 2020
- **ZK-Rollup vs Optimistic Rollup**: Two dominant L2 paradigms — ZK uses cryptographic proofs (instant finality, higher proving cost); Optimistic uses fraud proofs (7-day delay, lower cost, more mature)
- **CBDC**: Central Bank Digital Currency — state-issued digital money; permissioned ledger, not trustless; represents fiat money infrastructure modernisation, not decentralisation
- **Post-Quantum Cryptography (PQC)**: NIST-standardised algorithms (Dilithium, FALCON, Kyber) designed to resist quantum computers; migration is urgent in 2026–2030 window
- **RWA Tokenisation**: Putting ownership rights to off-chain assets (real estate, bonds, equities) on-chain as programmable tokens

---

## Contradictions

- [[sources/chainalysis-crypto-crime-report-2025]] reports DeFi losses improving (protocol security maturing) while [[sources/hacken-smart-contract-vulnerabilities-2025]] shows Q1 2026 ($482M) dramatically exceeding Q1 2024 ($45M). **Resolution**: The overall trend is improvement but with high variance — one large exploit can spike quarterly numbers; the median incident loss is still falling.
- RWA market size figures vary wildly depending on whether stablecoins are included: sources cite $0.67B, $32B, $297B, or $612B depending on scope. The most defensible narrow figure (non-stablecoin on-chain RWAs): **~$32B** (RWA.xyz, May 2026).
- The US GENIUS Act bans a retail CBDC from the Fed, yet the US dollar is the world's reserve currency — this creates tension as China's e-CNY expands cross-border via mBridge without US dollar equivalent.

---

## Open Questions

1. **Quantum timeline precision**: When will quantum computers reach "cryptographically relevant" scale? Industry consensus says "next decade" but without precision — makes migration prioritisation difficult.
2. **CBDC adoption gap**: Why do launched CBDCs (Nigeria, Bahamas, Jamaica) show low organic adoption despite government mandates? What design factors drive genuine user adoption vs airdrop-driven numbers?
3. **ZK proof EVM equivalence**: StarkNet and zkSync claim EVM-compatibility but at different levels of equivalence — which projects will achieve full equivalence and when?
4. **Regulatory fragmentation**: MiCA (EU), GENIUS Act (US), and FSB guidelines create diverging regulatory regimes — how will cross-border DeFi protocols operate under simultaneous conflicting rules?
5. **DPRK attribution mechanics**: How does Chainalysis attribute hacks to DPRK with enough confidence for government sanctions? What are the false-positive risks?
6. **MEV and fairness**: Is MEV fundamentally extractive (wealth transfer from users to validators), or can it be captured and redistributed? PBS (Proposer-Builder Separation) is the current Ethereum approach — has it meaningfully reduced harm?

---

## Sources

| Source | Author | Date | Confidence |
|---|---|---|---|
| [[sources/hacken-smart-contract-vulnerabilities-2025]] | Hacken Research | 2025 | High |
| [[sources/atlantic-council-cbdc-tracker-2026]] | Atlantic Council | 2026 | High |
| [[sources/chainalysis-crypto-crime-report-2025]] | Chainalysis | 2026 | High |
| [[sources/layer2-scaling-comparison-2025]] | CoinCryptoRank | 2025 | Medium |
| Fidelity — PoW vs PoS | Fidelity Investments | 2025 | High |
| thequantumspace.org PQC Migration | The Quantum Space | 2025 | Medium |
| CoinLedger — CBDC Developments | CoinLedger Research | 2025 | Medium |
