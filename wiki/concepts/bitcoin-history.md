---
type: concept
title: "History of Bitcoin"
domain: blockchain
complexity: high
tags: [bitcoin, history, satoshi-nakamoto, blockchain, cryptocurrency, halving, cypherpunk, Mt-Gox, ETF, institutional-adoption]
updated: 2026-07-28
status: established
created: 2026-07-28
related:
  - "[[concepts/blockchain-technology]]"
  - "[[concepts/blockchain-microcredentials]]"
  - "[[concepts/cryptography]]"
  - "[[concepts/ai-ethics-and-digital-society]]"
---

# History of Bitcoin

Bitcoin is the world's first decentralised digital currency — a peer-to-peer electronic cash system secured entirely by cryptography rather than institutional trust. From an anonymous nine-page whitepaper posted to a mailing list in 2008, it grew into a globally traded asset with a market capitalisation exceeding $2 trillion, and the first novel monetary system in centuries not controlled by any government or bank.

---

## Part I — Before Bitcoin: The Cypherpunk Foundation (1980s–2007)

Bitcoin did not emerge from nothing. It was the culmination of nearly three decades of cryptographic research and failed experiments in digital money. The intellectual lineage runs through the **Cypherpunk movement** — a loose coalition of cryptographers, mathematicians, and libertarians who communicated via mailing lists and believed that strong cryptography was the essential tool for preserving individual privacy and economic freedom against institutional overreach.

### Prior Art

| Project | Creator | Year | Contribution | Failure |
|---------|---------|------|-------------|---------|
| **DigiCash** | David Chaum | 1989 | First privacy-focused electronic cash; blind signatures for anonymity | Centralised; collapsed when the company folded (1998) |
| **Hashcash** | Adam Back | 1997 | Proof-of-work mechanism to price email spam | Not a currency; no transfer mechanism |
| **B-money** | Wei Dai | 1998 | Proposed decentralised electronic cash, distributed ledger concept | Incomplete design; never implemented; could not solve double-spending |
| **Bit Gold** | Nick Szabo | 1998 | Digital gold via proof-of-work; closest conceptual ancestor to Bitcoin | Theoretical only; no unified consensus; double-spend unsolved |
| **RPOW** | Hal Finney | 2004 | Made Hashcash proof-of-work tokens transferable; bridged spam prevention and digital money | Centralised server; single point of failure |

Satoshi Nakamoto cited Hashcash and b-money directly in the Bitcoin whitepaper. The double-spending problem — how to prevent the same digital coin being spent twice without a trusted central authority — was the key unsolved problem all predecessors failed to crack. Bitcoin's blockchain solved it for the first time.

---

## Part II — Genesis (2008–2009)

### The 2008 Context

Bitcoin's whitepaper appeared during the worst global financial crisis since the Great Depression. In September–October 2008, Lehman Brothers collapsed, the US government announced a $700 billion bank bailout (the Emergency Economic Stabilisation Act), and the fundamental fragility of centralised fractional-reserve banking became undeniable. Satoshi later described Bitcoin as motivated by the need for "an electronic payment system based on cryptographic proof instead of trust."

### October 31, 2008 — The Whitepaper

An entity using the pseudonym **Satoshi Nakamoto** distributed a nine-page paper titled *"Bitcoin: A Peer-to-Peer Electronic Cash System"* to the Cypherpunk mailing list at Metzdowd.com. The bitcoin.org domain had been registered on August 18, 2008.

The whitepaper's key innovations:
- **Blockchain** — a chain of cryptographically linked blocks forming an immutable transaction ledger
- **Proof of Work** — CPU-based mining creates a probabilistic barrier to rewriting history; the longest chain wins
- **UTXO model** — Unspent Transaction Outputs track coin ownership without accounts
- **Decentralised consensus** — majority hash power determines the canonical chain, eliminating the need for a trusted third party
- **21 million cap** — fixed supply enforced by protocol; deflationary by design

### January 3, 2009 — The Genesis Block

Satoshi mined **Block 0** — the Genesis Block — generating the first 50 BTC. The block's coinbase field contained an embedded message:

> *"The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"*

This served simultaneously as a cryptographic timestamp (proving no pre-mining before this date) and a philosophical statement — a critique of the monetary system Bitcoin was designed to circumvent. The 50 BTC from the Genesis Block were intentionally made unspendable.

