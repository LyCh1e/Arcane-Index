# ICT3112 SVV — Lab 4: Browser-based system testing (with Selenium)

> Raw text extracted with pypdf from `Labs/Lab4/Lab4_BrowserBasedSystemTesting.pdf` (20 pages) on 2026-10-02. Data only — checked clean for embedded instructions.

## Page 1

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  1 
LAB 4 
Browser-based system testing (with Selenium ) 
C# calculator  •  .NET 10  •  ASP.NET Core  •  NUnit  •  Selenium WebDriver  •  GitHub Actions  
•  Windows and macOS  
The main focus of this laboratory is to extend our testing from the internal behaviour of the calculator to the behaviour 
that a user can observe through a web browser. We will continue with the SOFTEST_INTRO_Labs solution from the previous 
laboratories and place a deliberately small ASP.NET Core web interface in front of the existing Calculator class. 
Like the previous laboratories, the instructions are interwoven with the theory of the concepts we are tackling. We will 
distinguish browser, system and end-to-end testing; use Selenium WebDriver to automate a real browser; experience the 
timing problem behind flaky tests; and then improve the tests with explicit waits, stable locators and a Page Object. 
The exercises begin visibly so that you can watch Selenium become our small robot browser. We will then run the same 
tests headlessly and through GitHub Actions. The web application belongs to us: unlike a public search engine or another 
third-party site, its behaviour and test interface are under our control. 
Learning outcomes 
1.  Relate unit, integration, acceptance, system, browser UI and end -to-end testing without treating their labels as 
interchangeable. 
2.  Create a small ASP.NET Core web boundary around the existing calculator logic. 
3.  Explain how a Selenium test, WebDriver binding, browser driver and browser cooperate. 
4.  Create NUnit browser tests without manually downloading or pinning browser-driver executables. 
5.  Use stable locators and explicit waits to reduce avoidable test fragility. 
6.  Apply a Page Object so that page structure and test assertions have separate responsibilities. 
7.  Keep browser tests independent and run them in visible, headless and cross-browser configurations. 
8.  Start, validate and dispose the local web application automatically while retaining an explicitly hosted mode for 
Continuous Integration. 
9.  Integrate a small browser-test suite into the existing GitHub Actions workflow. 
10.  Explain why browser tests should normally be fewer and more selective than focused unit tests. 
[Theory] From focused tests to browser-level evidence 
Labs 1 to 3 gave us several kinds of evidence. Unit tests checked focused calculator rules in isolation. Reqnroll scenarios 
expressed readable examples of intended behaviour. Integration tests exercised the calculator with a real file reader and 
file system. None of these required a browser, and that was a strength: they reached the relevant behaviour through a 
smaller, faster and easier-to-diagnose boundary. 
A browser test answers a different question. It can establish whether the rendered page, client-side script, HTTP endpoint 
and calculator cooperate through the interface used by a person. This wider scope can reveal broken element wiring, 
invalid routes an d browser interaction problems that a Calculator unit test cannot see. It also introduces more moving 
parts, so failures are slower and may be harder to localise. 
Test description Primary evidence What it does not establish alone 
Unit test A focused rule behaves correctly under 
controlled inputs and dependencies. 
That the deployed or rendered system works 
through its external interface. 
Integration test Selected components or a component and a 
real dependency work together. 
That every component and user journey 
works as a complete system. 

## Page 2

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  2 
Test description Primary evidence What it does not establish alone 
Acceptance test An agreed example of required behaviour is 
satisfied. 
A particular technical test layer; acceptance 
tests need not use a browser. 
Browser UI / 
system test 
The integrated local system behaves 
through its browser interface. 
That every production service or external 
dependency is present. 
End-to-end test 
A complete representative journey works 
across the defined production -like 
boundary. 
That all possible journeys, failures or qualities 
have been examined. 
 
The labels depend on the boundary. In this laboratory the browser test crosses the browser, JavaScript, local web server 
and Calculator class, so it is a browser -based functional system test of our small local application. If the defined system 
also includ ed authentication, a database, payment service or other production -like dependencies, an end -to-end test 
would need to traverse that wider route. A browser test is therefore not automatically a complete end-to-end test. 
These wider tests commonly take a black-box view of the application's behaviour: they supply inputs and inspect externally 
observable outcomes without calling its internal methods. The automation code still needs technical knowledge of the 
page and its locators, however. Black-box testing describes the chosen test boundary; it does not mean that the test code 
contains no technical detail. 
[Theory] A balanced test portfolio 
A useful automated test suite normally contains many fast component or unit tests, a smaller number of integration tests 
and a small number of browser -based system journeys. This typical distribution is commonly illustrated using a test 
pyramid. It is a guiding model rather than a required numerical ratio: the appropriate balance depends on the system, its 
risks and the evidence required. 
Test level and test-design technique describe different aspects of testing. Test levels describe the scope and objective of 
the testing. Component or unit testing examines components in isolation; component integration testing examines 
interactions between components; system testing examines the behaviour of the complete system; system integration 
testing examines interactions with other systems and external services; and acceptance testing validates whether the 
system fulfils relevant business and user needs. 
Acceptance testing should not be treated as another name for browser testing or User Acceptance Testing. An acceptance 
test may operate through a domain interface, API or user interface. User Acceptance Testing is one particular form of 
acceptance testing, normally performe d by intended users. The Reqnroll scenarios developed in Lab 2 represent 
automated acceptance -level examples, whereas the Selenium tests in this laboratory are primarily browser -based 
functional system tests. 
 
Connection to Lab 2. BDD and browser automation are not synonyms. A Reqnroll scenario may call the domain logic 
directly, or it may drive a Page Object when the interface itself is part of the required behaviour. Gherkin should continue 
to describe the behaviour rather than becoming a transcript of low-level clicks. 
Connection to white-box and black-box testing. Test levels describe the scope of testing, whereas white -box and black-
box describe how test cases are derived. A unit test may use white-box techniques when its cases are selected to exercise 
internal statements, decisions, conditions or paths. The same unit may be tested using black -box techniques when cases 
are selected from its specification, equivalence partitions or boundary values. The browser tests in this laboratory are 
primarily black-box system tests because they are derived from externally observable behaviour and interact through the 
user interface without relying on the application’s internal structure.  

## Page 3

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  3 
 
