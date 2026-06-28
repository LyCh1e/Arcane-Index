---
type: meta
status: established
title: "Hot Cache"
updated: 2026-06-28
tags: [meta, hot-cache]
---

# Recent Context

## Last Updated

2026-06-28. **Session: ingest — LeetCode 1946 (Maximum Element After Decreasing and Rearranging).** 1 source, 1 new concept page, 1 example created.

Problem introduces the **Sort + Greedy Constraint Propagation** paradigm — new concept page [[concepts/greedy-patterns]] created.

**Core pattern**: `arr.sort()` → `arr[0] = 1` → `arr[i] = min(arr[i], arr[i-1] + 1)` → `return arr[-1]`. Three decisions: (1) sort to make the optimal rearrangement trivial; (2) set the hard boundary at index 0; (3) propagate the adjacency cap left-to-right. Each step is O(1); only the sort is O(n log n).

**Why greedy is correct here**: at each position, `arr[i-1] + 1` is the maximum permitted value. Taking anything less can only reduce all future maxima — there is no future benefit to under-using the budget. Taking more violates the constraint. Therefore the greedy choice is uniquely optimal.

**Greedy vs DP heuristic**: if sorting the input and making one left-to-right pass solves the problem, it is almost certainly greedy. DP is needed when past choices interact with future options in non-trivial ways.

**Concept page structure**: Pattern 1 (Sort + Constraint Propagation) fully documented; Patterns 2 (Interval Greedy) and 3 (Two-Pass Greedy) left as placeholders.

**Key pages**: [[concepts/greedy-patterns]] (new), [[examples/leetcode-max-element-rearranging-python]] (new — traces for all three examples, step-by-step justification).

---

2026-06-28. **Session: ingest — LeetCode 1441 (Build an Array With Stack Operations).** 1 source, 1 new concept page, 1 example created.

Problem introduces the **greedy stream simulation** paradigm — distinct enough from array manipulation to warrant its own concept page: [[concepts/simulation-patterns]].

**Core pattern**: iterate stream 1→n with a `target_set`. If the current number is in the set → Push + remove. If not → Push + Pop (mandatory discard, not a skip). Break when `target_set` is empty. Three sub-insights: (1) convert target list to set before the loop for O(1) membership; (2) `not target_set` is a one-liner early-exit guard that works because matched elements are removed; (3) Push is always mandatory — Pop is optional immediately after.

**Practical bound**: the loop always exits at `number == target[-1]` (target is strictly increasing), so `n` is irrelevant in practice.

**Concept page structure**: Pattern 1 fully documented; Patterns 2 (state-machine) and 3 (grid simulation) left as placeholders to fill from future problems.

**Key pages**: [[concepts/simulation-patterns]] (new), [[examples/leetcode-stack-ops-python]] (new — full traces for all three examples).

---

2026-06-28. **Session: ingest — LeetCode 1365 & 448 (Count Smaller / Find Disappeared).** 1 source, 1 example created; [[concepts/array-manipulation-patterns]] extended with 2 more patterns (now 8 total).

**Pattern 7 — Prefix Sum on Frequency Array**: when values are bounded to a fixed range R (hint: `0 <= nums[i] <= 100`), build a freq array of size R+1, then accumulate prefix sums so `freq[i]` = count of values ≤ i. "How many values < x?" is `freq[x-1]` in O(1). Complexity O(n + R) time, O(R) space — effectively O(n)/O(1) when R is constant. Beats sort (O(n log n)) and brute force (O(n²)).

**Pattern 8 — Set Difference**: `set(range(1, n+1)) - set(nums)` finds all values in the expected universe absent from the array in O(n) time. Python's `-` operator on sets is `A.difference(B)` — elements in A not in B. Also useful: `&` (intersection), `|` (union), `^` (symmetric difference).

**LeetCode 645 note**: appeared again in the same session; already ingested as c-000078/079 — skipped without re-processing.

**Key pages**: [[examples/leetcode-count-missing-python]] (new — prefix sum trace + set difference walkthrough).

---

2026-06-28. **Session: ingest — LeetCode 645 (Set Mismatch).** 1 source, 1 example created; [[concepts/array-manipulation-patterns]] extended with 2 new patterns.

**Pattern 4 — Frequency Count**: build a `dict` or `Counter` of occurrences in one pass, then scan for values with count ≠ 1 in a second pass. `dict.get(key, 0)` avoids `KeyError` on absent keys; `Counter` returns 0 for missing keys by default. Applies to duplicates, missing values, majority elements, anagram detection.

**Pattern 5 — Math Sum Identity**: when the expected sum is known (`n*(n+1)//2` for 1→n), `sum(nums) - sum(set(nums))` gives the duplicate and `n*(n+1)//2 - sum(set(nums))` gives the missing number. O(1) extra space conceptually, though `set()` is O(n); true O(1) needs XOR or index-negation.

**Key pages**: [[examples/leetcode-set-mismatch-python]] (new — three annotated approaches with traces), [[concepts/array-manipulation-patterns]] (updated — now covers 5 patterns + reference pattern 6).

---

2026-06-28. **Session: ingest — LeetCode Array Basics (Python, 3 problems).** 1 source, 1 concept, 1 example created.

Three Easy-tier LeetCode array problems ingested as named patterns rather than one-off solutions.

**Pattern 1 — Concatenation** (LeetCode 1929): `nums + nums` in Python; language-agnostic equivalent pre-allocates `[0] * (2 * n)` and dual-writes each index `i` and `i + n`. O(n) time, O(1) extra space.

**Pattern 2 — Split-Midpoint Interleaving** (LeetCode 1470): a single array of 2n elements encodes two logical arrays side by side. Access them with `nums[i]` (first half) and `nums[i + n]` (second half). Interleave with a loop or nested list comprehension. Key idiom: `[val for i in range(n) for val in (nums[i], nums[i + n])]`. O(n) time, O(1) extra.

**Pattern 3 — Linear Scan with Running Counter** (LeetCode 485): track `current` streak, reset to 0 on mismatch, update `max_count` **inside** the match branch only (the maximum only grows when `current` grows). O(n) time, O(1) space. Extends naturally to the k-flip variant (LeetCode 1004 — sliding window).

**Key pages**: [[concepts/array-manipulation-patterns]] (new — pattern catalogue with Python idioms), [[examples/leetcode-array-basics-python]] (new — annotated solutions with traces).

---

## Last Updated

2026-06-25. **Session: project — ICT2216 TrialGuard CI/CD hardening + React gif fix.**

**CodeQL restored**: Added back the `codeql-analysis` job (JOB 4) removed in commit d49f989 (GHAS unavailable on personal private repos). Uses `github/codeql-action/init@v4` + `analyze@v4` with `permissions: security-events: write, actions: read, contents: read`. ESLint SARIF now uploads to both Code Scanning (`upload-sarif`) and as a downloadable artifact.

**CodeQL v3 → v4**: `github/codeql-action` v3 deprecated December 2026; all three steps (init, analyze, upload-sarif) bumped to v4.

**Node 20 deprecation pattern**: Pin to specific minor versions bundling Node 24 — `actions/checkout@v4.3.0`, `actions/setup-python@v5.6.0`, `actions/upload-artifact@v4.6.2`. Leave `actions/setup-node` as `@v4` floating — linter auto-bumped to `@v4.4.2` (non-existent release).

**Linter trap**: `replace_all` on `@v4` when `@v4.3.0` is already in the file matches the `v4` inside and doubles it to `@v4.3.0.3.0`. Always replace full version strings, not just major tags.

**React image sizing**: Drop the fixed-aspect-ratio `PhotoSlot` wrapper; use `<img style={{ width: '100%', display: 'block' }} />` to let the gif's natural height determine the container.

**Key pages**: [[learning/github-actions-version-deprecations]] (new), [[concepts/github-actions-cicd]] (updated — Action Version Management section).

---

2026-06-26. **Session: autoresearch — Kubernetes.** 2 rounds, 8 searches, 4 sources fetched, 3 wiki pages created.

**What Kubernetes is**: A desired-state container orchestration system. You declare what you want; the control plane reconciles actual cluster state to match. Originally Google's internal Borg/Omega system, open-sourced 2014, donated to CNCF.

**Architecture**: Control plane (kube-apiserver → etcd → kube-scheduler + kube-controller-manager) + worker nodes (kubelet + kube-proxy + container runtime). etcd is the single source of truth — HA production clusters require a 3- or 5-node etcd cluster with backups.

**Workload types**: Deployment (stateless, rolling updates, rollbacks) · StatefulSet (stateful — databases, Kafka; stable ordinal pod names, per-pod PVCs) · DaemonSet (one pod per node — CNI plugins, log collectors) · Job (one-off batch) · CronJob (scheduled batch). **Anti-pattern**: using a Deployment for a database — pods are rescheduled to different nodes and lose storage.

**Networking**: Services give pods a stable virtual IP + DNS. Service types: ClusterIP (internal only) / NodePort (external via static port) / LoadBalancer (cloud-provisioned LB). **Ingress ≠ Service** — it is a separate API object requiring a deployed Ingress controller (NGINX, Traefik, Envoy); without a controller, Ingress resources are inert.

**Critical security finding**: Kubernetes Secrets are base64-encoded, NOT encrypted, in etcd by default. Any user with etcd read access or Kubernetes `get` on a Secret reads the plaintext. Production clusters must enable `EncryptionConfiguration` with AES-GCM. RBAC: prefer `Role + RoleBinding` (namespace-scoped) over `ClusterRoleBinding`.

**Helm 4.0 (November 2025)**: Introduced server-side apply — delegates manifest merge to the Kubernetes API server, resolving field-ownership conflicts when multiple tools (ArgoCD, kubectl, Helm) manage the same resources.

**Kubernetes vs Docker Compose**: Compose is single-host (~50 MB), for local dev. Kubernetes is multi-node (~2 GB control plane), for production HA. They are complementary, not competing.

**Managed services**: GKE (fastest version adoption, ~2 weeks) / EKS (AWS-native) / AKS (Azure/Microsoft). All support K8s 1.33 as of Oct 2025.

**Key pages**: [[concepts/kubernetes]] (new — full reference), [[synthesis/research-kubernetes]] (new).

---

2026-06-25. **Session: autoresearch — Data Mapping.** 2 rounds, 5 searches, 4 sources fetched, 4 wiki pages created.

**What data mapping is**: The discipline of defining how data fields in one system correspond to fields in another — covering field correspondence, transformation rules, and validation logic. Applies to ETL pipelines, data migrations, API integrations, and compliance data inventories (GDPR Article 30 "records of processing").

**Key distinction — matching ≠ mapping**: Schema *matching* answers "are these two fields semantically equivalent?" (an algorithmic/ML question). Schema *mapping* defines how to transform one to the other (an engineering question). Conflating them is a common cause of integration bugs.

**Techniques taxonomy** (Atlan, 10 types): manual · spreadsheet-based · ETL tools · code-based (SQL/Python) · metadata-driven · schema matching + profiling · rule-based (conditional logic) · template-based · semantic · visualisation. Separately: 4 automation tiers — manual → semi-automated → automated → AI/semantic.

**Transformation types**: format conversion · type casting · aggregation · calculation/derivation · conditional logic · lookup enrichment · normalisation · splitting/merging.

**Process (12 steps distilled to 9)**: define scope → identify source/target schemas → profile source data → document mapping rules → apply transformations → test on subset → iterate → deploy with monitoring → maintain documentation as schemas evolve.

**ETL vs ELT**: in ETL, transformation runs in the pipeline (Talend, Informatica); in ELT, raw data loads first, then transforms in-place via SQL models (dbt). The mapping specification exists in both; it is just expressed differently.

**Object mapping in software**: DTO pattern (Fowler, *PoEAA*) separates domain objects from transport representations. Libraries: AutoMapper (.NET), MapStruct (Java). Related to, but distinct from, the Data Mapper OOP pattern — see [[synthesis/data-mapper-repository-room-retrofit]].

**Market consolidation (2025–2026)**: Salesforce acquired Informatica (May 2025); Fivetran and dbt merged (Oct 2025). Enterprise integration converging toward metadata-intelligence + cloud ELT.

**Key pages**: [[concepts/data-mapping]] (new), [[synthesis/research-data-mapping]] (new).

---

2026-06-25. **Session: ingest — ICT2216 Lecture 6 (Secure Software Implementation).** Created 1 new concept page; updated 2 existing; created 1 source page.

**Core insight — SSL/TLS Incompatibility Table**: Standard security measures do not compose the way developers assume. SSL/TLS encrypts the channel but not against phishing (the attacker *is* the server). Salted hashing is correct at-rest but forces cleartext transmission — a phishing server receives the plaintext before any hashing occurs. 2FA/OTP does not protect against real-time phishing proxies. Each measure protects against a specific attack vector only.

**Mitigations**: HSTS prevents MitM SSL stripping (forces HTTPS even on first redirect). PFS (via ECDHE cipher suites) prevents retrospective decryption of captured sessions. SRP (RFC 5054, 2007) addresses all three — phishing, MitM, and PFS — via zero-knowledge mutual authentication, but was not widely adopted due to a bootstrapping problem.

**Security Theatre**: Always verify that a control addresses its stated threat model rather than merely appearing to. A padlock ≠ phishing protection.

**FIDO/Passkeys**: FIDO2/WebAuthn is cryptographically sound (private key never leaves the device; origin-bound — phishing sites cannot trigger the registered key). Real-world UX is fragmented: cross-platform metadata doesn't exist in the spec, platforms steer users toward ecosystem lock-in, some browsers not supported on some services. Current verdict: elegantly designed, not yet "usable security".

**Passwordless OTP constraints (ICT2216 standard)**: 3-minute expiry; max 3 failed attempts per code; only the most recently issued code is valid (previous codes invalidated on new issue; used codes immediately invalidated).

**DevSecOps**: DevOps (Patrick Debois, 2009) extended with security embedded throughout the CI/CD pipeline — not as a final gate. CI vs Continuous Delivery (manual prod trigger) vs Continuous Deployment (fully automated) distinction now in [[concepts/github-actions-cicd]].

**Key pages**: [[concepts/fido-passkeys-passwordless]] (new — FIDO, passkeys, OTP design), [[concepts/secure-design-implementation]] (updated — SSL/TLS analysis section), [[concepts/github-actions-cicd]] (updated — DevSecOps intro).

---

2026-06-23. **Session: project — ICT2216 Lab 8 ESLint SAST, TrialGuard integration.** Updated [[examples/ict2216-lab8-static-code-analysis]] with real implementation learnings.

**GitHub Code Scanning limitation**: `github/codeql-action/upload-sarif` and CodeQL require Code Scanning, only available on public repos or private repos with GitHub Advanced Security (paid, orgs only). Workaround for personal private repos: replace `upload-sarif` with `actions/upload-artifact` — SARIF file becomes a downloadable artifact. CodeQL removed entirely.

**Permissions gotcha**: Any explicit `permissions:` block on a GitHub Actions job drops all unspecified permissions to `none`. Without `contents: read`, `actions/checkout` fails with `fatal: repository not found`. Always pair `security-events: write` with `contents: read`.

