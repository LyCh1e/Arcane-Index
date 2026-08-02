---
type: concept
title: "Browser Extensions"
domain: web-development
complexity: high
tags: [browser-extensions, manifest-v3, webextensions, chrome, firefox, content-scripts, service-worker, javascript, security]
updated: 2026-07-28
status: established
created: 2026-07-28
related:
  - "[[concepts/web-fundamentals]]"
  - "[[concepts/javascript-fundamentals]]"
  - "[[concepts/web-security-and-devops]]"
  - "[[concepts/prompt-injection]]"
  - "[[concepts/secure-input-validation]]"
---

# Browser Extensions

A browser extension is a software package that extends or modifies the behaviour of a web browser. Extensions are built using standard web technologies — HTML, CSS, and JavaScript — exposed via the **WebExtensions API**, a cross-browser standard implemented by Chrome, Firefox, Edge, Opera, and Safari (with Safari divergences).

Extensions can: inject code into web pages, intercept and modify network requests, add toolbar buttons and popup UIs, store data persistently, communicate with native applications, manage tabs and windows, and run background logic triggered by browser events.

---

## The WebExtensions API Standard

The WebExtensions API was standardised to allow the same extension codebase to run across multiple browsers with minimal changes. Chrome uses the `chrome.*` namespace; Firefox supports both `browser.*` (Promise-based, canonical) and `chrome.*` (callback-based, for compatibility). The `webextension-polyfill` library from Mozilla normalises this difference.

**Browser support matrix:**

| Browser | API Namespace | Async Style | MV3 Required? | webRequest retained? |
|---------|-------------|-------------|--------------|---------------------|
| Chrome | `chrome.*` | Callbacks (Promises supported) | Yes (MV2 disabled July 2025) | No (declarativeNetRequest only) |
| Firefox | `browser.*` | Promises | No (MV2 still supported) | Yes (MV2 + MV3) |
| Edge | `chrome.*` | Callbacks | Yes | No |
| Safari | `browser.*` | Promises | Yes (own variant) | Partial |

---

## Architecture — Five Core Components

Every extension is a directory of files. The browser loads it from a `.zip` archive (renamed `.crx` for Chrome, `.xpi` for Firefox) or directly from disk during development.

```
my-extension/
├── manifest.json        ← blueprint; required
├── service-worker.js    ← background logic
├── content.js           ← injected into web pages
├── popup.html           ← toolbar button UI
├── popup.js
├── options.html         ← settings page
├── options.js
└── icons/
    ├── icon-16.png
    ├── icon-48.png
    └── icon-128.png
```

---

### 1. manifest.json

The manifest is the single required file. It declares every aspect of the extension: identity, permissions, which scripts run where, and which UI elements exist.

**Minimal MV3 manifest:**

```json
{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0.0",
  "description": "What the extension does.",
  "icons": {
    "16": "icons/icon-16.png",
    "48": "icons/icon-48.png",
    "128": "icons/icon-128.png"
  },
  "action": {
    "default_popup": "popup.html",
    "default_icon": "icons/icon-48.png"
  },
  "background": {
    "service_worker": "service-worker.js"
  },
  "content_scripts": [
    {
      "matches": ["https://*.example.com/*"],
      "js": ["content.js"],
      "run_at": "document_idle"
    }
  ],
  "permissions": ["storage", "activeTab", "scripting"],
  "host_permissions": ["https://*.example.com/*"]
}
```

**Key manifest fields:**

| Field | Purpose |
|-------|---------|
| `manifest_version` | Must be `3` for MV3 (Chrome mandatory since July 2025) |
| `permissions` | Named API permissions: `"storage"`, `"tabs"`, `"alarms"`, `"notifications"`, etc. |
| `host_permissions` | URL patterns the extension may access: `"*://*.example.com/*"`, `"<all_urls>"` |
| `optional_permissions` | Permissions requested at runtime (not installation) — reduces install friction |
| `background.service_worker` | Path to the background service worker script |
| `content_scripts` | Array of `{matches, js, css, run_at}` — declares what to inject and where |
| `action` | Toolbar button config: `default_popup`, `default_icon`, `default_title` |
| `options_page` / `options_ui` | Settings page shown in extension management |
| `content_security_policy` | Restricts what scripts and resources the extension may load |
| `web_accessible_resources` | Files inside the extension package that web pages may load |

