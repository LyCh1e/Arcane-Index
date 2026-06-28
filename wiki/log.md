---
type: meta
status: established
title: "Operation Log"
updated: 2026-06-08
tags: [meta, log]
---

# Operation Log

Chronological record of all vault operations. Append-only — never edit past entries. New entries go at the TOP.

## 2026-06-28 | ingest | LeetCode 645 — Set Mismatch

- Source: `raw/leetcode-set-mismatch-2026-06-28.md`
- Summary: [[sources/leetcode-set-mismatch]]
- Pages created: [[sources/leetcode-set-mismatch]] (c-000078), [[examples/leetcode-set-mismatch-python]] (c-000079)
- Pages updated: [[concepts/array-manipulation-patterns]] (Pattern 4 Frequency Count + Pattern 5 Math Sum Identity added), [[wiki/index.md]], [[wiki/sources/_index.md]]
- Key insight: `dict.get(key, 0)` and `Counter` are two expressions of the same frequency-count pattern; the math sum identity (`sum(nums) - sum(set(nums))`) solves duplicate/missing in O(1) extra space when the expected aggregate is known.

---

## 2026-06-28 | ingest | LeetCode Array Basics — chat session (1929, 1470, 485)

- Source: `raw/leetcode-array-basics-2026-06-28.md`
- Summary: [[sources/leetcode-array-basics]]
- Pages created: [[concepts/array-manipulation-patterns]] (c-000076), [[examples/leetcode-array-basics-python]] (c-000077), [[sources/leetcode-array-basics]] (c-000075)
- Pages updated: [[wiki/index.md]], [[wiki/sources/_index.md]], [[wiki/areas/computer-science]]
- Key insight: Three named array patterns — concatenation, split-midpoint interleave, and linear scan with running counter — cover a large fraction of Easy-tier array problems.

---

## 2026-06-25 | project | ICT2216 TrialGuard — CodeQL restored + GitHub Actions action version deprecations

- Restored `codeql-analysis` job to `.github/workflows/ci-cd.yml` (removed in commit d49f989 due to GHAS limitation on personal private repos)
- Bumped `github/codeql-action` v3 → v4 across all three steps (init, analyze, upload-sarif); v3 deprecated December 2026
- Fixed Node 20 deprecation warnings: pinned `actions/checkout` to `@v4.3.0`, `actions/setup-python` to `@v5.6.0`, `actions/upload-artifact` to `@v4.6.2`; left `actions/setup-node` as floating `@v4` (pinned `@v4.4.2` resolved to a non-existent release)
- Key gotcha: linter auto-bumped `@v4.4.0` to `@v4.4.2` (non-existent); replace_all on `@v4` inside `@v4.3.0` doubled to `@v4.3.0.3.0`
- Also: replaced `PhotoSlot` placeholder in `Researchers.jsx` with actual `cohort.gif`; learned `objectFit: 'contain'` vs `'cover'`; dropping the fixed-aspect-ratio wrapper and using bare `<img width: 100%>` lets the image set the container height naturally
- Created: [[learning/github-actions-version-deprecations]]
- Updated: [[concepts/github-actions-cicd]] (new "Action Version Management" section)

---

## 2026-06-26 | setup | Epistemic Critique Skills

- New template: [[_templates/argument.md]] — structured argument note (claim, premises, evidence, counterarguments, falsifiability, belief history)
- New skill: `/critique` — full epistemic audit (18 fallacies, premise table, 8 cognitive biases, evidence quality, contradiction check against vault, steelman, falsifiability rating, verdict with confidence revision)
- New skill: `/steelman` — constructs the strongest opposing case then attacks your position; delivers clear verdict (argument survives / steelman wins / draw)
- New skill: `/track-belief` — snapshots confidence + position into Belief History table; tracks revision and abandonment; review mode shows trajectory across all snapshots
- New folder: [[wiki/arguments/_index.md]] — index with Active / Revised / Abandoned tables
- Updated: CLAUDE.md Plugin Skills table and vault structure

---

## 2026-06-26 | autoresearch | Kubernetes

- Rounds: 2 | Searches: 8 | Sources fetched: 4 | Pages created: 3
- New concept: [[concepts/kubernetes]] — full reference: architecture (control plane + worker nodes), all 7 workload types, Service types (ClusterIP/NodePort/LoadBalancer/ExternalName), Ingress, ConfigMap/Secret/PVC, RBAC, Pod Security Standards, Helm 4.0, managed services (GKE/EKS/AKS), kubectl commands, Kubernetes vs Docker Compose decision framework
- New source: [[sources/kubernetes-official-docs]]
- Synthesis: [[synthesis/research-kubernetes]]
- Addresses assigned: c-000073 – c-000075
- Key finding: Secrets are NOT encrypted in etcd by default (only base64-encoded); EncryptionConfiguration must be explicitly enabled for production clusters

---

## 2026-06-25 | autoresearch | Data Mapping

- Rounds: 2 | Searches: 5 | Sources fetched: 4 | Pages created: 4
- New concept: [[concepts/data-mapping]] — techniques (9 types), transformation types (8), 12-step process, mapping document structure, ETL vs ELT, object mapping (DTO/AutoMapper), tools landscape
- New sources: [[sources/airbyte-data-mapping-guide]], [[sources/atlan-data-mapping-guide]]
- Synthesis: [[synthesis/research-data-mapping]]
- Addresses assigned: c-000069 – c-000072
- Key finding: schema matching (are these equivalent?) ≠ schema mapping (how to transform one to the other) — conflating them is a common source of integration bugs

---

## 2026-06-25 | ingest | ICT2216 Lecture 6 — Secure Software Implementation

- Source: [[sources/ICT2216-lecture6-secure-implementation]]
- New concept: [[concepts/fido-passkeys-passwordless]] — FIDO Alliance, passkeys (registration/login flow), OTP/magic link design constraints, platform limitations (cross-platform inconsistency, lock-in)
- Updated: [[concepts/secure-design-implementation]] — new "SSL/TLS Security Analysis" section: incompatibility table, why salted hashing forces cleartext transmission, why phishing survives TLS, MitM SSL stripping, HSTS, PFS, cipher suite selection, SRP (RFC 5054), Security Theatre
- Updated: [[concepts/github-actions-cicd]] — DevSecOps definition, CI vs Continuous Delivery vs Continuous Deployment distinction table
- Address assigned: c-000068 (fido-passkeys-passwordless)

## 2026-06-23 | project | ICT2216 Lab 8 — ESLint SAST integrated into TrialGuard CI/CD

- Pages updated: [[examples/ict2216-lab8-static-code-analysis]] (added "Project Implementation" section)
- Key findings: GitHub Code Scanning unavailable on personal private repos → replaced upload-sarif with upload-artifact; explicit permissions block drops contents:read (breaks checkout); Vite+React needs no Babel parser for ESLint JSX; eslint-plugin-security detected real timing attack in Signup.jsx; Node 20 deprecated on runners → Node 24; CodeQL removed (requires Code Scanning)

## 2026-06-23 | ingest | ICT2216 Lab 9 — SonarQube

- Pages created: 2 (instructions_lab9.md + wiki example)
- Examples: [[examples/ict2216-lab9-sonarqube]]
- Key content: SonarQube + PostgreSQL via Docker Compose (port 9000), local scanner via sonarsource/sonar-scanner-cli Docker image, project token → GitHub Secrets (SONAR_TOKEN + SONAR_HOST_URL), sonarsource/sonarqube-scan-action GitHub Actions workflow, OOM fix (--memory=3g)

## 2026-06-23 | ingest | ICT2216 Lab 8 — Static Code Analysis

- Pages created: 2 (instructions_lab8.md + wiki example)
- Examples: [[examples/ict2216-lab8-static-code-analysis]]
- Key content: ESLint with Modern Flat Config (eslint.config.mjs), SARIF output via @microsoft/eslint-formatter-sarif, three security plugins (eslint-plugin-security / security-node / no-unsanitized), GitHub Actions workflow uploading SARIF to Code Scanning, GitHub CodeQL workflow

## 2026-06-23 | ingest | ICT2216 Lab 7 — GitHub Actions with Automated Testing

- Pages created: 2 (instructions_lab7.md + wiki example)
- Examples: [[examples/ict2216-lab7-automated-testing]]
- Key content: Mocha/Chai unit tests on Node.js, Selenium + ChromeDriver integration/UI tests via Docker, two-job GitHub Actions workflow (build → test) with selenium sidecar service and artifact hand-off via tar

## 2026-06-23 | ingest | ICT2216 Lab 6 — OWASP Dependency Check

- Pages created: 2
- Resources: [[resources/owasp-dependency-check]]
- Examples: [[examples/ict2216-lab6-owasp-dependency-check]]
- Key content: Docker-based local SCA scan, GitHub Actions workflow with artifact upload, Dependabot/Renovate alternatives

## 2026-06-23 | autoresearch | AI Workflows

- Rounds: 3 | Searches: 6 | Sources fetched: 2 | Pages created: 5
- Concepts: [[concepts/ai-workflows]], [[concepts/ai-workflow-orchestration]]
- Sources: [[sources/anthropic-building-effective-agents]], [[sources/aws-agentic-ai-patterns-2025]]
- Synthesis: [[synthesis/research-ai-workflows]]
- Key finding: AI workflows are distinguished from agents by whether the LLM controls its own process (agent) or follows predefined code paths (workflow); Anthropic's 5 patterns (Prompt Chaining, Routing, Parallelisation, Orchestrator-Workers, Evaluator-Optimiser) cover the majority of production use cases; the orchestration tool landscape splits into three distinct categories (agent orchestration, durable execution, data pipelines) and picking the wrong category is the most common architectural mistake.

## 2026-06-23 | autoresearch | Retrieval-Augmented Generation (RAG)

- Rounds: 3 | Searches: 6 | Sources fetched: 3 | Pages created: 6
- Concepts: [[concepts/retrieval-augmented-generation]], [[concepts/rag-architectures]]
- Entities: [[entities/graphrag-microsoft]]
- Sources: [[sources/humanloop-rag-architectures-2025]], [[sources/pinecone-rag-guide]]
- Synthesis: [[synthesis/research-rag]]
- Key finding: RAG is a four-stage pipeline (chunk → embed → retrieve → generate) that has evolved through four generations; hybrid search + re-ranking is the production default; GraphRAG (Microsoft) achieves 72–83% comprehensiveness improvement over vector RAG on holistic queries; chunking strategy performance is corpus-dependent — evaluate on your own data; RAG and MCP are converging at the agent layer.

## 2026-06-23 | autoresearch | MCP Servers (Model Context Protocol)

- Rounds: 3 | Searches: 5 | Sources fetched: 5 | Pages created: 7
- Concepts: [[concepts/mcp-model-context-protocol]], [[concepts/mcp-security]]
- Entities: [[entities/agentic-ai-foundation-aaif]]
- Sources: [[sources/anthropic-mcp-launch-2024]], [[sources/mcp-spec-2025-11-25]], [[sources/mcp-first-year-2025]]
- Synthesis: [[synthesis/research-mcp-servers]]
- Key finding: MCP is a provider-agnostic JSON-RPC 2.0 protocol (Host → Client → Server) that replaced fragmented LLM tool integrations; donated to the Linux Foundation's AAIF in Dec 2025; the Nov 2025 spec added async Tasks, CIMD OAuth, and M2M OAuth for headless agents; security risks include prompt injection, tool poisoning, and rug pull attacks.

