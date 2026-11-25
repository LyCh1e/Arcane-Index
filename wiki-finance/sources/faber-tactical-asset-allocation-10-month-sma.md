---
type: source
title: "Faber — A Quantitative Approach to Tactical Asset Allocation (10-month SMA timing)"
address: c-000148
domain: trading
source_type: paper
author: "Mebane T. Faber (summarised via Swedroe, etf.com; CXO Advisory; quantstrat documentation)"
date_published: 2007-01-01
url: "https://www.etf.com/sections/index-investor-corner/swedroe-why-financial-trends-persist"
confidence: medium
status: ingested
created: 2026-11-24
updated: 2026-11-24
tags: [trading, moving-average, 200-day, trend-following, tactical-asset-allocation, faber]
key_claims:
  - "The 10-month SMA is the monthly equivalent of the 200-day SMA: buy when the monthly price is above it, move to cash when below"
  - "Presented as a risk-reduction technique: equity-like returns with bond-like volatility and drawdown"
  - "Possible data-snooping in the choice of a 10-month window (CXO Advisory)"
---

# Faber: A Quantitative Approach to Tactical Asset Allocation

The paper tests a simple trend rule on US equities since 1900 and on other asset classes since 1973. The rule is a **10-month simple moving average**, chosen as the monthly form of Siegel's 200-day average for timing the DJIA; monthly data is easier to obtain over long periods and the lower frequency should reduce transaction costs (quantstrat documentation).

- **Rule:** buy when the monthly price is above the 10-month SMA; sell and hold cash when below. Entry and exit are at the signal close.
- **Reach:** the paper became the most downloaded on SSRN with more than 200,000 downloads; a 2018 update ("Revisited 10 Years Later") appeared in the Journal of Portfolio Management (Swedroe).
- **Result as reported:** Sharpe ratio improved from 0.45 to 0.80 in the tactical allocation framework (Swedroe). CXO Advisory reports a gross Sharpe of 0.98 and gross annualised return of 13.4% when cash is held in 10-year Treasuries, and that timing beat buy-and-hold on gross Sharpe for 3-, 6-, 9- and 12-month SMAs.
- **Purpose:** a risk-reduction signal that says when to leave a risky asset, not a source of entry timing.

## Reliability notes

- This page rests on **secondary summaries**; the original paper was not read. The journal name differs between secondary sources (Journal of Wealth Management versus Journal of Risk Management), so only the year is recorded.
- CXO Advisory notes that choosing a 10-month window may involve data-snooping bias.
- The test uses **SMA**, monthly, on asset-class indices. It does not test a 200 **EMA** on trading timeframes.

Used in [[moving-average-trading-evidence]] and [[research-emas-in-trading]].
