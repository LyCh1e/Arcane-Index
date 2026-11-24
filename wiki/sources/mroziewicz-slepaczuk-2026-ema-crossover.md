---
type: source
title: "Mroziewicz and Slepaczuk (2026) — Walk-forward optimisation of an EMA crossover strategy"
address: c-000150
domain: trading
source_type: paper
author: "T. Mroziewicz and R. Slepaczuk (University of Warsaw)"
date_published: 2026-02-11
url: "https://arxiv.org/html/2602.10785v1"
confidence: medium
status: ingested
created: 2026-11-24
updated: 2026-11-24
tags: [trading, ema, crossover, walk-forward, crypto, parameter-optimisation, preprint]
key_claims:
  - "EMA crossover performance is highly dependent on the chosen walk-forward window size"
  - "Tested EMA periods 5, 7, 10, 15, 20, 30, 40, 50, 100, 150, 200; fast above slow means long"
  - "Test-period results were similar to buy-and-hold with lower drawdown; break-even cost about 0.4% per transaction"
---

# Mroziewicz and Slepaczuk (2026): EMA crossover with walk-forward optimisation

arXiv:2602.10785v1, submitted 11 February 2026 (preprint, not peer-reviewed at the time of reading). Title as given: "A novel approach to trading strategy parameter optimization, using double out-of-sample data and walk-forward techniques".

- **Rule:** long when the fast EMA is at or above the slow EMA, short otherwise. EMA periods 5, 7, 10, 15, 20, 30, 40, 50, 100, 150 and 200; periods above 35 are "slow", the rest "fast" (the authors call the threshold somewhat arbitrary).
- **Data:** one-minute crypto prices resampled to 1, 5, 10, 15, 30 and 60 minutes; parameters optimised on Bitcoin and applied to Binance Coin and Ethereum; 0.1% fee per transaction.
- **Design:** training Feb 2018 to Sep 2019; one-time unseen test Nov 2019 to Aug 2021; 81 training and testing window-length combinations; pairs optimised on Sharpe ratio.
- **Findings:** all walk-forward combinations beat buy-and-hold in the training period; in the test period the strategy performed **similarly to buy-and-hold** with lower drawdown and a higher information ratio; blending with buy-and-hold gave the best overall result and a 50% drawdown reduction; break-even cost was about **0.4% per transaction**.
- **Stated limitations:** data-mining risk from testing many combinations, parameter decay over time, and a fixed trade sequence in the cost analysis.

## Reliability notes

The only source in this research that tests EMA pairs directly, but on crypto at 1 to 60 minutes and as a preprint. It does not isolate 9/20/200 as a set. Sharpe tables were not read.

Used in [[concepts/moving-average-trading-evidence]] and [[synthesis/research-emas-in-trading]].
