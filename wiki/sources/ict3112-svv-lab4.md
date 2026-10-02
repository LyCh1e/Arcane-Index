---
type: source
title: "ICT3112 SVV — Lab 4: Browser-based System Testing with Selenium"
source_file: "raw/ICT3112 Software Verification and Validation - Lab4_BrowserBasedSystemTesting.md"
domain: software-verification-validation
tags: [ict3112, svv, lab, selenium, webdriver, system-testing, browser-testing, page-object, explicit-wait, flaky-tests, aspnetcore, github-actions, test-levels]
created: 2026-10-02
---

# Source Index — ICT3112 SVV Lab 4: Browser-based System Testing (Selenium)

Course: **ICT3112 Software Verification and Validation** · Lab handout, 20 pages (`Labs/Lab4/Lab4_BrowserBasedSystemTesting.pdf`).
Stack: C# · .NET 10 · ASP.NET Core minimal API · NUnit · Selenium WebDriver · GitHub Actions · Windows/macOS.
Concept page: [[concepts/browser-based-system-testing]] · Worked solution: [[examples/ict3112-lab4-selenium-browser-testing]] · Builds on [[examples/ict3112-lab3-ci-and-dependencies]].

**Injection check:** text, metadata, annotations (13 reference links only), embedded files, white/tiny text and spaced-out letters all checked. The handout is clean (see [[learning/prompt-injection-in-lab-handout-pdf]]).

---

## Learning outcomes (10)

1. Relate unit, integration, acceptance, system, browser UI and end-to-end testing without treating their labels as interchangeable.
2. Create a small ASP.NET Core web boundary around the existing calculator.
3. Explain how test → WebDriver binding → browser driver → browser cooperate.
4. Create NUnit browser tests without downloading or pinning driver executables (Selenium Manager).
5. Use stable locators and explicit waits to reduce fragility.
6. Apply a Page Object (page structure separate from assertions).
7. Keep tests independent; run visible, headless and cross-browser.
8. Start, validate and dispose the app automatically, while keeping an externally hosted mode for CI.
9. Integrate a small browser suite into GitHub Actions.
10. Explain why browser tests should be fewer and more selective than unit tests.

---

## Theory sections

### What each kind of test establishes

| Test | Primary evidence | Does **not** establish alone |
|---|---|---|
| Unit | A focused rule behaves correctly under controlled inputs/dependencies | That the deployed/rendered system works through its external interface |
| Integration | Selected components (or component + real dependency) work together | That every component and journey works as a complete system |
| Acceptance | An agreed example of required behaviour is satisfied | A particular technical layer — need not use a browser |
| Browser UI / system | The integrated local system behaves through its browser interface | That every production service/external dependency is present |
| End-to-end | A complete representative journey works across the defined production-like boundary | That all journeys, failures or qualities were examined |

- **Labels depend on the boundary.** Browser → JS → local server → `Calculator` is a *browser-based functional system test*. It is not automatically end-to-end, because auth, DB or payments would widen the route.
- Black-box describes the chosen **test boundary**. The automation code still contains technical detail (locators).
- **Test pyramid** = a guiding model, *not* a required ratio. The balance depends on system, risk and evidence needed.
- **Test level vs design technique** (ISTQB CTFL 4.0.1 §2.2.1): levels = scope/objective (component, component integration, system, system integration, acceptance). White-box and black-box = how cases are derived. A unit can be tested with either.
- **Acceptance ≠ browser ≠ UAT.** Acceptance can go through domain, API or UI. UAT is one form of it, done by intended users. Lab 2 Reqnroll = automated acceptance-level. Lab 4 Selenium = browser-based functional system tests.
- BDD ≠ browser automation. Gherkin describes behaviour, not a transcript of clicks.

### Test the system you control
The old Selenium lab drove Google's calculator. A third party's HTML, consent prompts, localisation, experiments and rate limits change without our code changing. Our own page gives a **contract**: accessible labels plus `data-testid` hooks the team agrees to preserve (like a public API). EP/BVA cases belong in unit tests. The browser suite keeps only the representative primary flow (2+3) and alternative flow (÷0).