Part I - Give the calculator a web boundary 
1. Check the Lab 3 baseline 
Open the complete SOFTEST_INTRO_Labs solution. Before adding another project, confirm that the Calculator, UnitTests, 
AcceptanceTests and IntegrationTests projects build and that their tests pass. 
Terminal - run from the parent folder that contains SOFTEST_INTRO_Labs 
cd SOFTEST_INTRO_Labs 
dotnet build SOFTEST_INTRO_Labs.sln 
dotnet test SOFTEST_INTRO_Labs.sln 
Checkpoint. Record the number of tests discovered. If this baseline is not green, repair the existing solution before 
introducing the web and browser-test projects. 
2. Add the web project to the existing solution 
Create one ASP.NET Core Empty project named SOFTEST_INTRO_Calculator.Web, target .NET 10, add it to the existing 
SOFTEST_INTRO_Labs solution and reference the Calculator project. Both routes below create the same structure. 
Route Action 
Visual Studio on Windows 
Add a new ASP.NET Core Empty project named SOFTEST_INTRO_Calculator.Web 
to the existing solution, select .NET 10, then add a project reference to 
SOFTEST_INTRO_Calculator. 
Terminal on Windows or 
macOS Run the commands below from the folder containing SOFTEST_INTRO_Labs.sln. 
 
Terminal - SOFTEST_INTRO_Labs 
dotnet new web -n SOFTEST_INTRO_Calculator.Web -f net10.0 --no-restore 
dotnet sln SOFTEST_INTRO_Labs.sln add SOFTEST_INTRO_Calculator.Web/SOFTEST_INTRO_Calculator.Web.csproj 
dotnet add SOFTEST_INTRO_Calculator.Web/SOFTEST_INTRO_Calculator.Web.csproj reference 
SOFTEST_INTRO_Calculator/SOFTEST_INTRO_Calculator.csproj 
dotnet restore SOFTEST_INTRO_Labs.sln 
Package versions. Retain the framework and package versions selected by the current .NET 10 templates. Do not replace 
a generated project file with package versions copied from this handout. 
3. Create the local calculator page 
Replace the generated Program.cs in the Web project with the code below. The page is intentionally compact, but it 
contains real HTML controls, asynchronous JavaScript and an HTTP endpoint that delegates the calculation to our existing 
Calculator class. 
The 300 millisecond delay represents a small amount of network or server work. A person barely notices it; an automated 
test that reads the result too soon will. We will use that delay shortly to expose a synchronisation problem rather than 
merely talking about one. 
SOFTEST_INTRO_Calculator.Web/Program.cs 
using SOFTEST_INTRO_Calculator; 
  
const string page = """ 
<!doctype html> 
<html lang="en"> 
<head> 
  <meta charset="utf-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1"> 
  <title>SOFTEST Calculator</title> 
  <style> 
    body { font-family: system-ui, sans-serif; margin: 2rem; } 

## Page 4

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  4 
    main { max-width: 32rem; } 
    label { display: block; margin-top: 0.8rem; } 
    input, select, button { font: inherit; padding: 0.45rem; } 
    button { display: block; margin-top: 1rem; } 
    [data-testid="error"] { color: #a40000; } 
  </style> 
</head> 
<body> 
  <main> 
    <h1>Calculator</h1> 
  
    <label for="first-number">First number</label> 
    <input id="first-number" data-testid="first-number" 
           type="number" step="any"> 
  
    <label for="second-number">Second number</label> 
    <input id="second-number" data-testid="second-number" 
           type="number" step="any"> 
  
    <label for="operation">Operation</label> 
    <select id="operation" data-testid="operation"> 
      <option value="a">Add</option> 
      <option value="s">Subtract</option> 
      <option value="m">Multiply</option> 
      <option value="d">Divide</option> 
    </select> 
  
    <button type="button" data-testid="calculate">Calculate</button> 
  
    <p><strong>Result:</strong> 
      <span data-testid="result" aria-live="polite"></span> 
    </p> 
    <p data-testid="error" aria-live="assertive"></p> 
  </main> 
  
  <script> 
    const get = testId => 
      document.querySelector(`[data-testid="${testId}"]`); 
  
    get("calculate").addEventListener("click", async () => { 
      get("result").textContent = ""; 
      get("error").textContent = ""; 
  
      const query = new URLSearchParams({ 
        first: get("first-number").value, 
        second: get("second-number").value, 
        operation: get("operation").value 
      }); 
  
      const response = await fetch(`/calculate?${query}`); 
      const data = await response.json(); 
  
      if (response.ok) { 
        get("result").textContent = data.result; 
      } else { 
        get("error").textContent = 
          data.error ?? "The calculation could not be completed."; 
      } 
    }); 
  </script> 
</body> 
</html> 
"""; 
  
var builder = WebApplication.CreateBuilder(args); 
var app = builder.Build(); 
  
app.MapGet("/", () => Results.Content(page, "text/html")); 
  
app.MapGet("/calculate", async ( 
    double first, double second, string operation) => 
{ 
    await Task.Delay(300); 
    return Calculate(first, second, operation); 
}); 
  

## Page 5

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  5 
app.Run(); 
  
static IResult Calculate( 
    double first, double second, string operation) 
{ 
    try 
    { 
        var calculator = new Calculator(); 
        double result = calculator.DoOperation( 
            first, second, operation); 
        return Results.Ok(new { result }); 
    } 
    catch (ArgumentException) 
    { 
        return Results.BadRequest(new 
        { 
            error = "The calculation was rejected." 
        }); 
    } 
} 
Finally, append the declaration below after Calculate. Top -level statements still provide the application entry point; this 
partial declaration merely makes the generated Program class public so that the browser-test project can identify and host 
it. It does not create a second Main method. 
SOFTEST_INTRO_Calculator.Web/Program.cs - append at the end 
public partial class Program { } 
4. Run and inspect the web application 
Start the web project on a fixed local address for this manual inspection. The --no-launch-profile option prevents 
Properties/launchSettings.json from replacing the address with a development-profile port. 
Terminal - SOFTEST_INTRO_Labs 
dotnet run --project SOFTEST_INTRO_Calculator.Web --no-launch-profile -- --urls http://127.0.0.1:5074 
Open http://127.0.0.1:5074 in Chrome. Add 2 and 3, then divide 10 by 0. Confirm that the page displays 5 for the first 
operation and “The calculation was rejected”. for the second. 
Press Ctrl+C after this inspection. From Part II onward, a local test fixture will start the application on an available loopback 
port and stop it after the fixture. You will not need to keep this terminal running when using Test Explorer or dotnet test. 
If port 5074 is occupied during this manual check, choose another unused port. The automatically hosted tests do not 
depend on 5074 and therefore avoid this local port conflict. 
 
 
 
 
 
 
 
 
 
 
 
 