### January 2009 — First Transactions and Release

- **January 8**: Bitcoin v0.1 released
- **January 9**: Open-source Bitcoin client published on SourceForge
- **January 12**: First Bitcoin transaction — Satoshi sends **10 BTC to Hal Finney** (Block 170). Finney, whose RPOW project had most closely approached Bitcoin's design, was the first person to run a Bitcoin node besides Satoshi
- **October 2009**: New Liberty Standard establishes the first Bitcoin exchange rate: **$0.000764 per BTC** (calculated from the cost of electricity to mine one coin)
- **December 30, 2009**: First difficulty adjustment — mining difficulty increases for the first time as more hash power joins the network

### Satoshi's Anonymity and Disappearance

Satoshi's identity was never revealed. The pseudonymous approach served a practical purpose: a named founder would become a target for regulators and litigation, creating a centralised point of failure. By remaining anonymous and then withdrawing from the project, Satoshi ensured Bitcoin could evolve as a genuinely decentralised protocol with no controlling authority.

Satoshi's last known public post was in December 2010. Development was handed to **Gavin Andresen**, who became the lead developer. The estimated 1.1 million BTC in Satoshi's original wallets has never moved.

---

## Part III — Early Life: Price Discovery and the First Ecosystem (2010–2012)

### 2010 — The First Commercial Transaction

| Date | Event |
|------|-------|
| March 2010 | **BitcoinMarket.com** launched — first cryptocurrency exchange |
| May 22, 2010 | **Bitcoin Pizza Day** — Laszlo Hanyecz pays 10,000 BTC for two Papa John's pizzas, arranged via the Bitcoin Forum. The pizzas cost ~$41; at Bitcoin's 2025 peak, those coins would be worth over $1.26 billion |
| July 7 | Bitcoin v0.3 released; price increases approximately tenfold |
| July 17 | **Mt. Gox** (Magic: The Gathering Online eXchange, repurposed by Jed McCaleb) launches as a Bitcoin trading platform |
| August | Critical security vulnerability exploited — attacker generates 184 billion BTC in one transaction; Satoshi and developers patch and fork the network within hours |

**Price trajectory 2010:** ~$0.0008 (January) → ~$0.39 (December)

### 2011 — Parity, Volatility, and the First Bubble

- **February**: Bitcoin reaches **$1.00** — parity with the US dollar for the first time
- **April**: Gawker publishes article on Silk Road (an anonymous darknet marketplace using Bitcoin), causing a surge in interest and price
- **June**: Price spikes to **$31.91** — the first speculative bubble
- **June 19**: Mt. Gox suffers a major security breach; attacker compromises an auditor's account and sells BTC at $0.01, causing a flash crash. ~2,000 BTC stolen
- **July**: Bitomat exchange hacked; Mybitcoin service disappears with user funds
- **October 13**: Litecoin launched — first major Bitcoin fork, using Scrypt proof-of-work
- **November–December**: Price collapses to ~**$2.00** — an 87% crash

By end of 2011, 25% of the total 21 million Bitcoin (5.25 million coins) had been mined.

### 2012 — Building Infrastructure

- Bitcoin Foundation established (September 2012)
- **November 28, 2012**: **First halving** — block reward drops from **50 BTC to 25 BTC** per block. Price at halving: ~$12. The halving reduces the rate of new supply entering circulation, a mechanism designed to produce four-year scarcity cycles
- First major mainstream media coverage begins attracting developer talent and capital

**Price trajectory 2012:** ~$5 (January) → ~$13 (December)

---

## Part IV — The Dark Markets Era and First Crash (2013–2015)

### 2013 — $1,000 and the First Mainstream Moment

| Date | Event |
|------|-------|
| March 28 | Bitcoin market cap surpasses **$1 billion** for the first time |
| April | Price spikes to ~**$266**, then crashes 83% to ~$50 — first major bubble/crash cycle |
| October 2 | FBI shuts down **Silk Road** and arrests founder Ross Ulbricht ("Dread Pirate Roberts"); ~144,000 BTC seized. Silk Road had processed ~$1.2 billion in transactions since 2011 |
| November 28 | Bitcoin breaks **$1,000** for the first time amid intensifying media coverage |
| December | **China's People's Bank** prohibits financial institutions from handling Bitcoin transactions; price crashes from ~$1,240 to ~$500 |

