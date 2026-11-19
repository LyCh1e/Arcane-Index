---
type: concept
title: "Technical Indicators and Volatility-Based Risk Sizing"
domain: trading
complexity: medium
tags: [rsi, macd, moving-average, bollinger-bands, atr, position-sizing, stop-loss, risk-management]
created: 2026-11-19
updated: 2026-11-19
status: developing
related:
  - "[[concepts/candlestick-charts-and-patterns]]"
  - "[[concepts/perpetual-futures]]"
  - "[[examples/stock-prediction-neural-network]]"
  - "[[sources/trading-autoresearch-2026-11-19]]"
---

# Technical Indicators and Volatility-Based Risk Sizing

Indicators are functions of past OHLCV data. They **lag** by construction and describe history, not guarantees. Practitioners advise using two or three complementary indicators rather than many.

## Categories

| Category | Examples | Question answered |
|----------|----------|-------------------|
| Trend | SMA, EMA, ADX, Ichimoku | Which direction, and how strong? |
| Momentum | RSI, MACD, Stochastic | Is the move accelerating or fading? |
| Volatility | Bollinger Bands, ATR, Keltner | How large are typical moves? |
| Volume | OBV, volume profile | Is participation confirming the move? |

## Key Definitions

- **SMA(n)** = sum of the last n closes ÷ n. **EMA** weights recent closes more heavily.
- **RSI** compares average gains to average losses over a window (default 14). Conventional thresholds are 70 (overbought) and 30 (oversold), but in strong trends RSI can stay extreme for long periods.
- **MACD** = EMA(12) − EMA(26); the **signal line** is EMA(9) of the MACD; the histogram is their difference. Shorter settings (5, 35, 5) suit short-term trading; (8, 17, 9) suit weekly charts.
- **Bollinger Bands** = SMA(20) ± 2 standard deviations. Bands widen in high volatility and narrow in low volatility (a "squeeze"). The "95% inside the bands" figure assumes normally distributed returns, which markets do not follow; it is a default, not a promise.
- **ATR (Average True Range)** = moving average of the true range, where true range is the largest of high − low, |high − previous close| and |low − previous close|. It measures volatility, not direction.
- **ADX** measures trend strength: below 20 suggests no trend, 25–40 trending, above 40 strong.

## ATR-Based Risk Sizing

A common scheme:

1. Choose the fraction of equity to risk per trade (commonly 0.5–2%).
2. Place the stop at entry ∓ 2 × ATR (outside normal noise).
3. **Position size = amount risked ÷ stop distance.**

Example: entry 100, ATR 2.50, so the stop is at 95. Risking 200 gives a size of 200 ÷ 5 = 40 units. (A source using Risk ÷ ATR directly gives 80 units, which corresponds to a stop of one ATR; the multiplier you choose changes the size.)

On a leveraged perp, confirm that your **liquidation price** is well beyond your stop; otherwise the venue closes you out before your own risk rule does. See [[concepts/perpetual-futures]].

## Link to Machine Learning

The [[examples/stock-prediction-neural-network]] already computes 12 indicators as model inputs. ATR and funding-rate features are natural additions for crypto perps.