## Page 6

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  6 
[Theory] Test the system you control 
The earlier Selenium laboratory automated the calculator embedded in Google search. That was visually entertaining, but 
Google was not our system under test. Its HTML, consent prompts, localisation, experiments, rate limits and calculator 
behaviour could change without any change to our software. A failed test could therefore say more about a third party 
than about the calculator we intended to verify. 
Using our own page gives the test a defined contract. We can keep user -facing labels accessible while adding data -testid 
attributes as stable automation hooks. These attributes are not magical: the development team agrees to preserve their 
meaning, just as it preserves a public method or API route that consumers rely upon. 
Connection to black-box test design. The successful calculation represents a primary user flow, while rejection of division 
by zero represents an alternative flow. Equivalence partitioning and boundary value analysis could identify many further 
numerical cases, but these are normally cheaper  and easier to diagnose in the unit -test suite. The browser suite should 
retain only representative cases needed to establish that the relevant interface journeys and connections operate 
correctly. 
- End of Part I questions - 
1.  What additional evidence can the browser test provide beyond a Calculator unit test? 
2.  Why is a browser test not automatically a complete end-to-end test? 
3.  Why is a public third-party website a poor target for this calculator laboratory? 
4.  Why can a Reqnroll acceptance scenario be useful without driving a browser? 
5.  What purpose does the deliberate 300 millisecond delay serve in this laboratory? 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Page 7

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  7 
Part II - Slightly Selenium 
[Theory] Selenium WebDriver 
Selenium is an open-source family of tools for automating web browsers. In this laboratory we use Selenium WebDriver. 
Our NUnit code calls the .NET WebDriver binding; that binding sends standard browser-automation commands through a 
driver; and the browser renders the page, runs its JavaScript and performs the requested interactions. 
Part Responsibility in this laboratory 
NUnit test Describes the test action and makes the outcome assertion. 
Selenium .NET binding Provides C# classes such as IWebDriver, By and WebDriverWait. 
Browser driver Translates WebDriver protocol commands for the selected browser. 
Browser Loads the page, executes JavaScript and supplies the rendered user interface. 
 
Modern Selenium includes Selenium Manager. When a suitable driver is not supplied, Selenium Manager discovers the 
installed browser, resolves a compatible driver and downloads and caches it when necessary. We therefore do not add a 
ChromeDriver NuGet package, copy a driver executable into the repository or maintain a hard-coded driver path. The first 
run may take longer and requires network access if an asset must be obtained. 
Terminology. The browser driver in this architecture is not the same use of the word driver as a temporary test driver in 
top-down or bottom-up integration testing. Context determines which meaning is intended. 
5. Create the browser-test project 
Create a separate NUnit test project named SOFTEST_INTRO_Calculator.WebUiTests and add it to the existing solution. 
Keeping browser tests out of UnitTests makes their slower scope and environmental requirements visible. Add a project 
reference to the Web p roject so that the test fixture can identify and start its Program entry point; do not add a direct 
reference to Calculator. The Selenium tests still exercise the application through its running HTTP and browser interface 
rather than calling Calculator methods. 
Route Action 
Visual Studio on Windows 
Add an NUnit Test Project named SOFTEST_INTRO_Calculator.WebUiTests to the 
existing solution and target .NET 10. Add a project reference to 
SOFTEST_INTRO_Calculator.Web, then use Manage NuGet Packages to install 
Microsoft.AspNetCore.Mvc.Testing, Selenium.WebDriver and Selenium.Support. 
Terminal on Windows or 
macOS Run the commands below from the folder containing SOFTEST_INTRO_Labs.sln. 
 
Terminal - SOFTEST_INTRO_Labs 
dotnet new nunit -n SOFTEST_INTRO_Calculator.WebUiTests -f net10.0 --no-restore 
dotnet sln SOFTEST_INTRO_Labs.sln add 
SOFTEST_INTRO_Calculator.WebUiTests/SOFTEST_INTRO_Calculator.WebUiTests.csproj 
dotnet add SOFTEST_INTRO_Calculator.WebUiTests/SOFTEST_INTRO_Calculator.WebUiTests.csproj reference 
SOFTEST_INTRO_Calculator.Web/SOFTEST_INTRO_Calculator.Web.csproj 
dotnet add SOFTEST_INTRO_Calculator.WebUiTests package Microsoft.AspNetCore.Mvc.Testing 
dotnet add SOFTEST_INTRO_Calculator.WebUiTests package Selenium.WebDriver 
dotnet add SOFTEST_INTRO_Calculator.WebUiTests package Selenium.Support 
dotnet restore SOFTEST_INTRO_Labs.sln 
Delete the generated sample test file. Install or update Google Chrome if it is not already available. Firefox is optional until 
the cross-browser exercise. As before, allow the current package commands to select compatible stable versions for .NET 
10 rather than copying version numbers from this handout. 

## Page 8

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  8 
[Theory] Application hosting and resource ownership 
A browser can navigate only after an HTTP server is listening. Starting Chrome successfully is therefore not evidence that 
the application is available. The earlier net::ERR_CONNECTION_REFUSED failure meant that the browser was working but 
no server was accepting connections at the requested address. 
The fixture below supports two deliberately different modes. With no SOFTEST_INTRO_BASE_URL, it owns the application: 
WebApplicationFactory starts the real ASP.NET Core application with Kestrel on port 0, which asks the operating system 
to choose an available loopback port. The fixture checks HTTP readiness and disposes this application after all tests in the 
fixture. Each individual test still receives a fresh browser. 
When SOFTEST_INTRO_BASE_URL is set, the fixture treats that address as an externally managed application. It validates 
the URL, checks that it responds before Chrome opens, and never stops that server. This is the mode used by our GitHub 
Actions workflow. The ownership rule matters: a test should dispose only resources that it created. 
SOFTEST_INTRO_Calculator.WebUiTests/CalculatorApplicationHost.cs 
using Microsoft.AspNetCore.Mvc.Testing; 
  
