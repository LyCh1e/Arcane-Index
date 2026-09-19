---
type: example
status: established
created: 2026-09-19
updated: 2026-09-19
name: ict3112-lab3-ci-and-dependencies
description: ICT3112 SVV Lab 3 — GitHub Actions CI for the .NET 10 calculator solution, plus a FileReader dependency tested three ways (real-file integration tests, IFileReader parameter injection, Moq unit tests)
metadata:
  type: example
  domain: software-engineering
  course: ICT3112
  tags: [github-actions, ci, dotnet, nunit, moq, dependency-injection, integration-testing, regression-testing, csharp, lab]
---

# ICT3112 SVV Lab 3 — CI + testing with dependencies

**Lab file:** `Labs/Lab 3/Lab3_ContinuousIntegration_TestingDependencies.pdf`
**Built solution:** `Labs/Lab 3/SOFTEST_INTRO_Labs/` (copy of Lab 2's, own Git repo, `main`, 3 commits) · **Answers:** `Labs/Lab 3/LAB3_NOTES.md`
Builds on [[examples/ict3112-lab1-nunit-tdd-calculator]] and [[examples/ict3112-lab2-reqnroll-bdd]]. Concepts: [[concepts/test-doubles-and-dependency-injection]], [[concepts/github-actions-cicd]].

## Result

| Project | Tests |
|---|---|
| UnitTests | 75 (70 from Lab 1/2 + 5 new Moq tests) |
| IntegrationTests (new) | 4 |
| AcceptanceTests | 23 = 20 pass + 3 skipped (Lab 2 §7 `@ignore`d rows) |

Baseline before changes was 93 (70 + 23); now 102. Git commit sequence mirrors the handout: baseline → CI workflow → dependency changes.

## Part I — CI

`.github/workflows/dotnet.yml` (verbatim from handout): `on: push, pull_request`; `permissions: contents: read`; ubuntu-latest → `actions/checkout@v7` → `actions/setup-dotnet@v5` (`10.0.x`) → `dotnet restore` → `build --configuration Release --no-restore` → `test --no-build --verbosity normal`. Solution-level commands mean the IntegrationTests project is picked up automatically once it is in the `.sln`.

At `--verbosity normal` the summary format is `Total tests: N / Passed: N` per project — that is what to look for in the Actions log to prove tests were *discovered* (a green tick with 0 tests proves nothing).

Deliberate regression (§6) reproduced on a throwaway clone: `[TestCase(-3, 8, 5)]` changed to `6` gave `Failed Add_RepresentativeInputs_ReturnsSum(-3,8,6)` / `Expected: 6.0d … But was: 5.0d`. CI reports a *disagreement*; requirements decide which side is wrong.

## Part II — the dependency arc

1. **Tightly coupled:** `GenMagicNum(int choice, string path)` does `new FileReader()` internally → only testable with a real file → the first tests are **integration** tests (Calculator + FileReader + OS file system), using `Path.GetTempFileName()` (portable to Ubuntu CI, no absolute paths); `SetUp` writes `42`/`-7`, `TearDown` deletes.
2. **Inject:** `IFileReader` + `GenMagicNum(int, string, IFileReader)` with `ArgumentNullException.ThrowIfNull`. The integration tests then failed to **compile** (`CS7036`) — build feedback, not a behavioural failure — until they passed a real `FileReader`.
3. **Isolate:** Moq (added to UnitTests only, 4.20.72) — `Setup(r => r.Read("MagicNumbers.txt")).Returns(new[]{"42","-7"})`; result tests (stub role) + `Verify(..., Times.Once())` (mock role).

Semantics: returns `2 * |line[choice]|`; index `< 0` or `>= length` throws `ArgumentOutOfRangeException`. Whole-number strings only (`double.Parse` is culture-sensitive).

## Status caveat

Not yet published to GitHub, so the hosted-runner run of §5/§14 is **unobserved**. Instead, the workflow's exact three commands were run on a fresh clone (0 warnings/errors, all 102 tests discovered). See [[learning/ict3112-lab3-tooling-gotchas]].