---

### 2. Background Service Worker

The background script is the extension's event-driven engine. In MV3 it is a **service worker** — it activates in response to events and shuts down when idle. It has no access to the DOM of any web page, but has broad access to the WebExtensions API.

**Key characteristic — no persistent in-memory state.** Because the service worker can be killed and restarted at any time by the browser, any data stored in JavaScript variables is lost between activations. Use `chrome.storage` (see Storage section) for all state that must survive.

```javascript
// service-worker.js

// Fires when the extension is first installed or updated
chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed.');
  chrome.storage.local.set({ clickCount: 0 });
});

// Fires when the toolbar button is clicked (if no popup is defined)
chrome.action.onClicked.addListener((tab) => {
  chrome.tabs.sendMessage(tab.id, { action: 'highlight' });
});

// Listen for messages from content scripts or popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'fetchData') {
    fetch('https://api.example.com/data')
      .then(r => r.json())
      .then(data => sendResponse({ success: true, data }));
    return true; // keep channel open for async response
  }
});
```

**Events the service worker listens to:**

| Event | API |
|-------|-----|
| Extension install / update | `chrome.runtime.onInstalled` |
| Browser startup | `chrome.runtime.onStartup` |
| Toolbar button click | `chrome.action.onClicked` |
| Message from other contexts | `chrome.runtime.onMessage` |
| Tab created / updated / removed | `chrome.tabs.onCreated`, `.onUpdated`, `.onRemoved` |
| Scheduled alarm | `chrome.alarms.onAlarm` |
| Web request events | `chrome.declarativeNetRequest` rules (MV3) |
| Context menu item click | `chrome.contextMenus.onClicked` |

---

### 3. Content Scripts

Content scripts run **inside the context of a web page** — they can read and modify the page's DOM. They are isolated from the page's own JavaScript by a security boundary called the **isolated world**: the content script and the page share the same DOM tree but have separate JavaScript heaps, so they cannot access each other's variables or prototype chains.

Content scripts have **limited access** to the WebExtensions API — primarily `chrome.runtime.sendMessage` and `chrome.storage`. For anything more (e.g. `fetch` to cross-origin URLs, `chrome.tabs`) they must ask the background service worker via message passing.

```javascript
// content.js — injected into pages matching the manifest pattern

// Read and modify the DOM
document.querySelectorAll('a[href]').forEach(link => {
  link.style.color = 'red';
});

// Send a message to the background service worker
chrome.runtime.sendMessage({ type: 'pageLoaded', url: location.href }, (response) => {
  console.log('Background replied:', response);
});

// Listen for messages from the background / popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'highlight') {
    document.body.style.border = '3px solid orange';
  }
});
```

**Injection methods:**

| Method | How |
|--------|-----|
| **Declarative** | `content_scripts` in manifest — auto-injected on matching URLs |
| **Programmatic** | `chrome.scripting.executeScript()` called from service worker — injected on demand |

---

### 4. Popup (and Other UI)

The **popup** is an HTML page that opens when the user clicks the extension's toolbar button. It is a standard web page — HTML, CSS, JS — but runs in the extension's own isolated context (not inside any tab).

```html
<!-- popup.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="popup.css">
  </head>
  <body>
    <h1>My Extension</h1>
    <button id="go">Do something</button>
    <script src="popup.js"></script>
  </body>
</html>
```

```javascript
// popup.js
document.getElementById('go').addEventListener('click', async () => {
  // Query the active tab and send a message to its content script
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  chrome.tabs.sendMessage(tab.id, { action: 'highlight' });
});
```

**Other UI surfaces:**

| Surface | Description |
|---------|-------------|
| **Options page** | Full-page settings UI; opened via `chrome.runtime.openOptionsPage()` or extension management |
| **Sidebar** | Persistent panel alongside the page (Firefox-only: `sidebar_action`) |
| **DevTools panel** | Custom panel injected into browser DevTools |
| **Context menu** | Right-click menu items added via `chrome.contextMenus.create()` |
| **Notifications** | System-level notifications via `chrome.notifications` |
| **Omnibox** | Address-bar keyword triggers via `chrome.omnibox` |