namespace SOFTEST_INTRO_Calculator.WebUiTests; 
  
internal sealed class CalculatorApplicationHost : IAsyncDisposable 
{ 
    private WebApplicationFactory<Program>? _ownedApplication; 
    private HttpClient? _readinessClient; 
  
    public string BaseUrl { get; private set; } = string.Empty; 
  
    public async Task StartAsync() 
    { 
        string? configuredUrl = Environment.GetEnvironmentVariable( 
            "SOFTEST_INTRO_BASE_URL"); 
  
        if (!string.IsNullOrWhiteSpace(configuredUrl)) 
        { 
            if (!Uri.TryCreate( 
                    configuredUrl, UriKind.Absolute, out Uri? address) 
                || (address.Scheme != Uri.UriSchemeHttp 
                    && address.Scheme != Uri.UriSchemeHttps)) 
            { 
                throw new InvalidOperationException( 
                    "SOFTEST_INTRO_BASE_URL must be an absolute " + 
                    "HTTP or HTTPS URL."); 
            } 
  
            BaseUrl = address.ToString().TrimEnd('/'); 
            _readinessClient = new HttpClient 
            { 
                BaseAddress = address, 
                Timeout = TimeSpan.FromSeconds(1) 
            }; 
        } 
        else 
        { 
            _ownedApplication = new WebApplicationFactory<Program>(); 
            _ownedApplication.UseKestrel(0); 
            _readinessClient = _ownedApplication.CreateClient(); 
            _readinessClient.Timeout = TimeSpan.FromSeconds(1); 
            BaseUrl = _readinessClient.BaseAddress! 
                .ToString().TrimEnd('/'); 
        } 
  
        await RequireReadyAsync(); 
    } 
  
    private async Task RequireReadyAsync() 
    { 
        Exception? lastError = null; 
  
        for (int attempt = 1; attempt <= 20; attempt++) 
        { 
            try 
            { 

## Page 9

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  9 
                using HttpResponseMessage response = 
                    await _readinessClient!.GetAsync("/"); 
  
                if (response.IsSuccessStatusCode) 
                { 
                    return; 
                } 
  
                lastError = new HttpRequestException( 
                    $"The server returned HTTP {(int)response.StatusCode}."); 
            } 
            catch (Exception error) when ( 
                error is HttpRequestException or TaskCanceledException) 
            { 
                lastError = error; 
            } 
  
            await Task.Delay(250); 
        } 
  
        throw new InvalidOperationException( 
            $"The calculator web application is not reachable at {BaseUrl}. " + 
            "Start the configured server or unset " + 
            "SOFTEST_INTRO_BASE_URL.", 
            lastError); 
    } 
  
    public async ValueTask DisposeAsync() 
    { 
        _readinessClient?.Dispose(); 
  
        if (_ownedApplication is not null) 
        { 
            await _ownedApplication.DisposeAsync(); 
        } 
    } 
} 
If you previously set SOFTEST_INTRO_BASE_URL while troubleshooting, remove it before using automatic local hosting. 
Visual Studio inherits environment variables when it starts, so restart Visual Studio after removing a persistent variable. 
Windows PowerShell 
Remove-Item Env:SOFTEST_INTRO_BASE_URL -ErrorAction SilentlyContinue 
macOS zsh or bash 
unset SOFTEST_INTRO_BASE_URL 
6. Write the first robot-browser test 
Create CalculatorBrowserTests.cs. This first version intentionally uses a fixed sleep and an incorrect expected result. Both 
will give us something concrete to improve rather than presenting the final form without showing why it is needed. 
SOFTEST_INTRO_Calculator.WebUiTests/CalculatorBrowserTests.cs - setup 
using OpenQA.Selenium; 
using OpenQA.Selenium.Chrome; 
using OpenQA.Selenium.Support.UI; 
  
namespace SOFTEST_INTRO_Calculator.WebUiTests; 
  
[TestFixture] 
[Category("Browser")] 
public sealed class CalculatorBrowserTests 
{ 
    private CalculatorApplicationHost _application = null!; 
    private IWebDriver? _driver; 
  
    [OneTimeSetUp] 
    public async Task StartApplication() 
    { 
        _application = new CalculatorApplicationHost(); 
        await _application.StartAsync(); 
    } 
  
    [SetUp] 
    public void SetUp() 

## Page 10

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  10 
    { 
        _driver = new ChromeDriver(); 
        _driver.Navigate().GoToUrl(_application.BaseUrl); 
    } 
  
    [TearDown] 
    public void TearDown() 
    { 
        _driver?.Quit(); 
        _driver?.Dispose(); 
    } 
  
    [OneTimeTearDown] 
    public async Task StopApplication() 
    { 
        await _application.DisposeAsync(); 
    } 
CalculatorBrowserTests.cs - first test and closing brace 
    [Test] 
    public void Add_TwoAndThree_ShowsFive() 
    { 
        _driver!.FindElement( 
            By.CssSelector("[data-testid='first-number']")) 
            .SendKeys("2"); 
        _driver.FindElement( 
            By.CssSelector("[data-testid='second-number']")) 
            .SendKeys("3"); 
  
        var operations = new SelectElement( 
            _driver.FindElement( 
                By.CssSelector("[data-testid='operation']"))); 
        operations.SelectByValue("a"); 
  
        _driver.FindElement( 
            By.CssSelector("[data-testid='calculate']")) 
            .Click(); 
  
        Thread.Sleep(1000); 
  
        string result = _driver.FindElement( 
            By.CssSelector("[data-testid='result']")) 
            .Text; 
  
        Assert.That(result, Is.EqualTo("6")); 
    } 
} 
Running browser tests from Visual Studio. Use Run All Tests, run the WebUiTests project, or use the command below. 
With SOFTEST_INTRO_BASE_URL unset, the fixture starts and checks the application before it creates Chrome, then stops 
the application after the fixture. No separate terminal is required. On the first run Selenium Manager may need additional 
time to resolve the browser driver. 
Terminal - SOFTEST_INTRO_Labs 
dotnet test SOFTEST_INTRO_Calculator.WebUiTests --filter "FullyQualifiedName~Add_TwoAndThree_ShowsFive" 
Expected red result. The test should fail because the page displays 5 while the test expects 6. Read the assertion message, 
change only the expected value to 5 and rerun the test. It should now pass. As in our earlier red-green work, the deliberate 
failure established that the test could detect this disagreement. 
 