**Vite + React ESLint config**: No Babel parser needed — use `parserOptions.ecmaFeatures.jsx: true` with the default parser. Plugins: `eslint-plugin-react` + `eslint-plugin-security` + `eslint-plugin-no-unsanitized`. Skip `eslint-plugin-security-node` for browser apps. Disable `react/prop-types` and `react/no-unescaped-entities` (cosmetic noise). Security scan found a real `detect-possible-timing-attacks` warning in `Signup.jsx`.

**Node 20 deprecated on GitHub runners**: Updated all `setup-node` steps to `node-version: "24"`.

**Key page**: [[examples/ict2216-lab8-static-code-analysis]].

---

## Last Updated (previous)

2026-06-23. **Session: ingest — ICT2216 Lab 9 (SonarQube).** Created 1 wiki example page + instructions_lab9.md.

**Topic summary**: Lab 9 sets up SonarQube as a self-hosted SAST platform via Docker Compose, runs a local scan using the sonar-scanner-cli Docker image, and integrates results into GitHub Actions via the `sonarsource/sonarqube-scan-action`.

**Docker Compose setup**: Two services — `sonarqube:latest` (port 9000/9092) + `postgres:latest`. Four named volumes for persistence. Default login `admin/admin`. Start: `docker-compose -f sonarqube-compose.yml up`.

**Local scan flow**: Create local project in UI → Use global settings → Locally → Generate project token → Run `sonarsource/sonar-scanner-cli` Docker image with `-Dsonar.projectKey`, `-Dsonar.sources`, `-Dsonar.host.url`, `-Dsonar.login`. View results at `http://localhost:9000/dashboard?id=<project-key>`. Dashboard shows Quality Gate, Security/Reliability/Maintainability issue counts, Coverage %, Duplications %, Security Hotspots.

**GitHub Actions**: SonarQube must be publicly reachable (not localhost). Store `SONAR_TOKEN` and `SONAR_HOST_URL` as GitHub Secrets. Use `sonarsource/sonarqube-scan-action@master` — results pushed to SonarQube dashboard on every push/PR to `master`.

**OOM fix**: SonarQube needs >2 GB RAM in Docker — add `--memory=3g` to the `docker run` command if it crashes.

**Key comparison**: SonarQube (Lab 9) does deep semantic SAST across 25+ languages with a dashboard; ESLint (Lab 8) is lighter linting + security plugins outputting SARIF to GitHub Code Scanning. Use both in a pipeline for complementary coverage.

**Key pages**: [[examples/ict2216-lab9-sonarqube]] (lab walkthrough).

---

## Last Updated (previous)

2026-06-23. **Session: ingest — ICT2216 Lab 8 (Static Code Analysis).** Created 1 wiki example page + instructions_lab8.md.

**Topic summary**: Lab 8 covers SAST using ESLint with security plugins, outputting SARIF reports for GitHub Code Scanning, and GitHub CodeQL for deeper semantic analysis.

**ESLint setup**: Modern Flat Config (`eslint.config.mjs`) — array of config objects with direct plugin imports. Install `eslint@latest` + `@microsoft/eslint-formatter-sarif`. Run `npx eslint --init` to scaffold config. Run locally: `npx eslint . --format=@microsoft/eslint-formatter-sarif --output-file=reports/eslint-results.sarif`.

**GitHub Actions** (`cda-eslint.yml`): Single job — checkout → cache → npm install → ESLint with SARIF → `github/codeql-action/upload-sarif@v3`. Results appear under **Security → Code Scanning**. Use `|| true` on the ESLint run so a non-zero exit doesn't block the upload step.

**Three security plugins**: (1) `eslint-plugin-security` — detects `eval()`, ReDoS, insecure `Buffer()`; (2) `eslint-plugin-security-node` — Node.js-specific (insecure HTTP headers, improper user input); (3) `eslint-plugin-no-unsanitized` — prevents XSS via improper DOM manipulation. All added to `eslint.config.mjs` plugins/rules blocks.

**CodeQL** (`codeql.yml`): GitHub's semantic analysis engine. Uses `github/codeql-action/init` + `analyze` steps with a language matrix. Requires `permissions: security-events: write`.

**Lab note**: ESLint ≠ full SAST. Dedicated tools: Semgrep (lightweight), SonarQube (next lab — Lab 9). Other SARIF tools: Flake8 (Python), Checkstyle/PMD (Java), SonarCloud (multi-language).

**Key pages**: [[examples/ict2216-lab8-static-code-analysis]] (lab walkthrough).

---

## Last Updated (previous)

2026-06-23. **Session: ingest — ICT2216 Lab 7 (GitHub Actions with Automated Testing).** Created 1 wiki example page + instructions_lab7.md.

**Topic summary**: Lab 7 integrates automated unit and integration/UI testing into GitHub Actions. Two test layers: (1) **Mocha + Chai** unit tests on `getCurrentTimestamp()` — run locally with `npx mocha tests/test.js` or `npm test`; (2) **Selenium + ChromeDriver** integration tests that open a real (headless) Chrome browser and assert DOM content.

**Selenium setup via Docker**: `docker run -d -p 4444:4444 --name selenium-server --network host selenium/standalone-chrome`. The `SeleniumTest.mjs` script takes a `local` vs `github` CLI arg to switch between localhost and container network URLs.

**GitHub Actions workflow** (`selenium-tests.yml`): Two-job pipeline — `build` (npm install → tar artifact → upload) and `test` (`needs: build`, uses `node:20` container with `--network-alias=testserver`, plus a `selenium/standalone-chrome` service sidecar reachable at `http://selenium:4444/wd/hub`). Artifact hand-off via `upload-artifact` / `download-artifact`.

**Key design**: `SeleniumTest.mjs` switches URLs based on CLI arg so the same test file works locally and in CI. The test waits for `#timestamp` element with a 5 s timeout before asserting ISO 8601 format.

**Key pages**: [[examples/ict2216-lab7-automated-testing]] (lab walkthrough).

---

## Last Updated (previous)

2026-06-23. **Session: ingest — ICT2216 Lab 6 (OWASP Dependency Check).** Created 2 wiki pages: 1 resource, 1 example.

**Topic summary**: OWASP Dependency-Check is an SCA tool that scans third-party dependencies for publicly disclosed vulnerabilities using CPE → NVD matching. Generates CVE-linked HTML reports. Addresses OWASP Proactive Control C2 (Leverage Security Frameworks and Libraries).

**Local scan via Docker**: Pull `owasp/dependency-check`, mount project as `/src`, output dir as `/report`, and NVD cache as `/usr/share/dependency-check/data`. Run `--scan /src --format HTML --out /report`. Report saved to `odc-reports/`.

**GitHub Actions integration**: Use `dependency-check/Dependency-Check_Action@main` action, then `actions/upload-artifact@v4` to expose the HTML report as a downloadable artifact on the Actions run page. Triggers on `push` and `pull_request`.

**Alternative tools**: Dependabot (GitHub-native, auto-raises PRs for outdated packages, checks registries not CVE DB) and Renovate (similar, more scheduling options). Configured via `.github/dependabot.yml`. Neither replaces OWASP DC for CVE scanning — they complement it.

**Key pages**: [[resources/owasp-dependency-check]] (tool reference), [[examples/ict2216-lab6-owasp-dependency-check]] (lab walkthrough).

---

## Last Updated (previous)

2026-06-23. **Session: autoresearch — AI Workflows.** Created 5 new wiki pages: 2 concepts, 2 sources, 1 synthesis.

**Topic summary**: AI workflows are intelligent, end-to-end systems using LLMs, tools, memory, and retrieval to execute tasks with minimal human supervision. The key architectural distinction is workflow (predefined code paths) vs. agent (LLM dynamically controls its own process) — start with workflows, only escalate to agents when task steps cannot be predicted.

**Anthropic's 5 core patterns** (*Building Effective Agents*, Dec 2024): (1) **Prompt Chaining** — sequential LLM calls, each processing the prior output; (2) **Routing** — classifier dispatches input to a specialised handler or model tier; (3) **Parallelisation** — concurrent calls via sectioning (independent subtasks) or voting (multiple attempts); (4) **Orchestrator–Workers** — central LLM dynamically decomposes and delegates, then synthesises; (5) **Evaluator–Optimiser** — generator + evaluator loop until quality criteria are met.

**Foundational building block**: the augmented LLM — a model + retrieval (RAG) + tools (MCP servers) + memory. All five patterns compose from this unit.

**Tool taxonomy** (three distinct categories — wrong category = wrong tool): Agent orchestration (LangGraph, LlamaIndex, CrewAI, AutoGen), Durable execution (Temporal, Prefect), Data/batch pipelines (Airflow, Dagster). Production consensus: Dagster/Airflow for data side, Temporal for application durability, LangGraph agent loop inside the service.

**AI vs. RPA**: Complementary, not competing. RPA = "hands" (deterministic execution on structured data). AI workflows = "brain" (reasoning on unstructured inputs). Combined: 2–3× automation coverage. AI agents market growing 46.3% CAGR toward $52.6B by 2030.

**Observability** (LLM-native required): Smallest unit = span (one LLM call/tool call/retrieval/handoff). Tools: LangSmith (deepest LangGraph integration), Helicone (proxy, zero SDK changes), Langfuse (open-source).

**Cross-domain**: MCP servers are the standardised tool layer beneath orchestration frameworks; RAG is the retrieval component of every augmented LLM; context compression applies when workflow history overflows the context window.

**Key pages**: [[concepts/ai-workflows]] (patterns, components, RPA comparison), [[concepts/ai-workflow-orchestration]] (tool taxonomy, observability, decision guide), [[synthesis/research-ai-workflows]].

---

2026-06-23. **Session: autoresearch — Retrieval-Augmented Generation (RAG).** Created 6 new wiki pages: 2 concepts, 1 entity, 2 sources, 1 synthesis.

**Topic summary**: RAG is the dominant pattern for knowledge-intensive LLM applications, solving knowledge cutoff, hallucination, and private-data access in one framework. It is a four-stage pipeline — **Index** (chunk → embed → store), **Retrieve** (embed query → ANN search → top-k), **Augment** (inject into prompt), **Generate** — built on top of a vector database.

**Four generations of architecture**: Naive RAG (fixed pipeline) → Advanced RAG (HyDE, re-ranking, corrective, self-RAG, FLARE, parent-child chunking) → Modular/Adaptive RAG (swappable components, query routing) → Agentic RAG (LLM controls retrieval in a tool loop, Document Agents per source) and GraphRAG (Microsoft, knowledge graph + Leiden community detection + hierarchical summaries).

**Chunking**: Recursive chunking is the safe default. Semantic chunking is corpus-dependent — outperforms in clinical document studies but underperforms in general benchmarks. Always evaluate on your own data.

**Retrieval**: Hybrid search (dense semantic + sparse BM25) + cross-encoder re-ranking is the production default. Dense alone misses exact terms; sparse alone misses paraphrasing.

**Evaluation (RAGAS)**: Faithfulness (claims supported by context), Context Precision (retrieved relevance), Context Recall (coverage), Answer Relevancy. Target faithfulness ≥ 0.8 in production.

**GraphRAG**: 72–83% comprehensiveness improvement over vector RAG on holistic/relational queries. LazyGraphRAG (June 2025) cuts indexing cost to 0.1% of original. Best for large corpora with thematic/relationship questions.

**RAG vs fine-tuning**: Complementary, not competing. Fine-tune for behaviour/style; use RAG for current facts. Hybrid is the 2025 consensus.

**Cross-domain connections**: MCP Resources primitive = protocol-level RAG; context compression techniques apply to retrieved chunks that overflow the context window.

**Key pages**: [[concepts/retrieval-augmented-generation]] (pipeline + evaluation), [[concepts/rag-architectures]] (full taxonomy), [[entities/graphrag-microsoft]], [[synthesis/research-rag]] (synthesis).

---

2026-06-23. **Session: autoresearch — MCP Servers (Model Context Protocol).** Created 7 new wiki pages: 2 concepts, 1 entity, 3 sources, 1 synthesis.

**Topic summary**: The Model Context Protocol (MCP) is an open standard launched by Anthropic on 25 November 2024 to standardise how LLMs connect to external tools, data sources, and systems. Within 12 months it became the industry-wide default, adopted by OpenAI, Google DeepMind, and Microsoft.

**Architecture**: Three-layer — Host (LLM application), Client (session manager, lives inside the Host), Server (exposes tools/resources/prompts). Communication via JSON-RPC 2.0. One Host runs many Clients in parallel. Transport options: Stdio (local), HTTP+SSE (legacy remote), Streamable HTTP (modern remote, March 2025).

**Three primitives**: Tools (callable functions the LLM invokes), Resources (static data context), Prompts (interaction templates).

**Ecosystem**: MCP Registry launched September 2025; ~2,000 entries by November 2025, 500+ public servers by April 2026. Official reference servers split in May 2025 (active: filesystem/git/fetch/memory; archived: GitHub/Postgres/Slack/Brave). Recommended starter set: Filesystem, GitHub, Context7, Playwright, Sequential Thinking.

**November 2025 spec** (biggest update since launch): async Tasks primitive (call-now, fetch-later with state machine), CIMD-based OAuth (DNS-anchored client identity, replaces Dynamic Client Registration), Machine-to-Machine OAuth for headless agents, Cross App Access (XAA) for enterprise IdP controls, composable extensions framework.

**Governance**: Donated to the Agentic AI Foundation (AAIF) under the Linux Foundation, December 2025. Co-founders: Anthropic, OpenAI, Block. Supporting members: AWS, Google, Microsoft, Cloudflare, GitHub, Bloomberg.

**Security risks**: Prompt injection (model reads tool responses without provenance checks), tool poisoning (adversarial directives in tool descriptions — CVE-2025-54136), rug pull attacks (server mutates tool definitions post-install), supply chain vulnerabilities (CVE-2025-6514 in mcp-remote, 437,000+ downloads), over-privileged access (blast radius scales with agent credentials). The Nov 2025 spec mitigates some via CIMD and client security requirements.

**MCP vs function calling**: MCP is provider-agnostic and reusable across clients; function calling is simpler for lightweight single-app integrations. Production architectures use both.

**Key pages**: [[concepts/mcp-model-context-protocol]] (master reference), [[concepts/mcp-security]] (vulnerability taxonomy), [[entities/agentic-ai-foundation-aaif]], [[synthesis/research-mcp-servers]] (synthesis).

---

## Last Updated (previous)

2026-06-21. **Session: autoresearch — Context Compression of Chats with Large Language Models.** Created 8 new wiki pages: 3 concepts, 1 entity, 4 sources, 1 synthesis.

**Topic summary**: Context compression addresses the token-limit problem in LLM conversations and agentic tasks. Five technique families exist, operating at different layers of the stack:

