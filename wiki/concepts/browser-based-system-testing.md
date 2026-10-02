---
type: concept
status: established
created: 2026-10-02
updated: 2026-10-02
name: browser-based-system-testing
description: Browser-based functional system testing with Selenium WebDriver — where it sits among test levels, the WebDriver architecture and Selenium Manager, flakiness and explicit waits, stable locators, Page Objects, independence/headless/cross-browser, app-hosting ownership, CI orchestration, and what it cannot prove
metadata:
  type: concept
  domain: software-engineering
  course: ICT3112
  tags: [selenium, webdriver, browser-testing, system-testing, end-to-end-testing, page-object, explicit-wait, flaky-tests, locators, headless, cross-browser, selenium-grid, ci]
---

# Browser-based system testing (Selenium)

Source: [[sources/ict3112-svv-lab4]] · Worked example: [[examples/ict3112-lab4-selenium-browser-testing]] · Related: [[concepts/software-testing-fundamentals]], [[concepts/test-doubles-and-dependency-injection]], [[concepts/github-actions-cicd]], [[concepts/docker-compose]] (Selenium Grid compose), [[concepts/blackbox-testing-techniques]].

## 1. Where it sits — the label depends on the boundary
- A browser test checks that **the rendered page, client JS, HTTP endpoint and domain logic cooperate** through the interface a person uses. It catches broken element wiring, bad routes and response rendering, none of which a unit test can see.
- Driving browser → JS → local server → domain class is a **browser-based functional system test**. It is **end-to-end** only if the route spans the whole defined production-like boundary (auth, DB, payments…).
- **Acceptance ≠ browser testing ≠ UAT.** Acceptance tests can run against domain, API or UI. UAT is acceptance done by intended users.
- **Level vs technique are separate axes.** Levels describe scope (unit/component, component integration, system, system integration, acceptance). Black-box and white-box describe how cases are derived. Browser tests are usually black-box *by boundary*, but the code still knows locators.
- **Portfolio:** many unit, fewer integration, a *few* browser journeys. The pyramid is a guiding model, not a mandated ratio (see [[concepts/software-testing-fundamentals]]). Put EP/BVA cases in unit tests and keep the browser suite to the representative primary and alternative flows.

## 2. WebDriver architecture
`test (NUnit) → language binding (IWebDriver, By, WebDriverWait) → browser driver (WebDriver protocol) → browser (loads, runs JS, renders)`
- **Selenium Manager** (Selenium 4.6+) finds the installed browser, resolves and caches a matching driver, and can **download the browser itself** if it is missing (observed with Firefox, Selenium 4.50). There is no driver NuGet, no driver binary in the repo and no path. The first run is slow and needs network access.
- The *browser driver* here is not the *test driver* used in bottom-up integration ([[concepts/test-doubles-and-dependency-injection]]).

## 3. Flakiness and waits
- **Flaky test:** passes or fails with no relevant change to code or expectation. Timing assumptions are the classic cause.
- `Thread.Sleep(n)` wastes time when the app is fast and still fails when it is slow.
- An **explicit wait** (`WebDriverWait.Until(condition)`) polls an *observable condition* until true or timeout, and proceeds as soon as the state is reached.
- An **implicit wait** only retries *element lookup*. It is useless when the element exists and only its text or state changes. Don't mix implicit and explicit waits (combined timeouts become unpredictable).
- Demonstration: a 300 ms server delay plus removing the sleep → the result was read as empty in 3/3 runs. With a wait on non-empty text it passed 3/3.

## 4. Locators
Ranked from fragile to stable: absolute XPath tied to DOM position, then styling CSS classes, then id, accessible role/name, and `data-testid`. A `data-testid` is a **team contract** that keeps its meaning, like a public API route. Keep visible labels accessible as well.

## 5. Page Object pattern
- A class representing a page (or part of one) through the **services** it offers (`Open`, `Calculate`, `WaitForResult`, `WaitForError`).
- It **owns** locators (`static readonly By`), interaction and waits, and returns values.
- The **test owns** the inputs, the definition of "correct" and the assertion. **No assertions inside the Page Object.** Aim for one focused outcome assertion per test.
- Payoff: a markup change is repaired in one class, and tests read in domain language. In BDD, a Reqnroll step may call the Page Object, but the Gherkin still describes behaviour, not clicks.

## 6. Independence, headless and cross-browser
- **Fresh browser per test** (SetUp/TearDown) removes cookies, storage and crashed sessions. It does **not** reset server-side state (DB, accounts, queues). That needs data isolation.
- **Headless** (`--headless=new` + window size for Chrome, `-headless` for Firefox) changes display only. It is still a real engine running JS, so the evidence scope is unchanged. It is the default for CI.
- **Cross-browser:** select high-value journeys based on the supported user base and browser-specific risk. A `BrowserFactory` reading an env var avoids duplicating fixtures.
- **Parallelism** comes only after tests and data are isolated. Otherwise it is a new source of flakiness, and browsers are CPU and memory hungry.

## 7. Hosting the application under test — ownership
- "The browser started" is not evidence that the app is up. `ERR_CONNECTION_REFUSED` means the browser works and no server is listening.
- **Self-hosted mode:** `new WebApplicationFactory<Program>().UseKestrel(0)` (.NET 10) runs the real app on **real Kestrel** at an OS-chosen loopback port. The default TestServer is in-memory and unreachable from a browser. Poll `/` for readiness, dispose in `[OneTimeTearDown]`. This needs `public partial class Program {}` in a top-level-statement app.
- **External mode:** a base-URL env var means validate it as an absolute http(s) URL, poll it, and **never stop it**.
- **Rule:** dispose only what you created.
- **Diagnosis split:** an unreachable server fails in OneTimeSetUp, *before* any browser. Browser or driver startup fails in SetUp (`WebDriverException`/`SessionNotCreatedException`) after the server responded.

## 8. CI orchestration
1. Build once (Release).
2. Run non-browser tests: `dotnet test --filter "TestCategory!=Browser"`. Projects with only browser tests print "No test matches", which exits 0.
3. Start the app in the background: `dotnet run --no-build --no-launch-profile &`. `--no-launch-profile` stops `launchSettings.json` overriding `ASPNETCORE_URLS`. Add `trap 'kill $pid' EXIT`.
4. Run a curl readiness loop. This is orchestration, not an assertion, and it should `cat` the server log on timeout.
5. Run the browser tests headless with the base URL set.
- Check that **both groups were discovered** in the log. A green tick with 0 browser tests is not a pass. Never fix an infrastructure failure by deleting or filtering out the browser tests.

## 9. Limits — what a passing journey doesn't prove
Visual correctness, accessibility conformance, performance, security, every device/browser/version, usability, and real production dependencies. Each needs its own oracle and tooling. Browser automation **complements** unit, exploratory and non-functional testing.

## 10. Grid and Docker
**Selenium Grid** routes WebDriver commands to remote browser nodes (parallel, multi-browser/OS). **docker-selenium** images package the hub and nodes (compose example in [[concepts/docker-compose]]). Adopt them when local and CI browsers diverge, a remote farm is needed, or repeatable infrastructure outweighs the added images, networking and ports. Switch to `RemoteWebDriver` only then. Check ARM64 image availability.
