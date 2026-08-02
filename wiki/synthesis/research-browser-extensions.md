---
type: synthesis
title: "Research: Browser Extensions"
domain: web-development
maturity: established
tags: [research, browser-extensions, manifest-v3, webextensions, security, cross-browser, wxt, plasmo]
updated: 2026-07-28
created: 2026-07-28
---

# Research: Browser Extensions

**Research question:** What are browser extensions architecturally, how are they built, and what are the key security and cross-browser considerations in 2025–2026?

**Research method:** Autonomous web research — 5 search passes, 3 deep fetches. Sources: FreeToolKit MV3 guide, nitiweb.net architecture overview, MDN WebExtensions API, MV2 vs MV3 Medium analysis, Vectra AI / Pulsedive security analyses, WXT/Plasmo framework comparisons (2025).

---

## Summary

Browser extensions are full-privilege web applications that run inside the browser with access to APIs far beyond what a normal web page can reach — DOM of every site, network interception, credential storage, tab management, and system notifications. This power makes them both highly useful and a high-value attack target.

The landscape was fundamentally restructured by **Manifest V3**, which Google finalised in 2025 (MV2 globally disabled July 24, 2025). The architectural change from persistent background pages to ephemeral service workers, and from programmatic network interception to declarative rules, has reshaped what extensions can and cannot do — and created a lasting divergence between Chrome and Firefox.

---

## Core Findings

### 1. The Extension Architecture Is a Distributed System in Miniature

A browser extension is not a single script — it is three or more isolated execution contexts that communicate exclusively via message passing:

- **Background service worker** — event-driven, stateless between activations, no DOM access, full WebExtensions API
- **Content scripts** — DOM access, isolated JS heap, limited API access
- **Popup / options page** — standard web pages in the extension's own origin, full API access, short-lived

The critical design constraint is that **the service worker has no persistent in-memory state**. The browser can kill and restart it at any time. This makes `chrome.storage` — not variables — the only reliable persistence layer. Developers who treat extensions like Node.js servers (keeping state in module-level variables) hit bugs that are hard to reproduce because they depend on service worker lifecycle timing.

### 2. MV3 Is a Security Trade-off, Not a Pure Improvement

The MV3 changes address real security problems:

- **Remote code ban** eliminates the supply-chain vector where an extension fetches malicious JS from an attacker-controlled CDN after passing store review. This was a genuine attack pattern.
- **Declarative rules** are statically inspectable by store reviewers and the browser, reducing the attack surface of network interception.
- **Sleeping service workers** reduce persistent background processes as persistent footholds.

But the trade-offs are real:

- **`declarativeNetRequest`** cannot replicate all of `webRequest`'s dynamic blocking capability. The practical consequence — uBlock Origin on Chrome being meaningfully weaker than uBlock Origin on Firefox — is the most visible user-facing impact.
- **No persistent state** forces complex state management workarounds (repeated `chrome.storage` reads, keeping service workers alive with `chrome.alarms` pings).
- **Rule count limits** in `declarativeNetRequest` constrain how many blocking rules an ad-blocker can apply simultaneously.

Firefox's decision to retain `webRequest` and support MV2 alongside MV3 is a deliberate policy choice, not a technical lag. It positions Firefox as the browser for users who want full-capability privacy extensions.

### 3. Content Scripts Are the Highest-Risk Code You Write

Content scripts have a uniquely dangerous security posture: they run with extension privileges but in the context of an untrusted web page. Two attack surfaces:

**Extension → Page attack:** A vulnerable content script that passes page data to `innerHTML`, `eval()`, or `chrome.scripting.executeScript()` creates an XSS bridge — an attacker who controls the page can escalate to extension-level privileges, potentially accessing all tabs, history, and cookies.

**Page → Extension attack via message spoofing:** If a content script listens on `chrome.runtime.onMessage` and acts on messages without validating the sender, a malicious web page can `window.postMessage` into the content script and trigger privileged extension actions. Always check `sender.origin` or `sender.tab.id` before acting on messages.

The same allow-list-over-block-list principle from server-side input validation applies here. See [[concepts/secure-input-validation]].

### 4. Supply Chain Is Now the Primary Extension Threat Vector

MV3's remote-code ban significantly raises the bar for post-install payload delivery but does not address the dominant real-world threat: **supply chain compromise via developer account takeover and silent update push**.

The ShadyPanda campaign (2025) demonstrated the full sophistication: a threat group spent **seven years** publishing and maintaining benign extensions to build user trust and install counts before flipping them to malware via silent updates. The attack required no zero-day, no code injection, no store bypass — only patience and then one credential compromise.

Defences:
- **Store-side**: better developer account MFA enforcement, anomaly detection on update content deltas
- **Developer-side**: 2FA on all store accounts, dependency auditing, minimal permissions so a compromised update has limited blast radius
- **User-side**: periodic permission audits, prefer extensions from organisations (not individuals) for critical use cases, use browser extension security scanning tools

### 5. WXT Is the Community Standard for New Projects

The cross-browser extension framework ecosystem has converged. As of 2025:

- **WXT** (Vite-based, framework-agnostic, auto-generates manifest, supports MV2+MV3+all-browsers from one codebase) is the consensus recommendation for new projects
- **Plasmo** remains strong for React-heavy UIs with its Shadow DOM component injection (CSUI) approach
- Raw boilerplate (no framework) is only advisable for very simple extensions or developers who need full control

The value proposition of a framework is primarily: **manifest generation from project structure** (eliminates a class of configuration bugs), **HMR during development** (hot-module replacement for popup and options pages), and **cross-browser build targets** (same source, different outputs for Chrome/Firefox).

---

## Cross-Domain Connections

### Browser Extensions ↔ Prompt Injection

