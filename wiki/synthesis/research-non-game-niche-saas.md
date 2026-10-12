---
type: synthesis
title: "Research: Niche SaaS Ideas Beyond Games"
domain: business / software-engineering
maturity: developing
address: c-000134
tags: [research, saas, niche, obsidian, iot, fintech, computer-vision, compliance]
created: 2026-10-12
updated: 2026-10-12
related:
  - "[[synthesis/research-simple-saas-ideas]]"
  - "[[synthesis/research-game-saas-ideas]]"
  - "[[concepts/embedded-sensor-fusion-and-edge]]"
  - "[[concepts/wireless-and-iot]]"
  - "[[examples/stock-prediction-neural-network]]"
  - "[[concepts/digital-image-processing]]"
  - "[[concepts/transfer-learning-and-domain-adaptation]]"
  - "[[concepts/clustering-and-dimensionality-reduction]]"
sources:
  - "raw/articles/non-game-niche-saas-evidence-2026-10-12.md"
---

# Research: Niche SaaS Ideas Beyond Games

Third pass after [[synthesis/research-simple-saas-ideas]] and [[synthesis/research-game-saas-ideas]]. Evidence is in `raw/articles/non-game-niche-saas-evidence-2026-10-12.md`.

> [!warning] Evidence quality
> Obsidian income figures are self-reported by one developer. The temperature-monitoring page is a vendor's marketing page. The niche list is a blog with no pricing. Competitors were not checked for any idea below.

## Ideas

1. **Vault-to-quiz tool for note-takers.** Turn markdown notes (frontmatter, headings, wikilinks) into quizzes and revision sheets, either as an Obsidian plugin or a web app. Paid plugins sell at $19–$149 (one-off or lifetime), and a pre-sell post recommends collecting two paying buyers before building. Obsidian has 1,800+ plugins and spaced-repetition plugins already exist, so the angle must be structure-aware generation. Closest to the vault's own `update-study-notes` and `daily-notes` skills.
2. **Small-business cash-flow forecaster.** Forecast cash from invoices and bills for businesses with $1M–$20M revenue, with Best/Average/Worst bands as in [[examples/stock-prediction-neural-network]]. The niche list says accounting tools show history, not forecasts. Competitors were not checked.
3. **Low-cost temperature monitoring for small food businesses.** Off-the-shelf Bluetooth sensors, a gateway, threshold alerts and an audit log. Signal smoothing and thresholds follow [[concepts/embedded-sensor-fusion-and-edge]]; transport options are in [[concepts/wireless-and-iot]]. The vendor evidence targets multi-site operators on unpublished per-site pricing, which suggests a gap for single-shop owners. Hardware logistics add risk.
4. **Predictive maintenance for small manufacturers.** Vibration or current sensors with anomaly detection ([[concepts/clustering-and-dimensionality-reduction]]). The niche list says enterprise tools price out firms of 20–200 staff. The highest effort of the six.
5. **Licence and certification expiry tracker for trades.** A reminder and evidence-storage tool for regulated trades. A blog estimates $7K–$18K MRR, but the figure is unverified. Plain CRUD with strong switching costs once records are stored.
6. **Photo inspection reports.** Auto-tag defects in inspection photos and generate the report, using [[concepts/digital-image-processing]] and [[concepts/transfer-learning-and-domain-adaptation]]. A blog estimates $6K–$16K MRR (unverified).

## Recommendation

For a student with a notes vault, idea 1 is the cheapest test: pre-sell at $19 before coding, and stop if two people do not buy. Idea 3 is the most distinctive but needs hardware partners; test it by interviewing five food-stall owners first.
