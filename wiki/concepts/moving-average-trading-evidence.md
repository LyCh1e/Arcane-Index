---
type: concept
title: "Moving-Average Trading Rules: What the Evidence Says"
address: c-000156
domain: trading
complexity: high
status: developing
created: 2026-11-24
updated: 2026-11-24
sources: [cfa-moving-averages-sp500-2022, faber-tactical-asset-allocation-10-month-sma, rink-2023-technical-trading-rules, mroziewicz-slepaczuk-2026-ema-crossover, gray-2014-simulation-sma-rules, factset-golden-death-crosses-2018]
tags: [trading, moving-average, backtest, evidence, data-snooping, transaction-costs, golden-cross, death-cross]
related:
  - "[[concepts/exponential-moving-average]]"
  - "[[concepts/ema-9-20-200-roles]]"
  - "[[synthesis/research-emas-in-trading]]"
---

# Moving-Average Trading Rules: What the Evidence Says

The evidence is **mixed**. Slow trend filters on broad indices look useful as risk reducers; fast crossovers look fragile once costs, data snooping and time are taken into account. This page is a synthesis judgement drawn from the sources below.

## Evidence for

| Study | Finding |
|---|---|
| CFA Institute, S&P 500 1960s to present ([[sources/cfa-moving-averages-sp500-2022]]) | Long above and short below the **200-day** line: average daily return 0.06% to 0.10% above, -0.07% to -0.20% below, every decade. Reported significant at the 1% level; **before costs** |
| Faber, 10-month SMA ([[sources/faber-tactical-asset-allocation-10-month-sma]]) | Equity-like returns with bond-like volatility and drawdown; Sharpe from 0.45 to 0.80 in the allocation framework; framed as risk reduction |
| Gray, bootstrap ([[sources/gray-2014-simulation-sma-rules]]) | 20-day over 252-day rule "significantly better than buy and hold" on resampled history |
| Brock, Lakonishok and LeBaron (1992), via secondary descriptions | Moving-average and trading-range rules showed strong predictive power on the DJIA over about 90 years (original not read) |

## Evidence against or cautionary

| Study | Finding |
|---|---|
| Rink 2023, 41 indices, 6,406 rules ([[sources/rink-2023-technical-trading-rules]]) | Predictability declined over time; none of the developed markets predictable in 2009 to 2016; "quickly offset" by low costs; best past rules did worse than buy-and-hold afterwards |
| Gray, parametric simulations ([[sources/gray-2014-simulation-sma-rules]]) | Rule roughly equals buy-and-hold in normal, GARCH and GARCH-T worlds: it caps upside |
| Mroziewicz and Slepaczuk 2026, EMA pairs ([[sources/mroziewicz-slepaczuk-2026-ema-crossover]]) | Out-of-sample results about equal to buy-and-hold with lower drawdown; very sensitive to window choice; break-even cost about 0.4% per transaction |
| Urquhart, Gebka and Hudson (search snippet only) | Predictability of the moving-average rule diminished in three developed markets over 1987 to 2013 |

## Golden cross and death cross

- FactSet (1998 to 2018, US stocks of at least 300 million dollars market cap): golden crosses show positive short-term returns in most sectors; death crosses also had positive returns and beat golden crosses in the post-2009 bull market; "the jury is still out" ([[sources/factset-golden-death-crosses-2018]]).
- Media-reported LPL Research and Fundstrat studies found positive average forward returns after S&P 500 death crosses (LPL since 1950, 72% win rate at 12 months; Fundstrat after 48 occurrences since 1929) ([[sources/ema-practitioner-references-2026-11-24]]).
- A 50/200 cross lags by construction: it confirms a trend change rather than timing it. StockCharts defines a Golden Cross as a **daily** 50/200 event.

## Reading across the studies

1. **Slow beats fast.** The strongest results use 200-day or 10-month lines and monthly or daily data; short crossovers produce more trades and more whipsaw.
2. **Costs decide it.** Both Rink and Mroziewicz and Slepaczuk show profits disappearing at costs of roughly 0.2% to 0.4% per trade.
3. **The benefit is mostly risk reduction**, shown as lower drawdown and a better Sharpe ratio, not higher return.
4. **Decay and snooping.** Predictability fell in later samples; choosing the best window from many is itself a source of bias.
5. **SMA versus EMA.** The long-horizon evidence is about SMAs; EMAs on trading timeframes are barely tested.

> [!gap] Needs verification
> Faber and Brock et al. were read only through secondary summaries; the CFA study excludes costs and a reader disputes its execution timing.