Silk Road's shutdown demonstrated Bitcoin's resilience — despite hosting a major criminal marketplace, Bitcoin continued operating. It also triggered the first serious regulatory discussions worldwide.

### 2014 — The Mt. Gox Catastrophe

**February 2014** brought the most damaging event in Bitcoin's history to that point:

- **Mt. Gox**, then handling ~70% of all global Bitcoin trades, suspended withdrawals
- **February 28**: Mt. Gox filed for bankruptcy in Tokyo, revealing that **850,000 BTC** (belonging to ~24,000 customers, worth ~$500 million at the time; ~$100+ billion at 2025 prices) had been stolen — primarily through a years-long transaction malleability exploit
- Bitcoin price crashed from ~$1,000 to ~$300
- A subsequent investigation recovered ~200,000 BTC; creditor proceedings continued for over a decade
- The collapse triggered the first serious institutional risk discussions about cryptocurrency exchange custody

**Other 2014 developments:**
- UK classifies Bitcoin as an asset; exempts transactions from VAT
- New York DFS releases draft BitLicense regulations — first serious US cryptocurrency regulatory framework
- Microsoft begins accepting Bitcoin for digital products

**Price trajectory 2014:** ~$770 (January) → ~$320 (December)

### 2015 — Crypto Winter I

- Price bottoms at ~**$170** in January 2015
- Nasdaq and major banks begin experimenting with blockchain technology (recognising the ledger without accepting Bitcoin)
- Ethereum whitepaper gains traction; Vitalik Buterin launches Ethereum in July 2015, introducing smart contracts
- Bitcoin price slowly recovers to ~$430 by year end

---

## Part V — The Scaling Wars and the 2017 Boom (2016–2018)

### 2016 — The Second Halving and SegWit Debate

- **July 9, 2016**: **Second halving** — block reward drops from **25 BTC to 12.5 BTC**. Price at halving: ~$650
- Japan recognises virtual currencies as functioning like real money (legal framework)
- Network hash rate exceeds 1 exahash per second for the first time
- **SegWit (Segregated Witness)** formally proposed by Bitcoin Core developers: a soft fork to fix transaction malleability and increase effective block capacity by separating signature data from transaction data. Triggers the beginning of the **Bitcoin Scaling Wars**

**Price trajectory 2016:** ~$430 (January) → ~$960 (December)

### 2017 — Forks, Futures, and All-Time Highs

The scaling debate fractured the Bitcoin community:

- **August 1, 2017**: **Bitcoin Cash (BCH)** hard fork — Roger Ver and Jihan Wu's faction fork Bitcoin to increase the block size from 1MB to 8MB, arguing this better served Satoshi's original peer-to-peer cash vision. Bitcoin (BTC) retains the dominant network and price position
- **August 2017**: SegWit activates on Bitcoin mainnet — effective block capacity increases without a block size increase
- **October 2017**: **Bitcoin Gold (BTG)** hard fork — changes mining algorithm to GPU-based Equihash
- **December 10**: **CBOE** launches the first regulated Bitcoin futures contracts
- **December 17**: **CME** launches Bitcoin futures
- **December 17**: Bitcoin reaches all-time high of **~$19,783** (some exchanges briefly exceed $20,000)
- Earlier in 2017: Bitcoin first exceeded the price of one troy ounce of gold (March 2017)

The 2017 boom was fuelled by: retail speculation, Initial Coin Offering (ICO) mania, futures launch anticipation, and mainstream media saturation. Total cryptocurrency market cap grew from ~$17B (Jan 2017) to ~$830B (Jan 2018).

### November 2018 — Bitcoin Cash Civil War

- Roger Ver (Bitcoin Cash) vs. Craig Wright (claiming to be Satoshi Nakamoto) dispute over block size triggers another hard fork
- **November 15, 2018**: **Bitcoin SV (BSV)** splits from Bitcoin Cash. Craig Wright advocates massive 128MB blocks; loses the hash war against BCH

### 2018 — Crypto Winter II

