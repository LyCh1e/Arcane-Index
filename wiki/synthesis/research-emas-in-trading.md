---
type: synthesis
title: "Research: EMAs in Trading (9, 20 and 200)"
address: c-000157
domain: trading
status: developing
created: 2026-11-24
updated: 2026-11-24
tags: [research, trading, ema, moving-average, 9-ema, 20-ema, 200-ema, autoresearch]
related:
  - "[[concepts/exponential-moving-average]]"
  - "[[concepts/ema-9-20-200-roles]]"
  - "[[concepts/moving-average-trading-evidence]]"
  - "[[concepts/technical-indicators-and-risk-sizing]]"
sources:
  - "[[sources/cfa-moving-averages-sp500-2022]]"
  - "[[sources/faber-tactical-asset-allocation-10-month-sma]]"
  - "[[sources/rink-2023-technical-trading-rules]]"
  - "[[sources/mroziewicz-slepaczuk-2026-ema-crossover]]"
  - "[[sources/gray-2014-simulation-sma-rules]]"
  - "[[sources/factset-golden-death-crosses-2018]]"
  - "[[sources/ema-practitioner-references-2026-11-24]]"
---

# Research: EMAs in Trading (9, 20 and 200)

## Overview

An EMA is a moving average that weights recent prices more heavily, using the multiplier 2 / (N + 1). The 9, 20 and 200 are three horizons: the 9 for immediate momentum, the 20 for the short-to-medium trend and pullbacks, the 200 as the long-term trend filter. That is practitioner convention; research evidence supports slow trend filters as risk reducers more than fast crossovers as profit engines.

## The 9, 20 and 200 at a glance

| EMA | Shows | Used for | Evidence quality |
|---|---|---|---|
| 9 | Short-term momentum; moving floor or ceiling in a trend | Scalping and day-trade triggers; 9/20 cross | Convention only; one author calls it "nearly useless" |
| 20 | Short-to-medium trend; dynamic support or resistance; the pullback zone | Swing pullback entries; slower half of the 9/20 cross | Convention only |
| 200 | Long-term trend and bias; 200 days is about 40 weeks | Trend filter (above favours longs, below favours shorts) | Academic tests exist for the 200-day or 10-month **SMA**, not the 200 EMA |

## Key Findings

- The EMA multiplier is 2 / (N + 1): 0.20 for the 9, 0.0952 for the 20, about 0.00995 for the 200; each EMA(N) puts about 86.5% of its weight on its last N bars (Source: [[concepts/exponential-moving-average]], derived).
- EMAs react faster than SMAs but produce more false signals: "Less lag, more whipsaw; more smoothing, more lag" (Source: [[sources/ema-practitioner-references-2026-11-24]]).
- In the S&P 500, being above the 200-day average earned 0.06% to 0.10% a day and below it -0.07% to -0.20% in every decade from the 1960s, before costs (Source: [[sources/cfa-moving-averages-sp500-2022]]).
- A 10-month (about 200-day) SMA timing rule improved risk-adjusted returns across asset classes; it is a risk-reduction tool (Source: [[sources/faber-tactical-asset-allocation-10-month-sma]]).
- Across 41 markets and 6,406 rules, predictability faded and low costs wiped out profits (Source: [[sources/rink-2023-technical-trading-rules]]).
- An EMA-crossover walk-forward test on crypto matched buy-and-hold with lower drawdown, with a break-even cost of about 0.4% per trade (Source: [[sources/mroziewicz-slepaczuk-2026-ema-crossover]]).
- Golden and death crosses lag; death crosses have often been followed by positive returns (Sources: [[sources/factset-golden-death-crosses-2018]], [[sources/ema-practitioner-references-2026-11-24]]).

## Key Concepts

- [[concepts/exponential-moving-average]]: formula, weights, lag versus whipsaw.
- [[concepts/ema-9-20-200-roles]]: what each line shows and how the stack is read.
- [[concepts/moving-average-trading-evidence]]: studies for and against.

## Contradictions

- **Academic support versus Rink 2023.** CFA Institute and Faber find consistent benefits for the 200-day or 10-month line; Rink finds predictability gone in developed markets by 2009 to 2016 and erased by low costs. Rink is larger, peer-reviewed and controls data snooping; the CFA study ignores costs, so lean towards Rink for tradeable edge and towards CFA and Faber for trend-filter and risk-reduction value.
- **Death cross meaning.** Convention reads it as bearish; FactSet, LPL and Fundstrat find positive average forward returns after it. Signals lag, so they confirm rather than predict.
- **SMA or EMA for the long line.** Britannica pairs SMAs with longer-term analysis; many traders and scripts use a 200 EMA. The studies use SMAs.
- **"200 is roughly one trading year" (FXNX).** 200 of about 252 trading days is about 79% of a year, and Faber's 10-month equivalent matches 200 days better.
- **Usefulness of the 9.** Widely used by day traders; "nearly useless" per Dummies.

## Open Questions

- Does a 200 **EMA** on daily data match the evidence for the 200-day SMA? Not found.
- Does a 9/20 cross filtered by the 200 improve results after costs? No direct test found.
- What does a 200 EMA mean on 1 to 15 minute charts, and does it behave like a daily trend filter? Unverified.
- Do institutions cluster orders at the 200-day average? Claimed by blogs, no data found.
- The LuxAlgo page gave inconsistent content between search snippet and fetch; its 9/20/200 description is unconfirmed.
- Faber (2007) and Brock, Lakonishok and LeBaron (1992) were read only through secondary sources.

## Sources

- [[sources/cfa-moving-averages-sp500-2022]]: Hardin, Horstmeyer, El Boury; CFA Institute, 2022-02-08
- [[sources/faber-tactical-asset-allocation-10-month-sma]]: Faber, 2007 (secondary summaries)
- [[sources/rink-2023-technical-trading-rules]]: Rink, 2023
- [[sources/mroziewicz-slepaczuk-2026-ema-crossover]]: Mroziewicz and Slepaczuk, arXiv, 2026-02-11
- [[sources/gray-2014-simulation-sma-rules]]: Gray, Alpha Architect, 2014-07-28 (may be stale)
- [[sources/factset-golden-death-crosses-2018]]: Simmons, FactSet, 2018-06-26 (may be stale)
- [[sources/ema-practitioner-references-2026-11-24]]: Fidelity, Britannica, StockCharts, TMGM and others
