---
type: concept
title: "Perpetual Futures (Perps)"
domain: trading
complexity: medium
tags: [perpetuals, derivatives, funding-rate, mark-price, index-price, leverage, liquidation, margin, insurance-fund, basis-trade]
created: 2026-11-19
updated: 2026-11-19
status: developing
related:
  - "[[concepts/order-book-and-execution-costs]]"
  - "[[concepts/perpetual-dex-landscape]]"
  - "[[concepts/candlestick-charts-and-patterns]]"
  - "[[concepts/technical-indicators-and-risk-sizing]]"
  - "[[sources/trading-autoresearch-2026-11-19]]"
---

# Perpetual Futures (Perps)

A **perpetual future** is a derivative that tracks the price of an underlying asset but has **no expiry date**. Because there is no settlement date to pull the contract price towards spot, the contract uses a **funding rate**: a periodic payment exchanged directly between longs and shorts. Perpetuals reportedly account for over 90% of crypto derivatives volume.

## Core Mechanics

| Component | Role |
|-----------|------|
| **Margin and leverage** | The trader posts collateral (margin) and controls a larger notional position. Leverage of 10x means a 10% adverse move removes the whole margin (ignoring fees and maintenance margin). |
| **Index price** | Reference price of the underlying, usually a weighted blend of spot prices across several exchanges, or an oracle on-chain. Aggregation makes it hard to manipulate through one venue. |
| **Mark price** | The price used for unrealised profit and loss, margin and **liquidation**. Roughly the index price plus a bounded premium or basis derived from the perp's own order book. |
| **Last price** | The most recent traded price. It is *not* normally used for liquidation, because a single large trade could otherwise trigger cascades. |
| **Funding rate** | Periodic payment (commonly every 8 hours, some venues hourly) that anchors the perp price to the index. |
| **Liquidation engine and insurance fund** | When equity falls below maintenance margin, the position is closed. Any shortfall is absorbed by an insurance fund and, if that is exhausted, by auto-deleveraging (ADL) of profitable counterparties. |

## Funding Rate

- **Positive rate:** the perp trades above the index, so **longs pay shorts**. **Negative rate:** shorts pay longs.
- A widely used (Binance-style) form is:

  `Funding = Premium Index + clamp(Interest − Premium Index, −0.05%, +0.05%)`

  where `Premium Index = (Impact Bid − Index) / Index` for the long side (and the mirror form for shorts). The default interest component is 0.01% per 8 hours, roughly 10.95% annualised. Exact constants and intervals vary by venue.
- **Payment** = position notional × funding rate, charged only at settlement timestamps. Opening and closing between timestamps pays nothing.
- **Why it works:** if the perp is rich, shorting the perp and buying spot earns funding and pushes the perp back down; the reverse applies when the perp is cheap. This is the **cash-and-carry (basis) arbitrage**, and "funding farming" is the market-neutral version of it.
- **Signal use:** persistently high positive funding suggests crowded longs; funding spiking while spot volume stalls can mean a fragile rally. Treat it as sentiment, not a timing tool.

## Mark Price versus Last Price — Why It Matters

Liquidation is triggered by the **mark price** on most major venues (Hyperliquid included). A brief wick on the last price does not liquidate you if the mark price, anchored to the index, does not follow it. The converse also holds: if the index falls sharply, you can be liquidated even though your venue's own last price looks calm.

## Risk Notes

- **Funding drag:** holding a crowded side for days can cost more than the spread and fees combined.
- **Liquidation price** moves with funding and with isolated versus cross margin; always read the venue's own figure.
- **Cascades:** clustered liquidations push price through further liquidation levels.
- Perps are a leveraged product; position sizing is covered in [[concepts/technical-indicators-and-risk-sizing]].

## Origin

Robert Shiller proposed the idea of perpetual claims in 1993; BitMEX popularised the modern funding-rate perpetual in crypto, and Arthur Hayes adapted ideas from interest-rate swaps and cash-and-carry arbitrage.

## Links to Your Work

The [[examples/stock-prediction-neural-network]] forecasts OHLCV data; a perp venue exposes the same candle data plus **funding rate**, **open interest** and **mark price** as additional features worth considering.
