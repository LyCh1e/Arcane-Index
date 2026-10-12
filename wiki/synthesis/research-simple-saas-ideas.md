---
type: synthesis
title: "Research: Simple SaaS Ideas Built From the Vault"
domain: business / software-engineering
maturity: developing
address: c-000132
tags: [research, saas, micro-saas, product-ideas, rag, prompt-injection, credentials, performance-testing, pdpa]
created: 2026-10-12
updated: 2026-10-12
related:
  - "[[concepts/file-format-prompt-injection]]"
  - "[[concepts/retrieval-augmented-generation]]"
  - "[[concepts/rag-architectures]]"
  - "[[concepts/prompt-compression]]"
  - "[[concepts/mcp-model-context-protocol]]"
  - "[[concepts/performance-engineering]]"
  - "[[concepts/github-actions-cicd]]"
  - "[[concepts/privacy-data-protection-and-ip]]"
  - "[[concepts/browser-extensions]]"
  - "[[synthesis/research-blockchain-microcredentials]]"
  - "[[examples/ict3113-a1-ticket-triage-service]]"
  - "[[concepts/needfinding-and-task-analysis]]"
sources:
  - "raw/articles/simple-saas-market-evidence-2026-10-12.md"
---

# Research: Simple SaaS Ideas Built From the Vault

**Question:** Which simple SaaS products could be built from what this vault already teaches, and which look worth testing first?

**Method:** The vault was searched first. It has deep technical material but **no pages on SaaS markets, pricing or go-to-market**, so five web pages were read for pricing and demand evidence (saved to `raw/articles/simple-saas-market-evidence-2026-10-12.md`). Market figures are vendor or blog claims and are marked as such.

> [!warning] Evidence quality
> Revenue figures in the micro-SaaS articles are the authors' estimates. The RAG pricing table comes from a vendor (Ailog) that sells in the same market. Competitor landscapes for ideas 1, 5 and 6 were **not** checked.

## What makes a simple SaaS (from the market reading)

- A recurring, unavoidable, money-adjacent or risk-adjacent pain, in a niche that big tools overbuild for.
- Price points of $19–$99/month for dev tools and AI wrappers; $99–$500/month where the buyer is a business with a compliance or security worry.
- Validation before building: 10–20 customer conversations or pre-orders. The vault's [[concepts/needfinding-and-task-analysis]] gives the method: watch for **workarounds**, which show where the current tool fails.

## The ideas, ranked

### 1. Upload Guard — hidden-instruction scanner for documents (recommended first test)
- **Product:** upload or API-post a PDF, CSV/XLSX or text file; get back a report of hidden content (white-on-white text, sub-2pt fonts, off-page coordinates, invisible glyphs, zero-width Unicode, metadata) plus a cleaned text extract safe to hand to an LLM.
- **Vault basis:** [[concepts/file-format-prompt-injection]] lists the concealment techniques per format. Its benchmark finding is the product's core argument: **structural detection (how text is hidden) reached F1 0.960, versus 0.390 for text-only classifiers**. ManpowerGroup's ~100,000 CVs a year with hidden text gives a concrete buyer: recruiters and ATS vendors.
- **Simple MVP:** no LLM needed — a PDF parser, a few rules and a report page. FastAPI as in [[examples/ict3113-a1-ticket-triage-service]].
- **Price anchor:** PromptBrake charges $99 per scan pack and $499/month, but tests LLM endpoints, not documents. A $29–$99/month tier is plausible for small HR tools.
- **Risks:** buyers may be few and developer-heavy; AI-security is crowded; image-based attacks (pixel-level) are harder than the PDF case.
- **Distribution idea:** a browser extension ([[concepts/browser-extensions]]) that scans a file before it is attached to a chatbot.

### 2. Flat-price support bot for one niche
- **Product:** a RAG chatbot for a single vertical (for example clinics, tuition centres or property agents), with flat monthly pricing and PDPA-aware hosting.
- **Vault basis:** [[concepts/rag-architectures]] and [[synthesis/research-rag]] — recursive chunking as a safe default, hybrid search plus re-ranking as the highest-ROI upgrade, and "evaluate on your own corpus". [[concepts/prompt-compression]] cuts token cost. The Learnix examples show the vault owner already builds learner-facing chat with progress tracking.
- **Market evidence:** commodity tiers sit at $19–$399/month (Chatbase, CustomGPT, Tidio). Per-resolution tools such as Intercom Fin ($0.99 each) get costly at volume; the vendor article estimates ~$120,000/year at 15,000 conversations a month.
- **Risks:** the generic market is crowded. It only works if the niche is narrow and the setup (ingesting the client's documents) is done for them.

### 3. Performance-regression gate for pull requests
- **Product:** a GitHub Action plus small dashboard that runs a short open-loop load test and fails the pull request when p95 latency regresses against a stored baseline.
- **Vault basis:** [[concepts/performance-engineering]] (Lec07): six test types, **open-loop versus closed-loop** load, the regression test ("did the last change make it slower?") and the pipe-clean test. Its key lesson becomes a feature: **assert on the response body, not the status code** — a generator once reported 100% success while the server created zero orders. [[concepts/github-actions-cicd]] covers the pipeline side.
- **Price anchor:** dev tools at $19–$39/month per repo.
- **Risks:** k6, BlazeMeter and similar exist (not checked here); the value is in being simpler and cheaper.

### 4. Credential issuing for small training providers
- **Product:** issue W3C Verifiable Credentials / Open Badges 3.0 using `did:web`, with an optional daily Merkle-root anchor.
- **Vault basis:** [[synthesis/research-blockchain-microcredentials]] — `did:web` gives verifier independence without a blockchain; only hashes go on-chain, keeping GDPR/PDPA exposure thin; the market was reported at a 21.7% CAGR.
- **Market evidence:** Accredible starts at about US$996 a year. In Singapore, government-backed OpenCerts and local vendors already serve large institutions.
- **Risks:** strong incumbents and state infrastructure. Best aimed at small providers outside the big-institution channel, undercutting on price.

### 5. PDPA-safe redaction gateway
- **Product:** a proxy that strips NRIC/FIN numbers, phone numbers and emails from text before it reaches a cloud LLM, then restores them in the reply; logs what was removed.
- **Vault basis:** [[concepts/privacy-data-protection-and-ip]] covers PDPA consent obligations and PII definitions (NRIC, FIN, passport, phone, email).
- **Risks:** open-source redaction libraries exist; competitor and pricing research was not done for this idea.

### 6. Local-model ticket triage for SMEs
- **Product:** routes emails or tickets into fixed categories using a small local model, so no customer text leaves the company's server.
- **Vault basis:** [[examples/ict3113-a1-ticket-triage-service]] — working design with Ollama, SQLite and per-call JSON logs, including the `fallback_used` flag that separates "wrong answer" from "ignored the output format".
- **Risks:** the assignment version is deliberately naive (synchronous, no caching); CPU-only inference is slow, so a production version needs the optimisation work from ICT3113 Assignment 2.

## Recommendation

1. **Test Upload Guard first.** It has the strongest vault grounding, the smallest build and no model costs. Run 10–20 conversations with recruiters, HR-tech builders and anyone running LLMs on uploads before writing more than a prototype.
2. **Keep the niche RAG bot as the safer revenue route.** Demand is proven by the price tables; the work is choosing a vertical.
3. Treat the performance gate as a good portfolio project that is a plausible small product.

## Gaps this note leaves open

- No check of competitors for ideas 1, 3, 5 and 6.
- No Singapore-specific pricing beyond the Accredible listing.
- All revenue figures are unverified estimates.