## 2026-06-21 | autoresearch | Context Compression of Chats with Large Language Models

- Rounds: 2 | Searches: 8 | Sources fetched: 7 | Pages created: 8
- Concepts: [[concepts/context-compression-llm]], [[concepts/kv-cache-compression]], [[concepts/prompt-compression]]
- Entities: [[entities/llmlingua]]
- Sources: [[sources/acon-context-compression-agents]], [[sources/anthropic-effective-context-engineering]], [[sources/factory-ai-compression-evaluation-2025]], [[sources/kv-cache-compression-review-2025]]
- Synthesis: [[synthesis/research-context-compression-llm]]
- Key finding: Five distinct technique families exist (dialogue summarisation, prompt compression, KV cache compression, soft/latent compression, retrieval-based); higher compression ratio does NOT equal higher quality — Factory's 98.6% compression scored 0.35 points higher than OpenAI's 99.3% compression on production tasks; artifact tracking remains an open problem across all methods

## 2026-06-19 | project | ICT2216 TrialGuard — CD Pipeline (GitHub Actions → EC2)

- Updated: [[concepts/github-actions-cicd]] — added "CD: Deploying to EC2 via SSH" section covering the full deploy job pattern, `gh secret set` for adding secrets via CLI, the `git archive` approach for private repos, and the `-o LogLevel=ERROR` fix
- Created: [[learning/ssh-stdout-known-hosts-warning]] — SSH "Permanently added to known hosts" warning contaminates stdout when using `2>&1`; fix is `-o LogLevel=ERROR` on all SSH/SCP calls
- Key: GitHub repo secrets (EC2_HOST, EC2_SSH_KEY) added via `gh secret set` — encrypted at rest, masked in logs, write-only after creation, safe for school projects

## 2026-06-12 | autoresearch | Blockchain Technology

- Rounds: 3 | Searches: 9 | Sources fetched: 7 | Pages created: 8
- Sources: [[sources/hacken-smart-contract-vulnerabilities-2025]], [[sources/atlantic-council-cbdc-tracker-2026]], [[sources/chainalysis-crypto-crime-report-2025]], [[sources/layer2-scaling-comparison-2025]]
- Entities: [[entities/satoshi-nakamoto]], [[entities/vitalik-buterin]], [[entities/nick-szabo]]
- Synthesis: [[synthesis/research-blockchain-technology]]
- Concept updated: [[concepts/blockchain-technology]] (added §17 Live Statistics — 2025/2026 figures)
- Key finding: The biggest blockchain losses are no longer smart contract bugs but private key theft — the weakest link has moved from code to people; DPRK stole ≥$2.02B in 2025 alone

## 2026-06-12 | research | Blockchain Technology

- Created [[concepts/blockchain-technology]] (c-000067) — comprehensive research note
- Covers: block anatomy, cryptographic foundations (SHA-256, ECDSA, Merkle trees), transaction lifecycle, all major consensus mechanisms (PoW/PoS/DPoS/PBFT/PoA), UTXO vs account model, smart contracts (EVM, Solidity, risks), network architecture (node types), security threat model (51% attack, eclipse, long-range, quantum risk, privacy), scalability trilemma and Layer-2 rollups, real-world implementations (Bitcoin, Ethereum, Hyperledger Fabric), and cross-domain connections
- Diagrams: block chain linkage, Merkle tree, transaction flow sequence, PoW mining loop, PoS attestation flow, consensus quadrant chart, mindmap threat model, full transaction lifecycle, network architecture, EVM deployment pipeline
- Domain `blockchain` added (17th domain)
- Updated [[index.md]], [[hot.md]]

## 2026-06-11 | ingest | ICT2216 Labs 1–5 instruction files

- Source: `instructions_lab1.md` through `instructions_lab5.md` (step-by-step lab guides created from PDF lab sheets)
- No new example pages created — all five labs already had comprehensive pages in `wiki/examples/`
- Updated [[examples/ict2216-lab2-securityrat]]: added **Part 1 — CIA+AAA security requirements framework discussion** (this section was completely absent; the page only covered the SecurityRAT tool)
- Updated [[examples/_index.md]]: added four missing entries — Lab 4 (OWASP Threat Dragon), Lab 5 (GitHub Actions), Project Phase 4 Auth, Project Deployment Phases 9–12

## 2026-06-08 | ingest | ICT2216 Lecture 5 — Secure Software Design (transcript re-ingest)

- Source: spoken lecture transcript (Lecture 5 — same content as 2026-05-30 ingest, reviewed for new details)
- Three additions made to [[concepts/secure-design-implementation]]:
  - **Deactivate vs delete pattern** (referential integrity section) — add `active` column rather than physically removing user rows; preserves audit history and referential links
  - **Admin account installation-wizard model** (authentication design section) — prompt for admin credentials on first launch (Windows/Linux install pattern); never pre-seed hard-coded credentials
  - **NFR governing hash iteration count** (hashing section) — iteration count must be specified as a non-functional security requirement with hardware-based justification, not chosen arbitrarily
- Updated: [[concepts/secure-design-implementation]] (updated field, 3 additions)

## 2026-05-31 | project | ICT2216 TrialGuard — Phases 9–12 Deployment and Hardening

- Created: [[examples/ict2216-project-deployment-phases-9-12]] — full EC2 deployment workflow (git archive + SCP for private repos, PEM permissions, cert generation on Linux, docker compose, health checks, compliance report endpoint, daily backup service)
- Created: [[learning/docker-volume-host-dir-created-as-root]] — Docker creates bind-mount host dirs as root if missing; fix: `sudo chown <user>:<user>` or `mkdir -p` before first compose up
- Created: [[learning/docker-ro-mount-chmod-fails]] — `chmod` fails on `:ro` mounted scripts; fix: call `sh /backup.sh` instead of making file executable
- Created: [[learning/git-amend-remove-sensitive-push]] — remove sensitive info from latest pushed commit: edit file → `git add` → `git commit --amend --no-edit` → `git push --force origin main`
- Created: [[learning/windows-openssl-strawberry-broken]] — Strawberry Perl's OpenSSL maps config to non-existent Z: drive; generate TLS certs on EC2/Linux and SCP back instead
- Updated: [[index.md]] (1 example row, 4 learning rows)

## 2026-05-30 | lab | ICT2216 Lab 4 — OWASP Threat Dragon

- Lab file: `Lab4/Lab04 - OWASP Threat Dragon-2025.pdf`
- Created: [[resources/owasp-threat-dragon]] — two delivery variants (web/desktop/Docker), full stencil element table (Process/Store/Actor/DataFlow/TrustBoundary), both data-flow creation methods (drag + grey link tool), out-of-scope marking (dashed lines, reason field, threat generation disabled), red highlighting for open threats, customisable report, MS TMT vs Threat Dragon comparison table
- Created: [[examples/ict2216-lab4-owasp-threat-dragon]] — step-by-step lab walkthrough (5 steps: add elements → add flows/boundaries → out-of-scope → triage threats → report), key differences from Lab 3 MS TMT table, 4 gotchas (grey link ≠ red delete; trust boundaries drive threat count; out-of-scope ≠ delete; save frequently)
- Updated: [[sources/ICT2216-secure-software-development]] (Lab 4 row, new example, new resource)
- Updated: [[index.md]] (1 example row)

## 2026-05-30 | lab | ICT2216 Lab 5 — Nginx Reverse Proxy, Let's Encrypt TLS, GitHub Actions CI/CD