- Bitcoin crashes from ~$20,000 (January 2018) to ~**$3,200** (December 2018) — an 84% decline
- SEC rejects multiple Bitcoin ETF applications throughout 2018
- Facebook, Google, and Twitter ban cryptocurrency advertising
- ICO market collapses; most 2017-era altcoins lose 95%+ of value
- Institutional infrastructure (custodians, regulated exchanges) quietly builds despite price crash

**Price trajectory 2018:** ~$13,000 (January) → ~$3,200 (December)

---

## Part VI — Institutional Dawn (2019–2021)

### 2019 — Recovery and Infrastructure

- Price bottoms at ~$3,200 in January; recovers to briefly exceed **$13,000** in June (Libra/Facebook announcement effect)
- **Lightning Network** gains significant traction as a Layer 2 payment channel network for fast, low-fee Bitcoin transactions
- Fidelity Digital Assets launches — institutional custodian
- Ends 2019 at ~$7,200

### 2020 — The Institutional Inflection Point

| Date | Event |
|------|-------|
| March 12–13 | **"Black Thursday"** — COVID-19 panic causes Bitcoin to crash from ~$8,000 to ~**$3,800** in 48 hours, the largest single-day percentage drop since 2013 |
| May 11 | **Third halving** — block reward drops from **12.5 to 6.25 BTC**. Price at halving: ~$8,600 |
| August | **MicroStrategy** (Michael Saylor) announces $250M Bitcoin treasury purchase — first major publicly-traded company to adopt Bitcoin as primary treasury reserve asset. MicroStrategy goes on to purchase continuously, becoming the largest corporate holder |
| October | **Square** (Jack Dorsey) purchases $50M in Bitcoin (~1% of total assets) |
| October | **PayPal** announces US customers can buy, hold, and sell Bitcoin through PayPal accounts — exposes 350M users to Bitcoin |
| December | Bitcoin breaks its 2017 all-time high of ~$20,000 for the first time; ends year at ~$28,900 |

The COVID era proved decisive: central banks worldwide engaged in unprecedented money printing, pushing institutional investors toward Bitcoin as an inflation hedge and "digital gold" narrative crystallised.

### 2021 — The Trillion-Dollar Asset

| Date | Event |
|------|-------|
| February 8 | **Tesla** discloses a **$1.5 billion Bitcoin purchase** and announces it will accept BTC as payment |
| February 19 | Bitcoin market cap surpasses **$1 trillion** for the first time |
| April 14 | **Coinbase IPO** on Nasdaq (direct listing); Bitcoin hits ATH of **$64,863** the same day |
| May | Tesla suspends Bitcoin payments, citing environmental concerns (Elon Musk tweet); China announces crackdown on Bitcoin mining; price crashes to ~$30,000 |
| May–July | Chinese mining ban forces massive miner migration to US, Kazakhstan, and elsewhere — hash rate drops ~50%, then recovers fully within months |
| June 9 | **El Salvador** passes the Bitcoin Law, becoming the world's first country to adopt Bitcoin as **legal tender**; the government distributes $30 in BTC to all citizens via the Chivo wallet. IMF expresses concern |
| September 7 | El Salvador's Bitcoin Law takes effect |
| November 14 | **Taproot** upgrade activates — Bitcoin's most significant protocol upgrade since SegWit; improves privacy (Schnorr signatures replace ECDSA), enables more complex smart contracts, and reduces transaction sizes |
| November 10 | **All-time high: ~$69,044** |

**Price trajectory 2021:** ~$29,000 (January) → ~$69,000 (November) → ~$46,000 (December)

---

## Part VII — Collapse and Recovery (2022–2023)

### 2022 — Contagion

| Date | Event |
|------|-------|
| May 2022 | **Terra/Luna collapse** — TerraUSD (UST) algorithmic stablecoin loses its $1 peg; LUNA token crashes 99.9% within days; ~$60 billion in market value erased. Contagion spreads across the crypto ecosystem |
| June | **Three Arrows Capital (3AC)** — a $10B+ crypto hedge fund — defaults on loans; liquidated. **Celsius Network** and **Voyager Digital** freeze customer withdrawals; both later file for bankruptcy |
| June | Bitcoin falls to ~**$17,600** — down 75% from November 2021 ATH |
| November 2 | CoinDesk publishes a leaked Alameda Research balance sheet showing heavy FTX token (FTT) concentration |
| November 6 | **Binance CEO CZ** announces Binance will liquidate its FTT holdings |
| November 8 | FTX halts customer withdrawals as a bank run exceeds reserves |
| November 11 | **FTX files for bankruptcy**; Sam Bankman-Fried (SBF) resigns; FTX had misused ~$8 billion in customer funds to cover Alameda Research losses |
| November 11 | Bitcoin hits cycle low of ~**$15,500** |
| December | SBF arrested in the Bahamas; extradited to the US |

