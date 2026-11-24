---
type: source
title: "Gray (2014) — A Simulation Study on Simple Moving Average Rules (Alpha Architect)"
address: c-000151
domain: trading
source_type: article
author: "Wesley Gray, PhD"
date_published: 2014-07-28
url: "https://alphaarchitect.com/a-simulation-study-on-simple-moving-average-rules/"
confidence: medium
status: ingested
created: 2026-11-24
updated: 2026-11-24
tags: [trading, moving-average, simulation, monte-carlo, bootstrap, data-mining]
key_claims:
  - "In normal, GARCH and GARCH-T simulations the moving average rule is roughly equal to buy-and-hold or underwhelms"
  - "In a historical bootstrap the rule is significantly better than buy-and-hold"
  - "Data-mining and model limitations are both viable explanations for the gap"
---

# Gray (2014): Simulation study on SMA rules

Source is more than 3 years old: treat as potentially stale for current markets.

- **Test:** S&P 500 buy-and-hold against a rule that is risk-on when the **20-day average is above the 252-day average**, risk-off otherwise. Daily data 1990 to 2013; bootstrap data 1929 to 2013; 500 Monte Carlo scenarios per model.
- **Four environments:** normal distribution, GARCH (volatility clustering), GARCH with Student-t noise (fat tails), historical bootstrap.
- **Results:** "In a normally distributed world, moving average rules are roughly equal to buy and hold" (the rule "kills the upside"); GARCH and GARCH-T did not change the picture; in the **bootstrap** the rule was "significantly better than buy and hold".
- **Interpretation:** the author lists data-mining ("always a viable alternative hypothesis") and limits of parametric models as the two explanations, and concludes the rule may be promising in the real world with the data-mining caveat.

## Reliability notes

Practitioner research blog. Metric charts (Sharpe, drawdown, CAGR) were images and could not be read. Uses SMA rules, not EMAs.

Used in [[concepts/moving-average-trading-evidence]] and [[synthesis/research-emas-in-trading]].