- Lab file: `Lab5/X05-Github-Actions.pdf`
- Step 4.1–4.2: Created `Lab5/nginx-proxy/` with Nginx Docker Compose; updated `nginx.conf` for `localhost`; started with `docker compose up -d`; verified with `curl http://localhost/` → Hello World HTML
- Step 4.3–4.5: Prepared TLS config files (`nginx-compose-tls.yml` + `nginx-tls.conf`) with certbot entrypoint (ACME webroot challenge, email: lcslayer22@gmail.com); created `certbot/www/` and `certbot/conf/` directories; TLS config ready for deployment on team VM with real domain (replace `yourdomain.com`)
- Step 5: Created `Lab5/lab5-cicd/` standalone git repo with `index.html` at root and `.github/workflows/test-nginx.yml`; initialized git on `main` branch; GitHub CLI (gh) installed via winget; pending `gh auth login` + push
- Auto-renewal cron pattern documented (Step 4.6, optional): `0 3 * * * docker compose run --rm certbot renew && docker compose restart nginx`
- Created: [[concepts/nginx-reverse-proxy-and-tls]] (Nginx config, Let's Encrypt two challenge methods, TLS compose, nginx-tls.conf, auto-renewal)
- Created: [[concepts/github-actions-cicd]] (workflow YAML anatomy, triggers, runners, Docker in Actions, secrets, job dependencies, full pipeline stages for secure software)
- Created: [[examples/ict2216-lab5-github-actions]] (full lab walkthrough, all config files, key gotchas)
- Updated: [[sources/ICT2216-secure-software-development]] (Lab 5 entry, two new concept links, new example link)
- Updated: [[index.md]] (2 concept rows, 1 example row)

## 2026-05-26 | project | ICT2216 Project — Frontend Volume Bug Fix + start.py Refresh Automation

- Root cause identified: `frontend_dist` named volume is only seeded from image on first creation; rebuilding the image never updates an existing volume
- Fix: `purge_frontend_volume()` added to `start.py` — stops nginx/frontend-build, removes stopped containers holding the volume, deletes the volume, then `docker compose up -d --build` re-seeds it fresh
- Footer cleanup: removed Privacy/Terms/Security/HIPAA/GDPR/SOC 2 links from all four footer locations (Login.jsx, Signup.jsx, Landing.jsx, subpage-shell.jsx); each now shows only `© 2026 TRIALGUARD`
- Learning page created: [[learning/docker-named-volume-stale-content]] (named volume stale content gotcha, fix, and alternative patterns)
- Updated: [[concepts/docker-compose]] cross-reference added

---

## 2026-05-26 | project | ICT2216 Project — Phase 4 Authentication + Docker Stack Verification

- Project: TrialGuard — Secure Clinical Trial Participant Portal (ICT2216 Secure Software Development)
- Tasks completed: 4.1 Register, 4.2 Login (step 1), 4.3 Verify MFA (step 2), 4.4 Logout, 4.5 Audit log
- Example page created: [[examples/ict2216-project-phase4-auth]] (full auth blueprint, two-step MFA, session fixation prevention, audit log, CSRF approach, smoke test)
- Learning page created: [[learning/docker-compose-build-context]] (build context controls COPY visibility — fix for moved requirements.txt)
- Updated: [[concepts/docker-compose]] (added "Build Context — Shared Files Across Services" section)
- Docker build context change: `build: ./backend` → `build: { context: ., dockerfile: backend/Dockerfile }` in compose; `COPY . .` → `COPY backend/ .` in Dockerfile
- Frontend plumbing: `frontend/src/api.js` fetch wrapper; Vite dev proxy `/api` → `http://localhost:8080`
- start.py launcher created at repo root: builds stack, polls until ready, opens browser; full error handling
- Stack verified: all 6 containers healthy, `https://localhost` serves React SPA, `POST /api/auth/register` returns 201

---

## 2026-05-25 | project | ICT2216 Project — Vite + React SPA Refactor (TrialGuard)

- Project: TrialGuard — Secure Clinical Trial Participant Portal (ICT2216 Secure Software Development)
- Example page created: [[examples/ict2216-project-vite-refactor]]
- Learning page created: [[learning/vite-react-spa-migration]] (3 bugs + migration patterns)
- Resource page created: [[resources/vite]] (Vite build tool)
- Updated: [[examples/_index.md]], [[resources/_index.md]]
- Key migrations: UMD/CDN React → Vite; `Object.assign(window,{})` → ES modules; multi-page HTML → React Router v6 SPA
- Build verified: 42 modules, 0 errors, `npm run dev` functional

---

## 2026-05-30 | update | ICT2216 Lecture Transcript — Threat Modelling & Security by Design (recap lecture)

- Source: ICT2216 lecture transcript (threat modelling + all 10 OWASP Security by Design Principles)
- Updated: [[concepts/threat-modeling]] (dated 2026-05-30)
- Additions (3 targeted — existing pages already comprehensive):
  1. **Threat → Attack → Risk triangle** — Attack defined as the *realisation* of a threat; Risk clarified as the consequence that can be zero even when an attack occurs if the system is well-protected; SQL injection worked example illustrating the principle
  2. **AI threat specifics** — data poisoning (malicious training data) and prompt injection (overriding AI chatbot system instructions) added to Non-Human Threats section
  3. **Concrete STRIDE worked examples** — Spoofing (typosquatting: `amazom.com` impersonating `amazon.com`); Tampering (modifying `user_code` at checkout to charge a victim's credit card); Repudiation (signed delivery receipt as non-repudiation mechanism, with software equivalent: digital signatures + hash-chained audit logs)
- No new files created; all content absorbed into existing concept page
- No address counter change (update only)

---

## 2026-05-30 | ingest | ICT2216 Lecture 5 — Secure Software Design (Part 2) & Secure Agile Development

- Source: `raw/ICT2216 Lecture 5 Secure Software Development.md`
- Concept page created (1):
  - [[concepts/secure-design-implementation]] (c-000066)
- Source index updated: [[sources/ICT2216-secure-software-development]] (Lecture 5 section + new concept row)
- Address counter updated: 67
- Manifest updated with 1 new address_map entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md (85 pages, SSD now 7)
- Domain: secure-software-development (existing domain, +1 concept page)
- Coverage: CIA-AAA translated to design decisions — Confidentiality (masking, symmetric/asymmetric crypto comparison [key count N(N−1)/2 vs N, speed, non-repudiation], hybrid TLS approach, X.509 v3 certificate structure, client-side hashing), Integrity (salted/iterated hashing, bcrypt/PBKDF2, password storage comparison table, referential integrity, resource locking), Availability (replication/primary-secondary, failover clusters, vertical vs horizontal scaling), Authentication (MFA, SSO, passwordless authentication [WhatsApp/SingPass/Apple/Google examples]), Authorisation (RBAC vs UBAC, Data Access Control Matrix, least privilege/separation of duties/performance), Accountability (who/what/where/when, never log sensitive data, log rotation/write-once), Secure Agile Development (security activities across 6 sprint phases: Modelling/Sprint Planning/Sprint/Dynamic Testing/Release/Operations), 4-step Secure Design Architecture (architecture→threats→controls→document/validate), Physical Topology zones (Internet/DMZ/Intranet/Dev, layered firewall pattern), Logical Topology, Human and Non-Human Actors, External Dependencies security techniques table (8 areas)

---

## 2026-05-25 | update | ICT2216 Lecture — Secure Software Requirements (transcript)

- Source: ICT2216 lecture transcript (SSDLC requirements process — CIA+AAA deep-dive)
- Updated: [[concepts/secure-software-requirements]] (dated 2026-05-25)
- Additions (3 targeted additions to avoid duplicating already-comprehensive content):
  1. **Data-in-processing protection technologies** — Homomorphic Encryption (compute on ciphertext; computationally expensive) and Differential Privacy (statistical noise to prevent individual identification; approximate output) added to Confidentiality section
  2. **Usability vs. security tension** — DBS 6-digit PIN worked example added to Authentication section (10⁶ vs 10⁴ combinations; auditable rationale requirement)
  3. **NIST SSDF stakeholder roles** — three-role table added (Business Owner: approve/resource/accept risk; Developer: implement/test; Security Professional: expertise/threat model/assurance)
- No new files created; all content absorbed into existing concept page
- No address counter change (update only)

---

## 2026-05-24 | ingest | INF1007 Ethics & Professional Conduct

- Source: `raw/INF1007 Ethics & Professional Conduct Notes.md`
- Source index: [[sources/INF1007-ethics-professional-conduct]] (c-000060)
- Concept pages created (4):
  - [[concepts/ethical-frameworks]] (c-000061)
  - [[concepts/behavioural-ethics-and-workplace]] (c-000062)
  - [[concepts/privacy-data-protection-and-ip]] (c-000063)
  - [[concepts/ai-ethics-and-digital-society]] (c-000064)
- Area page created: [[areas/it-ethics]] (c-000065)
- Address counter updated: 66
- Manifest updated with 6 new address_map entries + INF1007 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain: it-ethics (new domain #16, 4 concept pages)
- Coverage: ethical frameworks (Kantianism, Utilitarianism, Social Contract, Virtue Ethics, SCS/ACM codes), behavioural ethics (Milgram/obedience, Stanford Prison/roles, moral licensing, anonymity, cognitive biases), workplace ethics (conflict of interest, whistleblowing, CSR), privacy (PDPA, government surveillance), hacker ethics, malware taxonomy, IP law (copyright/patent/trademark/trade secret/fair use), AI ethics (bias/fairness, deepfakes, accountability/explainability, 6 AI ethics principles), digital divide, automation, outsourcing

---

## 2026-05-23 | ingest | INF2004 Embedded Systems Programming

- Source: `raw/INF2004 Embedded Systems Programming Notes.md`
- Source index: [[sources/INF2004-embedded-systems-programming]] (c-000053)
- Concept pages created (5):
  - [[concepts/embedded-systems-fundamentals]] (c-000054)
  - [[concepts/embedded-io-and-interrupts]] (c-000055)
  - [[concepts/embedded-timers-and-rtos]] (c-000056)
  - [[concepts/embedded-testing-and-optimisation]] (c-000057)
  - [[concepts/embedded-sensor-fusion-and-edge]] (c-000058)
- Area page created: [[areas/embedded-systems]] (c-000059)
- Address counter updated: 60
- Manifest updated with 7 new address_map entries + INF2004 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain: embedded-systems (new domain #15, 5 concept pages)
- Coverage: Raspberry Pi Pico (RP2040), real-time taxonomy, hardware taxonomy, build pipeline, startup code, V-model, case studies (Therac-25/Ariane 5/Toyota), interrupt handling (IVT/ISR/stack), polling vs interrupts, timers/PWM/WDT, RTOS (task lifecycle/context switch/scheduling), FSM, testing (traceability/unit/integration/system), optimisation (power/performance/memory), sensor fusion, edge computing, TinyML

---

## 2026-05-23 | ingest | INF2001 Introduction to Software Engineering

- Source: `raw/INF2001 Intro To Software Engineering Notes.md`
- Source index: [[sources/INF2001-intro-software-engineering]] (c-000048)
- Concept pages created (4):
  - [[concepts/sdlc-models]] (c-000049)
  - [[concepts/uml-modelling]] (c-000050)
  - [[concepts/software-project-management]] (c-000051)
  - [[concepts/software-configuration-management]] (c-000052)
- Note: Weeks 2 (RE), 8–9 (design/architecture/GoF), 10–11 (testing/refactoring) cross-reference existing concept pages rather than duplicating them
- Address counter updated: 53
- Manifest updated with 5 new address_map entries + INF2001 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md
- Domain: software-engineering (existing domain, +4 pages → 13 total)
- Cross-domain connections: SCM + CI/CD → DevOps/web-development; SDLC models → agile project management; UML → all SE concept pages

---

## 2026-05-23 | ingest | INF1002 Programming Fundamentals

- Source: `raw/INF1002 Programming Fundamentals Notes.md`
- Source index: [[sources/INF1002-programming-fundamentals]] (c-000041)
- Concept pages created (5):
  - [[concepts/python-fundamentals]] (c-000042)
  - [[concepts/python-data-structures-and-io]] (c-000043)
  - [[concepts/python-functions-and-modules]] (c-000044)
  - [[concepts/c-programming-fundamentals]] (c-000045)
  - [[concepts/c-pointers-memory-and-data-structures]] (c-000046)
- Area page created: [[areas/programming-fundamentals]] (c-000047)
- Address counter updated: 48
- Manifest updated with 7 new address_map entries + INF1002 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain added: programming-fundamentals (14th domain)
- Cross-domain connections: computer-science (linked lists, recursion), operating-systems (C + memory), computer-architecture (compilation pipeline)

---

## 2026-05-22 | ingest | Learnix CTk teardown + file refactor

- Source: ICT2114 ITP project (Learnix), `src/ui/auth_ui.py` + `src/ui/chat_ui.py`
- Learning page created: [[learning/customtkinter-after-teardown]] — root cause analysis and 3-layer fix for CTk 5.2.2 `invalid command name` / `application has been destroyed` Tcl errors; includes `sys.path` / `load_dotenv` path update notes for moved files
- Concept page created: [[concepts/customtkinter-window-lifecycle]] — reusable teardown pattern: `quit()` → `after_cancel` loop → `destroy()` + Tcl `bgerror` override; covers plain `CTk()` wrapper and `CTk` subclass variants
- Indexes updated: `wiki/index.md` (Concepts + Learning tables), `wiki/hot.md`

---

## 2026-05-22 | ingest | INF1006 Computer Networks

- Source: `raw/INF1006 Computer Networks Notes.md`
- Source index: [[sources/INF1006-computer-networks]] (c-000032)
- Concept pages created (7):
  - [[concepts/tcp-ip-network-model]] (c-000033)
  - [[concepts/data-link-layer-ethernet]] (c-000034)
  - [[concepts/ip-addressing]] (c-000035)
  - [[concepts/network-layer-protocols]] (c-000036)
  - [[concepts/transport-layer-tcp-udp]] (c-000037)
  - [[concepts/wireless-and-iot]] (c-000038)
  - [[concepts/application-layer-dhcp-dns]] (c-000039)
- Area page created: [[areas/computer-networks]] (c-000040)
- Address counter updated: 41
- Manifest updated with 9 new address_map entries + INF1006 sources entry
- Indexes updated: wiki/index.md, wiki/concepts/_index.md, wiki/areas/_index.md
- Domain added: computer-networks (13th domain)

---

## 2026-05-21 | autoresearch | Software Testing

- Rounds: 3
- Sources found: 2 (ISTQB CTFL v4.0, Fowler Practical Test Pyramid)
- Pages created: [[concepts/software-testing-fundamentals]], [[concepts/test-driven-development]], [[concepts/test-design-techniques]], [[sources/istqb-ctfl-v4]], [[sources/fowler-practical-test-pyramid]], [[research-software-testing]]
- Synthesis: [[research-software-testing]]
- Key finding: Software testing is a three-layer pyramid (unit/integration/E2E) governed by seven ISTQB principles; TDD drives design through Red-Green-Refactor; BDD extends this to business-readable Gherkin specs; EP and BVA systematically reduce test volume while preserving defect detection.

---

## 2026-05-21 | wiki-lint | Health Check

- Pages scanned: 117
- Issues found: 28
- Auto-fixed: 5 (examples/_index.md, concepts/_index.md count, sources/_index.md cross-ref, areas/agile-project-management.md created, areas/_index.md updated)
- Needs review: counter drift (address-counter.txt=3 vs max observed c-000031; requires WSL --rebuild), dead manifest entry (DragonScale Memory.md), ~18 address-map frontmatter mismatches, mass `status:` + `created:` backfill
- Report: [[meta/lint-report-2026-05-21]]

---

## 2026-05-19 | Ingest — PSM I Cheatsheet (github.com/ambaena/scrum-psm1-cheatsheet)

- **Source**: ambaena/scrum-psm1-cheatsheet — README.md + how-to-face.md
- **Pages created**:
  - [[learning/psm1-cheatsheet-study-notes]] — PSM I study notes: readiness check, Agile Manifesto (4 categories/12 principles), Scrum big picture diagram, invalid Sprint types (Hardening/Sprint 0/Release/Design), PB ordering factors (Value+Risk+Size+Dependencies), three progress monitoring methods (burn-down/burn-up/cumulative flow), Daily Scrum role clarity, Sprint Review undone-work rule, Retrospective full scope, SM startup actions, Scaled Scrum rules, IKIWISI/YAGNI, full definitions glossary (20 terms), two-computer open-book exam strategy, pre-exam quick-reference checklist
- **Pages updated**:
  - [[concepts/scrum-framework]] — added: Invalid Sprint Types section, Scaled Scrum section, Daily Scrum role clarity (SM ensures but doesn't conduct; PO doesn't attend)
  - [[learning/_index.md]] — added PSM I cheatsheet entry
  - [[index]] — learning page added
  - [[log]] — this entry
  - [[hot]] — session summary updated

---

## 2026-05-19 | Ingest — Scrum Master Exam (80 Questions, YouTube Transcript)

- **Source**: YouTube — "80 Scrum Master Exam Questions" (CSM / PSM / ACP prep)
- **Pages created**:
  - [[learning/scrum-master-exam-study-notes]] — 80-question study notes: waterfall vs Scrum, empiricism precision, formal inspection events, framework composition, servant leadership distinction, SM as management position, self-managing teams, PO continuous collaboration, PB rules, backlog refinement (no development), Sprint Backlog ownership (Developers only), DoD rules, cross-functionality, velocity not a metric, burn-down interpretation, estimation unit freedom, testing strategy freedom, retro vs review distinction, end-of-product handling, 40-row key rules table
- **Pages updated**:
  - [[learning/_index.md]] — added scrum-open-assessment-study-notes (previously missing), scrum-master-exam-study-notes, Scrum skill-map entry
  - [[concepts/_index.md]] — added Agile Project Management domain section (scrum-framework), added security-by-design-principles to Secure Software Dev section, updated counts (54→58 pages, 11→12 domains, 15→17 sources)
  - [[sources/_index.md]] — added Scrum Guide to sources table and By Domain section
  - [[index]] — learning page added
  - [[log]] — this entry
  - [[hot]] — session summary and Recent Changes updated

---

## 2026-05-19 | Ingest — Scrum Open Assessment Quiz Bank

- **Source**: `raw/scrum-open-quiz-questions.md` — classmarker.com Scrum Open Quiz, 29/30 (96.7%)
- **Pages created**:
  - [[learning/scrum-open-assessment-study-notes]] — 30-question study notes grouped by theme: 15 common traps/misconceptions, roles Q&A tables, events timebox table, artifacts+commitments table, full key-facts reference (25 facts)
- **Pages updated**:
  - [[sources/scrum-guide-2020]] — Learning section added
  - [[index]] — learning page added to Learning table
  - [[log]] — this entry
  - [[hot]] — session summary updated

---

## 2026-05-19 | Ingest — The 2020 Scrum Guide

- **Source**: 2020 Scrum Guide (Ken Schwaber & Jeff Sutherland) — CC BY-SA 4.0
- **Pages created**:
  - [[sources/scrum-guide-2020]] — source index: key facts, canonical reference metadata, related concept links
  - [[concepts/scrum-framework]] — complete Scrum framework: theory (empiricism + lean, three pillars), five values, three accountabilities (Developers/PO/SM), five events with timeboxes, three artifacts with commitments (Product Goal/Sprint Goal/Definition of Done), quick-reference tables
- **Pages updated**:
  - [[index]] — new source and concept added (domain: agile-project-management)
  - [[log]] — this entry
  - [[hot]] — session summary and domain summary updated

---

## 2026-05-19 | Ingest — ICT2216 Lecture 4: Secure Software Design

- **Source**: `raw/ICT2216 Lecture 4 Secure Software Development.md`
- **Pages created**:
  - [[concepts/security-by-design-principles]] — design flaws vs. bugs (McGraw 50% finding), Banana Token case study, all 10 OWASP Security by Design Principles with worked examples and code, Security Architecture (physical vs. logical)
- **Pages updated**:
  - [[sources/ICT2216-secure-software-development]] — added Lecture 4 section (Secure Software Design), Lab 3 to Labs table, new concept to Concept Pages table, updated frontmatter topics
  - [[index]] — added `security-by-design-principles` to Concepts table
  - [[log]] — this entry
  - [[hot]] — updated session summary

---

## 2026-05-16 | Ingest — ICT2216 Lab 3: Microsoft Threat Modeling Tool

- **Source**: Lab 03 PDF — Introduction to Microsoft Threat Modeling Tool
- **Pages created**:
  - [[resources/microsoft-threat-modeling-tool]] — tool reference: install, 4-step workflow (Build→Analyze→Triage→Report), DFD stencils, STRIDE auto-generation, threat status system
  - [[examples/ict2216-lab3-threat-modeling-tool]] — Lab 03 walkthrough: 5 sequential steps, sample diagram, STRIDE checklist for project deliverable
- **Pages updated** (indexes):
  - [[index]] — added to Examples and Resources tables
  - [[log]] — this entry

---

## 2026-05-15 | Ingest — ICT2216 Lecture 3: Extended Security Requirements + Threat Modeling

- **Source**: `raw/ICT2216 Lecture 3 Secure Software Development.md`
- **Summary**: [[sources/ICT2216-secure-software-development]]
- **Pages updated**:
  - [[concepts/secure-software-requirements]] — added: General App Security Requirements (session/error/config/code management), Operational Requirements (deployment/archiving/anti-piracy), Other Requirements (TOC/TOU, procurement, GDPR), Anti-Requirements technique, Abuse/Misuse Case Modelling with ATM worked example
- **Pages created**:
  - [[concepts/threat-modeling]] — threat agents (8 human types + non-human), 5 threat identification steps (trust boundaries/DFDs/entry-exit/privileged functions/mis-actors), mis-actor network categories (web/network/co-located), 5-step threat modeling process, attack trees, full Microsoft STRIDE breakdown with countermeasures and OWASP cross-reference
- **Pages updated** (indexes):
  - [[concepts/_index]] — 53→54 pages; Secure Software Dev 4→5; threat-modeling row added
  - [[index]] — threat-modeling row added to Concepts section
  - [[sources/ICT2216-secure-software-development]] — Lecture 3 topic entries added; threat-modeling concept cross-reference added
  - [[areas/secure-software-development]] — threat-modeling row added to Concept Pages table
- **Key insight**: Threat modeling answers the question requirements cannot — not *what* to protect, but *how* an attacker will actually try to break the system. STRIDE maps attacker goals to CIA+AAA violations, closing the loop between Part 1 (requirements) and Part 2 (adversarial analysis) of Lecture 3.

---

## 2026-05-15 | Gap Resolution — Areas, Synthesis, Learning, Skill Files

- **Trigger**: Comprehensive lint pass identified orphaned concept clusters, empty `areas/` folder, stale sub-indexes, missing synthesis pages, empty learning index, and vague ingest skill step 6.
- **Pages created**:
  - [[areas/computer-architecture]] (ICT1011 — Von Neumann, MSP430, I/O & memory)
  - [[areas/mobile-development]] (INF2007 + INF1009 — MVVM, Jetpack Compose, coroutines)
  - [[areas/hci]] (INF2002 — Norman, Fitts, Gestalt, needfinding, usability evaluation)
  - [[synthesis/maths-to-ml-bridge]] (6 sections: matrix multiply→forward pass, OLS/GD duality, SVD→PCA, Gaussian NB, Z-score, beyond-maths table)
  - [[synthesis/web-security-ssdlc-bridge]] (INF1005 attack → OWASP 2025 → ASVS chapter → STRIDE threat, full mapping table)
  - [[synthesis/ict1011-ict1012-architecture-bridge]] (hardware handover from fixed partitioning to TLB, demand paging, replacement, thrashing)
  - [[synthesis/rest-api-cross-stack]] (Retrofit→OkHttp→Express→res.json() full lifecycle, verb mapping table, coroutine integration)
  - [[learning/ict1012-operating-systems-study-notes]]
  - [[learning/inf2003-database-systems-study-notes]]
  - [[learning/inf1008-data-structures-algorithms-study-notes]]
  - [[learning/inf1005-web-systems-study-notes]]
- **Pages updated**:
  - [[synthesis/_index]] — 4 new synthesis rows added
  - [[learning/_index]] — rebuilt from empty placeholder; 5 study-notes rows
  - [[areas/_index]] — date updated
  - [[index]] — synthesis and learning sections updated; date updated to 2026-05-15
  - [[hot]] — session entry added; Active Threads updated with all resolved items
  - [[log]] — this entry
- **Skill files updated**:
  - `skills/wiki-ingest/SKILL.md` — Step 6 rewritten: now enumerates all 6 `_index.md` files to update per ingest (sources, concepts, synthesis, learning, areas domain page, areas _index)
  - `skills/wiki-lint/SKILL.md` — Added Check 8a (Stale sub-index files): count pages on disk vs rows in each `_index.md`; report missing pages by name
- **Key insight**: Sub-index files are the vault's navigation backbone. Every ingest must update them or pages become silently orphaned — visible in Obsidian but unreachable from the index layer.

---

## 2026-05-14 — Synthesis: Four Cross-Domain Pages Created

- Action: SYNTHESIS
- Scope: 4 new pages in `wiki/synthesis/`
- Pages created:
  - `maths-to-ml-bridge.md` (171 lines) — linear algebra → neural networks; SVD/eigenvalues → PCA; probability → Gaussian Naive Bayes; statistics → feature scaling; module dependency chain
  - `web-security-ssdlc-bridge.md` (159 lines) — INF1005 code-level attacks (SQLi, XSS, CSRF, brute force) mapped to OWASP 2025 categories, ASVS verification levels (V2/V4/V5), and STRIDE threats; code vs process perspectives compared
  - `ict1011-ict1012-architecture-bridge.md` (199 lines) — ICT1011 paging data structure → ICT1012 TLB/EAT, page table structures, demand paging, page replacement algorithms, thrashing; full dependency chain documented
  - `rest-api-cross-stack.md` (288 lines) — Express CRUD routes ↔ Retrofit annotations; full HTTP request lifecycle; coroutine integration; error handling divergence; MVVM layer mapping
- Updated: `wiki/gaps/_index.md` — 4 missing synthesis gaps marked resolved; 2 open questions closed
- Sources read: 15 concept pages

---

## 2026-05-14 — Lint: Gap Detection

- Action: LINT
- Scope: All 52 concept pages, 15 source pages, 4 synthesis pages, meta indexes
- Updated: `wiki/gaps/_index.md` — populated from empty template with full gap report
- Updated: `wiki/sources/_index.md` — was missing 7 of 15 sources; now complete with all 15 by domain
- Findings:
  - No broken wikilinks found (suspected backslash was terminal rendering artefact)
  - ~20 older concept pages use short-form links (`[[page-name]]`) vs. vault standard (`[[concepts/page-name|Label]]`) — functional but inconsistent
  - 2 stale index pages: concepts/_index.md (placeholder), sources/_index.md (now fixed)
  - 4 missing synthesis pages documented: maths→ML, web security×SSDLC, ICT1011→ICT1012, REST API cross-stack
  - 3 orphaned concept clusters: mathematics (10 pages), machine learning (6 pages), partial software-engineering (3 pages)
  - learning/ folder near-empty (only 1 page); no study notes for any of 15 modules
  - areas/ folder empty; no domain overview pages exist
  - 3 open questions documented in gaps index

---

## 2026-05-14 — Ingest: INF1005 Web Systems & Technologies

- Action: INGEST
- Source: `raw/INF1005 Web Systems & Technologies Notes.md` (2,111 lines, 21 chapters)
- Textbook: Connolly & Hoar, *Fundamentals of Web Development* (3rd Edition)
- Created: `wiki/sources/INF1005-web-systems-technologies.md`
  - 21-chapter map, concept page cross-references
- Created: `wiki/concepts/web-fundamentals.md` (Chapters 1–4)
  - Internet vs Web distinction (ARPANET 1969, Berners-Lee 1989)
  - Packet switching vs circuit switching
  - TCP/IP 4-layer model: Application/Transport/Internet/Link
  - TCP (reliable, ACKs) vs UDP (fast, no guarantee)
  - IPv4 (exhausted 2011) vs IPv6; PAT
  - DNS: TLD types (gTLD/ccTLD/IDN), ICANN; 10-step resolution process
  - URL components: protocol/domain/port/path/query/fragment; relative URL types
  - HTTP methods (GET/POST/PUT/DELETE/HEAD); idempotency and safety
  - HTTP status codes: 200/301/304/401/404/500
  - Browser rendering metrics: TTFB/FP/FCP/LCP/TTI/CLS
  - Web stacks: LAMP/MERN/WISA/JAM
  - Web 2.0 and client-server architecture
- Created: `wiki/concepts/html-and-css.md` (Chapters 5–9)
  - HTML5 document structure: DOCTYPE/html/head/body; charset; lang
  - Semantic philosophy: structure and meaning, not presentation
  - Text/inline elements: p, div, span, strong, em, a, img, br, hr
  - Link types: absolute, relative, anchor, mailto; relative path variants
  - HTML5 structural elements: header/nav/main/section/article/aside/figure/footer/details/address
  - Tables: caption/thead/tbody/tfoot, colspan/rowspan, border-collapse; tables for data only
  - Forms: action/method, GET vs POST comparison; full form controls table; input types
  - Accessibility: fieldset/legend, label for, scope on th
  - Input validation layers: HTML5 (hint) → JS (UX) → server-side (guaranteed)
  - CSS syntax, placement (inline/embedded/external)
  - Selectors: element/universal/class/ID/group; attribute selectors; pseudo-class/element; combinators
  - Cascade: inheritance, specificity (ID>class>element), location
  - Box model: content/padding/border/margin; collapsing margins; border-box
  - CSS custom properties (variables)
  - Colour: named/RGB/hex/RGBa/HSL
  - Float, positioning (static/relative/absolute/fixed/sticky)
  - Flexbox: one-axis; flex-direction/flex-wrap/justify-content/align-items
  - Grid: two-axis; fr units; repeat(); grid-column/row placement
  - Responsive design: viewport meta tag, mobile-first, min-width media queries, responsive images
  - CSS effects: transitions, keyframe animations, transforms, filters
  - Sass: variables, nesting, mixins
  - WCAG POUR principles; W3C validator; accessibility practices
- Created: `wiki/concepts/javascript-fundamentals.md` (Chapters 10–12)
  - History: Netscape 1996 → ECMAScript 1997 → ES6 2015
  - var (hoisted, function-scoped) vs let/const (block-scoped)
  - Primitive types: Boolean/Number/String/Null/Undefined/Symbol
  - Truthy/Falsy values
  - Operators: `===` strict equality preferred
  - Control flow: if/else if/else, switch, ternary, while/do-while/for/for-of
  - Arrays: push/pop/length/destructuring; functional methods (forEach/find/filter/map/reduce/sort)
  - Objects: literal notation, dot/bracket access, destructuring, spread
  - JSON: JSON.parse() / JSON.stringify()
  - Functions: declaration (hoisted), expression, arrow syntax, default/rest parameters
  - Scope: global/function/block; hoisting; modules
  - Closures: inner function retains enclosing scope after execution
  - ES6 classes: constructor, inheritance (extends, super), prototype basis
  - DOM: tree of nodes; getElementById/querySelector/querySelectorAll
  - DOM properties: innerHTML (XSS risk)/textContent/classList/style/value
  - DOM manipulation: createElement/appendChild/insertBefore/removeChild
  - Event handling: addEventListener, DOMContentLoaded; event object (preventDefault/stopPropagation/target)
  - Event propagation: capturing → target → bubbling
  - Event delegation pattern
  - Regular expressions: /pattern/flags, .test()
  - Asynchronous: Fetch API → Promises (.then/.catch) → async/await
  - CORS: `Access-Control-Allow-Origin` header
  - Web Storage: localStorage (persistent) / sessionStorage (session)
  - Geolocation API: getCurrentPosition()
  - ES6 modules: export/import syntax; `type="module"` script attribute
- Created: `wiki/concepts/server-side-web-development.md` (Chapters 13–18, 21)
  - PHP: `<?php … ?>` tags; `$` prefix; `.` concatenation; dynamic typing
  - PHP control flow: if/elseif/else, switch, while/for/foreach ($arr as $k => $v)
  - PHP include/require (include_once/require_once)
  - PHP functions: default params, pass-by-reference (&$var), type declarations (PHP 7+)
  - PHP indexed arrays ($arr[]) and associative arrays ($arr["key"]); multidimensional
  - PHP OOP: __construct, $this->, public/private/protected, extends, parent::__construct()
  - PHP Superglobals: $_GET/$_POST/$_REQUEST/$_SESSION/$_COOKIE/$_FILES/$_SERVER/$_ENV
  - Form security: htmlspecialchars() (XSS), filter_var() (validate/sanitise), POST vs GET
  - LAMP stack: Linux/Apache/MySQL/PHP; Ubuntu setup commands
  - PDO: connect with error handling, prepare → bindValue → execute → fetch → null to close
  - SQL CRUD: SELECT/INSERT/UPDATE/DELETE; JOIN (INNER JOIN ON); GROUP BY + aggregate; transactions
  - Table relationships: one-to-many, one-to-one, many-to-many (junction table)
  - NoSQL: Key-Value/Document/Column/Graph; use cases; MongoDB with Mongoose schema/model/find
  - Node.js: V8 engine, event-driven non-blocking, single event-loop thread
  - Blocking (PHP/Apache: thread per request) vs non-blocking (Node.js: event loop continues)
  - Basic Node HTTP server; Express: routing, static files, route params
  - REST API: GET/GET:id/POST/PUT/DELETE mapped to CRUD
  - WebSockets (Socket.io): io.on('connection'), socket.on/io.emit; bidirectional real-time
  - EJS view engine: `<%= %>` for output, `<% %>` for code
  - Serverless: DBaaS/PaaS/FaaS; auto-scaling, reduced complexity
  - Modern frameworks: React (JSX, components), Next.js (React + SSR + routing), Remix (nested routing, parallel server loads), ASP.NET Core (C#/Razor), Blazor (WebAssembly/SignalR)
- Created: `wiki/concepts/web-security-and-devops.md` (Chapters 19–20)
  - CIA Triad: Confidentiality/Integrity/Availability
  - STRIDE: Spoofing/Tampering/Repudiation/Information Disclosure/DoS/Elevation of Privilege
  - Auth factors: Knowledge/Ownership/Inherence; MFA
  - Auth strategies: HTTP Basic, Form+Session, JWT Bearer, OAuth
  - Cryptography: AES (symmetric), RSA (asymmetric); public/private key pair
  - Digital signatures: authenticity + integrity + non-repudiation
  - TLS/HTTPS: successor to SSL; CA certificates (DV/OV/EV)
  - Credential storage: plain text (BAD) → MD5 (BAD) → bcrypt password_hash() + salting (GOOD)
  - SQL injection: `' OR '1'='1` attack; defence = prepared statements
  - XSS (reflected vs stored): defence = htmlspecialchars() + CSP headers
  - CSRF: hidden token in every state-changing form
  - Brute force: rate limiting + lockout + CAPTCHA
  - DoS/DDoS: CDN + load balancers + DDoS protection
  - Security misconfiguration: out-of-date software, default credentials, verbose errors
  - CI/CD: CI (tests on commit), CD Delivery (auto-release-ready), CD Deployment (auto-deploy)
  - Testing: unit/integration/functional/non-functional/penetration (Selenium)
  - Infrastructure as Code: Ansible/Vagrant/Terraform
  - Hosting: shared → VPS → dedicated → collocated → cloud
  - Cloud models: IaaS (servers) / PaaS (platform) / SaaS (software)
  - Server virtualisation: hypervisor, Docker (containers), Kubernetes (orchestration)
  - DNS records: A/AAAA/CNAME/MX/NS/TXT/SPF/PTR
  - Apache: httpd.conf, .htaccess, VirtualHost, URL rewriting with RewriteEngine
  - Monolithic vs Microservices architecture
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

---

## 2026-05-13 — Ingest: ICT1012 Operating Systems

- Action: INGEST
- Source: `raw/ICT1012 Operating Systems Notes.md` (7,856 lines, compiled lecture notes, 10 chapters)
- Authors: Dr. David Sanan & Assoc. Prof. Shang-Wei Lin, Singapore Institute of Technology
- Textbook: A. Silberschatz, P. Galvin, G. Gagne, *Operating System Concepts* (10th Ed.), Wiley, 2019
- Created: `wiki/sources/ICT1012-operating-systems.md`
  - Chapter map (Chapters 1–10), concept page cross-references, explicit note on ICT1011→ICT1012 paging handover
- Created: `wiki/concepts/os-processes-and-threads.md` (Chapters 1–4)
  - OS roles: hardware abstraction, resource allocator, synchronisation, communication, protection
  - Kernel, bootstrap (ROM), DMA (one interrupt per block), interrupt cycle (fetch→execute→check interrupts)
  - System calls: `int 0x80` (old Linux) vs `syscall` (modern); parameter passing (registers/memory block/stack); POSIX/Win32 APIs
  - Privilege modes: CPL bit in CS register; privileged ISA instructions (LGDT, MOV CRx, HLT, VMRUN)
  - OS design approaches: layered, modular, microkernel (Mach), monolithic (UNIX), hybrid (Darwin/Windows NT)
  - Process: text/data/BSS/heap/stack layout; 5-state diagram; PCB fields; long-/medium-/short-term schedulers
  - Process creation: fork/exec/wait/exit; zombie vs orphan; process tree (PID 1 = systemd)
  - IPC: shared memory (mmap, shm_open, ftruncate, munmap); message passing (mq_open/send/receive/close/unlink); blocking/non-blocking; buffer capacity (zero/bounded/unbounded)
  - Threads: economy/resource sharing/scalability/responsiveness; user vs kernel threads; M:1, 1:1, M:M, two-level models; Pthreads API; TLS; thread safety; Linux clone()
- Created: `wiki/concepts/cpu-scheduling-and-synchronisation.md` (Chapters 5–6)
  - CPU/I/O burst cycle; I/O-bound vs CPU-bound; dispatcher latency; preemptive vs non-preemptive
  - Scheduling criteria table: utilisation/throughput/turnaround/waiting/response
  - FCFS (convoy effect, worked avg-wait example); SJF (optimal, exponential averaging formula); SRTF; Priority+ageing; RR (quantum, (n−1)q bound); Multilevel Queue; Multilevel Feedback Queue (3-queue example)
  - Real-Time: soft vs hard; Rate Monotonic (shorter period = higher priority, ~69% utilisation limit); algorithm comparison table
  - Linux CFS: vruntime, nice −20→+19 maps to priorities 100–139
  - Race condition: counter++ / counter-- non-atomic worked example
  - Critical section: 3 requirements (mutual exclusion, progress, bounded waiting)
  - Hardware sync: test_and_set (full C code + both cases explained); compare_and_swap (C code, fewer cache invalidations)
  - Mutex locks: spinlock vs sleep-based; acquire/release C code
  - Semaphores: binary vs counting; wait/signal with blocking queue; synchronisation pattern; bounded-buffer solution (3 semaphores)
  - Semaphore misuse table; deadlock via circular wait; starvation; priority inversion → priority-inheritance protocol
- Created: `wiki/concepts/file-systems.md` (Chapters 7–7b)
  - File attributes, 8 file operations, open-file table
  - Access methods: sequential (tape/logs), direct/random (databases), indexed (large files)
  - Directory structures: single-level → two-level → tree → acyclic-graph (reference count) → general graph
  - Unix permissions: rwx per owner/group/others; r=4/w=2/x=1; chmod/chown/chgrp
  - Layered FS diagram: logical FS → file-org module → basic FS → I/O control → hardware
  - On-disk structures: boot control block, volume control block/superblock, directory, FCB/inode
  - Directory implementation: linear list O(n), ordered O(log n), hash table O(1)
  - Allocation methods: contiguous (start+length, best read perf, external fragmentation), linked (FAT variant), indexed (inode with direct/single-indirect/double-indirect/triple-indirect)
  - Performance table: sequential → contiguous/linked; random → indexed; growing → linked/indexed
  - Fragmentation: external (compaction) vs internal (smaller blocks); 50% rule
  - Free-space: bit vector (fast contiguous, 32 MB overhead for 1 TB at 4 KB blocks) vs linked list
  - Buffer cache; synchronous vs asynchronous writes
- Created: `wiki/concepts/memory-and-virtual-memory.md` (Chapters 8–9)
  - Base/limit registers; memory protection check
  - Address binding stages (compile/load/execution); logical vs physical address distinction
  - MMU relocation register; dynamic loading; dynamic linking (stubs, shared libraries)
  - Contiguous allocation: first-fit/best-fit/worst-fit; 50% rule; external fragmentation (compaction) vs internal fragmentation
  - Paging fundamentals: frame/page/page table definitions; address translation formula; hardware registers vs PTBR vs TLB
  - TLB: EAT formula (EAT = hit×mem + (1−hit)×2×mem); 99% hit example (10.1 ns); ASIDs
  - Memory protection: valid-invalid bit, protection bits, shared pages
  - Page table structures: two-level hierarchical (32-bit: 10+10+12); hashed (clustered, >32-bit); inverted (one global table, indexed by frame number)
  - Swapping: increases multiprogramming; swap individual pages in modern OS
  - Virtual memory benefits: logical > physical; efficient sharing; faster startup
  - Virtual address space: stack↓/hole/heap↑/data/BSS/text
  - Demand paging: valid-invalid bit; page fault 6 steps (trap → check → free frame → disk read → update PTE → restart)
  - EAT with page faults: EAT = 200 + p×7,999,800; p < 1/400,000 for <10% degradation
  - Page replacement: dirty bit; FIFO (Belady's anomaly); OPT (benchmark); LRU (counter or doubly-linked list); second-chance/clock (ref bit); enhanced second-chance (0,0)/(0,1)/(1,0)/(1,1) priority table; LFU/MFU
  - Frame allocation: equal/proportional; global (higher throughput) vs local (consistent per-process); reapers
  - Thrashing: cause and locality model; working-set WSSᵢ(Δ); D=ΣWSSᵢ; policy (suspend process if D > total frames)
  - PFF: too-low → remove frames; too-high → add frames
  - Prepaging; TLB reach; page pinning (I/O interlock); programme structure impact on page faults
- Created: `wiki/concepts/deadlocks.md` (Chapter 10)
  - 4 necessary conditions: mutual exclusion, hold-and-wait, no preemption, circular wait
  - Resource allocation graph: request edges (P→R), assignment edges (R→P); cycle+single instance → deadlock; cycle+multiple instances → possible
  - Prevention: break one condition structurally; ordered resource acquisition (prevents circular wait, most practical)
  - Avoidance: safe state = safe sequence exists; Banker's algorithm (Available/Max/Allocation/Need matrices); Safety Algorithm O(m×n²); Resource-Request Algorithm (pretend allocate → run safety → grant or rollback); worked example with 5 processes/3 resource types
  - Detection: wait-for graph (single instance, O(n²) cycle detection); detection algorithm (multiple instances, similar to Safety Algorithm, O(m×n²)); invocation strategies (every request / periodic / CPU utilisation threshold)
  - Recovery: terminate all deadlocked processes or one at a time (selection criteria: priority/progress/resources/impact); resource preemption with rollback and starvation counter
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

---

## 2026-05-13 — Ingest: ICT1011 Computer Organisation and Architecture

- Action: INGEST
- Source: `raw/ICT1011 Computer Organisation Architecture Notes.md` (15,297 lines, OCR'd slide deck, 10 chapters)
- Authors: Steven Wong & Xin Lou, Singapore Institute of Technology, ©2024
- Created: `wiki/sources/ICT1011-computer-organisation-architecture.md`
  - Chapter map, concept page cross-references, key module themes
- Created: `wiki/concepts/computer-architecture-fundamentals.md`
  - Architecture vs organisation distinction
  - Von Neumann stored-program concept, Fetch–Decode–Execute cycle, Von Neumann bottleneck
  - Computer classes: supercomputer → mainframe → minicomputer → microcomputer → embedded/SoC
  - Three basic operations: Store / Transform / Transfer
  - Memory hierarchy: Registers (<1 ns) → Cache (8–35 ns, SRAM) → Main Memory (20–100 ns, DRAM) → Secondary (5–20 ms)
  - Clock (synchronous design) and Reset (PC→0)
  - MSP430: 16-bit RISC MCU, 27 instructions, 7 addressing modes, 16 registers
  - Register map: R0=PC, R1=SP (pre-decrement/post-increment), R2=SR/CG1 (N/Z/C/V + GIE + power bits), R3=CG2, R4–R15 GPR
  - SR flags: N (MSB=1), Z (result=0), C (unsigned overflow), V (signed overflow)
  - Memory map: 0x0000–0x01FF (8-bit peripherals), 0x2400 (RAM start), 0x4400 (Flash start), 0xFF80–0xFFFF (interrupt vectors)
  - Little-endian byte ordering
  - Instruction formats: Format I (double operand), Format II (single operand), Format III (10-bit signed jump, ±512 words)
  - 7 addressing modes: Register, Indexed, Indirect, Indirect Auto-increment, Symbolic, Absolute, Immediate
- Created: `wiki/concepts/assembly-programming-msp430.md`
  - 4-column assembly syntax (label / mnemonic / operands / comment)
  - Assembler directives: section (.text/.data/.bss/.sect/.usect), memory (.byte/.word/.string/.space), symbol (.equ/.set), linking (.global/.ref/.def/.end)
  - 2-pass assembly: Pass 1 → symbol table; Pass 2 → machine code
  - Executable instructions: MOV (no flags), ADD/ADDC/DADD/SUB/SUBC (arithmetic), AND/BIS/XOR/BIC (logical), RRC/RLC/RRA (rotation), CMP/BIT (comparison, flags only), JEQ/JNE/JC/JNC/JN/JGE/JL/JMP (control flow), PUSH/CALL/RETI (stack/subroutine)
  - Emulated instructions: NOP, CLR, INC, DEC, INV, TST, SETC/CLRC, EINT/DINT, RET, BR, POP
  - CALL mechanism: SP−2; Mem[SP]←PC+2; PC←target
  - RET mechanism: PC←Mem[SP]; SP+2 (= MOV @SP+,PC)
  - Parameter passing: (1) registers — fast/limited; (2) memory block — not re-entrant; (3) stack — general, supports recursion
  - Pass by value vs pass by reference
  - Stack frames for local variables: SUB #N,SP at entry; ADD #N,SP at exit; stack frame layout diagram
- Created: `wiki/concepts/io-and-memory-systems.md`
  - Parallel vs serial, simplex/half-duplex/full-duplex
  - Async serial format: start(Space=0) + 7/8 data bits LSB-first + optional parity + stop(Mark=1)
  - Baud rate = 1/T; data rate < baud rate due to framing overhead
  - RS-232: DTE↔DCE, inverted logic (Mark=−3 to −15 V, Space=+3 to +15 V)
  - Memory-mapped I/O (MSP430/ARM) vs isolated I/O (x86 IN/OUT instructions)
  - Polled I/O: busy-wait loop; CPU-inefficient
  - Interrupt-driven I/O: IRQ → push PC+SR → ISR → RETI; CPU free between events
  - Bluetooth: 2402–2480 MHz, 79 × 1 MHz channels, FHSS 1600 hops/s, TDD-TDMA, piconet (1 master + ≤7 active slaves), scatternet, BLE for IoT
  - HDD structure: platters/tracks/cylinders/sectors; access time = Ts + Tr (avg = 0.5/RPS) + Tt = N/(RPS×DT×DS)
  - RAID 0 (striping, performance), RAID 1 (mirroring, fault-tolerance), RAID 10 (stripe+mirror)
  - Bus: data (bits/transfer width), address (log₂ max memory), control (R/W, IRQ, clock, reset)
  - Synchronous bus (clocked, simple, inflexible) vs asynchronous bus (handshake, flexible, slow device bottleneck)
  - Memory performance: access time, cycle time (> access time), transfer rate = 1/cycle time
  - SRAM: cross-coupled inverter latch + 2 transistors; fast, low density, cache
  - DRAM: 1 transistor + 1 capacitor; needs periodic refresh; high density, main memory
  - ROM/Flash family: ROM (manufacture) → PROM (fuse burn) → EPROM (UV erase) → EEPROM (electrical byte erase) → Flash (electrical block erase, high density, SSDs/phones)
  - Memory management: uni-program vs multi-program; swapping (disk ↔ main memory, I/O cost)
  - Fixed partitioning: internal fragmentation; dynamic partitioning: external fragmentation → coalesce / compact
  - Paging: process → pages; memory → frames; page table maps page# → frame#; logical address = page# + offset → frame# + offset; eliminates external fragmentation; enables virtual memory; MMU performs translation
- Updated: `wiki/index.md` (1 new source row, 3 new concept rows)
- Updated: `wiki/hot.md` (new session summary, 10 new key facts, new domain summary, recent changes)
- Updated: `wiki/log.md` (this entry)

---

## 2026-05-12 — Synthesis: RE×Security and RE×HCI gaps filled

- Action: SYNTHESISE
- Trigger: user requested both open gaps be filled
- Created: `wiki/synthesis/re-elicitation-cia-aaa-security-requirements.md`
  - McCall's Integrity as the bridge: CIA+AAA unpacks what "resist unauthorised access" means in practice
  - RE lifecycle (Eliciting → Analysing → Specifying → Validating → Managing) mapped step-by-step onto SSDLC requirement phases
  - BCIC framework applied to security: "the system shall be secure" decomposed into atomic, verifiable statements
  - OSA taxonomy (Secure Functional / Functional Security / Non-Functional Security / Secure Development) mapped onto RE functional/non-functional split
  - iRTM extended with Threat column linking each security requirement back to its CIA-AAA pillar and attacker model risk
  - Mag7 quality attributes assessed against the specific challenges of security requirements (ambiguity of "encrypted", completeness of misuse cases, consistency tension between Availability and Confidentiality)
  - McCall's other features (Reliability, Correctness, Maintainability, Testability) mapped to adjacent security concerns
- Created: `wiki/synthesis/re-elicitation-hci-needfinding.md`
  - Method-by-method mapping table: RE interviews ↔ HCI semi-structured interviews; RE observation ↔ HCI direct/indirect observation; RE surveys ↔ HCI Likert/Semantic Differential; RE JAD workshops ↔ HCI focus groups; ethnography as unnamed-but-present in RE
  - Key divergence: RE produces formal SRS (complete, traceable, verifiable); HCI produces research artefacts (personas, HTA, insight reports)
  - Output connection pipeline: Needfinding → HTA/TDH → Use Cases → SRS requirements → iRTM
  - Concrete example tracing "Submit assignment" from HTA leaf to functional requirement to iRTM entry
  - Pain points → BCIC Interpret step → hidden requirements (with 3 worked examples)
  - Declarative/procedural knowledge distinction → differentiated non-functional usability requirements for novices vs experts
  - UCD "Specify requirements" phase identified as the handoff point from HCI to RE
- Updated: `wiki/synthesis/_index.md` (2 new rows + 2 domain sections), `wiki/index.md` (Synthesis table), `wiki/hot.md`, `wiki/log.md`

---

## 2026-05-12 — Example: Stock Prediction Neural Network ingested

- Action: INGEST
- Trigger: user opened project and requested wiki write-back
- Created: `wiki/examples/stock-prediction-neural-network.md`
  - Custom two-layer NumPy neural network with He init, adaptive LR, Monte Carlo uncertainty
  - SOLID + DIP architecture: interfaces in `core/interfaces.py`, concrete wiring at `ui/app.py`
  - 12-feature data pipeline from Yahoo Finance via yfinance
  - Composite 0–100 accuracy scoring (MAPE 50% + directional 30% + in-range 20%)
  - Band calibration from historical residuals targeting 75% in-range rate
  - Background threading pattern with message-queue UI bridge (Tkinter never freezes)
  - Key bugs: inconsistent data parsing (commit 00552e7) was root cause of occasional wrong predictions
- Updated: `wiki/index.md` (Examples table), `wiki/hot.md`

---

## 2026-05-12 — Ingest: INF2003 Database Systems

- Action: INGEST
- Source: `raw/INF2003 Database Systems Notes.md` (Lectures 1–10 + 2 Tutorials, Dr. Tong Rong + Zhang Wei, AY2025/26)
- Created: `wiki/sources/INF2003-database-systems.md`
- Created: 6 concept pages in `wiki/concepts/`
  - `relational-database-fundamentals` — DB/DBMS motivation, 3-level data abstraction (view/logical/physical), physical vs logical data independence, relational data model (relation/tuple/attribute/domain/NULL), key hierarchy (superkey→candidate→primary→foreign), ACID properties, 6 stages of DB design, integrity constraint types (domain/key/referential), DBMS architecture tiers
  - `relational-algebra-and-sql` — 6 fundamental RA operators (σ, π, ∪, −, ×, ρ) with notation and SQL equivalents; extended operators (∩, ⋈, outer joins ⟕⟖⟗, ÷, ←); query efficiency (push σ/π before joins); SQL DDL (CREATE/ALTER/DROP/data types); DML (INSERT/UPDATE/DELETE/SELECT with arithmetic and aliases); multi-table queries; explicit JOIN syntax; UNION/INTERSECT/EXCEPT with ALL variants; aggregate functions (SUM/COUNT/AVG/MIN/MAX) with NULL behaviour; GROUP BY and HAVING with evaluation order; subqueries (IN/EXISTS/ANY/ALL); NULL semantics; LIKE patterns; ORDER BY; CHECK constraints; 8 query optimisation tips
  - `database-normalisation` — anomalies (insertion/update/deletion/redundancy); functional dependencies (definition, notation, legal instance constraint); Armstrong's axioms (Reflexivity/Augmentation/Transitivity + Union/Decomposition/Pseudo-Transitivity); attribute closure algorithm (X⁺) with step-by-step example; uses of closure (key finding, FD derivability, equivalence); 1NF (atomic values); BCNF definition (every non-trivial FD must have a superkey LHS); BCNF violation detection; BCNF decomposition algorithm with two worked examples; lossless join property (BCNF guarantees ✓); dependency preservation (BCNF does not guarantee ✗); normalisation vs. performance trade-off
  - `er-diagrams` — ER model history and purpose; Chen notation (all symbols defined); entities and entity sets; 4 attribute types (key/composite/multivalued/derived) with notation; relationships and their own attributes; participation constraints (total/partial) with examples; cardinality (1:1/M:1/1:N/M:N); degree (unary/binary/ternary — avoid ternary); weak entities (partial key, total participation, ON DELETE CASCADE); ISA/subclass with overlap and covering constraints; ER→schema conversion rules for: entity sets, composite attributes (flatten), multivalued attributes (separate table), relationship sets, M:N relationships, participation constraints (merge), weak entities, subclasses (3 strategies: ER-style/OO/single-table-with-NULLs); design decision guidance (entity vs attribute, entity vs relationship, N-ary vs binary)
  - `database-indexing-transactions` — file organisation (heap/sorted/indexed); hash index (O(1) equality, no range queries); B+ tree structure (root/internal/leaf, linked leaves, 50% min occupancy, high fanout); B+ tree search O(log n) + range search via leaf list; B+ tree insert (locate→insert→split leaf→push to parent→recurse); B+ tree delete (locate→remove→borrow from sibling or merge→recurse); ACID deep-dive with responsibility table; schedules (serial/equivalent/serializable); interleaving anomalies (dirty read/non-repeatable read/lost update); SQL TCL (COMMIT/ROLLBACK/SAVEPOINT with worked example); lock granularity (DB/table/page/row/field); deadlock (prevention + timeout detection); optimistic 3-phase concurrency (read private copy→validate→write); recovery (write-ahead log, checkpoints, redo/undo, off-site backup)
  - `nosql-and-data-warehousing` — RDBMS limitations (centralisation, schema rigidity, geo-distribution); 4 NoSQL categories (KV/document/columnar/graph) with examples; Redis (O(1) operations, in-memory, rich types); MongoDB CRUD (insert/find/update/remove with JS examples), RDBMS→MongoDB mapping table; columnar storage vs row storage, Cassandra/HBase, Facebook MySQL→Cassandra benchmark; Neo4j (node+edge+property model), RDBMS→graph mapping table; when to use NoSQL; SQL→NoSQL migration (3 strategies); data warehouse definition, ETL phases, star schema (fact table + dimension tables, benefits/drawbacks), snowflake schema (normalised dimensions, complex queries); OLAP cube (slice/dice/drill-down/roll-up/pivot with SQL examples); OLTP vs OLAP full comparison table; blockchain as append-only hash-chained ledger (tamper-resistance mechanism, Proof-of-Work, limitations as a database)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`
- Status: Complete

---

## 2026-05-12 — Synthesis: ICT2112 × INF2007 Knowledge Gaps Resolved

- Action: SYNTHESISE
- Trigger: two gaps identified during ICT2112 ingest (same session)
- Created: `wiki/synthesis/dip-hilt-dependency-injection.md`
  - Maps ICT2112 Dependency Inversion Principle → INF2007 Hilt framework, annotation by annotation
  - Covers: @Inject constructor = DIP declaration; @Binds = binding abstraction to concrete; @Provides = IoC container provision; @Singleton = managed singleton vs GoF Singleton; Hilt component hierarchy = scope/lifetime management; testability argument (fake injection vs untestable direct instantiation); design smell diagnosis table
- Created: `wiki/synthesis/data-mapper-repository-room-retrofit.md`
  - Maps ICT2112 data source patterns (Active Record, TDG, Data Mapper) → Android Room + Retrofit stack
  - Active Record = Room @Entity used directly as domain model (acceptable for simple CRUD)
  - Table Data Gateway = Room @Dao (method-by-method mapping shown)
  - Remote Data Gateway = Retrofit annotated interface
  - Data Mapper = Repository class + mapper extension functions (Entity↔Domain, DTO↔Domain)
  - Facade = Repository hiding both DAO and Retrofit behind one interface
  - Includes: full stack diagram with patterns named at each layer, when-to-use table (Active Record vs Data Mapper), leaky abstraction smell, quality attribute mapping
- Updated: `wiki/synthesis/_index.md`, `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`
- Status: Complete

---

## 2026-05-12 — Ingest: ICT2112 Software Design

- Action: INGEST
- Source: `raw/ICT2112 Software Design Notes.md` (Topics 1–8, Asst. Prof. Alex Q. Chen, AY2025/26)
- Created: `wiki/sources/ICT2112-software-design.md`
- Created: 2 concept pages in `wiki/concepts/`
  - `software-design-process` — Software design pipeline (Architecture → Detailed → Construction), four roles of architecture, quality attributes (Microsoft model: 10 attributes across user-facing/run-time/design), architecture drivers, coupling scale (Content → Data), cohesion scale (Informational → Coincidental), ATAM (9-step process, sensitivity points, tradeoffs, risks), design smells (Rigidity, Fragility, Immobility, Viscosity, Needless Complexity, Needless Repetition, Opacity), construction design (flow-based: pseudocode/flowcharts; table-based: decision tables, state transition tables)
  - `software-architecture-patterns` — Layered 3-Tier architecture (benefits, rules), domain layer patterns (Transaction Script / Table Module / Domain Model), data source patterns (Table Data Gateway / Row Data Gateway / Active Record / Data Mapper with comparison table), presentation patterns (MVC / MVP / MVVM with testability comparison), SOA/Microservices patterns (Gateway / Service Registry / Circuit Breaker three-state model / Adapter), end-to-end design pipeline, Library Books Management System case study
- Updated: `wiki/concepts/solid-and-design-patterns.md`
  - Added Builder and Prototype (creational) with C# examples
  - Added all 7 structural patterns: Adapter, Decorator, Facade, Composite, Proxy, Bridge, Flyweight (with C# examples for Adapter, Decorator, Facade)
  - Added all 11 behavioural patterns: Observer, Strategy, Command, Iterator, Template Method, State, Chain of Responsibility, Mediator, Memento, Visitor (with C# examples for Observer, Strategy, Iterator, Template Method)
  - Expanded Pattern Selection Guide to all 23 GoF patterns
  - Updated course tag from INF1009 → ICT2112; updated See Also links
- Updated: `wiki/index.md` (new source row, 2 new concept rows), `wiki/hot.md`, `wiki/log.md`
- Status: Complete

---

## 2026-05-11 — Ingest: INF2008 Machine Learning

- Action: INGEST
- Source: `raw/INF2008 Machine Learning Notes.md` (Lectures L00–L12, Donny Soh)
- Created: `wiki/sources/INF2008-machine-learning.md`
- Created: 6 concept pages in `wiki/concepts/`
  - `ml-foundations` — AI definitions, four narrow-AI perspectives, expert systems vs ML, supervised/unsupervised/reinforcement learning, CRISP-DM phases mapped to production components, business understanding framework (problem/decision/metric/intervention/value), MoonHub churn and JuneBank loan examples
  - `ml-data-understanding` — 7 DU stages: data generation process, schema, data types (cardinal continuous/discrete vs categorical nominal/ordinal), completeness, sanity checks (plausibility, consistency, leakage), representativeness (class imbalance), granularity and aggregation
  - `ml-model-training-evaluation` — baseline models (majority class, mean, default DT), train-validate-test split, stratification (M&Ms analogy), k-fold cross-validation, confusion matrix, Type I/II errors, accuracy/balanced accuracy/precision/recall/specificity/F1, bias-variance trade-off (4 cases, corrective actions), learning curves
  - `decision-trees-and-ensembles` — Gini impurity formula and worked example, entropy, greedy tree construction, stopping criteria (max_depth, min_samples_split, min_samples_leaf), bagging/bootstrap sampling, Random Forests (OOB estimation: ~36.8% OOB, feature subsampling), AdaBoost, Gradient Boosting (loss gradients, iterative residual fitting, early stopping), stacking; comparison table
  - `neural-networks-linear-models` — label encoding vs OHE (advantages, dangers, when to use), simple and multiple linear regression, RMSE, 4-step gradient descent loop (forward pass, loss, backprop, update), vectorised multiple regression, neuron (z→σ→a), hidden activations (ReLU/Leaky ReLU/tanh), output activations (identity/sigmoid/softmax), backpropagation chain rule, cross-entropy loss, worked backprop example
  - `clustering-and-dimensionality-reduction` — distance measures (L1/L2/L∞), k-NN, K-means objective function (why the mean minimises it), K-means algorithm, elbow method, silhouette score, K-means++, DBSCAN (core/border/noise points, ε/MinPts effects), K-means vs DBSCAN comparison, PCA (5 steps: standardise, covariance matrix, eigendecomposition, project, interpret), t-SNE (Gaussian→t-distribution probabilities, KL divergence gradient descent, perplexity), PCA vs t-SNE comparison
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Ingest: ICT2216 Lectures 1 & 2

- Action: INGEST
- Sources: `raw/ICT2216 Lecture 1 Secure Software Development.md`, `raw/ICT2216 Lecture 2 Secure Software Development.md`
- Created: `wiki/concepts/owasp-top-10.md` — OWASP Top 10 (2025): all 10 categories with scenarios, code examples, case studies (Instagram, SolarWinds, Bybit, Log4Shell), mitigations, and vulnerability category taxonomy
- Created: `wiki/concepts/vulnerability-tracking-frameworks.md` — CVE, NVD, CAPEC, MITRE ATT&CK, CVSS; BSIMM-16 (goals, SSF domains, 2026 trends), OpenSAMM (maturity levels 0–3), Microsoft SDL; comparison table
- Updated: `wiki/concepts/secure-software-requirements.md` — added IEEE 729 definition, OSA taxonomy (4 requirement types), full SSDLC requirement process (feasibility → gathering → specification → validation), detailed CIA-AAA content (SingHealth case study, DDoS mitigations, SLA terminology, NIST 800-63 password guidelines), PCI SSF and NIST SSDF frameworks
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — added Secure Software Concepts section, linked new concept pages
- Updated: `wiki/index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Ingest: INF1004 Mathematics 2

- Action: INGEST
- Source: `raw/INF1004 Mathematics 2 Notes.md`
- Created: `wiki/sources/INF1004-mathematics-2.md`
- Created: 5 concept pages in `wiki/concepts/`
  - `descriptive-statistics` — types of data, population vs sample, measures of location (mean/median/mode), spread (variance, CV), relative standing (quartiles, boxplot)
  - `probability-theory` — classical/empirical/subjective probability, complement/union/intersection rules, conditional probability, independence vs mutual exclusivity, Bayes' theorem, law of total probability
  - `probability-distributions` — discrete RV (expected value, variance), binomial distribution, continuous distributions (uniform, normal, standard normal), combining independent RVs, sampling distribution, Central Limit Theorem (CLT), sampling methods
  - `linear-algebra-matrices` — matrix types and operations, determinants (2×2 and 3×3), inverse matrix (2×2 formula and Gauss-Jordan), SLE (Ax = b), vectors (magnitude, dot product, orthogonality), parametric line equations, 2D geometric transformations, linear regression (least squares)
  - `eigenvalues-and-svd` — characteristic equation, eigenvalue/eigenvector computation, diagonalisation ($A = PDP^{-1}$, $A^n = PD^nP^{-1}$), SVD ($A = U\Sigma V^T$), SVD computation steps, applications (image compression, PCA, recommender systems, pseudoinverse)
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 2 Example Page

- Action: INGEST
- Source: ICT2216 Lab 2 — SecurityRAT example page (lab PDF content confirmed by user)
- Created: `wiki/examples/ict2216-lab2-securityrat.md` — full compose files, step-by-step, CRLF fix, gotchas table, container architecture
- Updated: `wiki/examples/_index.md`, `wiki/index.md` — Lab 2 example entry added
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — Lab 2 example linked
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 1 Ingest

- Action: INGEST
- Source: ICT2216 Secure Software Development — Lab 1 (Docker + Docker Compose)
- Created: `wiki/concepts/docker-compose.md` — compose file structure, networking, volumes, all four services (Nginx, MySQL, Git, Selenium)
- Created: `wiki/examples/ict2216-lab1-docker-compose.md` — full compose files, build steps, port map, notes
- Updated: `wiki/sources/ICT2216-secure-software-development.md` — added Lab 1, docker-compose concept, example page
- Updated: `wiki/examples/_index.md` — first entry added
- Updated: `wiki/index.md` — Concepts and Examples tables
- Status: Complete

---

## 2026-05-11 — ICT2216 Lab 2 Ingest

- Action: INGEST
- Source: ICT2216 Secure Software Development — Lab 2 (SecurityRAT + Secure Requirements)
- Created: `wiki/sources/ICT2216-secure-software-development.md`
- Created: `wiki/concepts/secure-software-requirements.md` — CIA + AAA pillars, risk identification, SANS SWAT / OWASP ASVS mapping
- Created: `wiki/resources/securityrat.md` — Docker setup, CRLF fix, default creds, container architecture
- Created: `wiki/learning/docker-windows-crlf.md` — Windows CRLF breaks Linux container scripts; Git Bash path translation gotcha
- Updated: `wiki/index.md` — Sources, Concepts, Learning, Resources tables
- Status: Complete

---

## 2026-05-11 — Ingest: INF1003 Mathematics 1

- Action: INGEST
- Source: `raw/INF1003 Mathematics 1 Notes.md`
- Created: `wiki/sources/INF1003-mathematics-1.md`
- Created: 5 concept pages in `wiki/concepts/`
  - `discrete-mathematics-foundations` — sequences (AP/GP/recurrence), number theory, modular arithmetic, GCD/LCM, Euclidean algorithm, RSA
  - `combinatorics` — product/sum/division rules, permutations, combinations, pigeonhole principle
  - `propositional-logic` — connectives, truth tables, tautologies, De Morgan's laws, logical equivalences
  - `predicate-logic-and-proofs` — quantifiers (∀/∃), negation rules, rules of inference (modus ponens/tollens etc.), proof methods
  - `sets-functions-relations` — set operations/identities, power sets, function types (injective/surjective/bijective), relation properties, equivalence relations, partial orders
- Updated: `wiki/index.md`, `wiki/sources/_index.md`, `raw/.manifest.json`
- Status: Complete

---

## 2026-05-11 — Structure Update & Writing Style

- Action: CONFIGURE
- Graph view: 13 colour groups applied to `graph.json` — each wiki folder now maps to its vault colour (blue = concepts/synthesis, green = sources, purple = examples/entities, gold = areas, teal = goals/learning, orange = resources, red = gaps, steel-blue = meta, grey = raw/templates)
- vault-colors.css: Added `wiki/examples` → purple nav colour
- CLAUDE.md: Added Writing Style section (British English, grammatically correct prose)
- CLAUDE.md: Updated Vault Structure diagram to include all subfolders
- wiki/examples/: Created folder with `_index.md` — for real-world examples and lab sessions
- wiki/index.md: Added Examples table section
- Status: Complete

---

## 2026-05-11 — First Ingest: 5 Course Notes

- Action: INGEST
- Sources: ICT2113, INF1008, INF1009, INF2007, INF2002
- Created: 5 source index pages in wiki/sources/
- Created: 12 concept pages in wiki/concepts/
  - requirements-engineering, lightweight-rcm (ICT2113)
  - algorithm-complexity, data-structures-fundamentals, sorting-and-searching, graph-algorithms (INF1008)
  - oop-four-pillars, solid-and-design-patterns (INF1009)
  - android-architecture, kotlin-coroutines (INF2007)
  - hci-fundamentals, needfinding-and-task-analysis (INF2002)
- Updated: wiki/index.md (Sources + Concepts tables), wiki/hot.md, raw/.manifest.json
- Status: Complete — vault ready for study/review use

---

## 2026-05-11 — Vault Scaffold

- Action: SCAFFOLD
- Mode: D (Personal / Second Brain) + E (Research)
- Purpose: Personal knowledge base for everything learned and to learn, linking knowledge, filling gaps
- Created: wiki/ structure with 9 domain folders + 4 meta files
- Created: Mode D+E templates (goal, learning, synthesis, gap)
- Applied: vault-colors.css visual customization
- Status: Ready for first ingest
