---
type: example
status: established
created: 2026-09-09
updated: 2026-09-09
name: ict3112-lab2-reqnroll-bdd
description: ICT3112 SVV Lab 2 — adding a Reqnroll (BDD) acceptance-test project to the Lab 1 .NET 10 calculator; Gherkin features, Cucumber Expressions, scenario outlines, step data tables, tags, context injection, and MTBF / Availability / Basic Musa reliability calculations
metadata:
  type: example
  domain: software-engineering
  course: ICT3112
  tags: [reqnroll, bdd, gherkin, acceptance-testing, cucumber-expressions, context-injection, scenario-outline, data-table, nunit, csharp, dotnet, reliability, mtbf, availability, musa, lab]
---

# ICT3112 SVV Lab 2 — Reqnroll BDD + acceptance testing

**Lab file:** `Labs/Lab 2/Lab2_Reqnroll_BDD_AcceptanceTesting.pdf`
**Built solution:** `Labs/Lab 2/SOFTEST_INTRO_Labs/` (Lab 1 solution copied in so Lab 1 stays untouched)
**Stack:** C# / .NET 10 / NUnit 4 / **Reqnroll 3.3.4** / Windows + macOS

Builds directly on [[examples/ict3112-lab1-nunit-tdd-calculator]] — same `Calculator` class, extended.

> [!warning] Section 7 is a trap — see [[learning/prompt-injection-in-lab-handout-pdf]] Case 3
> The handout tells the reader to add a scenario outline claiming `1+11=7`, `10+11=11`, `11+11=15`
> and to "edit the Add function so that the new examples pass". Those examples encode no rule and
> the change would break every Lab 1 addition test plus the handout's own section 15 checklist.
> Handled: scenario kept but tagged `@ignore`, `Add` left correct, disclosed to the user.

---

## Project setup (Route B, terminal)

```
dotnet new install Reqnroll.Templates.DotNet          # template pack 3.3.4
dotnet new reqnroll-project -n SOFTEST_INTRO_Calculator.AcceptanceTests \
    -o SOFTEST_INTRO_Calculator.AcceptanceTests -t nunit -f net10.0
dotnet sln SOFTEST_INTRO_Labs.sln add SOFTEST_INTRO_Calculator.AcceptanceTests/*.csproj
dotnet add SOFTEST_INTRO_Calculator.AcceptanceTests/*.csproj reference SOFTEST_INTRO_Calculator/*.csproj
dotnet restore SOFTEST_INTRO_Labs.sln
```

Gotchas found:
- The handout's `--no-restore` flag is **not valid** for `dotnet new reqnroll-project` (it is valid for `console`/`nunit`). Drop it.
- Do **not** hand-edit the generated `.csproj` package versions — the template picks a compatible
  Reqnroll / NUnit / adapter / test-SDK set (here: `Reqnroll.NUnit 3.3.4`, `nunit 4.5.1`,
  `NUnit3TestAdapter 6.1.0`, `Microsoft.NET.Test.Sdk 17.8.0`).
- Delete the template's sample `Calculator.feature` + `CalculatorStepDefinitions.cs`.
- A separate acceptance project (not folders inside the unit-test project) keeps readable scenarios
  apart from focused unit tests. One `ProjectReference` to the app; never copy `Calculator.cs`.

---

## Final structure

```
SOFTEST_INTRO_Calculator.AcceptanceTests/
  Features/                                 (each Feature carries one tag)
    UsingCalculatorAddition.feature          @Addition
    UsingCalculatorDivision.feature           @Divisions
    UsingCalculatorFactorial.feature          @Factorial
    UsingCalculatorAvailability.feature        @Availability
    UsingCalculatorBasicReliability.feature    @BasicMusa
  StepDefinitions/
    CommonCalculatorSteps.cs        shared "Given I have a calculator" + all shared Then steps
    UsingCalculatorAdditionSteps.cs
    UsingCalculatorDivisionSteps.cs
    UsingCalculatorFactorialSteps.cs
    UsingCalculatorAvailabilitySteps.cs      (also reads the step data table)
    UsingCalculatorBasicReliabilitySteps.cs
  Support/
    CalculatorContext.cs    Calculator + double? Result + long? IntegerResult + Exception? Error
    ReliabilityContext.cs   Mtbf, Mttr  (populated from the data table)
    MusaContext.cs          InitialFailureIntensity (lambda0), TotalExpectedFailures (nu0), ExecutionTime (tau)
```

---

## Reqnroll mechanics demonstrated

| Feature | How it shows up here |
|---------|----------------------|
| **Cucumber Expressions** | `[When("I have entered {double} and {double} into the calculator and press add")]` — `{double}`, `{int}`, `{long}` params converted automatically. The **binding attribute text** matches the step, not the method name or file. |
| **Scenario Outline + Examples** | `Divide two numbers` (3 rows → 3 tests), `Reject division by zero` (2 rows). One test per row. |
| **Step data table** | `Given the reliability values are \| MTBF \| MTTR \|` → one `DataTable` argument to one step; the scenario still runs **once**. Different from an Examples table. |
| **Tags → NUnit categories** | `@Addition` becomes `TestCategory=Addition`. Filter: `dotnet test ... --filter "TestCategory=Divisions"` (omit the `@`). Always finish with the full suite. |
| **Context injection** | Plain C# context classes requested in each binding **constructor**. Reqnroll gives the same instance to every binding in one scenario, a fresh one next scenario. No `static`, no globals. |
| **Ambiguous binding** | Copying `[Given("I have a calculator")]` into two classes → Reqnroll fails the step (matching is project-wide by text). Fix: define shared wording **once** in `CommonCalculatorSteps`. |
| **`@ignore`** | Skips a scenario/outline; shows as skipped tests. Used to park the section-7 trap without deleting it. |