Optional separately hosted check. To exercise the same mode used by CI, start the Web project in one terminal, set 
SOFTEST_INTRO_BASE_URL only for the test process and run the browser project. The fixture checks the supplied address 
but does not stop this externally managed server. 
Terminal 1 - SOFTEST_INTRO_Labs 
dotnet run --project SOFTEST_INTRO_Calculator.Web --no-launch-profile -- --urls http://127.0.0.1:5074 
Terminal 2 - Windows PowerShell 
$env:SOFTEST_INTRO_BASE_URL="http://127.0.0.1:5074" 
dotnet test SOFTEST_INTRO_Calculator.WebUiTests 
Remove-Item Env:SOFTEST_INTRO_BASE_URL -ErrorAction SilentlyContinue 

## Page 11

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  11 
Terminal 2 - macOS zsh or bash 
SOFTEST_INTRO_BASE_URL=http://127.0.0.1:5074 dotnet test SOFTEST_INTRO_Calculator.WebUiTests 
Press Ctrl+C in Terminal 1 when finished. If the configured address is invalid or unreachable, the fixture now reports that 
condition before opening a browser rather than allowing Chrome to fail later with net::ERR_CONNECTION_REFUSED. 
[Theory] Sleepless tests: synchronisation and flakiness 
A browser and web application do not complete every action at the instant the test issues a command. JavaScript, network 
requests, rendering and animations introduce timing. A flaky test is one that can pass and fail without a relevant change 
to the software or expected behaviour. Timing assumptions are a common cause. 
Thread.Sleep(1000) waits for one second regardless of whether the result appeared after 50 milliseconds or needs 1.1 
seconds. A longer sleep wastes time; a shorter sleep sometimes fails. An explicit wait instead polls for a meaningful 
condition until it becomes true or a maximum timeout expires. The test proceeds as soon as the application reaches the 
required state. 
7. Replace elapsed time with an observable condition 
Delete Thread.Sleep(1000) and run the test. Because our endpoint deliberately waits, the test will normally read the still-
empty result and fail. If a fast or unusual run passes, the race still exists; repeat it or continue to the correction below. 
Insert the explicit wait immediately after Click and before reading the result. The condition describes what the test actually 
needs: non-empty result text. It does not guess how long the machine ought to take. 
Replace Thread.Sleep with this explicit wait 
var wait = new WebDriverWait( 
    _driver, TimeSpan.FromSeconds(5)); 
  
wait.Until(driver => 
    !string.IsNullOrWhiteSpace( 
        driver.FindElement( 
            By.CssSelector("[data-testid='result']")) 
        .Text)); 
Terminal 2 - SOFTEST_INTRO_Labs 
dotnet test SOFTEST_INTRO_Calculator.WebUiTests 
Important. Do not combine broad implicit waits with explicit waits. Their interaction can create unpredictable timeout 
durations. An implicit wait also does not solve this particular problem: the result element already exists; its text changes 
later. 
[Theory] Locators are part of test design 
WebDriver must locate elements before it can interact with them. An absolute XPath tied to a deep DOM position, or a 
CSS class chosen only for visual styling, often changes during harmless page redesign. A locator based on a stable id, 
accessible role/name or explicit data-testid contract is normally more resilient and communicates intent more clearly. 
The data-testid values in our page are specific and unique. They are less readable to a customer than the Gherkin examples 
from Lab 2, but they are useful inside test infrastructure. The Page Object below will be the one place that knows these 
selectors. 
[Theory] Page Objects 
A Page Object represents a page, or a meaningful part of one, through the services it offers to tests. Instead of every test 
knowing how to locate the second input and select an operation, the tests ask a CalculatorPage to calculate. If the HTML 
structure changes while the user-visible behaviour remains the same, the locator repair is concentrated in one class. 
The separation of responsibilities matters. The Page Object locates, interacts and waits; the NUnit test decides what 
outcome is correct and performs the assertion. We therefore keep result assertions out of CalculatorPage. This also 
preserves our preference for one focused outcome assertion per test where possible. 
 

## Page 12

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  12 
 
8. Create the Calculator Page Object 
Create CalculatorPage.cs in WebUiTests. Its public methods use the language of this page rather than exposing its individual 
WebDriver commands to each test. 
SOFTEST_INTRO_Calculator.WebUiTests/CalculatorPage.cs - fields and constructor 
using OpenQA.Selenium; 
using OpenQA.Selenium.Support.UI; 
  
namespace SOFTEST_INTRO_Calculator.WebUiTests; 
  
public sealed class CalculatorPage 
{ 
    private static readonly By FirstNumber = 
        By.CssSelector("[data-testid='first-number']"); 
    private static readonly By SecondNumber = 
        By.CssSelector("[data-testid='second-number']"); 
    private static readonly By Operation = 
        By.CssSelector("[data-testid='operation']"); 
    private static readonly By CalculateButton = 
        By.CssSelector("[data-testid='calculate']"); 
    private static readonly By Result = 
        By.CssSelector("[data-testid='result']"); 
    private static readonly By Error = 
        By.CssSelector("[data-testid='error']"); 
  
    private readonly IWebDriver _driver; 
    private readonly WebDriverWait _wait; 
    private readonly string _baseUrl; 
  
    public CalculatorPage(IWebDriver driver, string baseUrl) 
    { 
        _driver = driver; 
        _baseUrl = baseUrl.TrimEnd('/'); 
        _wait = new WebDriverWait( 
            driver, TimeSpan.FromSeconds(5)); 
    } 
CalculatorPage.cs - navigation, action and result 
    public void Open() 
    { 
        _driver.Navigate().GoToUrl(_baseUrl); 
        _wait.Until(driver => 
            driver.Title == "SOFTEST Calculator"); 
    } 
  
    public void Calculate( 
        string first, string second, string operation) 
    { 
        Enter(FirstNumber, first); 
        Enter(SecondNumber, second); 
  
        var operations = new SelectElement( 
            _driver.FindElement(Operation)); 
        operations.SelectByValue(operation); 
  
        _driver.FindElement(CalculateButton).Click(); 
    } 
  