1. **Dialogue memory summarisation** (LangChain, LlamaIndex, Anthropic compaction, Mem0): periodically compress chat history into a summary. Mem0's selective memory formation achieves 80–90% token cost reduction and 26% response quality improvement vs basic chat history.
2. **Prompt compression / token-level** (LLMLingua-2, Evaluator Heads): remove low-information tokens from the input before sending to the target LLM. LLMLingua-2 (Microsoft, ACL 2024) achieves 1.6–2.9× end-to-end latency reduction at 2–5× compression ratios, task-agnostically.
3. **KV cache compression** (PyramidKV, ChunkKV, KVQuant): reduce memory consumed by the key-value tensors already inside the model. KV cache can consume up to 70% of GPU memory; three strategies: selective eviction, quantisation, layer sharing.
4. **Soft / latent compression** (Gist Tokens, AutoCompressor, 500xCompressor): encode prompts into continuous summary vectors rather than discrete tokens. Up to 26× compression and 40% FLOPs reduction; requires fine-tuning.
5. **Retrieval-based / just-in-time** (vector stores, structured notes): store information externally, retrieve only what is relevant per inference step. Most scalable approach for long-running agents.

**Key counterintuitive finding**: higher compression ratio ≠ better quality. In the Factory.ai evaluation (2025), OpenAI's 99.3%-compression method scored 0.35 points *lower* than Factory's 98.6%-compression anchored iterative method on production software engineering tasks. Preservation of structure matters more than minimising tokens.

**Open problem**: artifact tracking (knowing which files were modified in an agentic session) scores only 2.19–2.45 / 5 across all current methods. Summaries alone cannot reliably preserve this; structured external logs are needed.

**Key pages**: [[concepts/context-compression-llm]] (master taxonomy), [[concepts/prompt-compression]], [[concepts/kv-cache-compression]], [[entities/llmlingua]], [[synthesis/research-context-compression-llm]] (synthesis).

---

2026-06-19. **Session: project — ICT2216 TrialGuard, CD pipeline added to GitHub Actions CI/CD workflow.** Updated [[concepts/github-actions-cicd]] and created 1 learning page.

- **CD deploy job pattern**: Added a fourth job `deploy` to `.github/workflows/ci-cd.yml` that runs only on `push` to `main` (not PRs), gated on all CI and security scan jobs passing. Uses `if: github.event_name == 'push' && github.ref == 'refs/heads/main'` to suppress deployment on PR runs.
- **Step sequence mirrors deploy.sh/deploy.ps1**: Write PEM key from secret → test SSH → `git archive --format=tar HEAD` → SCP to EC2 → extract → `docker compose build --no-cache frontend-build` + volume purge + `docker compose up -d` → health check via `curl -sk https://localhost/api/health` → always-cleanup of PEM.
- **GitHub secrets via CLI**: `gh secret set EC2_HOST --body "student21@18.223.111.152"` and `gh secret set EC2_SSH_KEY --body "$(cat *.pem)"`. Secrets are encrypted with libsodium, masked in logs, inaccessible to fork PRs, and write-only after creation — safe to store SSH keys here.
- **Bug: SSH "Permanently added" warning contaminates stdout** ([[learning/ssh-stdout-known-hosts-warning]]): With `-o StrictHostKeyChecking=no` and `2>&1`, the SSH informational message `Warning: Permanently added '<host>' (ED25519) to the list of known hosts.` merges into the captured variable, breaking `[[ "$result" == "ok" ]]`. Fix: add `-o LogLevel=ERROR` to all SSH/SCP calls and drop `2>&1` from variable capture.
- **Why `git archive` not `git clone`**: Private repo cannot be cloned on EC2 without credentials. `git archive` bundles committed files from HEAD only (no `.git`, no history) and is pushed via SCP.

Created: [[learning/ssh-stdout-known-hosts-warning]]. Updated: [[concepts/github-actions-cicd]], [[wiki/index.md]], [[wiki/log.md]].

## Last Updated (previous)

2026-06-12. **Session: autoresearch — Blockchain Technology (3 rounds, 9 searches, 8 pages).** Full autoresearch loop executed. Key live findings (2025–2026 data):

- **Security**: Crypto theft >$3.4B in 2025; single Bybit hack = $1.5B (44 % of annual total); DPRK stole ≥$2.02B; DeFi losses improving (median incident down 75 % since 2022) but Q1 2026 shows spike ($482M, 44 incidents); attack vector shifted from smart contract bugs → private key / social engineering.
- **Layer 2**: Arbitrum ($15B+ TVL, 500+ apps), Optimism ($10B+), ZK rollups ($6.27B total TVL); Polygon PoS 7,000+ TPS; cross-rollup interoperability emerging 2025–2026; ZK STARKs are additionally quantum-resistant.
- **CBDCs**: 146 countries (98 % GDP) exploring; only 3 launched; China e-CNY at 16.7 trillion RMB / 3.4B transactions; mBridge volume 2,500× growth; US GENIUS Act (July 2025) bans Fed retail CBDC; EU decision pending 2026.
- **Post-Quantum**: NIST FIPS 204 (Dilithium / ML-DSA) is the signature standard; 2026–2030 is the critical hybrid migration window; Dilithium signatures are 40–70× larger than ECDSA — significant L1 block-size impact; Polkadot published Dilithium migration roadmap.
- **RWA tokenisation**: ~$32B on-chain (excl. stablecoins, May 2026); >$300B incl. stablecoins; Standard Chartered projects $30T by 2034.

Created: [[sources/hacken-smart-contract-vulnerabilities-2025]], [[sources/atlantic-council-cbdc-tracker-2026]], [[sources/chainalysis-crypto-crime-report-2025]], [[sources/layer2-scaling-comparison-2025]], [[entities/satoshi-nakamoto]], [[entities/vitalik-buterin]], [[entities/nick-szabo]], [[synthesis/research-blockchain-technology]].

2026-06-12. **Session: research — Blockchain Technology.** Created 1 concept page [[concepts/blockchain-technology]] (c-000067). Domain `blockchain` added as the 17th domain. The page is a deep-dive reference covering the full blockchain stack:

- **Block anatomy**: header fields (prev hash, Merkle root, nonce, target, timestamp), double-SHA-256 hashing, block size
- **Cryptographic foundations**: SHA-256 avalanche/pre-image/collision resistance; ECDSA over `secp256k1` — private key → public key (EC point multiplication) → address (RIPEMD-160 ∘ SHA-256); Merkle trees (O(log n) inclusion proofs; SPV nodes)
- **Transaction lifecycle**: sign → broadcast → mempool → miner selection → candidate block → consensus → append → confirmations
- **Consensus mechanisms**: PoW (nonce mining loop, difficulty adjustment, 51% attack economics), PoS (Ethereum Gasper/Casper FFG, RANDAO beacon, slashing), DPoS (EOS 21 delegates), PBFT (BFT, deterministic finality, O(n²) messages), PoA (permissioned chains)
- **UTXO vs Account model**: Bitcoin UTXO (parallel validation, privacy) vs Ethereum account (persistent balance, nonce, simpler smart contracts)
- **Smart contracts**: EVM bytecode/ABI, gas pricing, Solidity escrow example, re-entrancy (DAO hack), integer overflow, front-running, oracle manipulation
- **Security threats**: 51%/34% attack, eclipse attack, long-range PoS attack, Sybil, BGP hijacking; cryptographic quantum risk (Grover's on SHA-256 → safe; Shor's on ECDSA → vulnerable; post-quantum: CRYSTALS-Dilithium/Falcon); privacy (chain analysis, CoinJoin, zk-SNARKs, stealth addresses)
- **Scalability trilemma**: decentralisation × security × scalability; Optimistic Rollups (7-day fraud proof window) vs ZK Rollups (instant cryptographic finality); DPoS trade-off
- **Implementations**: Bitcoin (7 TPS, 21M cap, UTXO, Script), Ethereum (12s slots, EVM, PoS, rollup-native), Hyperledger Fabric (permissioned, Raft, X.509 MSP, channels)
- **10+ Mermaid diagrams**: block linkage, Merkle tree, sequence diagram, PoW flowchart, PoS attestation, quadrant chart, threat mindmap, full lifecycle, network topology, EVM deployment pipeline

## Last Updated (previous)

2026-06-08. **Session: ingest — ICT2216 Lecture 5 transcript (Secure Software Design Part 2 & Secure Agile Development).** No new files created. Three targeted additions to [[concepts/secure-design-implementation]], which was already comprehensive from the 2026-05-30 ingest. Additions extracted from the live lecture transcript:

- **Deactivate vs delete** (referential integrity): Rather than deleting a customer record (which orphans orders/order-detail rows), set an `active` flag. The row persists; the application treats the account as non-existent externally. Preserves referential integrity, audit history, and allows recovery.
- **Admin account — installation-wizard model**: Never pre-seed hard-coded admin credentials in the database. Prompt for the initial admin username and password on first application launch (same pattern as Windows/Linux OS installation). Credentials are hashed and stored by the setup routine; no default password is ever shipped or committed.
- **NFR for hash iteration count**: The bcrypt/PBKDF2 cost factor/iteration count must be specified as a non-functional security requirement with a hardware-justified rationale (e.g., "cost factor 12 → authentication < 300 ms on target hardware → attacker cost > 100 ms per guess"). An arbitrary iteration count is not acceptable; too high causes UX latency, too low is insecure.

2026-05-31. **Session: project — ICT2216 TrialGuard, Phases 9–12 completion and EC2 deployment.** Created 1 example page and 4 learning pages. Key outputs:

