---
type: entity
entity_type: person
title: "Satoshi Nakamoto"
aliases: ["Satoshi", "Bitcoin creator"]
tags: [blockchain, Bitcoin, cryptography, entities]
domain: blockchain
confidence: high
status: pseudonymous — true identity unknown
---

# Satoshi Nakamoto

## Who

Satoshi Nakamoto is the pseudonymous inventor of Bitcoin and the author of the Bitcoin whitepaper. The true identity — whether an individual or a group — has never been confirmed. Satoshi was last publicly active in late 2010.

## Key Contributions

| Contribution | Date | Significance |
|---|---|---|
| Bitcoin Whitepaper | October 2008 | Proposed the first decentralised peer-to-peer electronic cash system |
| Bitcoin Genesis Block | January 3, 2009 | First block ever mined; contains message: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks" |
| Bitcoin Core 0.1 | January 9, 2009 | Released first open-source Bitcoin client |
| Handover to Gavin Andresen | 2010 | Transferred project stewardship before disappearing |

## Technical Innovations

The whitepaper solved the **Byzantine Generals Problem** for digital cash by combining:
1. **Proof of Work** (Hashcash-derived, Adam Back 2002) — computational work as Sybil resistance
2. **Merkle trees** — efficient transaction summarisation
3. **UTXO model** — parallel-validatable transaction outputs
4. **Longest-chain rule** — fork resolution without central authority
5. **Difficulty adjustment** — self-regulating block time (~10 minutes)

The crucial innovation was not any single cryptographic primitive (all pre-existed) but their composition into a system achieving **trustless consensus among mutually distrusting parties**.

## Known Facts

- Estimated holdings: ~1 million BTC (from early mining, 2009)
- Communication: primarily via the Bitcoin Forum and direct emails with early contributors
- Disappeared: shortly after publishing Wikileaks's use of Bitcoin became public (late 2010)
- Original codebase: C++; intentionally conservative design

## Related

- [[concepts/blockchain-technology]]
- [[entities/vitalik-buterin]] — extended blockchain with smart contracts
- [[entities/nick-szabo]] — proposed "bit gold" (1998), a direct Bitcoin precursor; introduced the concept of smart contracts (1994)
