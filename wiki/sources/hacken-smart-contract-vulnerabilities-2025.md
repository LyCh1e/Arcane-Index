---
type: source
status: established
title: "Top 10 Smart Contract Vulnerabilities (Hacken, 2025)"
source_type: security-report
author: Hacken Research
date_published: 2025
url: https://hacken.io/discover/smart-contract-vulnerabilities/
confidence: high
key_claims:
  - Q1 2026 saw 44 incidents with $482M in total losses
  - Q1 2024 saw 16 incidents averaging $2.8M each
  - MEV bots have profited over $1 billion since June 2020
  - Beanstalk lost $181M to a flash loan governance attack
  - Reentrancy remains the most exploited vulnerability class
tags: [blockchain, smart-contracts, security, DeFi, exploits]
domain: blockchain
---

# Source: Top 10 Smart Contract Vulnerabilities — Hacken (2025)

## Summary

Hacken's authoritative security research report catalogues the ten most dangerous smart contract vulnerability classes, with real exploit examples, loss figures, and concrete prevention techniques. The report is updated with 2024–2026 incident data.

## Key Statistics

- **Q1 2024**: 16 exploit incidents → $45 million total losses ($2.8M average)
- **Q1 2026**: 44 incidents → $482 million total losses (significant escalation)
- **Flash loan attacks Q1 2024**: 10 high-profile incidents → $33M losses
- **MEV extraction**: >$1 billion profit by MEV bots since June 2020

## Top 10 Vulnerability Classes

| Rank | Vulnerability | Notable Hack | Loss |
|---|---|---|---|
| 1 | **Reentrancy** | Rari Capital (April 2022) | $80M |
| 2 | **Integer overflow/underflow** | Poolz Finance (March 2023) | $390K |
| 3 | **Improper access control** | HospoWise (public burn function) | — |
| 4 | **Front-running / MEV** | MEV bots collectively | >$1B |
| 5 | **Denial of service** | Gas limit exhaustion | — |
| 6 | **Weak randomness** | Block property manipulation | — |
| 7 | **Vulnerable external calls** | Dexible (February 2023) | $2M |
| 8 | **Logic errors** | Insufficient testing | — |
| 9 | **Oracle manipulation** | Inverse Finance (TWAP) | $15.6M |
| 10 | **Flash loan attacks** | Beanstalk ($181M governance takeover) | $181M |

## Detailed Findings

### Reentrancy
A contract makes an external call before updating its own state. The callee (attacker contract) recursively calls back into the victim contract, draining funds before the state is updated to reflect the first withdrawal.

- **Rari Capital** (April 2022, $80M): Violated the Checks-Effects-Interactions pattern in borrow function.
- **Orion Protocol** (February 2023, $3M): Reentrancy in `depositAsset()`.
- **Prevention**: Apply state changes before any external calls; use `nonReentrant` modifier from OpenZeppelin.

### Flash Loan Attacks
Uncollateralised loans within a single transaction, used to manipulate market prices or subvert governance:

- **Beanstalk** ($181M): Attacker borrowed enough governance tokens in one transaction to pass a malicious proposal. No time lock existed on governance.
- **Sonne Finance** (May 2024, $20M): Exploited Compound V2 fork vulnerability.
- **Prevention**: Time-lock governance actions; prohibit flash-loan-acquired tokens from voting; add anti-flash-loan guards.

### Oracle Manipulation
Price feed spoofing distorts on-chain value calculations:

- **BonqDAO** ($1.8M): Tellor oracle price feed vulnerability.
- **Lodestar** ($6.5M): GLPOracle manipulation.
- **Prevention**: Use Chainlink decentralised oracle networks; use VWAP pricing over TWAP where possible.

## General Best Practices

1. Use audited libraries (OpenZeppelin)
2. Achieve 100 % branch coverage with fuzzing
3. Professional third-party security audit before mainnet
4. Use SafeERC20 for all token operations
5. Use multisig wallets for admin functions
6. Lock pragma versions in deployed contracts

## Contribution to Wiki

This source grounds the security section of [[concepts/blockchain-technology]] with concrete loss figures and attack mechanics. It complements [[concepts/threat-modeling]] (STRIDE) and [[concepts/owasp-top-10]] by providing blockchain-specific attack taxonomy.