---

### 5. Message Passing — The Communication Layer

Extension components (service worker, content scripts, popup, options page) run in separate contexts and cannot share memory. All communication goes through the browser's **message-passing APIs**.

#### One-shot messages (fire and forget / single response)

```javascript
// Sender (any context)
chrome.runtime.sendMessage({ type: 'getCount' }, (response) => {
  console.log(response.count);
});

// Receiver (any other context)
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'getCount') {
    chrome.storage.local.get('clickCount', (data) => {
      sendResponse({ count: data.clickCount });
    });
    return true; // CRITICAL: return true to keep the channel open for async sendResponse
  }
});
```

#### Sending a message specifically to a content script in a tab

```javascript
// From service worker or popup
chrome.tabs.sendMessage(tabId, { action: 'scrape' }, (response) => {
  console.log(response.data);
});
```

#### Long-lived connections (ports)

```javascript
// Content script opens a port
const port = chrome.runtime.connect({ name: 'stream' });
port.postMessage({ data: 'hello' });
port.onMessage.addListener((msg) => console.log('Got:', msg));

// Service worker listens for connections
chrome.runtime.onConnect.addListener((port) => {
  port.onMessage.addListener((msg) => {
    port.postMessage({ echo: msg.data });
  });
});
```

---

## Storage APIs

Because the service worker has no persistent state, `chrome.storage` is how extensions persist data across activations and sessions.

| API | Scope | Persists across | Limit |
|-----|-------|----------------|-------|
| `chrome.storage.local` | This browser install | Sessions, restarts | 10 MB (unlimitedStorage permission: ∞) |
| `chrome.storage.session` | This browser session | Service worker restarts | 10 MB |
| `chrome.storage.sync` | Google account | Devices (if logged in) | 100 KB total, 8 KB per item |
| `chrome.storage.managed` | Admin-configured | Sessions | Read-only by extension |

```javascript
// Write
chrome.storage.local.set({ theme: 'dark', count: 42 });

// Read
chrome.storage.local.get(['theme', 'count'], (result) => {
  console.log(result.theme, result.count);
});

// Listen for changes
chrome.storage.onChanged.addListener((changes, areaName) => {
  if (areaName === 'local' && changes.theme) {
    applyTheme(changes.theme.newValue);
  }
});
```

---

## Permissions Model

Extensions must declare all required permissions upfront in the manifest. The browser displays these to the user at install time, and the Chrome Web Store uses them in its review process.

**Permission categories:**

| Category | Examples | Risk to user |
|----------|---------|-------------|
| **API permissions** | `"storage"`, `"alarms"`, `"notifications"` | Low |
| **Sensitive API permissions** | `"tabs"`, `"webNavigation"`, `"history"`, `"cookies"` | Medium |
| **Host permissions** | `"*://*.example.com/*"`, `"<all_urls>"` | High — grants DOM and network access to matched sites |
| **Optional permissions** | Any permission requested at runtime via `chrome.permissions.request()` | User-consented at point of need |

`"<all_urls>"` grants access to every site the user visits — it is the broadest and most dangerous host permission, and its use is heavily scrutinised by store reviewers and security auditors.

---

## Manifest V3 vs Manifest V2

MV3 is now mandatory for Chrome (MV2 disabled July 24, 2025). Firefox continues to support MV2 alongside MV3 as of 2026.

| Aspect | MV2 | MV3 |
|--------|-----|-----|
| **Background execution** | Persistent background page (always-on) | Service worker (event-driven, sleeps when idle) |
| **In-memory state** | Survives indefinitely | Lost when service worker is suspended |
| **Network request interception** | `webRequest` API — full programmatic control, can block/modify arbitrarily | `declarativeNetRequest` — rule-based, declarative; `webRequest` for observation only (no blocking) |
| **Remote code execution** | Allowed (could fetch and `eval()` remote JS) | Banned — all executable code must ship inside the extension package |
| **Content Security Policy** | Configurable, `eval()` allowable | Strict default; `eval()` prohibited |
| **Scripting injection** | `chrome.tabs.executeScript()` | `chrome.scripting.executeScript()` |
| **Impact on ad blockers** | uBlock Origin full capability | uBlock Origin Lite — rule-based only; meaningfully reduced blocking power vs. the Firefox MV2 version |

