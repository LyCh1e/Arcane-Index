---
type: entity
entity_type: person
title: "Nick Szabo"
aliases: ["Szabo"]
tags: [blockchain, smart-contracts, cryptography, entities]
domain: blockchain
confidence: high
---

# Nick Szabo

## Who

Nick Szabo is an American computer scientist, legal scholar, and cryptographer who originated the concept of **smart contracts** (1994) and proposed **Bit Gold** (1998), widely regarded as the direct intellectual predecessor to Bitcoin.

## Key Contributions

| Contribution | Date | Significance |
|---|---|---|
| Smart Contracts | 1994 | Proposed self-executing digital contracts with terms written in code — predated blockchain by 15 years |
| Bit Gold | 1998 | Proposed a decentralised digital currency using PoW and cryptographic chaining — no trusted third party required |
| Szabo's Law | — | "The blockchain is politically decentralised and architecturally decentralised but logically centralised" |

## Smart Contracts — Original Vision

Szabo's 1994 paper defined a smart contract as: *"a computerised transaction protocol that executes the terms of a contract. The general objectives are to satisfy common contractual conditions, minimise exceptions both malicious and accidental, and minimise the need for trusted intermediaries."*

His canonical example was the **vending machine** — a physical smart contract that automatically executes a transaction (dispenses product) when conditions are met (correct payment received).

Ethereum (2015) became the first general-purpose blockchain platform realising Szabo's vision.

## Bit Gold

Bit Gold (1998, never implemented) proposed:
1. A user creates a "challenge string" from the previous block
2. They perform proof-of-work on that string (find a hash with certain properties)
3. The result is published to a distributed registry

This is structurally identical to Bitcoin's block mining — the missing piece was Satoshi's Nakamoto consensus (longest-chain fork resolution). Szabo never resolved the "Byzantine" problem that Nakamoto solved.

## Relationship to Bitcoin

Szabo is frequently suggested as a candidate for Satoshi Nakamoto's true identity, primarily due to:
- Linguistic analysis matching Satoshi's writing style
- Bit Gold's near-identical architecture to Bitcoin
- Bitcoin published shortly after Szabo publicly announced abandoning Bit Gold

Szabo has consistently denied being Satoshi.

## Related

- [[concepts/blockchain-technology]]
- [[entities/satoshi-nakamoto]]
- [[entities/vitalik-buterin]]
