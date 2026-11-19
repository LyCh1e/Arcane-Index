---
type: source
title: "Trading Autoresearch — Perpetuals, Candles, Order Books and Indicators"
domain: trading
source-type: web-research
status: ingested
created: 2026-11-19
updated: 2026-11-19
tags: [trading, perpetuals, candlesticks, order-book, indicators, autoresearch]
---

# Trading Autoresearch (19 November 2026)

**Trigger:** the request "/autoresearch on trading, like perpetuals and candles and so on". The wiki held no relevant pages (only [[examples/stock-prediction-neural-network]]), so five web searches were run and the findings filed.

## Pages Produced

- [[concepts/perpetual-futures]]
- [[concepts/candlestick-charts-and-patterns]]
- [[concepts/order-book-and-execution-costs]]
- [[concepts/technical-indicators-and-risk-sizing]]
- [[concepts/perpetual-dex-landscape]]

## Main Sources

- BitMEX, "Perpetual Futures Explained" — blog.bitmex.com/what-are-perpetual-futures
- Spark glossary, "Perpetual Futures" and "Maker-Taker Fee Model" — spark.money/glossary
- Allium docs, perpetuals concepts — docs.allium.so/historical-data/perpetuals/concepts.md
- BeInCrypto / Zoomex, funding-rate and liquidation-engine explainer
- DEXTools tutorials on mark price and funding
- Liberated Stock Trader, candlestick reliability backtest (vendor study, not peer-reviewed)
- CMC Markets and Britannica Money, candlestick primers
- Spark Research, "Perpetual DEXs Are Reshaping Crypto Market Structure"; Yellow.com and Blockeden on Hyperliquid
- Parameter.io, order-book depth and imbalance; TMGM and Calmops indicator guides

## Confidence and Gaps

- Mechanics (funding, mark versus index, maker–taker) are consistent across sources: **high confidence**.
- Venue volume and market-share figures conflict between sources: **low confidence**.
- Candlestick win rates come from a single commercial backtest: **low confidence**.
- Not yet covered: options and implied volatility, open interest and liquidation-heatmap analysis, backtesting methodology (overfitting, walk-forward testing), exchange API specifics.