**Why Google made the change:** Security (remote code ban closes a supply-chain attack vector), privacy (declarative rules are inspectable at review time), and performance (sleeping service workers use fewer resources than persistent background pages).

**Controversy:** Privacy advocates and ad-blocking extension developers argue that `declarativeNetRequest`'s rule-count limits and lack of dynamic request inspection make sophisticated content blocking impossible. Firefox's decision to retain `webRequest` in MV3 has made it the preferred browser for power-user privacy extensions.

---

## Cross-Browser Development

### API compatibility

Chrome uses `chrome.*`; Firefox supports `browser.*` (native Promises). The **`webextension-polyfill`** library (Mozilla) wraps the `chrome.*` callbacks in Promises so the same code works in both. Most differences are then minor:

- `browser.runtime.*` ↔ `chrome.runtime.*`
- Firefox `sidebar_action` has no Chrome equivalent
- Firefox `contextualIdentities` (container tabs) has no Chrome equivalent
- Chrome enterprise policy APIs have no Firefox equivalent

### Cross-browser frameworks (2025)

| Framework | Approach | Best for |
|-----------|---------|---------|
| **WXT** | Vite-based; auto-generates manifest from project structure; MV2+MV3 + all browsers from one codebase | New projects, framework-agnostic |
| **Plasmo** | React-first; Shadow DOM component injection; CSUI (Content Script UI) | React developers, UI-heavy extensions |
| **CRXJS** | Vite plugin only; minimal abstraction | Developers who want full control |
| **web-ext** (Mozilla) | CLI tool for building, linting, running, and packaging; not a framework | Firefox-first; cross-browser packaging |

**WXT is the community consensus pick for new projects in 2025** — it abstracts manifest generation, handles MV2/MV3 switching, and integrates with all major UI frameworks.

---

## Development Workflow

### Loading an unpacked extension (Chrome)

1. Go to `chrome://extensions`
2. Enable **Developer Mode** (top-right toggle)
3. Click **Load unpacked** → select the extension directory
4. Extension appears in the toolbar
5. Edit files → click the **refresh icon** on the extension card to reload

**Debugging:**
- **Service worker**: click the *"Service Worker"* link on the extension card → opens DevTools
- **Content script**: open DevTools on any page the content script is injected into → Sources → Content scripts
- **Popup**: right-click the toolbar icon → *Inspect popup*

### Loading in Firefox (temporary)

```bash
# Install web-ext globally
npm install -g web-ext

# Run extension in Firefox with hot reload
web-ext run

# Build distributable .zip
web-ext build

# Lint for compatibility issues
web-ext lint
```

### Build pipeline (typical WXT project)

```bash
npm create wxt@latest my-extension
cd my-extension
npm install
npm run dev          # dev mode with hot reload
npm run build        # production build
npm run zip          # creates distributable .zip
```

---

## Publishing

### Chrome Web Store

1. Create a developer account ($5 one-time registration fee)
2. Build a production `.zip` of the extension directory
3. Submit via the Chrome Web Store Developer Dashboard
4. Review process: **1–3 business days** for most extensions; longer for sensitive permissions
5. Automated + manual review; extensions with `<all_urls>` or `webRequest` receive extra scrutiny
6. After approval, updates push to users automatically

### Firefox Add-ons (AMO)

