---
type: source
title: "CFA Institute — Technical Analysis Revisited: Moving Averages = Above Average Returns?"
address: c-000147
domain: trading
source_type: article
author: "Drew Hardin, with Derek Horstmeyer and Amine El Boury"
date_published: 2022-02-08
url: "https://rpc.cfainstitute.org/blogs/enterprising-investor/2022/technical-analysis-revisited-moving-averages-above-average-returns"
confidence: medium
status: ingested
created: 2026-11-24
updated: 2026-11-24
tags: [trading, moving-average, 200-day, 50-day, sp500, backtest, research]
key_claims:
  - "Long above and short below the S&P 500's 200-day moving average: average daily return above the line was 0.06% to 0.10% per decade, below it -0.07% to -0.20%"
  - "Outperformance was reported as significant at the 1% level across all decades studied (stated alongside the 50-day result)"
  - "Returns are reported without transaction costs; same-day close execution weakens the results (reader comment)"
---

# CFA Institute: Moving Averages = Above Average Returns?

Blog summary of an S&P 500 study across six decades (1960s to 2010-present). Two long/short portfolios go long when the index is above its moving average and short when below: one on the **50-day** line, one on the **200-day** line. A separate "crossing over" test holds only the day after a cross.

## Results (average daily return)

| Moving average | Above the line | Below the line | Spread |
|---|---|---|---|
| 50-day | 0.11% to 0.18% | -0.14% to -0.28% | 0.29% to 0.46% |
| 200-day | 0.06% to 0.10% | -0.07% to -0.20% | 0.16% to 0.29% |

- The day after a **cross**, the 200-day spread between crossing above and crossing below ranged from 0.20% (1960s) to 0.71% (1990s).
- The authors flag "considerable volatility on the crossing below side of the moving average as well as skewness in some cases" and suggest the excess return may be compensation for risk, "or maybe just a form of momentum risk".

## Reliability notes

- Costs are not modelled: the author states returns are before transaction costs and fees (in a comment reply, not the article body).
- A reader comment argues results are much weaker if trades are executed at the close using same-day averages; the author did not answer in the thread.
- These are **simple** moving averages on a stock index, not EMAs on short timeframes.

Used in [[concepts/moving-average-trading-evidence]] and [[synthesis/research-emas-in-trading]].
