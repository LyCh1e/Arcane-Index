---
type: source
title: "Hedera Developer Course — Lecture 1: Bitcoin, Digital Currencies & Crypto Wallets"
tags: [bitcoin, cryptocurrency, wallets, hedera, SWIFT, stablecoin, blockchain, digital-currencies, HashPack, Ledger]
domain: blockchain
source-file: "raw/Blockchain Lecture-1.pdf"
author: "Hendrik Ebbers (OpenElements / Swirlds Labs / Hedera)"
format: lecture-slides
slides: 62
ingested: 2026-08-12
status: ingested
related-concepts:
  - "[[concepts/bitcoin-history]]"
  - "[[concepts/hedera-network]]"
  - "[[concepts/crypto-wallets]]"
  - "[[concepts/blockchain-technology]]"
---

# Hedera Developer Course — Lecture 1: Bitcoin, Digital Currencies & Crypto Wallets

**Source:** `raw/Blockchain Lecture-1.pdf`
**Author:** Hendrik Ebbers — OpenElements / Swirlds Labs / Hedera
**Format:** 62 lecture slides
**Part of:** Three-part Hedera Developer Course (Java + Solidity)

---

## Course Structure (Slides 4–8)

The course is divided into three parts:

| Part | Focus |
|------|-------|
| **Part 1** | Blockchain and cryptography concepts (this lecture) |
| **Part 2** | DLT platforms — Ethereum, Hedera, EVM, smart contracts |
| **Part 3** | Hedera enterprise use cases and real-world application |

Languages used throughout: Java and Solidity.

---

## Bitcoin History (Slides 10–20)

### Origin

Satoshi Nakamoto published *"Bitcoin: A Peer-to-Peer Electronic Cash System"* in October 2008, hosted at **bitcoin.org**. The reference implementation followed in 2009, published at **github.com/bitcoin/bitcoin**. Satoshi became inactive in 2010 and has never been publicly identified (person or group).

Relevant figures on Satoshi's holdings and lost coins:

| Fact | Figure |
|------|--------|
| Satoshi's estimated holdings | 750,000–1,100,000 BTC |
| Estimated lost BTC (Chainalysis 2017) | 2.78 million–3.79 million BTC |
| Hard cap | 21 million BTC |

### Bitcoin's Four Original Goals

The lecture frames Bitcoin's design around four goals and assesses which were achieved:

| Goal | Achieved? | Note |
|------|-----------|------|
| Everyday currency | ✗ | Volatility and transaction friction make it impractical for daily purchases |
| Common currency (reduced exchange cost) | ✗ | Exchange into fiat remains costly; adoption too fragmented |
| Less exchange cost vs traditional rails | ✓ | Peer-to-peer transfers significantly cheaper than SWIFT MT103 |
| Cryptographic proof instead of trust | ✓ | Immutable blockchain removes the need for a trusted third party |

The lecture notes the broader label shifted from "Bitcoin" to "Crypto Currency" when discussing goal fulfilment — acknowledging that other cryptocurrencies (stablecoins, HBAR) address goals Bitcoin itself struggled with.

### Bitcoin Pizza Day (Slides 22–30)

| Event | Detail |
|-------|--------|
| Forum post | 18 May 2010 — Laszlo Hanyecz offered 10,000 BTC for two pizzas on the Bitcoin Forum |
| Confirmation | 22 May 2010 — "I just want to report that I successfully traded 10,000 bitcoins for pizza. Thanks jercos!" |
| Actual pizza cost | ~$41 |
| Value at $19,000/BTC | ~$190 million |

22 May is observed each year as **Bitcoin Pizza Day** — the first documented real-world commercial transaction using Bitcoin.

---

## Digital Currencies — Taxonomy (Slides 33–38)

The lecture distinguishes two fundamental categories:

### Coins
Properties:
- Backed by a **digital or physical asset** (or no asset at all — pure digital scarcity)
- **Intrinsic value** (or perceived scarcity value)
- Medium of exchange
- **Store of value** — the "digital gold" narrative

Examples: Bitcoin (BTC), Ether (ETH), HBAR

### Stablecoins
Properties:
- **Pegged** to a fiat currency (USD, SGD, EUR) or a commodity (gold)
- **Price stability** by design — removes the volatility that prevents coins from functioning as everyday currency
- Enables speed and programmability without speculative exposure

Examples: USDT (Tether), USDC, DAI

The key distinction: coins are designed as stores of value or speculative assets; stablecoins are designed as **stable mediums of exchange**.

---

## Crypto Hype Drivers (Context, Slides)

The lecture identifies several psychological and cultural drivers behind cryptocurrency speculation:

- **FOMO** (Fear Of Missing Out) — retail investors entering during price peaks
- **Influencer effect** — celebrities and social-media personalities promoting projects without technical understanding
- **Financial sovereignty narrative** — "be your own bank"
- **Financial inclusion narrative** — reaching the unbanked population
- **Digital gold narrative** — Bitcoin as a hedge against inflation and fiat debasement

These drivers explain price cycles but are distinct from genuine enterprise utility.

---

## Real Use Case — Standard Bank × Shinhan Bank (Slides 40–47)

### The Old System (SWIFT MT103)

International transfer from **Standard Bank (South Africa) → Shinhan Bank (South Korea)**:

```
Standard Bank (ZA)
       │ SWIFT MT103
       ▼
Global Mega Bank (correspondent)
       │ SWIFT MT103
       ▼
Regional Correspondent Bank (South Korea)
       │
       ▼
Shinhan Bank (KR)
```

| Property | Old (SWIFT MT103) |
|----------|-----------------|
| Fee | $40+ |
| Settlement time | Up to 6 business days |
| Tracking | None — no real-time visibility |
| Hours | Limited banking hours |
| Hops | 2+ correspondent/intermediary banks |

### The New System (Hedera Stablecoin PoC — September 2023)

Both banks issue custom stablecoins on Hedera. The transfer becomes a direct on-chain swap — no correspondent banks, no SWIFT.

| Property | Hedera PoC (Sept 2023) |
|----------|----------------------|
| Fee | <$0.10 |
| Settlement time | <1 minute |
| Tracking | Real-time (HashScan) |
| Hours | 24/7 |
| Intermediaries | None |

This use case is the primary enterprise argument for Hedera in the lecture: **the value proposition is not replacing Bitcoin, but replacing SWIFT for cross-border settlements with stablecoins on a fast, low-fee, governed DLT**.

---

## Crypto Wallets (Slides 49–62)

### Key Analogy (Lecture Framing)

> "Your public key is like your bank account ID.  
> Your private key is like your online banking password — but if you lose it, no bank employee can reset it."

This framing is the most important teaching point: **there is no account recovery**. Loss of the private key means permanent loss of funds with no recourse.

### Wallet Categories

| Type | Temperature | Connection | Description |
|------|-------------|------------|-------------|
| **Hardware** | Cold | Offline | Physical device (e.g. Ledger); private key never leaves the device |
| **Paper** | Cold | Offline | Printed QR code; ultimate cold storage; fragile (fire, water) |
| **Desktop** | Hot | Online | Software on a personal computer |
| **Mobile** | Hot | Online | App on a smartphone |
| **Web** | Hot | Online | Browser-based; most convenient, highest risk |

**Hot** = internet-connected; convenient but exposed to online attack vectors.  
**Cold** = offline; more secure but less convenient for frequent transactions.

### Security Features to Look For

- Encryption of stored keys
- Two-factor authentication (2FA)
- Backup and recovery options
- Multi-signature (multi-sig) support

### Specific Wallets Covered

#### Coinbase Wallet
- Mobile app and Chrome extension
- Supports Bitcoin, Ethereum, and ERC-20 tokens
- Non-custodial (user holds keys); distinct from the Coinbase exchange account

#### HashPack
- **Leading HBAR wallet** on the Hedera network
- Supports Hedera Testnet — users receive daily free testnet HBAR
- Browser extension + mobile
- Recommended for all Hedera development exercises

#### Ledger (Hardware)
- Cold storage device supporting **1,000+ cryptocurrencies** including BTC, ETH, HBAR
- Private key never exposed to the internet
- Recovery: **24-word mnemonic phrase** (BIP-39 standard) — must be written down and stored securely offline
- Loss of the mnemonic = permanent loss of funds

---

## Hands-On Exercises

| Exercise | Platform |
|----------|----------|
| Examine crypto prices — compare BTC, ETH, USDT, HBAR, memecoins (Blades of Glory, Lion King, Mother of Memes), SCAM token | Coinbase |
| Install HashPack, create a Testnet account, send coins | Hedera Testnet |

The SCAM token exercise is pedagogical: demonstrating that any token can be created and listed, and that absence of regulation means zero protection for buyers.

---

## Source Quality Assessment

| Criterion | Rating | Notes |
|-----------|--------|-------|
| Technical accuracy | High | Bitcoin history facts align with primary sources; use case figures from documented Sept 2023 PoC |
| Currency | High | Stablecoin PoC is Sept 2023; wallet landscape current as of lecture date |
| Bias | Low | Clearly pro-Hedera framing; Bitcoin goals assessed fairly (two ✗) |
| Depth | Medium | Introductory course — concepts accurate but surface-level; refer to `[[concepts/bitcoin-history]]` for full historical depth |
| Practical value | High | HashPack + Testnet exercises directly applicable to Hedera development track |

---

## Key Concepts Introduced

- [[concepts/bitcoin-history]] — Satoshi Nakamoto, Bitcoin Pizza Day, 4 goals, halving cycles
- [[concepts/crypto-wallets]] — public/private key, wallet taxonomy (hot/cold), HashPack, Ledger, mnemonic phrases
- [[concepts/hedera-network]] — Standard Bank × Shinhan Bank SWIFT vs Hedera stablecoin PoC (Sept 2023)
- [[concepts/blockchain-technology]] — coins vs stablecoins taxonomy; digital gold narrative

---

## Related Pages

- [[sources/hedera-lecture-2-blockchain-hashing]] — Lecture 2: block anatomy, hash chaining, SHA family, Java `MessageDigest`
- [[concepts/bitcoin-history]] — comprehensive Bitcoin history from cypherpunk origins to 2025 ATH
- [[concepts/hedera-network]] — Hedera architecture, governing council, native services, SDK patterns
- [[concepts/crypto-wallets]] — full wallet taxonomy, key management, hot/cold security trade-offs