FTX's collapse was the largest fraud in cryptocurrency history and triggered global regulatory responses. Bitcoin ended 2022 at ~$16,500 — down 65% for the year.

### 2023 — Quiet Recovery

- Bitcoin opens 2023 at ~$16,500 and begins a sustained recovery
- March: **Silvergate** and **Silicon Valley Bank** collapse (US banking mini-crisis); Bitcoin briefly rallies as investors question traditional banking
- **June**: **BlackRock** files for a spot Bitcoin ETF with the SEC — a seismic signal, given BlackRock's $9 trillion AUM and near-perfect ETF approval record
- Multiple other major asset managers (Fidelity, Invesco, Ark/21Shares) follow with spot ETF applications
- May: First BRC-20 tokens (fungible tokens on Bitcoin using Ordinals inscriptions) launch; over 24,000 tokens and $447M market cap by May 31
- Bitcoin closes 2023 at ~**$42,000** — recovering 155% from the FTX lows

---

## Part VIII — Institutional Legitimacy and New Highs (2024–2025)

### 2024 — The ETF Era Begins

| Date | Event |
|------|-------|
| January 10 | **SEC approves 11 spot Bitcoin ETFs** simultaneously — including **BlackRock IBIT** and **Fidelity FBTC**. BlackRock's IBIT becomes one of the fastest ETFs in history to reach $10B, then $50B, in AUM |
| January–March | Record institutional inflows; Bitcoin rises from ~$44,000 to new ATH |
| March 14 | **New all-time high: ~$73,750** |
| April 20 | **Fourth halving** — block reward drops from **6.25 to 3.125 BTC**. Price: ~$64,968. Over 93% of all 21 million Bitcoin already mined; annual new supply inflation drops below **1%** |
| November | Donald Trump wins the US presidential election on an explicitly pro-crypto platform; markets rally sharply in anticipation of regulatory clarity |
| December | Bitcoin surpasses **$100,000** for the first time |

### 2025 — Sovereign and Institutional Scale

| Date | Event |
|------|-------|
| January | **New ATH: ~$109,114** — driven by post-election euphoria and institutional inflows |
| Early 2025 | Institutional Bitcoin holdings across all entities approach **$196 billion** |
| 2025 | **MicroStrategy** (rebranded to Strategy) holds over 500,000 BTC — more than 2.3% of the entire Bitcoin supply |
| 2025 | Multiple US states propose legislation to hold Bitcoin in state treasury reserves |
| October 6 | **New ATH: ~$126,198** |

---

## The Four Halving Cycles — Summary

Bitcoin's supply schedule reduces the block reward approximately every four years (every 210,000 blocks). This creates a predictable supply shock mechanism that has historically coincided with bull market cycles.

| Halving | Date | Block Reward | Price at Halving | Subsequent ATH | Days to ATH |
|---------|------|-------------|-----------------|----------------|-------------|
| Genesis supply | Jan 2009 | 50 BTC | ~$0.00 | — | — |
| **1st Halving** | Nov 28, 2012 | 25 BTC | ~$12 | ~$1,240 (Nov 2013) | ~367 days |
| **2nd Halving** | Jul 9, 2016 | 12.5 BTC | ~$650 | ~$19,783 (Dec 2017) | ~526 days |
| **3rd Halving** | May 11, 2020 | 6.25 BTC | ~$8,600 | ~$69,044 (Nov 2021) | ~549 days |
| **4th Halving** | Apr 20, 2024 | 3.125 BTC | ~$64,968 | ~$126,198 (Oct 2025) | ~537 days |

Each successive cycle has seen higher absolute ATHs, but diminishing percentage gains as Bitcoin's market cap grows and the structural supply shock shrinks in relative magnitude.

---

## Bitcoin Price History — Key Figures

