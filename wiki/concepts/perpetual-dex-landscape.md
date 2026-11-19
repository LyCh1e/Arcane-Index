---
type: concept
title: "Perpetual DEX Landscape (2026)"
domain: trading
complexity: medium
tags: [perp-dex, hyperliquid, dydx, gmx, jupiter, lighter, aster, rwa-perps, on-chain-derivatives]
created: 2026-11-19
updated: 2026-11-19
status: developing
related:
  - "[[concepts/perpetual-futures]]"
  - "[[concepts/order-book-and-execution-costs]]"
  - "[[concepts/distributed-ledger-technology]]"
  - "[[sources/trading-autoresearch-2026-11-19]]"
---

# Perpetual DEX Landscape (2026)

A **perpetual DEX** offers leveraged perps with self-custody: trades, funding payments and liquidations are verifiable on-chain. Figures below come from secondary blogs and aggregator summaries citing DefiLlama; they conflict in places, so treat them as indicative.

## Three Architecture Models

| Model | How prices and liquidity work | Examples |
|-------|-------------------------------|----------|
| **Oracle-based pool (peer-to-pool)** | Traders trade against a liquidity pool at an oracle price; zero slippage but pool bears trader PnL | GMX, Jupiter Perps (Solana) |
| **Order book (CLOB)** | Central limit order book, on-chain or off-chain with on-chain settlement | Hyperliquid (own L1), dYdX v4 (Cosmos app-chain), Aster |
| **Virtual AMM (vAMM)** | Pricing curve with no real reserves | Early Perpetual Protocol |

## Market Snapshot

- Hyperliquid is reported as the dominant venue: 30-day perp volume above $800 billion in March 2026 (over 70% of on-chain derivatives volume in one source), though another April 2026 source cites about $180 billion and describes share pressure from Lighter and Aster. The discrepancy shows how definitions and windows differ.
- dYdX remains the long-running order-book venue; GMX the main pool model.
- **RWA perps** (commodities, FX, indices) were reported at roughly 31% of on-chain perp volume by July 2026, up from 1.3% at the start of the year. In March 2026 a licensed S&P 500 perpetual launched on Hyperliquid through a builder-deployed market (HIP-3).
- Binance alone processed roughly $4.9 trillion in futures volume in Q1 2026, so centralised venues still dominate.
- Funding rates on perp DEXs are used as a sentiment indicator, and CEX–DEX funding divergences create arbitrage opportunities.

## Risks

Smart-contract and oracle risk, wash-trading suspicions on newer venues, liquidity fragmentation, and regulatory uncertainty around licensed real-world-asset perps.
