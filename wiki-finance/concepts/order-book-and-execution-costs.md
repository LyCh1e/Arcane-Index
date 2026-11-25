---
type: concept
title: Order Books, Spread, Slippage and Maker–Taker Fees
domain: trading
complexity: low
tags:
  - order-book
  - bid-ask-spread
  - slippage
  - market-order
  - limit-order
  - maker-taker
  - liquidity
  - market-depth
created: 2026-11-19
updated: 2026-11-19
status: developing
related:
  - "[[perpetual-futures]]"
  - "[[candlestick-charts-and-patterns]]"
  - "[[trading-autoresearch-2026-11-19]]"
---

# Order Books, Spread, Slippage and Maker–Taker Fees

## The Order Book

An **order book** lists resting buy orders (**bids**) and sell orders (**asks**) by price level. The highest bid and lowest ask form the **bid–ask spread**, and their midpoint is the **mid-price**. Candles are built from *trades*, not from the book, so they hide the liquidity that determined execution.

## Order Types

- **Market order:** executes immediately against the book. Timing is certain; price is not. It consumes liquidity and so is a **taker** order.
- **Limit order:** "this price or better". It may fill late, partially or never. A resting limit order is a **maker** order; one that crosses the spread immediately is still a taker.
- **Stop, stop-limit and trailing stop:** conditional orders for risk control. On perps, check whether the trigger uses last price or mark price.

## The Cost Stack

`Total cost = spread + slippage + fee`

- **Spread:** crossing it costs about half the spread each way, so a round trip costs roughly the full spread.
- **Slippage:** the difference between the expected price and the average fill. It grows with order size, speed and shallow depth, because a large market order walks up the book.
- **Fees:** most venues use a **maker–taker** model, with lower (sometimes negative) fees for makers because they deepen the book. Typical taker fees on major perp venues are in the order of 0.04–0.06%; check each venue's current schedule.

Worked example: a market buy of BTC perp pays a spread of roughly 0.01–0.03%, plus slippage, plus a taker fee of about 0.05% each way — so a round trip can cost 0.1% or more before any price movement. A low-cap altcoin with a 10% spread loses about 9.5% on an immediate round trip.

## Depth and Imbalance

`Imbalance = (Bid depth − Ask depth) / (Bid depth + Ask depth)`

A positive value means more resting buy interest. It is a short-horizon microstructure feature, not a prediction on its own.

## Practical Rules

- Check depth before choosing a market order: good depth means small slippage; sparse depth suggests a limit order.
- Frequent traders are dominated by fees and spread; infrequent traders by slippage.
- Automated market makers (AMMs) and oracle-based perp pools do not have an order book in this sense; see [[perpetual-dex-landscape]].