| Year | Low | High | Key Driver |
|------|-----|------|-----------|
| 2009 | ~$0.00 | ~$0.001 | First exchange rate established |
| 2010 | ~$0.003 | ~$0.39 | Pizza transaction; Mt. Gox launch |
| 2011 | ~$0.67 | ~$31.91 | First mainstream bubble; Silk Road discovery |
| 2012 | ~$4.00 | ~$13.00 | First halving |
| 2013 | ~$13 | ~$1,240 | Market cap $1B; Silk Road bust; China interest |
| 2014 | ~$300 | ~$1,000 | Mt. Gox collapse; crypto winter |
| 2015 | ~$170 | ~$490 | Bottom of first crypto winter |
| 2016 | ~$360 | ~$970 | Second halving; SegWit debate |
| 2017 | ~$780 | ~$19,783 | Retail mania; BCH fork; CME futures |
| 2018 | ~$3,200 | ~$17,000 | Crypto Winter II; ETF rejections |
| 2019 | ~$3,300 | ~$13,000 | Institutional infrastructure build |
| 2020 | ~$3,800 | ~$29,300 | COVID crash; 3rd halving; MicroStrategy |
| 2021 | ~$27,700 | ~$69,044 | Tesla; Coinbase IPO; El Salvador; Taproot |
| 2022 | ~$15,500 | ~$47,800 | Luna collapse; 3AC; FTX fraud |
| 2023 | ~$16,500 | ~$44,700 | Recovery; BlackRock ETF filing |
| 2024 | ~$38,500 | ~$108,000 | Spot ETF approval; 4th halving |
| 2025 | ~$78,000 | ~$126,198 | Institutional scale; political shift |

---

## Major Recurring Themes

### Theme 1: Trust Crises Repeat at Each Cycle
Every major crash has involved a centralised custodian failing (Mt. Gox 2014, Bitfinex 2016, FTX 2022) — the very failure mode Bitcoin was designed to eliminate. Each crisis accelerated the push toward self-custody and decentralised infrastructure.

### Theme 2: Every Regulatory Crackdown Has Failed to Stop Bitcoin
China banned Bitcoin mining (2021), financial institutions from handling it (2013), and exchanges (multiple times). The US SEC rejected every spot ETF application for a decade. In each case, Bitcoin continued operating. The June 2021 China mining ban caused the hash rate to drop 50%; it fully recovered within months as miners relocated.

### Theme 3: Halvings Correlate With Bull Cycles
All four halvings preceded new all-time highs within 12–18 months. The mechanism is debated (supply shock, narrative catalyst, or survivorship bias) but the pattern has held through 2025. Post-ETF, however, institutional demand has begun to decouple Bitcoin's price from strict four-year halving cycles.

### Theme 4: Institutional Adoption Follows Infrastructure, Not Price
Fidelity, BlackRock, and CME built Bitcoin infrastructure during bear markets (2018–2019, 2022–2023). The approvals and product launches came during or preceding bull markets. This suggests institutional adoption is a lagging infrastructure story, not a real-time price story.

### Theme 5: Satoshi's 1.1 Million BTC Has Never Moved
Despite being the most valuable known wallet cluster in history, the coins attributed to Satoshi's early mining have never been spent. This is simultaneously evidence for Satoshi's death (some researchers), a principled decision to not distort the market, or continued anonymity management.

---

## Connections to Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/blockchain-technology]] | The technical underpinning of every Bitcoin mechanism: hashing, Merkle trees, proof of work, consensus, UTXO model |
| [[concepts/blockchain-microcredentials]] | Bitcoin's blockchain is one of the DLT options for anchoring credential hashes; Bitcoin's design principles (decentralisation, immutability, cryptographic proof) inform the VC trust model |
| [[concepts/cryptography]] | SHA-256 (block hashing), ECDSA/Schnorr (transaction signing), Merkle trees (block integrity), zero-knowledge proofs (Lightning Network privacy) |
| [[concepts/ai-ethics-and-digital-society]] | Bitcoin's environmental impact (proof-of-work energy consumption), financial inclusion implications (El Salvador, Africa SMS payments), and regulatory philosophy debates are digital-society ethics questions |
| [[concepts/privacy-data-protection-and-ip]] | Bitcoin's pseudonymity vs. full anonymity; chain analysis de-anonymisation; GDPR questions around on-chain transaction data |
