---
type: source
title: "Rink (2023) — The predictive ability of technical trading rules in developed and emerging equity markets"
address: c-000149
domain: trading
source_type: paper
author: "Kevin Rink (Goethe University Frankfurt)"
date_published: 2023-08-01
url: "https://link.springer.com/content/pdf/10.1007/s11408-023-00433-2.pdf"
confidence: high
status: ingested
created: 2026-11-24
updated: 2026-11-24
tags: [trading, technical-analysis, moving-average, data-snooping, transaction-costs, market-efficiency]
key_claims:
  - "6,406 rules (2,049 moving-average rules) tested on 41 national indices with data-snooping control"
  - "By 2009-2016 no developed market was predictable; low transaction costs quickly offset predictive power"
  - "Recently best-performing rules performed significantly worse than buy-and-hold afterwards"
---

# Rink (2023): Predictive ability of technical trading rules

Published in *Financial Markets and Portfolio Management*, vol. 37, pp. 403 to 456 (DOI 10.1007/s11408-023-00433-2).

| Item | Detail |
|---|---|
| Markets | 41 national indices (23 developed, 18 emerging); daily closes, up to 66 years ending May 2016 |
| Rules | 6,406: 600 RSI, 497 filter, **2,049 moving average**, 1,220 support/resistance, 2,040 channel breakout |
| Method | Multiple hypothesis testing (Stepwise Superior Predictive Ability test) to control data snooping; Sharpe ratio difference against buy-and-hold, p below 0.1 |

## Findings

- **In-sample** 13 of 23 developed and 14 of 18 emerging markets showed predictable returns, but predictability **declined over time**; by 2009 to 2016 no developed market was predictable.
- **Costs:** "the predictive power of many rules is quickly offset by the introduction of low transaction costs"; only 5 developed and 4 emerging markets kept outperforming rules at single-trip costs of 20 basis points or more.
- **Persistence:** rules that were best in one 3-year window generally did not outperform in the next.
- **Conclusion:** the results "cast serious doubt on whether investors could have earned any excess profits" with the rules studied.

## Reliability notes

Peer-reviewed, large sample, explicit data-snooping control. The text read covered the first 100,000 of about 148,000 characters. It covers equity indices at daily frequency, not intraday or crypto.

Used in [[moving-average-trading-evidence]] and [[research-emas-in-trading]].
