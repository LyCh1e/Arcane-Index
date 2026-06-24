---
type: source
status: established
title: "Crypto Crime Report 2025 — Chainalysis"
source_type: industry-report
author: Chainalysis
date_published: 2026
url: https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/
confidence: high
key_claims:
  - Total crypto theft in 2025 exceeded $3.4 billion
  - Single Bybit hack ($1.5B) = 44% of annual total
  - DeFi protocol losses were $680M in 2025 (down from $2.62B peak in 2022)
  - North Korea (DPRK) stole at least $2.02 billion in 2025
  - Median loss per DeFi incident fell 75% from $6M (2022) to $1.5M (2025)
  - Protocol logic exploits caused 89.1% of DeFi losses in 2025
tags: [blockchain, security, DeFi, hacks, cybercrime, North-Korea]
domain: blockchain
---

# Source: Chainalysis Crypto Crime Report 2025

## Summary

Chainalysis is the leading blockchain analytics firm. Its annual crypto crime report analyses on-chain data to quantify theft, fraud, ransomware, and money laundering. The 2025 report (published 2026) covers full-year 2025 activity.

## Headline Figures

| Metric | 2025 Figure |
|---|---|
| Total crypto stolen | **>$3.4 billion** |
| Single largest incident | Bybit exchange hack — **$1.5 billion** (DPRK attributed) |
| Bybit share of annual total | **44 %** |
| DeFi protocol losses | **$680 million** |
| DeFi TVL peak (2025) | $171.9 billion (early October) |
| DeFi TVL year-end | $116.7 billion (Q4 decline) |
| Ethereum share of DeFi TVL | 56.5 % |

## Trends

### Concentration Risk
Theft is increasingly concentrated in fewer, larger events. One incident (Bybit) represented nearly half of all annual losses, whereas 2022-2023 saw losses spread across many mid-size exploits.

### DeFi Security Improvement
DeFi protocol losses have improved dramatically from the 2022 peak:

| Year | DeFi Losses | Trend |
|---|---|---|
| 2022 | $2.62 billion | Peak |
| 2024 | $534 million | −80 % |
| 2025 | $680 million | Partial rebound |

Median loss per incident: **$6M → $1.5M** (75 % reduction 2022–2025) — suggests protocol-level security is genuinely improving.

### Shift in Attack Vectors
- **2022**: Smart contract bugs dominated losses
- **2025**: Protocol logic exploits caused **89.1 %** of DeFi losses
- Private key / personal wallet compromises grew from 7.3 % of stolen value (2022) → **44 %** (2024)
- CeFi (centralised exchanges) became a larger target than DeFi for the first time

### North Korean Threat Actor
DPRK-affiliated groups (Lazarus Group, TraderTraitor) remain the single largest threat:
- 2025 stolen: **≥$2.02 billion** (record)
- 2024 stolen: ~$1.34 billion
- Increase: **+$681 million year-over-year**
- Primary method: social engineering of exchange employees → private key compromise

## Contribution to Wiki

Grounds the threat model section of [[concepts/blockchain-technology]] with authoritative loss statistics. Connects to [[concepts/security-by-design-principles]] (private key management as design concern) and [[concepts/owasp-top-10]].