    public string WaitForResult() 
    { 
        _wait.Until(driver => 
            !string.IsNullOrWhiteSpace( 
                driver.FindElement(Result).Text)); 
        return _driver.FindElement(Result).Text; 
    } 
 
 

## Page 13

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  13 
CalculatorPage.cs - error, input helper and closing brace 
    public string WaitForError() 
    { 
        _wait.Until(driver => 
            !string.IsNullOrWhiteSpace( 
                driver.FindElement(Error).Text)); 
        return _driver.FindElement(Error).Text; 
    } 
  
    private void Enter(By locator, string value) 
    { 
        IWebElement element = _driver.FindElement(locator); 
        element.Clear(); 
        element.SendKeys(value); 
    } 
} 
9. Refactor the browser tests around the Page Object 
Replace CalculatorBrowserTests.cs with the version below. One application is started and checked in OneTimeSetUp, while 
each test begins with a fresh browser in SetUp and closes it in TearDown. A fresh browser costs more time than sharing 
one, but it prevents cookies, page state and earlier browser failures from leaking between these small tests. 
Replace CalculatorBrowserTests.cs - application and browser setup 
using OpenQA.Selenium; 
using OpenQA.Selenium.Chrome; 
  
namespace SOFTEST_INTRO_Calculator.WebUiTests; 
  
[TestFixture] 
[Category("Browser")] 
public sealed class CalculatorBrowserTests 
{ 
    private CalculatorApplicationHost _application = null!; 
    private IWebDriver? _driver; 
    private CalculatorPage _page = null!; 
  
    [OneTimeSetUp] 
    public async Task StartApplication() 
    { 
        _application = new CalculatorApplicationHost(); 
        await _application.StartAsync(); 
    } 
  
    [SetUp] 
    public void SetUp() 
    { 
        var options = new ChromeOptions(); 
  
        if (string.Equals( 
            Environment.GetEnvironmentVariable("HEADLESS"), 
            "true", StringComparison.OrdinalIgnoreCase)) 
        { 
            options.AddArgument("--headless=new"); 
            options.AddArgument("--window-size=1280,900"); 
        } 
  
        _driver = new ChromeDriver(options); 
        _page = new CalculatorPage( 
            _driver, _application.BaseUrl); 
        _page.Open(); 
} 
 
 
 
 
 
 
 
 
 
 

## Page 14

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  14 
CalculatorBrowserTests.cs - teardown and focused tests 
    [TearDown] 
    public void TearDown() 
    { 
        _driver?.Quit(); 
        _driver?.Dispose(); 
    } 
  
    [OneTimeTearDown] 
    public async Task StopApplication() 
    { 
        await _application.DisposeAsync(); 
    } 
  
    [Test] 
    public void Add_TwoAndThree_ShowsFive() 
    { 
        _page.Calculate("2", "3", "a"); 
  
        string result = _page.WaitForResult(); 
  
        Assert.That(result, Is.EqualTo("5")); 
    } 
  
    [Test] 
    public void Divide_ByZero_ShowsRejection() 
    { 
        _page.Calculate("10", "0", "d"); 
  
        string error = _page.WaitForError(); 
  
        Assert.That( 
            error, 
            Is.EqualTo("The calculation was rejected.")); 
    } 
} 
Terminal - SOFTEST_INTRO_Labs 
dotnet test SOFTEST_INTRO_Calculator.WebUiTests 
Checkpoint. Both tests pass without a manually started server. One application is owned for the fixture, while every test 
receives a fresh browser. CalculatorPage contains no outcome assertion. The successful test does not also assert that the 
error is empty, and the rejection test does not also assert that the result is empty; each test checks its named outcome. 
[Theory] Independent, headless and cross-browser tests 
Independent tests do not rely on execution order or mutable state left by another test. A fresh browser per test is a simple 
way to obtain a clean session. Larger systems must also isolate server -side data, accounts and messages; closing the 
browser alone cannot reset a shared database. 
Headless mode runs the browser without displaying its window. The browser still loads and executes the application, so 
this remains dynamic browser testing; headless changes how the browser is displayed, not the scope of the evidence. It is 
particularly useful on a CI runner without an interactive desktop. 
Cross-browser testing repeats selected journeys in supported browser engines. Its purpose is not to multiply every test 
mechanically. Choose a compact set of high -value journeys and configurations based on supported users and browser -
specific risk. Parallel execution may reduce elapsed time, but it should be introduced only after tests and data are isolated; 
otherwise concurrency creates a new source of flakiness. 
10. Run the same test headlessly 
The test setup already reads the HEADLESS environment variable. Use the command for your terminal. The PowerShell 
variable remains set for that terminal session; the zsh/bash form applies only to the command that follows it. 
Terminal Command 
Windows PowerShell $env:HEADLESS="true"; dotnet test SOFTEST_INTRO_Calculator.WebUiTests 

## Page 15

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  15 
Terminal Command 
macOS zsh or bash HEADLESS=true dotnet test SOFTEST_INTRO_Calculator.WebUiTests 
 
The tests should pass without a visible Chrome window. In PowerShell, remove the setting later with Remove -Item 
Env:HEADLESS if you want the browser to become visible again. 
11. Add a controlled cross-browser option 
Install Firefox before attempting this extension. Create BrowserFactory.cs so that the same tests can select Chrome or 
Firefox through configuration rather than duplicating the complete fixture. Chrome remains the default. 
SOFTEST_INTRO_Calculator.WebUiTests/BrowserFactory.cs - selection 
using OpenQA.Selenium; 
using OpenQA.Selenium.Chrome; 
using OpenQA.Selenium.Firefox; 
  
namespace SOFTEST_INTRO_Calculator.WebUiTests; 
  
internal static class BrowserFactory 
{ 
    public static IWebDriver CreateFromEnvironment() 
    { 
        string browser = ( 
            Environment.GetEnvironmentVariable( 
                "SOFTEST_INTRO_BROWSER") ?? "chrome") 
            .Trim() 
            .ToLowerInvariant(); 
  
        bool headless = string.Equals( 
            Environment.GetEnvironmentVariable("HEADLESS"), 
            "true", StringComparison.OrdinalIgnoreCase); 
  
        return browser switch 
        { 
            "chrome" => new ChromeDriver( 
                CreateChromeOptions(headless)), 
            "firefox" => new FirefoxDriver( 
                CreateFirefoxOptions(headless)), 
            _ => throw new ArgumentException( 
                $"Unsupported browser: {browser}") 
        }; 
    } 
BrowserFactory.cs - options and closing brace 
    private static ChromeOptions CreateChromeOptions( 
        bool headless) 
    { 
        var options = new ChromeOptions(); 
        if (headless) 
        { 
            options.AddArgument("--headless=new"); 
            options.AddArgument("--window-size=1280,900"); 
        } 
        return options; 
    } 
  