1. Create a developer account (free)
2. Build with `web-ext build`
3. Submit `.zip` at [addons.mozilla.org](https://addons.mozilla.org/developers/)
4. Code signing is mandatory for public distribution
5. Unlisted extensions (for private/enterprise use) are signed automatically without review
6. Listed extensions undergo manual review

---

## Security Model and Threat Landscape

### Extension security properties

- Extensions run in a **privileged origin** (`chrome-extension://[id]/`), isolated from web pages
- Content scripts run in an **isolated world** — they share the DOM but not the JS heap with the page; the page cannot read extension variables
- Extensions can only use APIs their manifest declares — permissions are enforced by the browser at the API call level
- MV3's remote code ban prevents dynamically fetched and executed payloads

### Attack surface

| Vector | Description |
|--------|-------------|
| **Overpermissioned extension** | A legitimate extension with `<all_urls>` can read all page content, intercept form submissions, and exfiltrate credentials from every site |
| **Supply chain compromise** | Developer account phished; attacker pushes malicious update through the trusted store update channel — users auto-update silently |
| **Malicious extension in store** | Extension publishes benign behaviour during review, later activates malicious code from a remote flag (now harder with MV3's remote-code ban) |
| **Long-con acquisition** | Attacker purchases a high-install extension after it builds trust over years, then pushes weaponised update (ShadyPanda campaign, 2025: 7-year operation) |
| **Content script XSS** | Content script trusts injected page data and passes it to `innerHTML` or `eval()`, creating an XSS bridging extension privileges |

### Real-world incidents (2025–2026)

| Incident | Detail |
|----------|--------|
| **35+ extensions compromised (Dec 2024 – Jan 2025)** | Phishing campaign against Chrome extension developers; injected data-stealing malware into extensions with millions of users |
| **ShadyPanda campaign** | Threat group spent 7 years publishing benign extensions to accumulate installs and trust, then flipped them to malware via silent update |
| **Malwarebytes "SpyStore" campaign (mid-2025)** | Malicious extensions in official Chrome and Edge stores spied on millions of users |
| **Cline/OpenClaw prompt injection → extension supply chain (Feb 2026)** | Prompt injection in a Claude-powered GitHub Actions workflow led to ~4,000 developer machines compromised via extension update (see [[concepts/prompt-injection]]) |

### Secure extension development checklist

- Request the minimum permissions necessary; use `optional_permissions` for non-core features
- Never use `<all_urls>` unless truly required
- Sanitise all content received from web pages before processing in the content script
- Never pass untrusted page content to `innerHTML`, `eval()`, or `chrome.scripting.executeScript()`
- Pin dependencies and audit with `npm audit` / `web-ext lint`
- Enable 2FA on the Chrome Web Store and Firefox AMO developer accounts — supply chain attacks target developer credentials
- Review all dependencies for privilege escalation risks — a malicious npm package in the build can ship arbitrary code inside the extension

---

## Key WebExtensions APIs — Quick Reference

| API | What it does |
|-----|-------------|
| `chrome.runtime` | Messaging, lifecycle, extension identity |
| `chrome.storage` | Persistent key-value storage (local, sync, session, managed) |
| `chrome.tabs` | Query, create, update, close tabs; inject scripts |
| `chrome.scripting` | Programmatic content script injection (MV3) |
| `chrome.declarativeNetRequest` | Rule-based network request blocking/modification (MV3) |
| `chrome.webRequest` | Observe (not block) network requests (MV3 Chrome); full interception (Firefox) |
| `chrome.alarms` | Schedule periodic or one-time callbacks — survives service worker restart |
| `chrome.notifications` | System-level desktop notifications |
| `chrome.contextMenus` | Add items to the browser right-click menu |
| `chrome.identity` | OAuth 2.0 authentication flows |
| `chrome.cookies` | Read, write, monitor cookies |
| `chrome.bookmarks` | Manage browser bookmarks |
| `chrome.history` | Access browsing history |
| `chrome.downloads` | Monitor and control downloads |
| `chrome.omnibox` | Register an address-bar keyword trigger |
| `chrome.devtools` | Add panels to browser DevTools |

---

## Connections to Other Vault Concepts

| Page | Relationship |
|------|-------------|
| [[concepts/javascript-fundamentals]] | Extensions are pure JavaScript (+ HTML/CSS); async/await, Promises, ES modules all apply directly |
| [[concepts/web-fundamentals]] | Extensions operate on the same DOM, HTTP, and CSP model as standard web pages |
| [[concepts/web-security-and-devops]] | Extension CSP, XSS bridging via content scripts, and the `same-origin policy` as it applies to extensions |
| [[concepts/prompt-injection]] | The Cline/OpenClaw attack (Feb 2026) chained prompt injection → extension supply chain compromise |
| [[concepts/secure-input-validation]] | Content scripts must treat all data from the page as untrusted; the same allow-list principles apply |
| [[concepts/github-actions-cicd]] | Extension CI/CD pipelines use standard GitHub Actions patterns; `web-ext lint` and automated store publishing via the Chrome Web Store API |
