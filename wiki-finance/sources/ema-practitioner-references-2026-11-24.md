---
type: source
title: "EMA practitioner and educational references (Fidelity, Britannica, StockCharts and others)"
address: c-000153
domain: trading
source_type: web-research
author: "Various (Fidelity; Britannica Money, K. Montevirgen; StockCharts Insider; TMGM; Dummies; FXNX; TradingView authors; Business Insider and Yahoo summaries of LPL and Fundstrat)"
date_published: 2026-11-24
url: "https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/ema"
confidence: medium
status: ingested
created: 2026-11-24
updated: 2026-11-24
tags: [trading, ema, education, practitioner, 9-ema, 20-ema, 200-ema, golden-cross]
key_claims:
  - "EMA multiplier is 2 / (N + 1); first EMA seeded with the N-period SMA (Britannica)"
  - "Most common settings are 9, 20 or 21, 50 and 200; 12 and 26 are reserved for MACD (TMGM)"
  - "Less lag means more whipsaw; more smoothing means more lag (StockCharts)"
---

# EMA practitioner and educational references

A bundle of non-academic sources read during [[research-emas-in-trading]]. Treat roles for 9, 20 and 200 as **practitioner convention**, not tested findings.

| Source | What it contributes | Confidence |
|---|---|---|
| Fidelity, EMA guide | EMA = (K x (C - P)) + P, K from the period count; follows price more closely than an SMA of the same period; "a rising EMA tends to support the price action, while a falling EMA tends to provide resistance"; "not designed to identify a trade at the exact bottom and top" | high (broker education) |
| Britannica Money (K. Montevirgen) | SMA and EMA steps; multiplier 2 / (X + 1), 20 days gives 0.0952 (9.52%); each 20-day SMA point carries 5% weight against 9.52% for the latest EMA close; EMA baseline ideally a year (about 256 trading days); the page does not mention 9 | high |
| StockCharts Insider (K. Montevirgen, 2 Nov 2026) | "Less lag, more whipsaw; more smoothing, more lag"; shorter pairs (5/20) chop more than 50/200; avoid crossovers in sideways markets; a Golden Cross is a **daily** 50/200 event, not a 50/200 cross on a one-minute chart; convert periods across timeframes (daily 50 and 200 become weekly 10 and 40) | high |
| TMGM academy | Common settings 9, 20 or 21, 50, 200; day traders and scalpers lean on EMA, swing and position traders on SMA | medium |
| Dummies (trading guide) | Shorter periods give more but less reliable signals; "a nine-period moving average is nearly useless" for the authors | medium |
| Bitget wiki, EBC | The 9 EMA as a short-term momentum filter, a "moving floor" or "moving ceiling" in strong trends, and the 9/20 or 9/21 cross | low (exchange and broker marketing) |
| FXNX blog | 200 EMA as "institutional line in the sand"; rule "no longs below the Daily 200 EMA, no shorts above it" | low (unsupported) |
| TradingView idea posts | 9/21 EMA bounce and crossover setups with volume and RSI filters; one 4-hour script calls the 9 the "trigger" and the 21 the "trend" line | low (individual traders) |
| Business Insider, Yahoo (LPL Research, Fundstrat) | After S&P 500 death crosses since 1950, 3-, 6- and 12-month average forward returns were positive, with a 72% win rate at 12 months (LPL); Fundstrat found positive returns after 48 occurrences since 1929 | medium (media-reported) |
| LuxAlgo library | Describes a three-EMA day-trade pack with 9, 20, 200 in a search snippet, but the fetched page named no default periods and defined no 9/20/200 setup | low (inconsistent) |

Used in [[exponential-moving-average]] and [[ema-9-20-200-roles]].
