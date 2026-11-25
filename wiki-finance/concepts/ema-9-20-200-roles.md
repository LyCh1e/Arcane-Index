---
type: concept
title: The 9, 20 and 200 EMAs — What Each Shows
address: c-000155
domain: trading
complexity: medium
status: developing
created: 2026-11-24
updated: 2026-11-24
sources:
  - ema-practitioner-references-2026-11-24
  - faber-tactical-asset-allocation-10-month-sma
  - mroziewicz-slepaczuk-2026-ema-crossover
tags:
  - trading
  - ema
  - 9-ema
  - 20-ema
  - 200-ema
  - trend
  - momentum
  - support-resistance
  - crossover
related:
  - "[[exponential-moving-average]]"
  - "[[moving-average-trading-evidence]]"
  - "[[technical-indicators-and-risk-sizing]]"
  - "[[research-emas-in-trading]]"
---

# The 9, 20 and 200 EMAs: What Each Shows

> [!warning] Convention, not proven edge
> The roles below are **practitioner convention** drawn from broker education and trader write-ups. No source read tests the 9/20/200 trio as a set. Evidence on whether moving-average signals make money is in [[moving-average-trading-evidence]].

## One line each

| EMA | Horizon (derived) | Role in convention | Typical user |
|---|---|---|---|
| **9** | About the last 9 bars; fastest of the three | Immediate momentum and short-term bias; the "trigger" line; acts as a moving floor in an uptrend or ceiling in a downtrend | Scalpers, day traders |
| **20** (or 21) | About 20 bars (20 trading days is roughly a month on a daily chart) | Short-to-medium trend line and dynamic support or resistance; pullback zone; the slower half of the 9/20 cross | Day and swing traders |
| **200** | About 200 bars (200 trading days is about 40 weeks, close to the 10-month average used in academic timing tests) | Long-term trend filter and bias: price above favours longs, below favours shorts | Swing and position traders, and as a filter for intraday traders |

Sources: Bitget, EBC and TradingView idea posts describe the 9 and the 9/20 or 9/21 cross; TMGM lists 9, 20 or 21, 50 and 200 as the most common settings; Fidelity gives the support and resistance behaviour of a rising or falling EMA (all via [[ema-practitioner-references-2026-11-24]]).

## What each line is used to read

- **Price versus the 9:** price above the 9 signals short-term bullish momentum, below signals bearish; in strong trends price often rides the 9 without closing below it.
- **9 versus 20:** a 9 crossing above the 20 is the usual short-term bullish trigger and a cross below the bearish one; the area between the two lines is used as a pullback entry zone when a reversal candle forms (the 9/21 bounce setup).
- **Slope and distance:** slope shows direction, position shows bias, distance from the line shows how stretched price is.
- **Price versus the 200:** a trend filter. The rule "no longs below the daily 200 EMA, no shorts above it" circulates among traders but is unsupported (low confidence).

## Reading the three together

| Arrangement | Convention reading |
|---|---|
| Price above 9, 9 above 20, 20 above 200, all rising | Strong uptrend; pullbacks to the 9/20 zone are the usual entry area |
| Price between the 20 and the 200 | Pullback inside a larger trend, or a transition |
| Price below 200, 9 below 20 | Downtrend; shorts favoured |
| 9 and 20 tangled and flat, price crossing both | Range or chop; crossovers are unreliable here |

In a sideways market MA crossovers whip back and forth: "crossovers don't work in choppy markets", and shorter pairs such as 5/20 chop more than 50/200 even in a trend (Source: [[ema-practitioner-references-2026-11-24]]).

## Cautions

- **Period depends on timeframe.** A 200 EMA on a 5-minute chart spans a few trading sessions, not 200 days; StockCharts stresses that a cross on an intraday chart is not a Golden Cross, which is a daily 50/200 event.
- **9 is contested.** A Dummies author calls a nine-period average "nearly useless" for generating too many hard-to-follow signals, against widespread day-trader use.
- **200 as "institutional level".** Claims that institutions queue orders at the 200 are repeated by blogs but not supported by data in the sources read (low confidence).
- **Evidence mismatch.** The long-horizon tests (Faber, CFA Institute) use the 200-day or 10-month **SMA** on indices, not a 200 EMA on trading timeframes; the only direct EMA test found is on crypto minute data ([[mroziewicz-slepaczuk-2026-ema-crossover]]).
- **Not a signal on its own.** Moving averages lag and "often come in late"; use them as confirmation of trend and bias.

> [!gap] Needs verification
> Whether a 9/20 cross filtered by the 200 improves results after costs has no direct test in the sources read.