### Selenium WebDriver architecture
| Part | Responsibility |
|---|---|
| NUnit test | Describes the action, makes the assertion |
| .NET binding | `IWebDriver`, `By`, `WebDriverWait` |
| Browser driver | Translates WebDriver protocol commands for the browser |
| Browser | Loads the page, runs JS, renders the UI |

**Selenium Manager** discovers the browser, resolves and caches a compatible driver. No ChromeDriver NuGet, no driver in the repo, no hard-coded path. The first run is slower and may need network access. "Browser driver" ≠ the *test driver* of top-down/bottom-up integration.

### Hosting and resource ownership
A browser can navigate only once a server is listening. `net::ERR_CONNECTION_REFUSED` means the browser works but nothing is accepting connections. Two modes: no `SOFTEST_INTRO_BASE_URL` → the fixture **owns** the app (`WebApplicationFactory` + `UseKestrel(0)`, readiness check, dispose after the fixture). Set → validate and check the external app, **never stop it**. *A test disposes only resources it created.*

### Sleepless tests
Flaky = can pass and fail with no relevant change. `Thread.Sleep(1000)` is too slow when the result is fast and too short when the machine is slow. An **explicit wait** polls a meaningful condition up to a timeout. Do not mix broad implicit waits with explicit ones (unpredictable timeouts). An implicit wait doesn't help here because the element exists and only its text changes.

### Locators and Page Objects
Absolute XPath and styling classes break on harmless redesign. A stable id, accessible role/name or `data-testid` is resilient and shows intent. A Page Object offers page *services* (`Calculate`, `WaitForResult`). It locates, interacts and waits. The **test** decides correctness and asserts. Keep one focused outcome assertion per test.

### Independence, headless and cross-browser
A fresh browser per test gives a clean session but not a clean server (DB, accounts, messages). Headless changes display, not evidence scope (still dynamic testing), and suits CI. Cross-browser: choose a compact set of high-value journeys by user base and browser-specific risk. Don't parallelise until tests and data are isolated.

### CI orchestration
CI deliberately uses the external mode. Order: run non-browser tests (`--filter "TestCategory!=Browser"`), start the Web project with `--no-launch-profile` (so `launchSettings.json` can't override `ASPNETCORE_URLS`), run a curl readiness loop (orchestration, not an assertion, and it prints the server log on timeout), run headless WebUiTests, then `trap` kills the server. Don't "fix" a browser infrastructure failure by deleting tests or filtering them out.

### What Selenium does not replace
Visual perfection, accessibility conformance, performance, security, all-device compatibility. Each needs its own oracle, technique and tooling. **Grid** routes WebDriver commands to remote browsers (parallel, multi-browser/OS). **Docker** images make Grid and browsers repeatable. Both are deliberately not used here: they are worth it only when local and CI environments diverge, a remote Grid is needed, or repeatability outweighs the complexity. On ARM64, check image architecture.

---

## Practical steps (15)

| Part | Steps |
|---|---|
| I — web boundary | 1 baseline · 2 `dotnet new web` + ref Calculator · 3 `Program.cs` (raw-string page, `/calculate` with 300 ms delay, `public partial class Program {}`) · 4 run on `127.0.0.1:5074` with `--no-launch-profile` |
| II — Selenium | 5 NUnit `WebUiTests` (ref Web only; Mvc.Testing, Selenium.WebDriver, Selenium.Support) · `CalculatorApplicationHost` · 6 first test with sleep + wrong expected 6 (red → 5) · 7 remove sleep (race) → explicit wait · 8 `CalculatorPage` · 9 refactor, add ÷0 test · 10 `HEADLESS=true` · 11 `BrowserFactory` (`SOFTEST_INTRO_BROWSER`) |
| III — CI | 12 two-stage workflow · 13 push, confirm both groups discovered · 14 deliberate 5→6 CI failure then restore · 15 final checklist |

Optional continuations: bind one Reqnroll scenario to `CalculatorPage`; screenshots and logs on failure as CI artifacts; a Chrome+Firefox smoke matrix with cost recorded; `RemoteWebDriver` only once a Grid exists.

## End-of-part questions
Part I (5), Part II (8), Part III (7). Answers are in `Labs/Lab4/LAB4_NOTES.md`, summarised in [[examples/ict3112-lab4-selenium-browser-testing]].
