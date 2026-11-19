---
type: concept
title: "Candlestick Charts, OHLC and Common Patterns"
domain: trading
complexity: low
tags: [candlesticks, ohlc, ohlcv, technical-analysis, doji, hammer, engulfing, backtesting]
created: 2026-11-19
updated: 2026-11-19
status: developing
related:
  - "[[concepts/perpetual-futures]]"
  - "[[concepts/technical-indicators-and-risk-sizing]]"
  - "[[examples/stock-prediction-neural-network]]"
  - "[[sources/trading-autoresearch-2026-11-19]]"
---

# Candlestick Charts, OHLC and Common Patterns

A **candle** summarises one time interval (1 minute, 1 hour, 1 day, and so on) with four prices: **Open, High, Low, Close**. Adding traded **Volume** gives **OHLCV**, the standard data format returned by exchange APIs and by `yfinance`.

## Anatomy

- **Body:** the range between open and close. Close above open is bullish (green or hollow); close below open is bearish (red or filled).
- **Wicks (shadows):** the extremes beyond the body. A long lower wick shows buyers rejecting lower prices; a long upper wick shows sellers rejecting higher prices.
- Candlesticks were developed by Japanese rice traders in the eighteenth century and carry the same four data points as an OHLC bar chart, only drawn so that body and wicks are easier to read.
- On 24/7 markets such as crypto perps, a "daily" candle depends on the venue's UTC cut-off; the same timeframe can differ slightly between exchanges.

## Common Patterns

| Pattern | Shape | Usual reading |
|---------|-------|---------------|
| **Doji** | Open ≈ close, wicks both sides | Indecision; needs confirmation from the next candle |
| **Hammer** | Small body, long lower wick, after a downtrend | Possible bullish reversal |
| **Inverted hammer** | Small body, long upper wick, after a downtrend | Buyers testing higher prices |
| **Shooting star** | Hammer-like with long upper wick, after an uptrend | Possible bearish reversal |
| **Bullish / bearish engulfing** | Second body fully covers the first | Reversal in the direction of the second candle |
| **Morning / evening star** | Three-candle reversal around a small middle candle | Reversal after a trend |
| **Marubozu** | Body with almost no wicks | Strong one-sided pressure |
| **Harami** | Small body inside the previous large body | Momentum pause |

## How Reliable Are They?

- Context matters more than shape: a hammer at established support, with rising volume, is treated as stronger than one mid-trend.
- One vendor backtest (25 patterns, 30 Dow Jones stocks, 20 years, 56,680 trades) reported win rates of only about 55–60% for the best patterns (inverted hammer 60%, gravestone doji 57%, bearish engulfing 57%). Edges of that size are easily erased by fees, spread and slippage — see [[concepts/order-book-and-execution-costs]].
- **Caveat:** that study is a commercial blog, not peer-reviewed, and tested equities, not leveraged crypto. Treat the numbers as an order of magnitude, and backtest on your own data with out-of-sample periods.

## Practical Notes

- Combine patterns with trend (moving averages) and volume rather than trading them in isolation.
- Higher timeframes (4h, daily) are less noisy than 1-minute candles.
- For machine learning, raw patterns are rarely used directly; derived features (returns, wick-to-body ratios, indicator values) are more usual — see [[concepts/technical-indicators-and-risk-sizing]].
