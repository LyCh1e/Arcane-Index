---
type: source
folder: wiki/sources
title: INF2007 Mobile Application Development Notes
course: INF2007
status: ingested
updated: 2026-05-09
tags:
  - source
  - mobile
  - android
  - kotlin
  - inf2007
related:
  - kotlin-language
  - android-fundamentals
  - jetpack-compose
  - android-architecture
  - android-di-networking
  - kotlin-coroutines
  - android-background-work
  - mobile-security-patterns
---

# INF2007 Mobile Application Development — Lecture Notes
**Singapore Institute of Technology | AY2025/26 Trimester 2**
**Lecturer: Jeannie S. Lee**

---

## Table of Contents
1. [Course Overview (L0)](#l0-course-overview)
2. [Kotlin Crash Course (L01A)](#l01a-kotlin-crash-course)
3. [Android Platform Introduction (L02)](#l02-android-platform-introduction)
4. [App Fundamentals (L02A)](#l02a-app-fundamentals)
5. [Development Environment & Workflow (L02B)](#l02b-development-environment--workflow)
6. [Jetpack Compose (L03)](#l03-jetpack-compose)
7. [State Hoisting (L04)](#l04-state-hoisting)
8. [Navigation and ViewModel (L05)](#l05-navigation-and-viewmodel)
9. [Architecture (L07)](#l07-architecture)
10. [Hilt and Retrofit (L08)](#l08-hilt-and-retrofit)
11. [Threading & Coroutines (L09)](#l09-threading--coroutines)
12. [Background Work, Broadcast Receiver, Content Provider (L10)](#l10-background-work-broadcast-receiver-content-provider)
13. [Quick Reference](#quick-reference)

---

## L0: Course Overview

### Reference Books
- A. Leiva, *Kotlin for Android Developers*, CreateSpace, 2016
- D. Jemerov & S. Isakova, *Kotlin in Action*, Manning, 2017
- I. Galata, E. Shapiro & J. Howard, *Kotlin Apprentice*, Razeware, 2019

---

## L01A: Kotlin Crash Course

### Variable Declaration
Use `val` for immutable variables (never reassigned), `var` for mutable ones.

```kotlin
var count: Int = 10
count = 15
val languageName: String = "Kotlin"  // cannot be reassigned
```

### Null Safety
Kotlin variables cannot hold null by default. Suffix the type with `?` to allow null.

```kotlin
val languageName: String = null   // Fails to compile
val languageName: String? = null  // OK — nullable type
```

Handle nullable variables carefully to avoid `NullPointerException`.

### Conditionals
`if`, `when`, and `try-catch` are **expressions** in Kotlin — they return values.

### Functions
- Named, extension, inline, and higher-order functions
- Named parameters, multi-value returns (destructuring)
- Lambdas / anonymous functions; semicolons optional

```kotlin
fun greet(name: String): String = "Hello, $name"
val greetLambda = { name: String -> "Hello, $name" }
```

### Classes & Encapsulation
Kotlin auto-generates getters/setters; customise with `get()` / `set()` when needed.

```kotlin
class Car(val wheels: List<Wheel>) {
    private val doorLock: DoorLock = ...
    val gallonsOfFuelInTank: Int = 15
        private set  // setter is private
    fun unlockDoor(key: Key): Boolean { ... }
}
```

### Key Feature Recap
- Null safety (drastically limits NPEs)
- `if`, `try-catch`, `when` as expressions
- `var` / `val` keywords
- Extension, inline, multi-value return functions
- Functional programming: lambdas, higher-order functions
- Named function parameters
- Semicolons optional
- Naming: PascalCase for files with multiple declarations

---

## L02: Android Platform Introduction

### Android OS Stack (simplified, top → bottom)
1. System Apps
2. Java API Framework (Activity Manager, Content Providers, Resource Manager…)
3. Android Runtime (ART) / Native C/C++ Libraries
4. Hardware Abstraction Layer (HAL)
5. Linux Kernel

**Activity Manager** — manages app lifecycle and the navigation back stack.
**Activity** — app component providing a single focused task for the user.

### Virtual Machines Recap
- Early Android: **Dalvik VM** (JIT compilation)
- Modern Android: **ART** (Ahead-of-Time compilation, faster runtime)

---

## L02A: App Fundamentals

### Main App Building Blocks

| Component | Description |
|---|---|
| **Activity** | UI component, typically one screen |
| **Service** | Background long-running operation, no UI |
| **Intent** | Events/messages to start components or send broadcasts |
| **BroadcastReceiver** | Responds to system-wide broadcast announcements |
| **ContentProvider** | Manages shared application data across app boundaries |

### Activity
- Primary class for user interaction
- One Activity = one focused task / one screen
- Apps typically have many activities, laid out as a **back stack**
- Top activity is visible/foreground; background activities are stopped but state retained
- Back button resumes previous activity; Home button moves app to background

### Activity Lifecycle
`onCreate()` → `onStart()` → `onResume()` → `onPause()` → `onStop()` → `onDestroy()`

### Intent
- **Explicit Intent**: targets a specific component by class name
- **Implicit Intent**: declares a general action; Android resolves which component handles it
- Used to start Activities, Services, and send Broadcasts

### Summary
- Apps consist of different components/building blocks
- An app normally runs in one process (could be more)
- Components are instantiated as needed

---

## L02B: Development Environment & Workflow

### Development Environment
- Primary IDE: **Android Studio**
- Key tools: Layout Editor, Logcat, Android Monitor, Profiler

### Emulation vs Simulation
- **Emulator**: fully mimics hardware behaviour — slower but more accurate
- **Simulator**: approximates behaviour — faster but less accurate

### App Workflow
1. Design UI (XML Layout Editor or Jetpack Compose)
2. **Implement Code** — Kotlin/Java classes; at least one Activity with `onCreate()` initialisation
3. Build & compile
4. Test (device or emulator)
5. Deploy / release

### Version Control & CI
- Use **Git** for source control
- **Continuous Integration (CI)** automates build and test pipelines on every commit

---

## L03: Jetpack Compose

### Learning Outcomes
1. Explain why Jetpack Compose exists — limitations of old XML View system vs declarative approach
2. Understand composition, recomposition, and disposal
3. Write simple, correct composables with state using `remember` and `mutableStateOf`

### Why Jetpack Compose?
- Modern toolkit for building native Android UI
- Simplifies UI with **less code** and intuitive Kotlin APIs
- No XML layout files or Layout Editor needed
- Build UI with declarative composable functions
- Requires minimum SDK API level 21+

> **Imperative (old XML):** describe *how* to update the UI step by step.
> **Declarative (Compose):** describe *what* the UI should look like given current state.

### Composable Functions
- Annotated with `@Composable`
- Written in Kotlin — support `if`, loops, helper function calls
- Emit UI; cannot return values
- Dynamic and flexible by nature

### Compose Lifecycle
1. **Composition** — Compose calls composable functions and builds the UI tree
2. **Recomposition** — when state changes, Compose re-runs affected composables
3. **Disposal** — composable leaves the composition

### Recomposition
- Triggered when state changes
- Compose is **selective**: only recomposes functions whose inputs may have changed
- Skips composables whose inputs haven't changed
- Does **not** restart the Activity or re-inflate XML layouts

### UI Tree, Layout Basics & Modifiers
- Compose builds a UI tree from nested composable calls
- Common layout composables: `Column`, `Row`, `Box`
- **Modifiers** chain layout/drawing properties:

```kotlin
Modifier
    .fillMaxWidth()
    .padding(bottom = 32.dp)
    .clickable { ... }
```

### State in Jetpack Compose
- **State**: any value that can change over time
- UI in Compose is immutable — you change *state*, which triggers recomposition
- Use `remember { mutableStateOf(...) }` to hold state within a composable

```kotlin
var userNum by remember { mutableStateOf("") }
TextField(
    value = userNum,
    onValueChange = { userNum = it },
    modifier = Modifier.fillMaxWidth().padding(bottom = 32.dp)
)
Text(text = "Your enter $userNum")
```

---

## L04: State Hoisting

### State Hoisting Pattern
- Move state **up** to a common ancestor so composables become **stateless**
- Pass state **down** as parameters; pass event **callbacks up**
- Stateless composables are easier to test, preview, and reuse

### Stateless vs Stateful
- **Stateful**: owns and manages state internally
- **Stateless**: receives state and events as parameters — preferred for reusable components

---

## L05: Navigation and ViewModel

### Jetpack Navigation
- Define a nav graph with routes/destinations
- Use `NavController` to navigate: `navController.navigate("route")`
- Back stack management: `popUpTo()` with `inclusive = true/false`

### Driving Navigation with State
- Navigation should be a **side-effect of state change**, not a direct click listener
- **Do NOT** pass `NavController` into the ViewModel — keeps ViewModel unaware of Android framework

```kotlin
// ViewModel
var isLoggedIn by mutableStateOf(false)
fun login() { isLoggedIn = true }

// Composable
val loggedIn = viewModel.isLoggedIn
LaunchedEffect(loggedIn) {
    if (loggedIn) {
        navController.navigate("home") {
            popUpTo("login") { inclusive = true }
        }
    }
}
```

### ViewModel
- Survives configuration changes (e.g., screen rotation)
- Holds and manages UI-related state
- Use `MutableStateFlow` exposed as `StateFlow` for reactive state

```kotlin
class MainViewModel : ViewModel() {
    private val _state = MutableStateFlow(0)
    val state = _state.asStateFlow()
    fun increase() { _state.value++ }
}

// In composable
val viewmodel: MainViewModel = viewModel()
val state by viewmodel.state.collectAsState()
```

> A factory (or Hilt) is needed when the ViewModel has constructor parameters.

---

## L07: Architecture

### Architecture Patterns Overview
- **MVC** — Model, View, Controller
- **MVP** — Model, View, Presenter
- **MVVM** — Model, View, ViewModel ← Android recommended
- **MVI** — `view(model(intent()))`; unidirectional cycle

### Recommended Jetpack Architecture

```
UI (Compose)  <──State──  ViewModel  <──  Repository
     │                                         │
   Event                              DAO (Room) + Network (Retrofit)
```

**Key principles:**
- Separation of concerns — drive UI from data models
- Unidirectional data flow — events go up, state flows down
- Single source of truth
- Coroutines & Flows for async data
- Dependency injection best practices

### ViewModel in Architecture

```kotlin
class MainViewModel(private val repository: WordRepository) : ViewModel() {
    val allWords = repository.allWords.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(),
        initialValue = emptyList()
    )
    fun insert(word: String) = viewModelScope.launch {
        repository.insert(Word(word = word))
    }
}
```

### Room (Local Database)
- Abstraction layer over SQLite
- **Entity** (`@Entity`): data class mapped to a DB table
- **DAO**: interface with `@Query`, `@Insert`, `@Update`, `@Delete`
- **RoomDatabase**: abstract class; always access via singleton

### Repository
- Best practice — not a library class, just a design pattern
- Provides a **single clean API** to app data
- Decides whether to fetch from network or use cached local data
- Hides implementation details from ViewModel

### Preference DataStore
- Replaces SharedPreferences for async key-value storage
- Coroutine-based; returns `Flow`

### LiveData vs StateFlow
| | LiveData | StateFlow |
|---|---|---|
| API | Android-specific | Kotlin coroutines |
| Lifecycle-aware | Yes (auto) | Yes (with `repeatOnLifecycle`) |
| Preferred in Compose | No | **Yes** |

---

## L08: Hilt and Retrofit

### Dependency Injection (DI)
- A **dependency** is supplied as a parameter rather than instantiated inside the class
- Enables a **DAG** (Directed Acyclic Graph) of dependencies
- Improves testability, maintainability, and decoupling

### Hilt
- DI framework for Android (Android-specific version of Dagger)
- Uses **annotation processing** and code generation
- Automatically injects Android classes (Activities, Fragments, ViewModels)
- Finds appropriate injection point (e.g., `onCreate()`) automatically

Two common ways to provide dependencies:
1. `@Inject` on constructor
2. `@Module` / `@Provides` or `@Binds` / `@InstallIn` with scope

```kotlin
class TestDependency @Inject constructor() {
    val name = "123"
}

class TestData @Inject constructor(
    testDependency: TestDependency  // Hilt injects this
) {
    val name = testDependency.name
}

class MainActivity : ComponentActivity() {
    @Inject lateinit var testDependency: TestDependency
}
```

> Once using `@Inject`, the conventional constructor call (`TestDependency()`) won't work — Hilt manages instantiation.

### Retrofit
- Type-safe HTTP REST client for Android
- Define API as a Kotlin interface with annotations
- Works seamlessly with coroutines (`suspend` functions) and OkHttp

```kotlin
interface ApiService {
    @GET("users/{id}")
    suspend fun getUser(@Path("id") id: Int): User
}
```

### Summary
- DI: dependency supplied as parameter, forms a DAG
- Hilt: annotation-based DI framework
- Retrofit: REST client that works with coroutines

---

## L09: Threading & Coroutines

### Android Threading
- **Main (UI) Thread**: all UI updates must happen here
- Long-running work on main thread → **ANR** (App Not Responding)
- Offload network, disk, and CPU-heavy work to background threads/coroutines

### Coroutines — Key Ideas
- `suspend fun` = lightweight virtual threading; suspends without blocking the thread
- Each coroutine belongs to a `CoroutineScope`

### Coroutine Builders

| Builder | Purpose |
|---|---|
| `runBlocking {}` | Bridges blocking code and suspending functions |
| `launch {}` | Fire-and-forget; returns a `Job` (cancellable) |
| `async {}` | Returns a `Deferred`; use `.await()` to get result |

```kotlin
// launch: fire-and-forget
viewModelScope.launch {
    repository.insert(word)
}

// async/await: get a result
val result = async { fetchData() }.await()
```

### Suspend Functions
- Does **not block** the thread — suspends the coroutine; thread is freed for other work
- Can only be called from within a coroutine or another suspend function
- `suspend` modifier alone does not start a coroutine or provide a scope

```kotlin
suspend fun printDot() {
    println(".")
    delay(1000)  // suspends, does not block
}
```

### Structured Concurrency
- Manages and tracks the hierarchy of coroutines and their lifetimes
- `CoroutineContext` = `Job` + `Dispatcher` + other elements

**Dispatchers:**
| Dispatcher | Use Case |
|---|---|
| `Dispatchers.Main` | UI thread operations |
| `Dispatchers.IO` | Network / disk I/O |
| `Dispatchers.Default` | CPU-intensive computation |

### Flow
- **Cold stream** — only emits when collected
- **StateFlow** — hot flow that always holds a current value; ideal for UI state
- Collect in composables with `.collectAsState()`

### Side Effects in Compose
- `LaunchedEffect(key)` — runs a coroutine block when `key` changes; used for navigation, analytics, etc.
- `SideEffect` — runs synchronously after every successful recomposition
- `DisposableEffect` — runs setup/cleanup when composable enters/leaves composition

---

## L10: Background Work, Broadcast Receiver, Content Provider

### Background Work Overview
All four main components (Activity, Service, BroadcastReceiver, ContentProvider) run on the **main UI thread** — always offload long-running work to background threads.

Options for background work:
- **Coroutines** — asynchronous work within app lifecycle
- **Services** — component-level background execution
- **WorkManager** — persistent, lifecycle-independent work

### Services
Two main types:
1. **Started Service** (`startService()`) — runs until explicitly stopped; use background thread inside
2. **Bound Service** — clients bind and interact via an interface

### WorkManager
- Recommended solution for **persistent background work**
- Survives app restarts and system reboots
- Supports: Immediate, Long Running, Deferrable work
- Features: work constraints, robust scheduling, work chaining

```
WorkManager > JobScheduler > AlarmManager (for persistent/scheduled work)
```

### Broadcast Receivers
- Implements the **Publish-Subscribe** pattern
- Receives broadcasts from: System (battery, connectivity) or other apps (custom)
- Can be triggered even when the app is **not running**

**Dynamic (preferred)** — registered in code; exists only while app is running:

```kotlin
class NewBroadcastReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // handle broadcast
    }
}

class SomeActivity {
    private val receiver = NewBroadcastReceiver()
    override fun onResume() {
        super.onResume()
        registerReceiver(receiver, IntentFilter(Intent.ACTION_HEADSET_PLUG))
    }
    override fun onPause() {
        super.onPause()
        unregisterReceiver(receiver)
    }
}
```

**Static** — declared in `AndroidManifest.xml`; can receive broadcasts when app not running.

### Content Provider
- Manages a **shared set of application data** accessible across app boundaries
- Exposes a standard URI-based interface for CRUD operations
- Common uses: contacts, media files, or exposing custom app data to other apps

---

## Quick Reference

| Topic | Key Points |
|---|---|
| **Kotlin** | `val`/`var`, null safety (`?`), lambdas, extension functions, expressions |
| **Android Components** | Activity, Service, Intent, BroadcastReceiver, ContentProvider |
| **Jetpack Compose** | Declarative, `@Composable`, recomposition, `remember`, `mutableStateOf` |
| **State** | State hoisting, unidirectional data flow, stateless composables |
| **Navigation** | NavController, nav graph, state-driven navigation (not click-driven) |
| **ViewModel** | Survives config changes, `StateFlow`, `viewModelScope` |
| **Architecture** | MVVM, Repository pattern, Room, single source of truth |
| **Hilt** | `@Inject`, `@Module`/`@Provides`, annotation-based DAG DI |
| **Retrofit** | Type-safe REST client, interface-based API, `suspend` support |
| **Coroutines** | `launch`, `async`, `suspend`, Dispatchers, Flow, structured concurrency |
| **Background** | WorkManager (persistent), Services (foreground/background), BroadcastReceiver |
| **Content Provider** | Shared data across apps, URI-based CRUD |

---

*Notes compiled from INF2007 MAD lecture slides, AY2025/26 Trimester 2, SIT.*