- **Phase 12 Could Have completions**: (1) Flask `GET /api/health` endpoint + `healthcheck` blocks for `flask` and `pii_vault` in docker-compose; nginx now waits on `flask: service_healthy`. (2) `GET /api/admin/compliance-report` — admin-only, returns aggregated user/trial/participant/consent/audit-log summary, every export writes an audit event. (3) `db-backup` service: `mysql:8.0` container loops every 24h calling `sh /backup.sh`, dumps both MySQL DBs to `db_backups` named volume, rotates to 7 most recent.
- **EC2 Deployment** ([[examples/ict2216-project-deployment-phases-9-12]]): Private repo cannot be cloned on EC2 — used `git archive --format=tar HEAD -o file.tar` + `scp` + `tar xf` instead. `.env` and `nginx/certs/` are gitignored and pushed separately via SCP. PEM key permissions must be fixed on Windows first: `icacls key.pem /inheritance:r /grant:r "%USERNAME%:F"`. All 7 containers healthy: flask, pii_vault, mysql, vault_db, mongodb, nginx, db-backup. HTTPS 200 OK, HTTP→HTTPS 301 verified, all security headers confirmed.
- **Bug: Docker bind-mount dir created as root** ([[learning/docker-volume-host-dir-created-as-root]]): If the host-side path of a bind mount doesn't exist, Docker creates it as root. Blocked SCP of TLS cert files. Fix: `sudo chown <user>:<user>` or `mkdir -p` the directory before first `docker compose up`.
- **Bug: chmod on :ro mount fails** ([[learning/docker-ro-mount-chmod-fails]]): `db-backup` entrypoint tried `chmod +x /backup.sh` but script is mounted `:ro`. Container restart-looped. Fix: call `sh /backup.sh` — shell interpreter needs no execute bit on the script file.
- **Git: clean sensitive info from pushed commit** ([[learning/git-amend-remove-sensitive-push]]): EC2 IP, SSH username, and key filename accidentally landed in a README commit that was already on GitHub. Fix: edit files → `git add` → `git commit --amend --no-edit` → `git push --force origin main`. Old hash `9403ecd` replaced by `12233b2`.
- **Windows OpenSSL broken on Strawberry Perl** ([[learning/windows-openssl-strawberry-broken]]): `C:\Strawberry\c\bin\openssl.exe` maps config to `Z:/extlib/.../ssl/openssl.cnf` (Z: drive doesn't exist). `-subj` flag silently ignored, old cert left in place. Fix: generate certs on EC2 with Linux OpenSSL and SCP back. Git Bash's bundled OpenSSL also works as an alternative.
- **Domain/URL display**: Self-signed cert regenerated with `CN=medi.trialguard.com`. Browser address bar always shows the real URL navigated to — only DNS or hosts-file tricks can change it. Added `18.223.111.152 medi.trialguard.com` to local hosts file makes the domain work locally without real DNS.

2026-05-30 (evening). **Session: ingest — ICT2216 Lab 4 (OWASP Threat Dragon).** Created 1 resource page and 1 example page. OWASP Threat Dragon (v2.3.0) is a free, open-source, cross-platform threat modeling tool — a direct alternative to Lab 3's Microsoft TMT. Two delivery variants: **desktop** (Electron app, offline) and **web** (self-hosted, also available as `appsecco/owasp-threat-dragon` Docker image). DFD stencil elements: Process (circle), Store (rectangle), Actor (rectangle), Data Flow (arrow), Trust Boundary (dashed border). Two ways to create data flows: drag ends from stencil, or the **grey link tool** (turns green when active) — select source → click link icon → click destination → flow auto-created. **Out-of-scope elements**: checked in Properties panel, renders with dashed border, threat generation disabled, requires a reason string. **Open threat highlighting**: elements with unmitigated threats are highlighted **red** on the diagram — scan the canvas for red rather than reading a list. **Report**: from Threat Model details view → "Report" button; customisable (toggle out-of-scope, mitigated, diagrams). Key comparison vs MS TMT: Threat Dragon works cross-platform and in Docker (MS TMT is Windows-only); Threat Dragon has out-of-scope marking and visual red highlighting (MS TMT has neither); MS TMT has 4-state triage (Not Started/Needs Investigation/Mitigated/Not Applicable) vs Threat Dragon's 3-state (Open/Mitigated/Not Applicable). Key gotcha: grey link icon and red delete icon are adjacent — wrong click deletes the element. Created [[resources/owasp-threat-dragon]] and [[examples/ict2216-lab4-owasp-threat-dragon]].

2026-05-30 (afternoon). **Session: lab — ICT2216 Lab 5 (Nginx Reverse Proxy + GitHub Actions).** Created 2 concept pages and 1 example page. Address counter not incremented (lab session, not address-tracked domain). Key outputs:
- **Nginx Reverse Proxy** ([[concepts/nginx-reverse-proxy-and-tls]]): Nginx serves as a reverse proxy handling TLS termination. HTTP-only compose: `nginx:latest` image, port 80:80, `nginx.conf` mounted as read-only, `index.html` mounted at `/var/www/html/`. TLS compose adds certbot service sharing two volumes: `certbot/www` (served by Nginx at `/.well-known/acme-challenge/`) and `certbot/conf` (holds issued certs at `/etc/letsencrypt/live/domain/`). Certbot runs in `certonly --webroot` mode (ACME HTTP-01 challenge) or `--manual --preferred-challenges dns` (DNS-01 when port 80 not public). cert paths go into `nginx-tls.conf` as `ssl_certificate fullchain.pem` and `ssl_certificate_key privkey.pem`. HTTP server block redirects all traffic to HTTPS (`return 301 https://$host$request_uri`) except `/.well-known/acme-challenge/`. Auto-renewal: cron at 03:00 daily (`certbot renew` + `nginx restart`); Let's Encrypt certs expire every 90 days; certbot only renews within 30 days of expiry.
- **GitHub Actions CI/CD** ([[concepts/github-actions-cicd]]): Workflows live in `.github/workflows/*.yml`. Anatomy: `on:` (triggers: push/pull_request/schedule/workflow_dispatch) → `jobs:` (parallel by default, `needs:` for sequencing) → `steps:` (`uses:` for Marketplace Actions, `run:` for shell). Ubuntu runners have Docker pre-installed — use `docker run`/`docker compose` directly in `run:` steps. Key context vars: `${{ github.workspace }}` (repo checkout path), `${{ secrets.NAME }}` (repo secrets). Self-hosted runners (`runs-on: self-hosted`) allow deployment to team VM. Secure pipeline stages: Build → Unit Test → SAST → Dependency Scan → Container Push → Deploy to Staging → DAST → Release. Lab 5 workflow tests Nginx by mounting `index.html` from workspace, waiting 5 s, curling, and grepping for "Hello World" — non-zero exit from `grep` fails the workflow.
- **Lab 5 completed work** ([[examples/ict2216-lab5-github-actions]]): `Lab5/nginx-proxy/` created locally with HTTP Nginx running on `localhost:80` (verified with `curl`). TLS config files prepared with certbot entrypoint (email lcslayer22@gmail.com); real cert requires team VM with public domain. `Lab5/lab5-cicd/` git repo initialized on `main` branch with `index.html` + `.github/workflows/test-nginx.yml`; GitHub CLI installed (gh 2.93.0 via winget); push pending `gh auth login`.
- **Gotchas**: `index.html` must be at repo root (workflow mounts `${{ github.workspace }}/index.html`); Let's Encrypt cannot issue certs for `localhost`; certbot uses `certonly` mode — does NOT edit nginx.conf; CRLF on Windows breaks shell scripts inside containers (use LF).

2026-05-30 (2). **Session: update — ICT2216 Lecture Transcript (Threat Modelling & Security by Design recap).** No new files created. Three targeted additions to [[concepts/threat-modeling]] — existing pages already comprehensive for both topics. Additions: (1) **Threat → Attack → Risk triangle**: threat = possibility; attack = realisation of threat; risk = consequence (can be zero if system well-protected — SQL injection worked example: if parameterised queries used, risk of data leakage = 0 even though attack occurred). (2) **AI threat specifics**: data poisoning (malicious training data corrupts model outputs) + prompt injection (malicious user input overrides AI chatbot system instructions → data disclosure or unintended actions). (3) **Concrete STRIDE worked examples**: Spoofing — typosquatting `amazom.com` visually impersonates `amazon.com`, harvesting credentials; Tampering — attacker modifies `user_code=126` to `user_code=123` at checkout, charging a victim's credit card for goods they receive; Repudiation — signed delivery receipt as non-repudiation (customer cannot deny receipt; software equivalent = digital signatures + hash-chained audit logs proving specific authenticated user performed specific action at specific time).

2026-05-30. **Session: ingest — ICT2216 Lecture 5 (Secure Software Design Part 2 & Secure Agile Development).** Created 1 concept page [[concepts/secure-design-implementation]] (c-000066). Address counter updated to 67. This page bridges the CIA-AAA requirements (what to protect) and the Security by Design Principles (how to think) by providing the *concrete design decisions* for each of the six pillars:
- **Confidentiality Design**: Two disclosure-protection categories — *masking* (display layer, e.g., `**** **** **** 1234`) and *cryptographic techniques* (transit, at-rest, archives). Symmetric vs. asymmetric comparison: symmetric uses N(N−1)/2 keys for N parties, fast, no non-repudiation (AES, 3DES); asymmetric uses N key pairs for N parties, slow, provides non-repudiation (RSA, ECC). Hybrid approach (TLS): asymmetric for key exchange + symmetric for bulk transfer. X.509 v3 certificate: 9 fields (version/serial/algorithm/issuer DN/validity/subject/public key/extensions/CA signature). Client-side hashing + challenge-response design options.
- **Integrity Design**: Rainbow table attacks defeated by per-user random salts. Key stretching (bcrypt/PBKDF2): ~60,000 iterations. Password storage comparison table (plaintext ❌ → unsalted MD5/SHA-256 ❌ → salted SHA-256 ✅ → salted+iterated+metadata ✅). Metadata: creation date, last login, failed login count, password history. Referential integrity (no orphaned FK records). Resource locking for concurrent access (e.g., simultaneous bank transfers).
- **Availability Design**: Replication (primary-secondary). Failover (auto switch, transparent). Vertical scaling (more resources, still SPOF) vs. horizontal scaling (more nodes, preferred — eliminates SPOF).
- **Authentication Design**: MFA + SSO design considerations. Passwordless: register device (something-you-have) → OTP for initial identity validation → device approval for subsequent logins. Examples: WhatsApp, Microsoft Accounts, SingPass, Apple ID, Google.
- **Authorisation Design**: RBAC (roles → permissions, scales) vs. UBAC (direct user-permission, for tiny user sets only). Data Access Control Matrix (who × what × which data). Least privilege + separation of duties + performance impact of complex checks.
- **Accountability Design**: Who/what/where/when. Never log PII or credentials in plaintext. Write-once/WORM or append-only storage. Log rotation and retention policy.
- **Secure Agile Development**: 6-phase security integration — Modelling → Sprint Planning (DoR includes security criteria) → Sprint (SAST/code review/CI) → Dynamic Testing (DAST/pen test) → Release (red teaming/automated deploy) → Operations (vulnerability tracking/monitoring).
- **Secure Design Architecture (4 steps)**: (1) Document architecture (topology/services/actors/data/auth/authorisation/auditing) → (2) Identify threats (trust boundaries/DFDs/STRIDE/OWASP Top 10/CWE Top 25/attack trees) → (3) Implement controls (validation/encryption/replication/ACLs/MFA/logging) → (4) Document & validate (threat profile/residual risk/V&V report). Physical zones: Internet (highest exposure) → DMZ (app servers, between two firewalls) → Intranet → Dev (also secured). External dependencies security techniques table: 8 areas (auth/password mgmt/cert mgmt/flow control/auditing/IDS/database security/sandboxing).

2026-05-26 (continued). **Session: project — ICT2216 TrialGuard, frontend volume bug fix + start.py refresh automation.** Clarification added: the stale volume problem only affects services that use a named volume as a build-artifact hand-off between two containers (frontend-build → nginx). Flask and pii_vault bake code directly into the image and run from it — no intermediate volume, no stale risk. MySQL/MongoDB named volumes hold persistent data, not build artifacts, so they must not be purged. Updated [[learning/docker-named-volume-stale-content]] with a service-by-service risk table.

2026-05-26 (continued). **Session: project — ICT2216 TrialGuard, frontend volume bug fix + start.py refresh automation.** Root cause of stale UI after rebuilds: `frontend_dist` named volume is only seeded from the image when it is **empty** — rebuilding the image never overwrites existing volume content. Fix: `purge_frontend_volume()` in `start.py` stops nginx/frontend-build, removes stopped containers holding the volume, deletes it, then `docker compose up -d --build` re-seeds it from the new image. Also cleaned up all four footer locations (Login, Signup, Landing, subpage-shell) to show only `© 2026 TRIALGUARD`. Created [[learning/docker-named-volume-stale-content]].

2026-05-26. **Session: project — ICT2216 TrialGuard, Phase 4 Authentication + Docker stack verification.** Completed Phase 4 (tasks 4.1–4.5) in full: register, login (step 1), verify-mfa (step 2), logout endpoints, and hash-chained audit log. Key design decisions: (1) Two-step login via intermediate session key `mfa_pending_user_id` — no full session issued until TOTP verified; (2) `session.clear()` before issuing the real session to prevent session fixation; (3) Same generic `401 Invalid credentials.` for locked accounts and wrong passwords — no timing oracle; (4) Auth blueprint CSRF-exempted (Flask-WTF) because JSON API — protection via SameSite=Strict + CORS; (5) bcrypt cost 12 + pyotp TOTP; (6) Account lockout at 5 failures → 15 min. Audit log uses SHA-256 hash chain: each row hashes `prev_hash + timestamp + user_id + action_type + outcome`. **Docker build context fix:** moving `requirements.txt` to repo root broke `COPY requirements.txt .` in both Dockerfiles — fixed by changing compose build contexts to `.` (repo root) with explicit `dockerfile:` paths, and scoping app-code COPY to `COPY backend/ .` / `COPY pii_vault/ .`. **Frontend API plumbing:** `frontend/src/api.js` central fetch wrapper (credentials, JSON, error throw). **Vite dev proxy:** `/api` → `http://localhost:8080`. **start.py launcher:** single file at repo root — runs `docker compose up -d --build`, polls `https://localhost` every 2 s until ready (up to 2 min), opens browser; full error handling for missing docker, daemon not running, compose failure, unhealthy containers, browser open failure. **Smoke test verified:** `https://localhost` serves React SPA; `POST /api/auth/register` returns 201 with `totp_uri`. Created [[examples/ict2216-project-phase4-auth]], [[learning/docker-compose-build-context]]. Updated [[concepts/docker-compose]] (build context split pattern).

2026-05-25 (evening). **Session: project — ICT2216 TrialGuard, Vite + React SPA refactor.** Migrated a 6-page vanilla HTML/UMD React prototype into a proper Vite + React 18 + React Router v6 SPA. All CDN script tags and Babel standalone removed; `Object.assign(window,{})` global exposure replaced with ES module named/default exports; `<a href="page.html">` links replaced with `<Link to="/route">` and `useNavigate`. Folder structure: `src/main.jsx` (entry) → `src/App.jsx` (routes) → `src/data/` (landing.js, portal.js) → `src/components/` (shared.jsx, portal-shell.jsx) → `src/pages/` (6 pages). Three bugs found and fixed during migration: (1) `React.Fragment` with `key` requires `import { Fragment }` — not namespace access via `React.Fragment`; (2) `useState` mistakenly used instead of `useEffect` for form-reset-on-modal-open side effect — `useState`'s second argument is silently ignored; (3) `.pa-modal-bg` used `position: absolute` which broke in SPA context where the containing `pa-root` div is positioned — fixed to `position: fixed`. Old prototype files (17 files + design-canvas state) deleted from root. Build: 42 modules, 0 errors. Created [[examples/ict2216-project-vite-refactor]], [[learning/vite-react-spa-migration]], [[resources/vite]].

2026-05-25. **Session: update — ICT2216 Lecture Transcript (Secure Software Requirements).** No new files created. Three targeted additions made to [[concepts/secure-software-requirements]], which was already comprehensive. Additions:
- **Data-in-processing technologies**: Homomorphic Encryption (compute on ciphertext without decryption; computationally expensive, specialist use only) and Differential Privacy (calibrated statistical noise on query results; output is approximate) added to the Confidentiality section's data-states discussion.
- **Usability vs. security tension**: DBS 6-digit PIN example added to Authentication — a 6-digit PIN has 10⁶ = 1,000,000 combinations vs. 10⁴ = 10,000 for 4-digit (100× more brute-force resistant); requirement must explicitly document the chosen balance and its rationale so the decision is auditable.
- **NIST SSDF stakeholder roles**: Three-role table added under the SSDF framework entry: Business Owner (defines context, approves requirements, accepts residual risk), Developer (implements secure coding, performs security testing), Security Professional (provides expertise, conducts threat modelling, validates assurance). Each role owns a distinct phase: what/why → how built securely → assurance.

2026-05-24. **Session: ingest — INF1007 Ethics & Professional Conduct.** New domain `it-ethics` (16th domain) added. Created 1 source index ([[sources/INF1007-ethics-professional-conduct]], c-000060), 4 concept pages, and 1 area page. Address counter updated to 66. Textbook: *Ethics for the Information Age, 9th ed.* (Quinn, Pearson). Concept pages:
- [[concepts/ethical-frameworks]] (c-000061) — Three levels of moral guidance (rules/principles/frameworks). Non-workable theories: Subjective Relativism (no universal standard), Cultural Relativism (variance ≠ correctness), Divine Command (secular/multicultural society; not reason-based), Ethical Egoism (justifies patently immoral acts). Workable theories: **Kantianism** (Immanuel Kant — deontological; Categorical Imperative 1st formulation universality test ["can I will my maxim to be a universal law?" — borrowing-without-repaying self-defeats, plagiarism self-defeats] + 2nd formulation humanity ["never treat persons merely as means to an end"]); **Act Utilitarianism** (Bentham/Mill — consequentialist; sum all happiness changes for all affected parties, maximise; highway-routing worked example); **Rule Utilitarianism** (adopt rules that maximise happiness if universally followed); **Social Contract Theory** (Hobbes/Locke/Rousseau/Rawls — rational mutual agreement; Rawls' two principles of justice: equal basic liberties + difference principle [inequalities must benefit least advantaged]; veil of ignorance — choose rules without knowing your social position); **Virtue Ethics** (Aristotle — character-focused; identify relevant virtues, ask what a virtuous person would do). Full 9-row framework summary table. SCS Code (4 pillars: Integrity/Responsibility/Competence/Professionalism with sub-duties). ACM Code (4 sections: 7 general ethical principles, 9 professional responsibilities, 7 leadership principles, 2 compliance obligations).
- [[concepts/behavioural-ethics-and-workplace]] (c-000062) — Behavioural ethics vs normative ethics (descriptive vs prescriptive). Situational factors: **Obedience to authority** (Milgram 1961–1962 — ordinary people administered maximum shocks when instructed by authority; implication: IT professionals must speak up when orders conflict with professional judgement); **Roles** (Stanford Prison Experiment, Zimbardo 1971 — randomly assigned guards became abusive; role determines behaviour more than personality); **Moral Licensing** (prior good acts give "moral credit" that permits a later lapse); **Anonymity** (online anonymity reduces perceived detection risk, lowers ethical inhibitions; CCTV effective deterrent by increasing perceived detection). Cognitive biases: **Cognitive Dissonance** (contradictory beliefs → discomfort → defence mechanisms: behaviour change / belief change / avoidance / rationalisation); **Confirmation Bias** (seek and remember information confirming existing views; filters out contradictory ethical considerations); **Conformity Bias** (align with group norms — can be prosocial or can lead to group wrongdoing); **Fundamental Attribution Error** (overestimate character, underestimate situation in others) + **Self-Serving Bias** (attribute own successes to character, failures to external factors). Workplace ethics: **Conflict of Interest** (financial/personal-relationship/dual-role examples; manage via disclosure, recusal, institutional policy); **Bribery vs gifts** (culturally dependent; key criterion is intent to influence); **Whistleblowing** (good motive only; 5 conditions: serious harm + internal reporting + exhausted internal channels + documented evidence + good-faith belief; dominant view: duty to public overrides employer loyalty); **CSR** (corporate ethical responsibility to environment/community/employees; 5 elements including leadership commitment).
- [[concepts/privacy-data-protection-and-ip]] (c-000063) — Privacy definition (right to control information about oneself; balanced against transparency/accountability/safety). Threats: data aggregation, surveillance, data breaches, social media. PII examples (NRIC, full name, passport, photo, email, phone). **PDPA** (Singapore's Personal Data Protection Act) — 8 key obligations: Consent (informed/specific/voluntary), Notification, Purpose Limitation (new purpose needs fresh consent), Access and Correction, Accuracy, Protection (reasonable security arrangements), Retention Limitation, Transfer Limitation. Government surveillance: types of government data; privacy vs security tension (utilitarian for vs Kantian/social-contract against; chilling effect on free expression); culture and privacy (individualistic vs collectivist comparison table). Four ethical frameworks applied to privacy. **Malware taxonomy** (Virus/Worm/Trojan/Ransomware/Spyware/Adware comparison table). **Hacker Ethics** (information-is-free/sharing/decentralisation tenets vs ACM 2.8 authorised access and ACM 1.5 respect creative works; Kantian: unauthorised access treats owner as means; Rule Utilitarian: universal unauthorised access produces net harm). **IP law** — 6 types table (Copyright: automatic, life+70 yrs; Patent: registered, ~20 yrs; Trademark: registered, renewable; Trade Secret: NDA-protected, no time limit; Registered Design; GI). Trade secrets in computing: algorithms, source code, customer lists. Copyright in digital age: perfect copies at zero cost, P2P distribution. Software piracy vs Open Source (still copyright, permissively licensed). Fair use 4-factor test. Ethical frameworks applied to IP (Kantian: creators as ends; Utilitarian: incentivise innovation; Social Contract: society agrees IP benefits all).
- [[concepts/ai-ethics-and-digital-society]] (c-000064) — **Digital society**: IT and automation (historical continuity with industrial revolution; jobs eliminated/created/changed); **Digital Divide** (4 dimensions: device/connectivity/literacy/global; geographic/economic/age/global affected groups; Rawls difference principle applies); Globalisation and outsourcing (for: cheaper goods, focus, developing-country jobs; against: displacement, exploitation, community harm). **AI taxonomy**: Weak/Narrow (exists; Siri, recommendation systems), Strong/AGI (hypothetical), Superintelligence (hypothetical). **AI ethical concerns**: Bias and fairness (facial recognition errors, hiring discrimination, recidivism bias; Kantian/Utilitarian/Social Contract analysis); Misuse (deepfakes for scams, disinformation, state surveillance, autonomous weapons); Accountability and transparency (who is responsible? developer/deployer/user; opacity of black-box models; explainability as ethical requirement in healthcare/justice/lending); Privacy (undisclosed data collection, inference attacks, computer vision surveillance); Job displacement (structural unemployment; counter-argument: technology historically creates new jobs). **6 AI ethics principles**: Fairness, Transparency, Accountability, Privacy, Safety and Security, Human Oversight. Four ethical frameworks applied to AI (Kantian: respect autonomy and dignity; Utilitarian: weigh benefits against harms concentrated on vulnerable; Social Contract: would agree only with oversight and fairness; Virtue Ethics: responsible, honest, caring developers). Technology-society dynamic: bidirectional relationship, IT professionals' special responsibility. Area page: [[areas/it-ethics]] (c-000065) with 5-theory quick-reference table, cross-domain connection diagram, key vocabulary.

2026-05-23. **Session: ingest — INF2004 Embedded Systems Programming.** New domain `embedded-systems` (15th domain) added. Created 1 source index ([[sources/INF2004-embedded-systems-programming]], c-000053), 5 concept pages, and 1 area page. Address counter updated to 60. Coverage spans 11 lecture segments (W0–W10):
- [[concepts/embedded-systems-fundamentals]] (c-000054) — ES definition (dedicated/sensor-actuator/real-time/limited-resources/µC-based), hard/soft/non real-time taxonomy, hardware taxonomy (µC/SoC/ASIC/µP/DSP/FPGA/GPU/NPU), edge-fog-cloud architecture (billions/millions/thousands scale), ES vs general-purpose SW comparison, build pipeline (C→compiler→.o→linker+.ld+.a→ELF→binary/.uf2), startup code (`crt0.s`: disable IRQ → copy data → zero BSS → init stack/heap → enable IRQ → call `main()`), cross-compilation vs native compilation, V-model SDLC for embedded (each left-side artefact paired with right-side test), three canonical failure case studies: Therac-25 (race condition / missing hardware interlocks / Heisenbug), Ariane 5 (64-bit float → 16-bit int overflow, `(float)H_O/65536.0`, reused code not re-validated), Toyota (spaghetti code, 11 000+ globals, stack overflow, no MISRA-C).
- [[concepts/embedded-io-and-interrupts]] (c-000055) — Requirements writing ("shall" mandatory / "should" advisory), traceability (req→design→code→test), problematic requirement patterns (untraceable/untestable/imprecise/no-tolerance/too-complex/implementation-describing), NFRs as emergent properties (performance/safety/dependability/resources/constraints); IVT structure on ARM Cortex-M (address 0x00000000 = SP, 0x00000004 = Reset, 0x0000000C = HardFault, 0x0000004C = IRQ0), interrupt handling sequence (context push to stack → IVT lookup → ISR branch → clear flag → RETI → context pop), ISR rules (short/fast, clear flag, global variables only, no infinite loops, consider re-entrancy, mask unneeded interrupts), interrupt configuration 5-step process, edge vs level triggering, polling vs interrupts comparison (CPU utilisation/latency/power/complexity), timing constraints (polling: `2c ≤ c+p ≤ D ≤ T`; interrupt: `h+c ≤ D ≤ T`), UART/SPI/I2C comparison table, ADC resolution and SNR improvement via oversampling.
- [[concepts/embedded-timers-and-rtos]] (c-000056) — Clock fundamentals (synchronous circuits, master clock, internal dividers, power vs frequency trade-off), RTC (32.768 kHz = 2¹⁵ Hz, 15 divide-by-two stages → 1 Hz, battery-backed), timer modes (count-down/up, one-shot/free-running/periodic, interrupt on endpoint), WDT (CPU reset when target reached, software must "kick" it periodically, essential for unattended systems), PWM (duty cycle = `(period − duty_count)/period × 100`, hardware counter runs independently of CPU); RTOS rationale (predictable timing, task scheduling, inter-task comms, fault tolerance), microkernel vs monolithic kernel, task lifecycle (Ready/Running/Blocked/Terminated), TCB (PC/SP/priority/state/scheduling info), context switch (save registers+PC+SP to stack → load next task), scheduling algorithms (Round Robin time-slicing, Pre-emptive Priority, RMS shorter-period→higher-priority, EDF nearest-deadline, LST least-slack); FSM (states/transitions/inputs, state diagram, state table, deterministic embedded control pattern).
- [[concepts/embedded-testing-and-optimisation]] (c-000057) — Traceability chain (Req→HLD→LLD→Code→Test with example `R1: log temp every 5 min → D1.2.1: log_temp_data() → T1.3: run 15 min, expect 3 entries`), anti-patterns (gold plating, untested requirements), best practices (auto-generated IDs, V-model link, change impact tracing), cost-of-late-bug escalation (1× unit → 10× integration → 100× system → 1000× field), V-model test levels (unit/integration/system/acceptance), unit testing (one module at a time, white+black box, best for boundary bugs), white-box vs black-box comparison table, coverage strategies (boundary/exceptional/justify), integration testing (interface-focused, trace to HLD, all boundary values at each interface), system testing (real hardware, requirements-driven, performance/safety/off-nominal), 10-risk escalation list (unit fail → peer review → integration fail → acceptance fail → field report → escalation → emergency patch → public exposure → legal → catastrophic); power optimisation (P=V×I, P_total=P_dynamic+P_static, clock/voltage scaling, interrupt over polling, low-power coding practices: unsigned types/pointers/static-const/no-float/countdown-for/short-ISRs), compiler flags -O0 to -O3/-Os, C techniques (right types/register-calling/hardware-loops/asm-inline/CSE elimination/loop-unrolling/vendor-libs), memory techniques (Thumb ISA, short-int over int, cache-friendly data structures).
- [[concepts/embedded-sensor-fusion-and-edge]] (c-000058) — Sensor definition (stimulus→transducer→electrical), physical sensing principles (capacitance/resistance/inductance/piezo/Seebeck/light), sensor system pipeline (sensor→signal conditioning→ADC→µC→actuator), signal conditioning 5-step process (filter/zero/scale/linearise/convert), preprocessing table (past→smoothing EMA/MA, present→filtering FIR/IIR, future→prediction Kalman), Kalman filter (Predict→Measure→Correct→Repeat, optimal for linear+Gaussian), why filtering is insufficient (cannot fix bias/drift/missing info), complementary filter formula (`output = α×fast + (1−α)×slow`), sensor fusion taxonomy by abstraction (data/feature/decision level), by centralisation (centralised/distributed/decentralised-hybrid), by competition (competitive-redundancy/complementary/coordinated), advantages (robustness/coverage/confidence/resolution); actuators (hardware that converts command → physical change, types: electrical/hydraulic/pneumatic, servo = negative feedback for position control); edge-fog-cloud architecture table, edge computing definition (NIST: computation at network edge for cloud downstream + IoT upstream), characteristics→benefits mapping, TinyML (on-device ML inference, low power, small model, quantisation/pruning/knowledge-distillation/efficient-architectures, frameworks: TFLite for MCUs/CMSIS-NN/Edge-Impulse/uTensor, applications: gesture recognition/keyword spotting/predictive maintenance).
Area page: [[areas/embedded-systems]] (c-000059) with Pico platform spec table, cross-domain connections diagram (C Programming/Computer Architecture/OS/ML/Networks all feed into embedded), and key vocabulary.

2026-05-23. **Session: ingest — INF2001 Introduction to Software Engineering.** Domain `software-engineering` extended (+4 pages → 13 total). Created 1 source index ([[sources/INF2001-intro-software-engineering]], c-000048) and 4 concept pages. Most INF2001 content (Requirements Engineering, Software Design, Architectural Patterns, GoF Design Patterns, Testing) was already covered by ICT2113, ICT2112, and autoresearch ingests; new pages focus on genuinely novel topics:
- [[concepts/sdlc-models]] (c-000049) — full SDLC lifecycle models comparison: Waterfall (1970, Royce, sequential/BDUF, good for stable requirements), Rapid Prototyping (throwaway prototype before spec, same single-delivery flaw), Spiral (Boehm, 4-phase iterations, radius = accumulated cost, risk analysis every cycle, good for high-risk large systems), RUP (2003, UML/component-based, 4 business phases Inception/Elaboration/Construction/Transition, adaptable framework, good for medium/large), Agile (Manifesto 2001, timeboxed sprints, descoping not deferred features, fixed time not fixed features); full comparison table across 5 dimensions.
- [[concepts/uml-modelling]] (c-000050) — all 5 UML diagrams in a single page with diagram progression (Use Case → Activity → Class → Sequence → Component → Architecture): Use Case (actors/goals/system boundary, <<include>> mandatory reuse, <<extend>> optional conditional, full description template); Activity (start/end nodes, rounded rectangles, diamonds, fork/join bars, branch/merge rules); Class (visibility -, #, + symbols, noun extraction method, class confirmation criteria: remembrance/services/multiple attributes, OOP principles in diagram form); Sequence (participants/lifelines, solid call arrow/dashed return, activation boxes, opt/alt/loop/ref frames, creation new/destruction ×); Component (components as higher-level than classes, lollipop = provided interface, socket = required interface, <<delegate>>, ports).
- [[concepts/software-project-management]] (c-000051) — WBS (100% coverage rule, mutually exclusive, outcomes-based, max 6 sub-tasks, decompose until 2–20 day leaf tasks, forgotten task checklist), Gantt charts, Cone of Uncertainty (4× range at requirements → 1.5× at end of analysis), software size estimation (LOC: language-dependent, small fraction of total effort; FP: language-independent, from requirements; UCP: use case diagram weights actors and use cases).
- [[concepts/software-configuration-management]] (c-000052) — 4 SCM pillars (Change Control, Version Management, System Building, Release Management); Change Control process (CR → CCB evaluation → ECO → check-out → implement → check-in → baseline); Version terminology (version/revision/variant/repository/workspace/check-out/in/branching/merging); Git workflow diagram (workspace → index → local repo → remote repo, key commands); CI/CD — Continuous Integration (Booch 1994, Fowler: commit daily, automated build+test per commit, fix broken build immediately) vs Continuous Delivery (automates release process, software releasable at any time); CI/CD pipeline stages.

2026-05-23. **Session: ingest — INF1002 Programming Fundamentals.** New domain `programming-fundamentals` (14th domain) added. Created 1 source index ([[sources/INF1002-programming-fundamentals]], c-000041), 5 concept pages, and 1 area page. Concept pages:
- [[concepts/python-fundamentals]] (c-000042) — Variables, dynamic typing, scalar types (int/float/bool/str/None), type casting, arithmetic operators, console I/O (`input()`/`print()`), f-string format specifiers (align, width, precision), control flow (if/elif/else, match-case Python 3.10+, while, for, range), break/continue/pass, PEP 8 conventions.
- [[concepts/python-data-structures-and-io]] (c-000043) — Strings (immutable, slicing `s[start:end:step]`, 10 common methods), Lists (mutable, append/insert/remove/del/pop, deep vs shallow copy via `copy.deepcopy`), Tuples (immutable, parentheses, trailing comma for single-element), Dictionaries (key-value, immutable keys, .keys()/.values()/.items()), list comprehensions `[expr for x in iterable if cond]`, file I/O (open modes r/w/a/r+/w+/b, read/readline/readlines, write/writelines, `with` context manager — auto-close + exception safety).
- [[concepts/python-functions-and-modules]] (c-000044) — Functions (def, docstrings, positional/keyword/default args, `*args` tuple, `**kwargs` dict), LEGB scope resolution (Local/Enclosing/Global/Built-in), `global` and `nonlocal` keywords, modules and packages (`import`, `from import`, stdlib highlights), HOFs — `sorted(key=)`, `map()`, `filter()`, `reduce()` from functools — all return lazy iterators, lambda expressions (`lambda arg: expr`, auto-return, single statement only), recursion (base case + decomposition + composition pattern, factorial, Fibonacci, recursion vs iteration tradeoffs, Python default limit 1000).
- [[concepts/c-programming-fundamentals]] (c-000045) — C history (BCPL→B→C, Ritchie 1972, Unix rewrite), C vs Python comparison table (compiled/static/manual vs interpreted/dynamic/GC), compilation pipeline (preprocessor→compiler→assembler→linker→loader), `#include` / `#define`, data types + format specifiers (int `%d`, float `%f`, char `%c`, double `%lf`), printf format flags (- left-align, + sign, 0 zero-pad, width, .precision), scanf with `&` address-of, control flow (if-else, switch-case with break, for, while, do-while), function prototypes, call-by-value, scope (file/block), arrays (0-indexed, no bounds check, 2D, passing to functions), strings as null-terminated `char[]`, string library (`strlen/strcpy/strcmp/strcat/sprintf`) and `<stdlib.h>` conversions (`atoi/atol/atof`).
- [[concepts/c-pointers-memory-and-data-structures]] (c-000046) — Pointer declaration (`int *ptr`), `&` address-of and `*` dereference, NULL pointer, pointer arithmetic (increments by sizeof type), arrays-pointers equivalence (`arr[i]` ≡ `*(arr+i)`), constant vs variable pointers, pointers-to-pointers (`int **`), call-by-reference pattern (pass `&var`, receive `int *ptr`, modify via `*ptr`), dynamic memory (`malloc` uninitialised / `calloc` zeroed / `realloc` / `free`, always check NULL, memory leaks), structs (dot `.` for value, arrow `->` for pointer), `typedef struct { … } TypeName`, linked lists (self-referential `struct node_struct`, head pointer, search/insert-at-head/delete/traversal/free-all), file I/O in C (`FILE *`, `fopen`/`fclose`, `fprintf`/`fscanf`/`fgets`/`fputs`, `fread`/`fwrite` for binary, `fseek`/`ftell`/`rewind` for random access), C memory layout diagram (text/data/BSS/heap↑/↓stack).
Area page: [[areas/programming-fundamentals]] (c-000047). Key cross-domain connections: linked lists and recursion extend to [[concepts/data-structures-fundamentals]]; C pointers and memory layout underpin [[concepts/memory-and-virtual-memory]]; the compilation pipeline connects to [[concepts/assembly-programming-msp430]]; Python HOFs and functional style feed into data science and ML scripts.

2026-05-22. **Session: Learnix (ICT2114 ITP) — CTk teardown bug fix + file refactor.** Fixed `invalid command name` Tcl errors in CustomTkinter 5.2.2 (`check_dpi_scaling`, `update`, `<lambda>`). Root cause: CTk registers internal `after` timers that fire against destroyed widgets. Three-layer fix: (1) use `quit()` not `destroy()` inside mainloop callbacks so the loop exits cleanly; (2) cancel all pending `after` IDs via `tk.call("after", "info")` before calling `destroy()`; (3) override Tcl `bgerror` to silently drop "invalid command name" / "application has been destroyed" noise from background-thread race conditions. Also refactored `src/auth_ui.py` → `src/ui/auth_ui.py`, `src/chat_ui.py` → `src/ui/chat_ui.py`, `src/auth_db.py` → `src/db/auth_db.py`; key lessons: `Path(__file__).resolve().parent` must become `.parent.parent` after moving into a subdirectory, and `load_dotenv(...)` paths need the same update. Created [[concepts/customtkinter-window-lifecycle]] and [[learning/customtkinter-after-teardown]].

2026-05-22. **Session: ingest — INF1006 Computer Networks.** New domain `computer-networks` (13th domain) added to the vault. Created 1 source index ([[sources/INF1006-computer-networks]], c-000032), 7 concept pages, and 1 area page. Concept pages:
- [[concepts/tcp-ip-network-model]] (c-000033) — 5-layer TCP/IP vs OSI 7-layer, PDU terms (segment/packet/frame), address hierarchy (port/IP/MAC), packet switching, LAN vs WAN.
- [[concepts/data-link-layer-ethernet]] (c-000034) — CSMA/CD with BEB (minimum frame 64 B, t_frame ≥ 2×t_prop), MAC addresses (48-bit, OUI), Ethernet frame structure (Preamble→SFD→DA→SA→Type→Data→FCS), switch self-learning + frame forwarding, STP (Root Bridge, Root Port, Designated Port, Blocking).
- [[concepts/ip-addressing]] (c-000035) — IPv4 header fields, classful A–E, CIDR prefix notation, subnetting + VLSM (hosts = 2^n − 2), longest prefix match, fragmentation (Identification/DF/MF/Offset), IPv6 128-bit + :: abbreviation, migration (dual stack, 6to4 tunnelling, NAT64).
- [[concepts/network-layer-protocols]] (c-000036) — IGP vs EGP taxonomy, OSPF (link-state, 3 phases: Neighbour Discovery/Topology Exchange/Route Calculation, LSA freshness rules, Dijkstra), BGP (path-vector, AS paths), ICMP (echo/traceroute TTL trick), ARP (broadcast request → unicast reply → ARP table).
- [[concepts/transport-layer-tcp-udp]] (c-000037) — TCP vs UDP comparison, TCP segment fields, 3-way handshake (SYN/SYNACK/ACK), flow control (rwnd), reliable transfer (seq numbers, cumulative ACK, fast retransmit on 3 dup ACKs), RTT estimation (EWMA α=0.875), congestion control (slow start exponential → CA linear, timeout resets cwnd to 1, 3 dup ACKs sets cwnd=ssthresh+3), GBN/SR efficiency formulae.
- [[concepts/wireless-and-iot]] (c-000038) — CSMA/CA vs CSMA/CD, hidden terminal problem, RTS/CTS, 802.11 standards table (b/a/g/n/ac/ah), LPWAN comparison (NB-IoT/LTE-M/LoRaWAN/Wi-Fi HaLow — range/data rate/spectrum), MQTT (pub-sub, broker, QoS 0/1/2, ports 1883/8883).
- [[concepts/application-layer-dhcp-dns]] (c-000039) — DHCP DORA (Discover/Offer/Request/ACK), key fields (CIAddr/YIAddr/SIAddr/CHAddr/broadcast flag), DNS hierarchy (root → TLD → authoritative), recursive resolution 6-step process, record types (A/AAAA/CNAME/MX/NS/PTR).
Area page: [[areas/computer-networks]] (c-000040). Address counter updated to 41. Key cross-domain connections: OSPF uses Dijkstra (→[[concepts/graph-algorithms]]); sockets bridge OS processes to TCP ports (→[[concepts/os-processes-and-threads]]); DNS/HTTP underpin the web stack (→[[concepts/web-fundamentals]]).

2026-05-21. **Session: (1) autoresearch — Software Testing.** New domain added to vault. Created 3 concept pages: [[concepts/software-testing-fundamentals]] (ISTQB 7 principles, 4 testing levels, Testing Pyramid, static/dynamic, black/white box, regression); [[concepts/test-driven-development]] (Red-Green-Refactor cycle, Arrange-Act-Assert, BDD/Gherkin/Given-When-Then, Three Amigos, TDD vs BDD comparison); [[concepts/test-design-techniques]] (Equivalence Partitioning, Boundary Value Analysis, Statement/Branch/Path coverage, mutation testing, coverage targets). 2 source pages: [[sources/istqb-ctfl-v4]] (CTFL v4.0, 2024), [[sources/fowler-practical-test-pyramid]] (Practical Test Pyramid, martinfowler.com). Synthesis: [[research-software-testing]]. Key connections to existing wiki: TDD enforces DIP → maps to [[concepts/solid-and-design-patterns]]; BDD specs are executable requirements → maps to [[concepts/requirements-engineering]]; DAST = dynamic security testing → maps to [[synthesis/web-security-ssdlc-bridge]]; shift-left aligns with Sprint cadence → maps to [[concepts/scrum-framework]]. **(2) wiki-lint.** 117 pages scanned, 28 issues found. 5 auto-fixed: examples/_index.md (missing lab3 entry), concepts/_index.md (count 58→56, SSD 7→6), sources/_index.md (security-by-design-principles cross-ref), created [[areas/agile-project-management]], updated [[areas/_index.md]]. Key outstanding issues: DragonScale counter drift (counter=3, max observed=c-000031 → run `--rebuild` in WSL); dead manifest entry (DragonScale Memory.md); 18 address-map frontmatter mismatches; mass `status:`/`created:` backfill needed. Report: [[meta/lint-report-2026-05-21]].

2026-05-19. Session: (1) PSM I Cheatsheet (ambaena GitHub) ingested — Agile Manifesto 4 categories, invalid Sprint types, Scaled Scrum rules, Daily Scrum role clarity, exam strategy (two-computer open-book), full 20-term glossary; updated scrum-framework concept page with invalid Sprint types + Scaled Scrum section. (2) Scrum Master Exam 80-question YouTube transcript ingested — created study notes with waterfall vs Scrum comparison, empiricism precision, formal inspection events, servant leadership distinction, self-managing team rules, PB/Sprint Backlog ownership, DoD rules, velocity myth, burn-down interpretation, retro vs review distinction, 40-row quick-reference table. Fixed three stale _index.md files (learning, concepts, sources). (2) Scrum Open Assessment quiz bank ingested (29/30, 96.7%). (3) 2020 Scrum Guide ingested — new domain agile-project-management added to vault. Created source index and full concept page covering Scrum theory (empiricism + lean, three pillars), five values (CFORC), three accountabilities (Developers/PO/SM), five events with timeboxes, three artifacts with commitments (Product Goal/Sprint Goal/Definition of Done). (2) ICT2216 Lecture 4 — Secure Software Design ingested. Created [[concepts/security-by-design-principles]]: Gary McGraw's 50% finding (half of all security problems are design *flaws*, not bugs), the Banana Token smart contract hack as a real-world design-level failure, all 10 OWASP Security by Design Principles with code snippets and worked examples, and Security Architecture (physical vs. logical views).

2026-05-16. Session: ICT2216 Lab 3 — Microsoft Threat Modeling Tool ingested. Created resource page for the tool (4-step workflow, DFD stencils, threat status system) and lab example page (5 sequential steps, sample DFD, STRIDE project checklist).

2026-05-15. Sessions: (1) Vault gap resolution — 11 domain areas pages, 4 synthesis pages, 4 study-notes pages, skill file updates, index rebuilds. (2) ICT2216 Lecture 3 — extended security requirements (session/error/config/code management, anti-requirements, misuse cases) + full threat modelling (threat agents, DFDs, STRIDE, attack trees).

2026-05-14. Sessions: (1) INF1005 Web Systems & Technologies — Internet/HTTP/DNS, HTML5/CSS, JavaScript, PHP/Node.js, MySQL, security, DevOps.

---

2026-05-13. Sessions: (1) ICT2112 Software Design — design process, GoF patterns (all 23), architectural/layer patterns, SOA, ATAM. (2) INF2003 Database Systems — relational model, full SQL, BCNF normalisation, ER diagrams, B+ tree indexing, ACID transactions, NoSQL, data warehousing. (3) Synthesis gaps filled — RE×Security (McCall Integrity ↔ CIA-AAA) and RE×HCI (elicitation ↔ needfinding). (4) ICT1011 Computer Organisation and Architecture — Von Neumann, MSP430 ISA/assembly/modular programming, I/O interfacing, memory technologies, memory management. (5) ICT1012 Operating Systems — full OS stack: processes/threads/IPC, CPU scheduling, synchronisation, file systems, memory/virtual memory, deadlocks.

## Key Recent Facts

- **ICT1011 Computer Architecture**: Von Neumann stored-program concept, common bus. Computer classes: supercomputer → mainframe → minicomputer → microcomputer → embedded/SoC. 3 basic operations: Store/Transform/Transfer.
- **ICT1011 Memory Hierarchy**: Registers (< 1 ns) → Cache (8–35 ns, SRAM) → Main Memory (20–100 ns, DRAM) → Secondary (5–20 ms). Volatile vs non-volatile.
- **ICT1011 MSP430 ISA**: 16-bit RISC MCU, 27 core instructions, 7 addressing modes, 16 registers. R0=PC, R1=SP (pre-decrement/post-increment), R2=SR (N/Z/C/V flags + GIE + power), R3=CG2 (constant generator), R4–R15 GPR. Little-endian. Memory map: 0x0000–0x01FF (8-bit peripherals), 0x2400 (RAM), 0x4400 (Flash), 0xFF80–0xFFFF (interrupt vectors).
- **ICT1011 Instruction Formats**: Format I (double operand), Format II (single operand), Format III (10-bit signed jump offset, ±512 words). 7 modes: Register, Indexed, Indirect, Indirect Auto-increment, Symbolic, Absolute, Immediate.
- **ICT1011 Assembly**: 4 columns (label/mnemonic/operand/comment). Directives: .text/.data/.bss/.byte/.word/.equ/.global. 2-pass assembly: Pass 1 → symbol table; Pass 2 → machine code. Emulated instructions map to core instructions (NOP=MOV R3,R3; CLR=MOV #0; RET=MOV @SP+,PC).
- **ICT1011 Modular Programming**: CALL = push PC+2 (SP−2) then jump; RET = MOV @SP+,PC. 3 parameter-passing strategies: registers (fast), memory block (not re-entrant), stack (general, supports recursion). Local variables via SUB #N,SP at entry; ADD #N,SP at exit.
- **ICT1011 I/O**: Parallel vs serial; simplex/half-duplex/full-duplex. Async serial: start(0) + 7/8 data bits (LSB first) + parity + stop(1); baud = 1/T. RS-232 for DTE↔DCE. Memory-mapped I/O (MSP430) vs isolated I/O (x86). Polled (busy-wait, CPU inefficient) vs interrupt-driven (ISR, efficient). Bluetooth: 2402–2480 MHz, FHSS 1600 hops/s, piconet (1 master + ≤7 slaves), BLE for IoT.
- **ICT1011 Secondary Memory**: HDD platters/tracks/cylinders/sectors. Access time = Ts + Tr + Tt. RAID 0 (stripe, performance), RAID 1 (mirror, fault-tolerance), RAID 10 (both).
- **ICT1011 Primary Memory**: Bus: data (width = bits/transfer), address (width = log₂ max memory), control. Synchronous bus (clocked, simple) vs asynchronous (handshake, flexible). SRAM (latch, fast, cache); DRAM (capacitor+refresh, high density, main memory). ROM→PROM→EPROM→EEPROM→Flash (block-erase, SSDs/phones).
- **ICT1011 Memory Management**: Uni-program (1 process) vs multi-program (concurrent). Swapping: long-term queue/intermediate queue ↔ main memory. Partitioning: fixed (internal fragmentation) vs dynamic (external fragmentation → coalesce/compact). Paging: process split into pages, memory into frames (same size); page table maps page# → frame#; logical address = page#+offset → physical = frame#+offset; eliminates external fragmentation.

- **INF1005 Internet & Web**: ARPANET 1969 (packet switching) → TCP/IP 1983. Web 1989 (Berners-Lee). TCP/IP model: Application/Transport/Internet/Link. TCP = reliable+ordered; UDP = fast+no guarantee. IPv4 exhausted 2011; IPv6 128-bit. DNS resolution: 10 steps; TLDs (gTLD/ccTLD/IDN); ICANN. URL = protocol://domain:port/path?query#fragment. HTTP methods: GET (idempotent, safe) / POST / PUT (idempotent) / DELETE. Status codes: 200/301/304/401/404/500. Browser metrics: TTFB/FCP/LCP/TTI/CLS. Stacks: LAMP/MERN/JAM.
- **INF1005 HTML & CSS**: `<!DOCTYPE html>` → `<html lang>` → `<head>` → `<body>`. Semantic elements: `<header>/<nav>/<main>/<section>/<article>/<aside>/<footer>`. Forms: action+method; GET (bookmarkable, URL) vs POST (body, state-changing). Input types: text/password/email/number/date/checkbox/radio/file/hidden. Validation: HTML5 (hint) → JS (UX) → **server-side (only guaranteed)**. CSS selectors: element/class/ID/group/attribute/pseudo/combinator. Cascade: specificity (ID>class>element) then location. Box model: content+padding+border+margin; border-box sizing. Flexbox: one-axis, justify-content/align-items. Grid: two-axis, fr units, repeat(). Responsive: `<meta viewport>`, mobile-first, `@media (min-width:…)`. WCAG POUR: Perceivable/Operable/Understandable/Robust.
- **INF1005 JavaScript**: `var` (hoisted, function-scope) / `let` / `const` (block-scope). Falsy: false/null/""/0/NaN/undefined. Strict equality `===` preferred. Arrays: push/pop/forEach/find/filter/map/reduce/sort. Objects: destructuring, spread. JSON: `JSON.parse()`/`JSON.stringify()`. Arrow functions: `(a,b) => a+b`. Closures: inner function retains outer scope. ES6 classes (syntactic sugar over prototypes). DOM: `querySelector`/`querySelectorAll`; `textContent`/`innerHTML`/`classList`; `addEventListener`. Events: capturing → target → bubbling; `preventDefault()`/`stopPropagation()`; delegation. Async: Fetch API → Promises (`.then/.catch`) → `async/await`. CORS: server needs `Access-Control-Allow-Origin`. localStorage/sessionStorage; Geolocation API. ES6 modules: `export`/`import`.
- **INF1005 PHP & Server-Side**: PHP embeds in HTML (`<?php … ?>`); variables with `$`; concatenation with `.`. Superglobals: `$_GET/$_POST/$_SESSION/$_FILES/$_SERVER`. Indexed arrays (`$arr[]`) and associative arrays (`$arr["key"]`). OOP: `__construct`, `$this->`, `public/private/protected`, `extends`+`parent::__construct`. Sanitise: `htmlspecialchars()` (XSS), `filter_var()` (validate), prepared statements (SQLi). LAMP: Linux/Apache/MySQL/PHP. PDO: `prepare` → `bindValue` → `execute` → `fetch`. SQL CRUD + JOIN + GROUP BY + transactions. NoSQL: Key-Value/Document/Column/Graph. Node.js: V8 engine, event-driven non-blocking, single thread. Express: routing (`app.get/post/put/delete`), REST API, static files. WebSockets (Socket.io): two-way real-time. EJS: server-side templates. React/Next.js/Remix/ASP.NET/Blazor overview.
- **INF1005 Web Security**: CIA Triad: Confidentiality/Integrity/Availability. STRIDE: Spoofing/Tampering/Repudiation/Info Disclosure/DoS/Elevation of Privilege. Auth: Knowledge/Ownership/Inherence factors; MFA. Strategies: HTTP Basic / Form+Session / JWT Bearer / OAuth. Crypto: AES (symmetric); RSA (asymmetric: public encrypts, private decrypts); digital signatures. TLS/HTTPS: certificates from CA (DV/OV/EV). Credential storage: bcrypt `password_hash()` + salting. SQLi defence: prepared statements. XSS (reflected/stored): `htmlspecialchars()` + CSP headers. CSRF: hidden token in every state-changing form. Brute force: rate limiting + lockout + CAPTCHA. DoS/DDoS: CDN + load balancing. DevOps: CI (tests on commit) → CD (auto-release/deploy). Testing: unit/integration/functional/non-functional/pen-test. Hosting: shared → VPS → dedicated → collocated → cloud. Cloud: IaaS/PaaS/SaaS. DNS records: A/AAAA/CNAME/MX/NS/TXT/PTR. Apache: VirtualHost, .htaccess, URL rewriting.

- **ICT1012 OS Fundamentals**: OS = hardware abstraction + resource allocator + sync/communication/protection. Kernel runs at all times. Bootstrap in ROM. DMA = 1 interrupt per block transfer. System calls via `int 0x80` (old) or `syscall` (modern); APIs: POSIX/Win32. Privilege modes: CPL bit in CS register; ring 0 = kernel, ring 1 = user. OS designs: layered, modular, microkernel (Mach, message-passing), monolithic (UNIX), hybrid (Darwin, Windows NT).
- **ICT1012 Processes & Threads**: Process states: new → ready → running → waiting → terminated. PCB stores: state, PID, PC, registers, scheduling info, memory info, I/O status. Schedulers: long-term (degree of multiprogramming), medium-term (swapping), short-term (CPU). fork/exec/wait/exit; zombie (parent not yet wait'd) vs orphan (parent died). IPC: shared memory (mmap/shm_open) or message passing (mq_open/send/receive), blocking/non-blocking. Threads share code/data/files but own registers+stack. Models: M:1, 1:1 (Linux/Windows), M:M, two-level. Linux uses clone() → tasks. thread safety: reentrant/TLS/atomic.
- **ICT1012 CPU Scheduling**: Criteria: utilisation, throughput, turnaround, waiting, response. FCFS (convoy effect); SJF (optimal avg wait, exponential averaging τ(n+1)=α·t(n)+(1−α)·τ(n)); SRTF (preemptive SJF); Priority (starvation → ageing); RR (quantum q, each process waits ≤(n−1)q); Multilevel Queue (permanent assignment); Multilevel Feedback Queue (ageing between queues). Rate Monotonic (hard real-time, shorter period = higher priority, ~69% CPU utilisation limit). Linux CFS: vruntime — always run lowest vruntime; nice −20 to +19.
- **ICT1012 Synchronisation**: Race condition = shared data, order-dependent result. Critical section requirements: mutual exclusion, progress, bounded waiting. test_and_set (atomic read+set-to-true); compare_and_swap (only writes if value matches expected — fewer cache invalidations). Mutex = spinlock or sleep-based. Semaphore: binary (≡ mutex) or counting (resource pool); wait(S) decrements, signal(S) increments; blocking queue avoids busy-wait. Bounded-buffer: mutex + not_empty(0) + not_full(n). Priority inversion → priority-inheritance protocol.
- **ICT1012 File Systems**: File attributes: name, identifier, type, location, size, protection, timestamps. Access: sequential, direct/random, indexed. Directory structures: single-level → two-level → tree → acyclic-graph (ref count for safe delete) → general graph (cycle detection needed). Unix permissions: rwx per owner/group/others; r=4, w=2, x=1. Layered FS: logical FS → file-org module → basic FS → I/O control → hardware. On-disk: boot block, superblock, inode/FCB. Allocation: contiguous (best performance, external fragmentation), linked (FAT: pointers in table at volume start), indexed (inode with direct + single/double/triple indirect blocks). Free space: bit vector (fast contiguous scan) vs linked list (no wasted space). Buffer cache: sync write (safe, slow) vs async write (fast, eventual consistency).
- **ICT1012 Virtual Memory**: Address binding: compile/load/execution time. MMU translates logical → physical via relocation register. Paging: page table maps page# → frame#; TLB caches recent translations (EAT = hit_ratio×mem + (1−hit)×2×mem; 99% hit → 10.1 ns vs 10 ns). ASIDs allow multi-process TLBs. Page table structures: hierarchical (two-level, 32-bit), hashed (>32-bit), inverted (one global table, indexed by frame). Demand paging: valid-invalid bit; page fault → 6 steps (trap→check→free frame→disk read→update PTE→restart). Page replacement: FIFO (Belady's anomaly), OPT (benchmark only), LRU (counter or linked list), second-chance/clock (ref bit=1 → skip and clear), enhanced second-chance (0,0)→(0,1)→(1,0)→(1,1). Thrashing: total WSSᵢ > physical memory; PFF control: too-low PFF → remove frames; too-high → add frames.
- **ICT1012 Deadlocks**: 4 necessary conditions: mutual exclusion, hold-and-wait, no preemption, circular wait. Resource allocation graph: cycle + single instances → deadlock; cycle + multiple instances → possible deadlock. Prevention: break one condition structurally; ordered resource acquisition prevents circular wait. Avoidance: Banker's algorithm — safe state = safe sequence exists (Safety Algorithm O(m×n²)); Resource-Request Algorithm = pretend allocate → run Safety → grant or rollback. Detection: wait-for graph (single instance, O(n²) cycle detection); detection algorithm (multiple instances, O(m×n²)). Recovery: terminate all or one-at-a-time; or preempt resources with rollback (starvation risk).

- **INF2003 Relational Model**: DB/DBMS 3-level abstraction (view/logical/physical). Physical independence easier than logical. Relation = table of unordered tuples; keys: superkey → candidate key → primary key → foreign key. ACID (Atomicity/Consistency/Isolation/Durability). 6 design stages: Requirements → Conceptual (ER) → Logical → Refinement (BCNF) → Physical → Security.
- **INF2003 Relational Algebra**: 6 fundamental operators — σ (select rows), π (select columns), ∪, −, × (cartesian product), ρ (rename). Extended: ∩, ⋈ (natural join), outer joins (⟕⟖⟗), ÷ (division — "for all" queries), ← (assignment). Push σ/π before joins for efficiency.
- **INF2003 SQL**: DDL (`CREATE TABLE`, `ALTER`, `DROP`). DML: `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY`. Aggregate: SUM/COUNT/AVG/MIN/MAX. NULL semantics: use `IS NULL` not `= NULL`. Set ops: `UNION`/`INTERSECT`/`EXCEPT` (+ ALL variants). Subqueries: `IN`, `EXISTS`, `ANY`, `ALL`. Optimisation: `EXISTS` > `COUNT(*)>0`; JOINs > correlated subqueries; avoid leading wildcards.
- **INF2003 Normalisation**: Anomalies: insertion/update/deletion/redundancy. FD: X→Y. Armstrong's axioms: Reflexivity, Augmentation, Transitivity (+ Union/Decomposition/PseudoTransitivity). Closure X⁺: iteratively add attributes. BCNF: every non-trivial FD X→Y must have X as superkey. Decomposition: lossless (BCNF guarantees) ✓; dependency-preserving (BCNF does NOT guarantee) ✗.
- **INF2003 ER Diagrams**: Entity (rectangle), relationship (diamond), attribute (oval). Attribute types: key/composite/multivalued/derived. Participation: total (double line) vs partial (single). Cardinality: 1:1/M:1/1:N/M:N. Weak entity = depends on owner for identity. ISA = subclass with overlap/covering constraints. ER→schema: entity→table, composite→flatten, multivalued→separate table, M:N relationship→table with composite PK, weak entity→merged with identifying relationship.
- **INF2003 Indexing**: Heap/sorted/indexed file organisations. Hash index: O(1) equality only. B+ tree: all data in leaves (linked list); internal nodes route; min 50% occupancy; O(log n) search/insert/delete; supports range queries; insert splits leaves upward; delete borrows from sibling or merges.
- **INF2003 Transactions**: ACID deep-dive. Serial schedule = safest. Serializable = equivalent to some serial. Interleaving → dirty reads/lost updates. TCL: COMMIT/ROLLBACK/SAVEPOINT. Lock granularity: DB→table→page→row→field. Deadlock: prevent by ordering; detect by timeout. Optimistic 3-phase: read (private copy) → validate → write. Recovery: write-ahead transaction log on separate device; checkpoint + redo/undo.
- **INF2003 NoSQL**: Key-value (Redis, O(1) get/set/del); Document (MongoDB, schema-less JSON/BSON, no joins); Columnar (Cassandra, column-wise storage, compression, fast aggregation); Graph (Neo4j, node+edge+property, traversal). Use NoSQL when ACID not needed, data is large/diverse, or high availability required.
- **INF2003 Data Warehouse**: ETL (Extract→Transform→Load). Star schema: 1 fact table + N dimension tables (denormalised, simple queries). Snowflake: normalised dimensions (storage savings, slower queries). OLAP cube operations: Slice (fix dimension), Dice (sub-cube), Drill Down (summary→detail), Roll Up (detail→summary), Pivot (rotate). OLTP vs OLAP: OLTP normalised+fast writes; OLAP denormalised+complex reads.

- **ICT2112 Design Process**: Architecture → Detailed → Construction. Architecture serves 4 roles (Structural, Communication, Quality, Foundation). Detailed design = Interface Design + Component Design. Construction design produces pseudocode/flowcharts (flow-based) and decision/state-transition tables (table-based).
- **Quality attributes** (Microsoft model): Usability; Availability, Performance, Reliability, Scalability, Security (run-time); Conceptual Integrity, Maintainability, Reusability, Testability (design).
- **Coupling scale (tight → loose)**: Content → Common → Control → Stamp → Data. **Cohesion scale (high → low)**: Informational → Functional → Communicational → Procedural → Temporal → Logical → Coincidental.
- **Architectural/Layer patterns**: Layered 3-Tier (Presentation / Domain / Data Source). Domain layer: Transaction Script (simple), Table Module (medium), Domain Model (complex). Data Source: Table Data Gateway, Row Data Gateway, Active Record, Data Mapper (cleanest separation). Presentation: MVC, MVP (passive view, testable Presenter), MVVM (two-way binding).
- **SOA patterns**: Gateway (single entry point), Service Registry/Discovery (Consul/Eureka), Circuit Breaker (Closed → Open → Half-Open), Adapter (bridge incompatible interfaces).
- **GoF Patterns — all 23**: Creational (Singleton, Factory Method, Abstract Factory, Builder, Prototype); Structural (Adapter, Decorator, Facade, Composite, Proxy, Bridge, Flyweight); Behavioural (Observer, Strategy, Command, Iterator, Template Method, State, CoR, Mediator, Memento, Visitor).
- **Design Evaluation — ATAM**: 9-step process; outputs sensitivity points, tradeoffs, risks, non-risks. **Design Smells**: Rigidity, Fragility, Immobility, Viscosity, Needless Complexity, Needless Repetition, Opacity.

## Domain Summaries

**Scrum / Agile** (2020 Scrum Guide + PSM I prep): Scrum is an empirical framework (not a methodology) built on transparency, inspection, and adaptation. **Invalid Sprint types** (exam trap): Hardening/Stabilisation Sprint, Sprint 0, Release Sprint, Design Sprint — none exist in Scrum. **Scaled Scrum**: one PO + one Product Backlog per product regardless of team count; one integrated Increment; shared DoD as minimum; teams need not synchronise. **Agile Manifesto** — 4 categories: Project (early delivery, welcome change, frequent releases, sustainable pace, working software as measure), Product (simplicity, technical excellence), People (face-to-face, daily collaboration, self-organising teams, motivated individuals), Process (regular retrospection). **Exam strategy (PSM I)**: open-book, two computers; first loop flags uncertain questions; second loop researches them; pass mark is 85 %. Three roles: Developers (create the Increment, own the Sprint Backlog), Product Owner (one person; owns the Product Backlog and Product Goal; sole authority to cancel a Sprint), Scrum Master (servant-leader; establishes Scrum; removes impediments). Five events: Sprint (≤1 month, fixed — container for all others), Sprint Planning (≤8 hrs; defines Sprint Goal + selects items + creates plan), Daily Scrum (15 min; Developers only; progress toward Sprint Goal), Sprint Review (≤4 hrs; inspect Increment with stakeholders; not a release gate), Sprint Retrospective (≤3 hrs; closes the Sprint; improves team effectiveness). Three artifacts + commitments: Product Backlog (→ Product Goal), Sprint Backlog (→ Sprint Goal), Increment (→ Definition of Done). Key rules: Scrum is immutable (partial Scrum is not Scrum); Sprint Goal is fixed but scope is negotiable; Increment may be released at any time without waiting for Sprint Review; Definition of Done is shared across all teams on the same product.

**Database Systems** (INF2003): Full relational model from ACID to normalisation. The 6-stage design process runs: requirements → ER diagram → relational schema → BCNF refinement → physical design (B+ tree indexes) → security. SQL is the declarative layer over relational algebra; every SELECT maps to σ/π/⋈. Normalisation uses FD closure and BCNF to eliminate all anomalies while guaranteeing lossless decomposition (but not always dependency preservation). B+ tree is the universal index: O(log n) equality and range, dynamic insert/delete. ACID transactions are enforced via write-ahead logging + locking (or optimistic 3-phase). NoSQL trades ACID for scale and flexibility; choose the model (KV/document/columnar/graph) based on query patterns. Data warehouses deliberately de-normalise into star/snowflake schemas for OLAP analytics.

**Software Design** (ICT2112): Full design pipeline from architecture to construction. Coupling/cohesion are the two key internal quality metrics. The 3-Tier layered architecture separates Presentation, Domain, and Data Source concerns; each layer has specific patterns (MVC, Domain Model, Data Mapper). SOLID + GoF patterns are applied at the detailed design level. ATAM evaluates architecture against quality attributes. Design smells (Rigidity, Fragility …) signal SOLID violations.

**Secure Software Development** (ICT2216): Security requirements derived from CIA + AAA pillars. OWASP ASVS provides tiered verification (Level 1–3). SecurityRAT automates requirement selection. Docker Compose is the primary deployment tool across all labs. Windows Docker deployments require CRLF-to-LF conversion for shell scripts; use PowerShell for `docker exec` with Linux paths. **Lecture 4 — Security by Design**: 50% of security problems are design *flaws* not bugs (McGraw 2006) — even perfect code cannot fix a flawed design. The 10 OWASP Security by Design Principles are: (1) Minimise attack surface, (2) Secure defaults, (3) Least privilege, (4) Defence in depth, (5) Fail securely (initialise `isAdmin = false`), (6) Don't trust services, (7) Separation of duties, (8) Avoid obscurity, (9) Keep it simple, (10) Fix correctly (root cause + broad testing). Security architecture has two views: physical (infrastructure topology) and logical (service/trust boundaries).

**Software Engineering** (ICT2113 + INF1009): Requirements Engineering covers the full RE lifecycle — BCIC analysis, PS/SRS documents, McCall's quality model (3 perspectives, 11 features), iRTM for traceability. Lightweight RCM covers User Stories (3C's, INVEST, Connextra) and UseCase 2.0 (parent-UC, Stories, Slices, 8-step process). OOP covers the 4 pillars with Java/C++ comparison, OOP relationships (Association/Aggregation/Composition), and UML class diagrams.

**Computer Architecture** (ICT1011): Full hardware stack from Von Neumann fundamentals through MSP430 assembly to memory management. The MSP430 RISC MCU is the teaching platform throughout: 16-bit, 27 instructions, 7 addressing modes, 16 registers (R0=PC, R1=SP, R2=SR, R3=CG2). I/O chapter covers serial communications (async framing, RS-232), polled vs interrupt-driven I/O, and Bluetooth (FHSS piconet). Memory chapters cover SRAM (cache) vs DRAM (main memory), ROM/Flash (non-volatile), and memory management (swapping → partitioning → paging). Paging is the capstone concept bridging into OS (ICT1012).

**Web Development** (INF1005): Full web stack from network fundamentals to modern frameworks. The Internet (1969, ARPANET) is the infrastructure; the Web (1989, Berners-Lee) is the application. TCP/IP layers: Link → IP → Transport (TCP/UDP) → Application (HTTP). DNS resolves hostnames to IPs via a 10-step hierarchical process. HTTP is stateless request/response; GET is safe and idempotent; POST is neither. HTML5 provides semantic structure (not just presentation); CSS handles appearance (cascade: specificity → location). Layout tools: Flexbox (one-axis) and Grid (two-axis). Responsive design requires the viewport meta tag and mobile-first media queries. JavaScript runs in the browser: dynamic typing, closures, prototype-based OOP. The DOM is a tree; `querySelector` + `addEventListener` are the primary manipulation tools. Async programming uses Promises and `async/await` with the Fetch API. PHP and Node.js handle server-side logic; PDO with prepared statements prevents SQL injection. REST APIs map HTTP verbs to CRUD. Security: CIA triad, STRIDE model, bcrypt for passwords, XSS prevention via output escaping, CSRF tokens, TLS/HTTPS.

**Operating Systems** (ICT1012): Full OS stack built directly on ICT1011's paging foundation. Processes and threads establish the execution model (fork/exec, PCB, schedulers, IPC, Pthreads). CPU scheduling covers FCFS → SJF → Priority → RR → Multilevel Feedback Queue → Linux CFS. Synchronisation addresses race conditions using hardware primitives (test_and_set, compare_and_swap), mutex locks, and semaphores — culminating in the bounded-buffer producer–consumer solution. File systems provide the persistent storage model: allocation methods (contiguous/linked/indexed), directory structures, Unix permissions, and free-space management. Memory and virtual memory extend paging to the OS level: TLB, page table structures, demand paging, page replacement algorithms (LRU approximations, second-chance), thrashing, and working-set model. Deadlocks close the module with the four necessary conditions, Banker's algorithm for avoidance, detection via wait-for graphs, and recovery strategies.

**Computer Science** (INF1008): Algorithm complexity from Big-Oh through Master Theorem. Data structures from arrays to B-Trees with a full complexity comparison table. Sorting (Bubble/Selection/Insertion/Merge/Quick) and string algorithms (Brute Force/KMP/Boyer-Moore) with when-to-use guidance. Graph algorithms: DFS/BFS/Topological Sort, MST (Prim's vs Kruskal's), shortest paths (Dijkstra vs Bellman-Ford).

**Mobile Development** (INF2007): Android OS stack, 4 app components, Activity lifecycle. Jetpack Compose declarative UI with recomposition and state hoisting. Full MVVM architecture (UI → ViewModel → Repository → Room/Retrofit). Kotlin coroutines (launch/async, Dispatchers, Structured Concurrency), Flow/StateFlow, Hilt DI, Retrofit, WorkManager.

**HCI** (INF2002): Definition, UI vs UX distinction. History from Memex (1945) to ubiquitous computing (Weiser 1991) to touchscreens. Real-world design failures (Air Inter 148, Anton Yelchin, Hawaii missile alert). UCD principles, personas, paper prototyping. Needfinding methods (observation, ethnography, surveys/Likert/Semantic Differential, interviews, focus groups). Task analysis (HTA, TDH with XOR/AND/OR, knowledge-based / declarative vs procedural).

## Recent Changes

- Created: `wiki/learning/psm1-cheatsheet-study-notes.md` (Agile Manifesto, invalid Sprint types, Scaled Scrum, exam strategy, 20-term glossary)
- Updated: `wiki/concepts/scrum-framework.md` (Invalid Sprint Types + Scaled Scrum + Daily Scrum role clarity)

- Created: `wiki/learning/scrum-master-exam-study-notes.md` (80-question CSM/PSM/ACP prep, 40-row reference table)
- Fixed: `wiki/learning/_index.md`, `wiki/concepts/_index.md`, `wiki/sources/_index.md` — all three were stale

- Created: `wiki/learning/scrum-open-assessment-study-notes.md` (15 traps + role/event/artifact Q&A + 25-fact reference table)
- Updated: `wiki/sources/scrum-guide-2020.md`, `wiki/index.md`, `wiki/log.md`, `wiki/hot.md`

- Created: `wiki/concepts/security-by-design-principles.md` (10 OWASP principles, design flaws vs bugs, Banana Token case study, Security Architecture physical vs logical)
- Updated: `wiki/sources/ICT2216-secure-software-development.md` (Lecture 4 section, Lab 3 entry, new concept link)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

- Created: `wiki/sources/INF1005-web-systems-technologies.md` (chapter map, concept page cross-references)
- Created: `wiki/concepts/web-fundamentals.md` (Internet/Web history, TCP/IP model, DNS 10-step resolution, URLs, HTTP methods/status codes, browser rendering metrics, web stacks)
- Created: `wiki/concepts/html-and-css.md` (HTML5 document structure, semantic elements, tables, forms, validation layers; CSS selectors/cascade/box model; Flexbox/Grid/responsive design/animations/Sass; WCAG POUR)
- Created: `wiki/concepts/javascript-fundamentals.md` (types/operators/arrays/objects/functions/scope/closures/classes; DOM manipulation; event handling/propagation/delegation; async/Fetch/Promises/await; CORS; modules; browser APIs)
- Created: `wiki/concepts/server-side-web-development.md` (PHP syntax/arrays/OOP/superglobals; form processing/sanitisation; LAMP stack; MySQL+PDO; SQL CRUD/JOIN; NoSQL types/Mongoose; Node.js event loop; Express/REST API; WebSockets; EJS; serverless; modern frameworks)
- Created: `wiki/concepts/web-security-and-devops.md` (CIA/STRIDE; auth factors/strategies; cryptography/TLS/HTTPS; bcrypt/salting; SQL injection/XSS/CSRF/brute-force/DoS defences; CI/CD; testing types; hosting/cloud models; DNS records; Apache config)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

- Created: `wiki/sources/ICT1012-operating-systems.md` (chapter map, concept page cross-references, ICT1011→ICT1012 continuity note)
- Created: `wiki/concepts/os-processes-and-threads.md` (OS roles, bootstrap/DMA, system calls, OS designs, process states/PCB/schedulers, fork/exec/zombie/orphan, IPC, threads+Pthreads)
- Created: `wiki/concepts/cpu-scheduling-and-synchronisation.md` (scheduling criteria, FCFS/SJF/SRTF/Priority/RR/MLQ/MLFQ/CFS, race conditions, critical section, test_and_set, compare_and_swap, mutex, semaphores, bounded-buffer, priority inversion)
- Created: `wiki/concepts/file-systems.md` (file attributes/operations, access methods, directory structures, Unix rwx permissions, layered FS, allocation methods, free-space management, buffer cache)
- Created: `wiki/concepts/memory-and-virtual-memory.md` (address binding, MMU, paging, TLB EAT, page table structures, virtual memory, demand paging, page replacement algorithms, thrashing, working-set, PFF)
- Created: `wiki/concepts/deadlocks.md` (4 necessary conditions, resource allocation graph, prevention, Banker's algorithm, detection algorithms, recovery)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

- Created: `wiki/sources/ICT1011-computer-organisation-architecture.md`
- Created: `wiki/concepts/computer-architecture-fundamentals.md` (Von Neumann, computer classes, memory hierarchy, MSP430 registers/memory map/ISA formats/addressing modes)
- Created: `wiki/concepts/assembly-programming-msp430.md` (syntax, directives, 2-pass assembly, executable instructions, emulated instructions, CALL/RET, parameter passing, stack frames)
- Created: `wiki/concepts/io-and-memory-systems.md` (serial/parallel I/O, async framing, polled vs interrupt, Bluetooth, HDD, RAID, bus interconnect, SRAM vs DRAM, ROM/Flash, memory management: swapping/partitioning/paging)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`



- Created: `wiki/synthesis/re-elicitation-cia-aaa-security-requirements.md` (McCall Integrity ↔ CIA-AAA; RE lifecycle ↔ SSDLC; BCIC for security; Mag7 on security requirements)
- Created: `wiki/synthesis/re-elicitation-hci-needfinding.md` (method mapping table; HTA/TDH → requirements pipeline; personas → stakeholder profiles; pain points → BCIC Interpret)
- Updated: `wiki/synthesis/_index.md`, `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

- Created: `wiki/examples/stock-prediction-neural-network.md` (custom NN project — SOLID ML + Tkinter GUI)
- Created: `wiki/sources/INF2003-database-systems.md`
- Created: 6 concept pages — `relational-database-fundamentals`, `relational-algebra-and-sql`, `database-normalisation`, `er-diagrams`, `database-indexing-transactions`, `nosql-and-data-warehousing`
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

- Created: `wiki/sources/ICT2112-software-design.md`
- Created: `wiki/concepts/software-design-process.md` (design pipeline, quality attributes, coupling/cohesion, ATAM, design smells, construction design)
- Created: `wiki/concepts/software-architecture-patterns.md` (layered, domain/data-source/presentation patterns, SOA)
- Updated: `wiki/concepts/solid-and-design-patterns.md` (added Builder, Prototype + all structural and behavioural GoF patterns; now covers all 23)
- Updated: `wiki/index.md`, `wiki/hot.md`, `wiki/log.md`

## Active Threads

- ICT2216 Lab 2 Steps 5–7 (browser UI / artifact exploration) — user to complete independently
- ✓ Resolved: [[learning/ict1012-operating-systems-study-notes]] — exam-prep summary for ICT1012
- ✓ Resolved: [[learning/inf2003-database-systems-study-notes]] — exam-prep summary for INF2003
- ✓ Resolved: [[learning/inf1008-data-structures-algorithms-study-notes]] — exam-prep summary for INF1008
- ✓ Resolved: [[learning/inf1005-web-systems-study-notes]] — exam-prep summary for INF1005
- ✓ Resolved: [[synthesis/maths-to-ml-bridge]] — matrix multiplication as forward pass; OLS vs gradient descent; SVD→PCA; Gaussian NB; Z-score scaling
- ✓ Resolved: [[synthesis/web-security-ssdlc-bridge]] — SQLi/XSS/CSRF → OWASP 2025 → ASVS chapter → STRIDE threat mapping
- ✓ Resolved: [[synthesis/ict1011-ict1012-architecture-bridge]] — hardware handover: paging (ICT1011) → TLB/demand paging/replacement/thrashing (ICT1012)
- ✓ Resolved: [[synthesis/rest-api-cross-stack]] — Retrofit → OkHttp → Express → res.json() full HTTP lifecycle with coroutine integration
- ✓ Resolved: [[synthesis/dip-hilt-dependency-injection]] — DIP → Hilt mapping written
- ✓ Resolved: [[synthesis/data-mapper-repository-room-retrofit]] — Data Mapper → Repository/Room/Retrofit mapping written
- ✓ Resolved: [[synthesis/re-elicitation-cia-aaa-security-requirements]] — McCall Integrity ↔ CIA+AAA; RE lifecycle ↔ SSDLC requirements phases; BCIC applied to security requirements
- ✓ Resolved: [[synthesis/re-elicitation-hci-needfinding]] — Needfinding methods ↔ RE elicitation; HTA/TDH → use cases → SRS; personas → stakeholder profiles; pain points → BCIC Interpret → hidden requirements
