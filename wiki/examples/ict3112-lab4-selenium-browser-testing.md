---
type: example
status: established
created: 2026-10-02
updated: 2026-10-02
name: ict3112-lab4-selenium-browser-testing
description: ICT3112 SVV Lab 4 — ASP.NET Core minimal-API page around the calculator, Selenium WebDriver NUnit tests with explicit waits, a Page Object, WebApplicationFactory.UseKestrel(0) self-hosting vs an external SOFTEST_INTRO_BASE_URL, and a two-stage GitHub Actions workflow
metadata:
  type: example
  domain: software-engineering
  course: ICT3112
  tags: [selenium, webdriver, nunit, page-object, explicit-wait, flaky-tests, aspnetcore, webapplicationfactory, github-actions, system-testing, csharp, lab]
---

# ICT3112 SVV Lab 4 — Browser-based system testing (Selenium)

**Lab file:** `Labs/Lab4/Lab4_BrowserBasedSystemTesting.pdf` · **Solution:** `Labs/Lab4/SOFTEST_INTRO_Labs/` · **Answers:** `Labs/Lab4/LAB4_NOTES.md`
Builds on [[examples/ict3112-lab3-ci-and-dependencies]]. Source: [[sources/ict3112-svv-lab4]]. Concepts: [[concepts/browser-based-system-testing]], [[concepts/software-testing-fundamentals]], [[concepts/github-actions-cicd]].

## Shape
- `SOFTEST_INTRO_Calculator.Web`: `dotnet new web`, one raw-string HTML page (`data-testid` hooks) + `GET /calculate` that `await Task.Delay(300)` then calls `Calculator.DoOperation`; `ArgumentException` → 400 `"The calculation was rejected."`. Ends with `public partial class Program { }` so tests can host it.
- `SOFTEST_INTRO_Calculator.WebUiTests` (NUnit, references **Web only**): `CalculatorApplicationHost`, `CalculatorPage` (Page Object), `BrowserFactory` (`SOFTEST_INTRO_BROWSER`, `HEADLESS`), `CalculatorBrowserTests` (`[Category("Browser")]`, 2 tests).
- Packages from current templates: Selenium.WebDriver/Support 4.50.0, Mvc.Testing 10.0.12. No driver package — Selenium Manager resolves it.

## Reusable patterns
- **Two hosting modes in one fixture.** Env var unset → `new WebApplicationFactory<Program>(); factory.UseKestrel(0); factory.CreateClient()` gives a *real* Kestrel on an OS-chosen loopback port (browser can reach it, unlike the default TestServer); readiness-poll `/` 20×250 ms; dispose in OneTimeTearDown. Env var set → validate absolute http(s) URL, poll it, **never stop it** (ownership rule).
- **Fresh browser per test** ([SetUp]/[TearDown]), one app per fixture ([OneTimeSetUp]).
- **Explicit wait on the observable condition** (`WebDriverWait.Until(d => !string.IsNullOrWhiteSpace(d.FindElement(Result).Text))`). Implicit waits don't help — the span exists, its text changes later.
- **Page Object** holds locators/actions/waits and returns strings; tests own the assertion.
- **CI:** build once (Release) → `dotnet test --filter "TestCategory!=Browser"` → bash step: `dotnet run --no-build --no-launch-profile &`, `trap kill EXIT`, curl readiness loop that `cat`s the server log on timeout, then `dotnet test WebUiTests` headless. `--no-launch-profile` stops `launchSettings.json` overriding `ASPNETCORE_URLS`.

## Observed evidence
- Baseline 102 → final **104** (75 unit + 4 integration + 23 acceptance [3 skipped] + 2 browser).
- Red first: expected "6" → `But was: "5"`. Removing `Thread.Sleep(1000)` → `But was: <string.Empty>` in 3/3 runs; explicit wait → 3/3 green.
- Firefox **not installed** still passed: Selenium Manager 4.50 downloaded a Firefox build (first run 72 s vs 4 s Chrome).
- Unreachable `SOFTEST_INTRO_BASE_URL` fails in OneTimeSetUp ("not reachable … unset SOFTEST_INTRO_BASE_URL") before any browser starts — the clean split between server-down and browser-startup failures.
- `--filter "TestCategory!=Browser"` prints "No test matches" for WebUiTests but exits 0.
- Monorepo adaptation: repo-root workflow uses `defaults.run.working-directory: Lab4/SOFTEST_INTRO_Labs`. Not pushed; the workflow commands were replayed on a clean copy in `%TEMP%\l4ci` (short path — see [[learning/ict3112-lab3-tooling-gotchas]]).