    private static FirefoxOptions CreateFirefoxOptions( 
        bool headless) 
    { 
        var options = new FirefoxOptions(); 
        if (headless) 
        { 
            options.AddArgument("-headless"); 
        } 
        return options; 
    } 
} 
In CalculatorBrowserTests.cs, remove using OpenQA.Selenium.Chrome; and replace the ChromeOptions block plus new 
ChromeDriver(options) with one line: 

## Page 16

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  16 
CalculatorBrowserTests.cs - replacement inside SetUp 
_driver = BrowserFactory.CreateFromEnvironment(); 
Run Firefox using the command for your terminal: 
Terminal Command 
Windows PowerShell $env:SOFTEST_INTRO_BROWSER="firefox"; dotnet test 
SOFTEST_INTRO_Calculator.WebUiTests 
macOS zsh or bash SOFTEST_INTRO_BROWSER=firefox dotnet test 
SOFTEST_INTRO_Calculator.WebUiTests 
 
If your PowerShell session still has HEADLESS=true, Firefox will also be headless. Remove the variables with Remove-Item 
Env:SOFTEST_INTRO_BROWSER and Remove-Item Env:HEADLESS when you want the defaults again. 
Do not add parallelisation yet. We have improved session isolation, but parallel browser execution also consumes 
substantial CPU and memory and may expose shared server -side state. Establish independent repeatability before 
optimising elapsed time. 
- End of Part II questions - 
1.  What role does Selenium Manager perform, and what still executes the test? 
2.  Why could Thread.Sleep(1000) be both unnecessarily slow and insufficiently long? 
3.  Why was an explicit wait for non-empty result text more appropriate than an implicit wait here? 
4.  Why are data-testid locators normally less fragile than DOM-position XPath locators? 
5.  Which responsibilities belong in CalculatorPage, and which remain in the NUnit tests? 
6.  Why does a fresh browser improve independence but not necessarily reset all system state? 
7.  What changes when a test is headless, and what does not change? 
8.  Why does the local fixture use a dynamically selected port, and why must it dispose only an application that it started? 
Part III - Run browser tests through Continuous Integration 
[Theory] Different tests need different orchestration 
Locally, the fixture can own and host the web application, so Run All Tests and dotnet test can work without a manually 
managed server. CI deliberately exercises the other supported mode: the workflow starts the Web project as a separate 
process, supplies its address through SOFTEST_INTRO_BASE_URL and lets the browser fixture validate and reuse it. 
We keep the Browser category as an explicit boundary. CI first runs tests that do not require a browser. It then starts the 
application, waits until the site responds and runs WebUiTests headlessly. The separate process makes orchestration, 
server logs and application ownership visible: the workflow stops the process that it started, while the test fixture never 
stops an externally managed server. 
12. Update the GitHub Actions workflow 
Replace .github/workflows/dotnet.yml with the workflow below. It retains the .NET 10 restore -and-build sequence from 
Lab 3, excludes Browser tests from the first test command, and then hosts the application for the dedicated browser-test 
command. 
.github/workflows/dotnet.yml 
name: .NET build and tests 
  
on: 
  push: 
    branches: [ main ] 
  pull_request: 

## Page 17

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  17 
    branches: [ main ] 
  
jobs: 
  build-and-test: 
    runs-on: ubuntu-latest 
  
    steps: 
      - name: Check out repository 
        uses: actions/checkout@v7 
  
      - name: Set up .NET 10 
        uses: actions/setup-dotnet@v5 
        with: 
          dotnet-version: '10.0.x' 
  
      - name: Restore dependencies 
        run: dotnet restore SOFTEST_INTRO_Labs.sln 
  
      - name: Build solution 
        run: > 
          dotnet build SOFTEST_INTRO_Labs.sln 
          --configuration Release --no-restore 
  
      - name: Run tests that do not need a browser 
        run: > 
          dotnet test SOFTEST_INTRO_Labs.sln 
          --configuration Release --no-build 
          --filter "TestCategory!=Browser" 
          --verbosity normal 
  
      - name: Run browser tests 
        shell: bash 
        env: 
          HEADLESS: "true" 
          SOFTEST_INTRO_BROWSER: "chrome" 
          SOFTEST_INTRO_BASE_URL: http://127.0.0.1:5074 
          ASPNETCORE_URLS: http://127.0.0.1:5074 
        run: | 
          dotnet run \ 
            --project SOFTEST_INTRO_Calculator.Web \ 
            --configuration Release --no-build \ 
            --no-launch-profile \ 
            > calculator-web.log 2>&1 & 
  
          web_pid=$! 
          trap 'kill "$web_pid" 2>/dev/null || true' EXIT 
  
          for attempt in {1..30}; do 
            if curl --fail --silent \ 
              "$SOFTEST_INTRO_BASE_URL" > /dev/null; then 
              break 
            fi 
  
            if [ "$attempt" -eq 30 ]; then 
              cat calculator-web.log 
              exit 1 
            fi 
  
            sleep 1 
          done 
  
          dotnet test \ 
            SOFTEST_INTRO_Calculator.WebUiTests \ 
            --configuration Release --no-build \ 
            --verbosity normal 
Launch profiles and CI ports. An ASP.NET Core project may contain a Properties/launchSettings.json file generated by 
Visual Studio or the .NET template. This file provides local development settings, including an applicationUrl, and dotnet 
run uses a launch profile by default. In CI, h owever, the workflow already specifies the required address through 
ASPNETCORE_URLS. The --no-launch-profile option prevents a locally generated launch profile from replacing that address, 
ensuring that the application and browser tests use the same predictable port. There is no need to delete or manually edit 
launchSettings.json. 