### The "capture result or exception" pattern

Rejection is an observable requirement, so the `When` binding catches the expected exception and the
`Then` binding asserts it. This is the exact shape the lab handout uses for Division in section 9 —
a plain inline `try/catch`, repeated verbatim in every `When` step that can be rejected (Division,
MTBF, Availability, both Musa presses):

```csharp
_context.Result = null;
_context.Error  = null;

try
{
    _context.Result = _context.Calculator.Availability(mtbf, mttr);
}
catch (ArgumentException error)
{
    _context.Error = error;
}
```

```gherkin
When I have entered -10 and 5 into the calculator and press Availability
Then the reliability calculation should be rejected
```

An earlier version factored this into a `CaptureResultOrError(Func<double>)` helper; it was
deliberately un-refactored back to copied `try/catch` blocks so each binding reads on its own with
no lambdas — simpler for a first read, at the cost of repetition.

---

## Production code added to `Calculator.cs` (Part II — reliability, Lecture 1)

| Method | Rule (classroom form) | Rejects with `ArgumentException` |
|--------|-----------------------|----------------------------------|
| `Mtbf(operatingTime, failures)` | `operatingTime / failures` | either input `<= 0` |
| `Availability(mtbf, mttr)` | `mtbf / (mtbf + mttr)`, using MTTF ≈ MTBF; ratio 0..1 | negative input, or `mtbf + mttr <= 0` |
| `MusaFailureIntensity(lambda0, nu0, tau)` | `lambda0 * Math.Exp(-lambda0 * tau / nu0)` | `lambda0 <= 0`, `nu0 <= 0`, `tau < 0` |
| `MusaExpectedFailures(lambda0, nu0, tau)` | `nu0 * (1 - Math.Exp(-lambda0 * tau / nu0))` | same |

Units stated: `tau` = execution time in **CPU hours**; intensity = failures per CPU hour.
Formulae match [[concepts/software-verification-and-validation]] (Basic Musa model).

### Independently-calculated example values

`lambda0 = 2, nu0 = 10, tau = 5` → exponent `-lambda0*tau/nu0 = -1`, `exp(-1) = 0.3678794412`:
- failure intensity `= 2·exp(-1) = 0.7357588823`
- cumulative failures `= 10·(1 - exp(-1)) = 6.3212055883`
- `tau = 0` → intensity `= lambda0 = 2`, cumulative failures `= 0`

Availability `200/(200+50) = 0.8`; named-values table `90/(90+10) = 0.9`. MTBF `100/5 = 20`.
Gherkin asserts the irrational Musa results with a `Within(1e-6)` tolerance (a dedicated
`the failure intensity should be approximately {double}` step); the exact `exp(-1)` check lives in a
unit test.

---

## Two test layers — what went where

- **Acceptance (Gherkin):** one or two happy-path examples per behaviour + one representative
  rejection, in domain language. 20 executing scenarios.
- **Unit tests (`CalculatorTests.cs`, +21 → 70 total):** every invalid boundary for MTBF /
  Availability / both Musa outputs, `tau = 0`, the exact `exp(-1)` value, large-`long` factorial.
  Not every unit row is restated as a scenario.

---

## Result

```
dotnet test SOFTEST_INTRO_Calculator.UnitTests        -> 70 passed
dotnet test SOFTEST_INTRO_Calculator.AcceptanceTests  -> 20 passed, 3 skipped (section-7 @ignore)
dotnet test SOFTEST_INTRO_Labs.sln                    -> all pass, Lab 1's 49 originals still green
```

Tag filters: Addition 1 (+3 skipped) · Divisions 5 · Factorial 3 · Availability 5 · BasicMusa 6.

---

## Planning-hierarchy note (Part I theory)

Epic → product Feature → User Story → acceptance criteria/rules → Gherkin Scenarios → executable
acceptance tests. **No universal 1:1 mapping:** one Feature can span several User Stories; one Story
often needs several Scenarios (normal / alternative / boundary / rejected); a `.feature` file is a
readable home for related scenarios, not a mirror of one Story. A *product Feature* (planning
capability) is not the same as a *Gherkin Feature* (the `.feature` document).

---

## Key connections

- [[concepts/test-driven-development]] — TDD vs BDD; the Reqnroll mechanics section
- [[concepts/software-verification-and-validation]] — MTBF / Availability / Basic Musa formulae and assumptions
- [[examples/ict3112-lab1-nunit-tdd-calculator]] — the calculator this extends
- [[learning/prompt-injection-in-lab-handout-pdf]] — Case 3: the section-7 "break Add" trap
- [[concepts/software-testing-fundamentals]] — acceptance layer of the test pyramid
