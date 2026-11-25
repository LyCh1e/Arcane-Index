---
type: concept
title: Exponential Moving Average (EMA)
address: c-000154
domain: trading
complexity: medium
status: developing
created: 2026-11-24
updated: 2026-11-24
sources:
  - ema-practitioner-references-2026-11-24
  - mroziewicz-slepaczuk-2026-ema-crossover
tags:
  - trading
  - ema
  - moving-average
  - indicator
  - lag
  - smoothing
  - whipsaw
related:
  - "[[technical-indicators-and-risk-sizing]]"
  - "[[ema-9-20-200-roles]]"
  - "[[moving-average-trading-evidence]]"
  - "[[research-emas-in-trading]]"
---

# Exponential Moving Average (EMA)

An EMA is a moving average that weights recent prices more heavily than old ones, so it follows price more closely than a simple moving average (SMA) of the same period. It is a trend-direction tool, not a prediction: "All moving averages, including the EMA, are not designed to identify a trade at the exact bottom and top" (Source: [[ema-practitioner-references-2026-11-24]]).

## Formula

- Multiplier: **k = 2 / (N + 1)** for an N-period EMA.
- Update: **EMA now = k x price + (1 - k) x EMA previous**, equivalently EMA = (price - previous EMA) x k + previous EMA.
- Seed: the first EMA equals the N-period SMA. The seed's influence decays, so only early values are affected.
- Example: N = 9, price 105, previous EMA 100: 100 + 0.2 x 5 = 101.0.

An SMA gives each of N bars equal weight (1/N); the EMA is cumulative and every past price still contributes, with diminishing weight. For N = 20 an SMA bar carries 5% and the latest EMA close 9.52% (Source: [[ema-practitioner-references-2026-11-24]]; the same 2/(N+1) weighting is used in the arXiv study [[mroziewicz-slepaczuk-2026-ema-crossover]]).

## What 9, 20 and 200 mean numerically

Derived by calculation from k = 2 / (N + 1); these are properties of the maths, not claims from the sources.

| N | k | Weight of latest bar | SMA weight per bar | Share of EMA weight in last N bars | Average age of data | Half the weight within |
|---|---|---|---|---|---|---|
| 9 | 0.2000 | 20.0% | 11.1% | 86.6% | 4.0 bars | 3.1 bars |
| 20 | 0.0952 | 9.52% | 5.0% | 86.5% | 9.5 bars | 6.9 bars |
| 200 | 0.00995 | about 1.0% | 0.5% | 86.5% | 99.5 bars | 69.3 bars |

Each EMA(N) puts about 86.5% of its weight on the last N bars, so "9", "20" and "200" are best read as time horizons: roughly the last 9, 20 and 200 bars of whatever timeframe the chart uses.

## EMA versus SMA

| | SMA | EMA |
|---|---|---|
| Weighting | Equal over N bars; oldest drops out | Exponentially decaying; nothing drops out |
| Reaction to a sharp turn | Slower | "responds more quickly" (Britannica) |
| Typical use per sources | Longer-term trend analysis | Short-term trading |
| Risk | More lag | More short-term changes and false signals ("double-edged", Fidelity) |

The split of SMA for longer horizons and EMA for shorter ones is a convention (Britannica, TMGM), and many traders still run a 200 EMA. Almost all long-horizon academic evidence found tests **SMA** versions; see [[moving-average-trading-evidence]].

## Lag and whipsaw

"Less lag, more whipsaw; more smoothing, more lag" (StockCharts). Shorter periods give more signals but a larger share are false; longer periods give fewer, more reliable signals that arrive later. Filters (a percentage band or a time requirement) reduce whipsaws at the cost of extra lag.

## Practical points

- **Timeframe matters.** The same period gives different signals on different timeframes; to carry a daily 50 and 200 to a weekly chart use 10 and 40 (Source: [[ema-practitioner-references-2026-11-24]]).
- **Baseline.** Britannica suggests a daily EMA ideally includes prices back a full year (about 256 trading days) for accuracy.
- **MACD** is built from EMAs: 12 minus 26, with a 9-period EMA as the signal line ([[technical-indicators-and-risk-sizing]]). That 9 is a different use from a 9 EMA plotted on price.

> [!gap] Needs verification
> Whether an EMA outperforms an SMA after costs for the same period was not found in the sources read.