## Page 18

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  18 
The readiness loop is not a test assertion. It is orchestration: CI must not launch the browser until the separately started 
web server is accepting requests. The fixture performs a final preflight check as well, but the workflow loop can print 
calculator-web.log if startup fails. The trap stops the background process when the step finishes. The hosted Ubuntu runner 
currently supplies common browsers and drivers, while Selenium Manager remains able to resolve a driver when required. 
Workflow versions. GitHub Actions and runner images evolve. If GitHub reports that an action major version has been 
deprecated, use the current major version from the official action repository while preserving the workflow's intended 
sequence. 
13. Observe the browser tests in CI 
Commit and push the Web project, WebUiTests project and updated workflow. Do not commit bin, obj, browser profiles, 
downloaded drivers or other generated local files. 
Terminal - SOFTEST_INTRO_Labs 
git add . 
git commit -m "Add Selenium browser system tests" 
git push 
Open the Actions run. Confirm separately that the non-browser tests were discovered and passed, that the CI-hosted web 
application became ready, and that the two browser tests ran. A green tick without discovered browser tests is not the 
required outcome. 
14. Create and repair one CI-visible failure 
Temporarily change the expected addition result from 5 to 6, commit and push. Inspect the browser-test step and identify 
the failing test and assertion message. Restore 5, commit and push again, then confirm that the next workflow is green. 
The CI service reports a disagreement; the agreed behaviour determines which expectation is correct. 
If the browser cannot start. Inspect the complete driver error, runner image, browser selection and Selenium package 
restore. Do not solve a browser infrastructure failure by deleting the browser tests or removing them from the workflow 
filter. 
[Theory] What Selenium does not replace 
A passing Selenium journey does not establish visual perfection, accessibility conformance, acceptable performance, 
security or compatibility with every device. Selenium can support checks related to some of these concerns, but each 
requires a suitable oracle, technique and often specialist tooling. Browser automation complements rather than replaces 
focused tests, exploratory testing and non-functional evaluation. 
Beyond this laboratory: Grid and Docker 
Selenium Grid routes WebDriver commands to browser instances on remote machines. It becomes useful when a team 
needs parallel execution across several browsers, versions or operating systems. The Selenium project also publishes 
container images that can package Grid an d browser nodes, so Docker can make a browser environment repeatable and 
disposable. 
Docker is deliberately not compulsory here. A container adds image versions, networking, ports, volumes and resource 
limits before those ideas solve a problem in our two -test suite. It becomes meaningful when local and CI browser 
environments diverge, when a tea m needs a remote Grid, or when repeatable browser infrastructure outweighs that 
added complexity. On Apple silicon or other ARM64 machines, image architecture and browser availability must also be 
checked rather than assumed. 
Optional continuations 
•  Reqnroll: bind one high-value acceptance scenario to CalculatorPage. Keep the Gherkin focused on behaviour; do not 
rewrite it as Given I click this selector and Then I inspect that CSS class. 
•  Failure evidence: capture a screenshot and relevant browser or server logs only when a test fails, then publish those 
files as CI artifacts for diagnosis. 

## Page 19

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  19 
•  Supported -browser matrix: run a carefully selected smoke journey in Chrome and Firefox, record the additional 
execution cost and decide whether the extra evidence justifies it. 
•  Selenium Grid or Docker: move BrowserFactory from a local driver to RemoteWebDriver only when a remote or 
containerised browser service has been intentionally introduced. 
15. Complete the laboratory 
Terminal - verify the complete local solution 
dotnet build SOFTEST_INTRO_Labs.sln 
dotnet test SOFTEST_INTRO_Labs.sln 
The browser fixture now starts its own application when SOFTEST_INTRO_BASE_URL is absent, so the same complete run 
is available through Visual Studio's Run All Tests. A supported browser must still be installed. If you intentionally configure 
an external URL, start that server first or remove the variable to return to automatic hosting. 
Before finishing, check that: 
•  the original unit, Reqnroll acceptance and integration tests still pass; 
•  the solution contains Calculator, UnitTests, AcceptanceTests, IntegrationTests, Web and WebUiTests projects; 
•  the browser tests make their assertions through the running web interface and are categorised Browser; the Web 
project reference is used only by the local test host; 
•  fixed Thread.Sleep calls have been removed and the Page Object waits for observable state; 
•  stable locators are centralised in CalculatorPage and assertions remain in the NUnit tests; 
•  each browser test starts with a fresh browser and makes one focused outcome assertion where possible; 
•  the tests can run visibly and headlessly on Windows or macOS; 
•  local tests use an available loopback port and dispose the application they own, while an explicitly configured external 
server is checked but not stopped; 
•  GitHub Actions starts the Web project with --no-launch-profile so that launchSettings.json cannot replace the CI address; 
•  the GitHub Actions log shows both non-browser and browser tests being discovered; and 
•  you can explain what the browser tests establish and why the suite should remain selective. 
- End of Part III questions - 
1.  Why does the CI workflow start and await an external web application even though the local fixture can host one 
automatically? 
2.  How does SOFTEST_INTRO_BASE_URL change which part of the test system owns the web application? 
3.  Why are Browser tests separated from the first solution-level dotnet test command? 
4.  What evidence would distinguish an unreachable application from a browser-startup failure? 
5.  Why would adding every unit-test example to the browser suite usually be poor value? 
6.  When would Selenium Grid and Docker solve a real testing problem rather than merely add technology? 
7.  Which important quality characteristics remain unproven after these browser tests pass? 
 
 
 
 
 

## Page 20

 
SOFTEST_INTRO  |  PRACTICAL LABS Lab 4 
page  |  20 
Useful references 
Selenium, browsers, GitHub Actions and hosted runner images continue to evolve. Use the official sources below when an 
interface or version changes, while preserving the testing principles and intended evidence described in this laboratory. 
[Terminology Reference] International Software Testing Qualifications Board (ISTQB), Certified Tester Foundation Level Syllabus, Version 4.0.1, 
Section 2.2.1, “Test Levels.” 
Selenium documentation - WebDriver 
Selenium documentation - Selenium Manager 
Selenium documentation - Waiting strategies 
Selenium documentation - Page Object Models 
Selenium documentation - Grid 
SeleniumHQ - Docker Selenium 
NuGet Gallery - Selenium.WebDriver 
Microsoft Learn - Integration tests in ASP.NET Core 
Microsoft Learn - WebApplicationFactory and UseKestrel 
Microsoft Learn - ASP.NET Core Minimal APIs 
Microsoft Learn - dotnet run and launch profiles 
GitHub Docs - Building and testing .NET 
GitHub hosted runner image software 