The Cline/OpenClaw attack (February 2026) demonstrated the convergence of these two threat categories: a prompt injection payload in a Claude-powered GitHub Actions workflow compromised an npm package, which shipped inside an extension update, which then installed persistent daemons on ~4,000 developer machines. Extensions are a delivery and persistence layer for post-prompt-injection payloads in agentic AI systems. See [[concepts/prompt-injection]].

### Browser Extensions ↔ JavaScript Fundamentals

Extensions are plain JavaScript in every meaningful sense. The same async/await, Promises, ES modules, closures, and event-loop mental model applies. The one non-standard primitive is the message-passing API — but it is modelled on the browser's own `postMessage` + `addEventListener` pattern. A developer fluent in modern JavaScript can write a working extension in an afternoon; the learning curve is the browser-specific APIs and the isolated-world security model, not the language. See [[concepts/javascript-fundamentals]].

### Browser Extensions ↔ Web Security

Extensions extend the browser's security model in predictable ways: the extension origin (`chrome-extension://[id]/`) has its own CSP, its own cookie jar, and its own `same-origin policy` enforcement. Content scripts bridge the extension origin and the page origin under controlled conditions. Every injection point (DOM manipulation, message receipt, storage read) is an input validation surface identical in kind to server-side inputs — the same escaping, sanitisation, and allow-listing discipline applies. See [[concepts/web-security-and-devops]].

### Browser Extensions ↔ CI/CD

Publishing to the Chrome Web Store and Firefox AMO can be fully automated. The Chrome Web Store Publish API and `web-ext sign` (Firefox) accept signed packages via CI, with standard GitHub Actions workflows handling build → test → lint → publish. The same pipeline practices that apply to any web application (pinned dependency versions, `npm audit`, automated testing, secrets in CI environment variables) apply here. See [[concepts/github-actions-cicd]].

---

## Extension Mental Model — One Diagram

```
  ┌─────────────────────────────────────────────────────────┐
  │                    Browser Process                       │
  │                                                         │
  │  ┌──────────────────────┐   ┌───────────────────────┐  │
  │  │  Service Worker       │   │  Popup / Options Page │  │
  │  │  (Background)         │   │  (Extension Origin)   │  │
  │  │                       │   │                       │  │
  │  │  Full WebExt API      │   │  Full WebExt API      │  │
  │  │  No DOM               │   │  DOM of own page      │  │
  │  │  No persistent state  │   │  Short-lived          │  │
  │  └──────────┬────────────┘   └──────────┬────────────┘  │
  │             │   chrome.runtime.sendMessage              │
  │             │◄─────────────────────────►│              │
  │             │                            │              │
  │  ┌──────────▼───────────────────────────▼───────────┐  │
  │  │              Message Passing Bus                  │  │
  │  │    chrome.runtime / chrome.tabs.sendMessage       │  │
  │  └──────────────────────┬────────────────────────────┘  │
  │                         │                               │
  │  ┌──────────────────────▼────────────────────────────┐  │
  │  │              Content Script                       │  │
  │  │              (Isolated World)                     │  │
  │  │                                                   │  │
  │  │  DOM access (shared with page)                    │  │
  │  │  Separate JS heap (from page)                     │  │
  │  │  Limited WebExt API (runtime, storage only)       │  │
  │  └────────────────────────┬──────────────────────────┘  │
  │                           │ DOM reads/writes             │
  │  ┌────────────────────────▼──────────────────────────┐  │
  │  │              Web Page (Untrusted)                 │  │
  │  │              Normal JS sandbox                    │  │
  │  └───────────────────────────────────────────────────┘  │
  └─────────────────────────────────────────────────────────┘
```

---

## Open Questions / Gaps

- **Safari extension compatibility**: Safari's WebExtensions implementation diverges more than Firefox from Chrome — how difficult is full four-browser (Chrome, Firefox, Edge, Safari) compatibility in practice with WXT?
- **MV3 rule limits in practice**: `declarativeNetRequest` has a default limit of 30,000 static rules per extension. How do large ad-blocker lists (EasyList: ~70,000+ rules) work around this at scale?
- **Service worker persistence**: Chrome's service worker kill-and-restart lifecycle is inconsistent across OS and version — what is the reliable minimum state-persistence pattern for production extensions?
- **Automated store review evasion**: MV3 bans remote code execution, but attackers can still use runtime feature flags over legitimate HTTPS fetches to activate dormant payloads (payload delivery ≠ payload execution). How are stores detecting this post-MV3?

---

## Source Pages

- [FreeToolKit — Building Chrome Extensions in 2025: Manifest V3](https://www.freetoolkit.io/blog/building-chrome-extensions-2025-guide)
- [nitiweb.net — Building Browser Extensions in 2025: Tools and Architecture](https://nitiweb.net/blog/browser-extension-development-2025)
- [MDN Web Docs — WebExtensions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions)
- [Medium — MV2 vs MV3: What Changed and Why 2025 Was the Turning Point](https://medium.com/@idmossab/nifest-v2-vs-manifest-v3-chrome-extensions-what-changed-and-why-2025-was-the-turning-point-53b031b70fc6)
- [Pulsedive — Compromised Browser Extensions: A Growing Threat Vector (Jan 2025)](https://blog.pulsedive.com/compromised-browser-extensions-a-growing-threat-vector/)
- [DevKit.best — Chrome Extension Framework Comparison 2025](https://www.devkit.best/blog/mdx/chrome-extension-framework-comparison-2025)
- [The Hacker News — Browser Extension Risk Guide After ShadyPanda](https://thehackernews.com/2025/12/a-browser-extension-risk-guide-after.html)

**Primary concept page:** [[concepts/browser-extensions]]
