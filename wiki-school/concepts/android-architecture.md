---
type: concept
title: "Android Architecture"
domain: mobile-development
course: INF2007
complexity: high
tags: [android, mvvm, jetpack-compose, room, viewmodel, navigation, lifecycle, activity]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000010
---

# Android Architecture

Android architecture covers everything from the OS stack up to the application architecture pattern recommended by Google (MVVM with the Jetpack libraries). Understanding the full stack — from how the OS manages processes to how UI state flows through a ViewModel — is essential for building apps that are responsive, testable, and survive configuration changes.

## Android OS Stack

From lowest to highest:

| Layer | Contents |
|-------|----------|
| **Linux Kernel** | Drivers, memory management, process management, security |
| **HAL (Hardware Abstraction Layer)** | Standardises hardware interfaces for the framework |
| **Android Runtime (ART)** | Compiles and runs Dalvik bytecode (AOT + JIT); manages garbage collection |
| **Native C/C++ Libraries** | OpenGL ES, SQLite, WebKit, media codecs |
| **Java API Framework** | Activity Manager, Window Manager, Content Providers, View System |
| **System Apps** | Dialer, SMS, Browser |
| **User Apps** | Your app |

ART replaced Dalvik VM in Android 5.0 (Lollipop). ART uses Ahead-Of-Time (AOT) compilation — apps run faster but install slightly slower.

## The Four App Components

Android's process model is component-based. The OS can launch any component independently.

### 1. Activity

A single screen with a user interface. The most common component. Activities are stacked in a **back stack** — Back button pops the stack.

Each Activity has a lifecycle (see below). Multiple activities in an app communicate via Intents.

### 2. Service

A component that performs long-running operations **in the background** with no UI. Types:
- **Foreground service**: user-visible (notification required), survives app backgrounding (music player)
- **Background service**: no notification, can be killed by OS; use WorkManager instead
- **Bound service**: allows other components to bind and interact via IPC

### 3. BroadcastReceiver

Responds to system-wide broadcast announcements (battery low, connectivity change, boot complete). Can also receive custom broadcasts. Should execute quickly — long work offloaded to a Service or WorkManager.

### 4. ContentProvider

Manages structured shared data across apps. Backed by SQLite, files, or network. Uses URI-based addressing (`content://authority/path`). Contacts, MediaStore, and Calendar use built-in ContentProviders.

### Intents

Messaging objects that activate components:
- **Explicit Intent**: specifies exact target component by class (`new Intent(this, DetailActivity.class)`)
- **Implicit Intent**: specifies an action (`ACTION_VIEW`, `ACTION_SEND`); OS resolves to appropriate app

## Activity Lifecycle

```
onCreate() → onStart() → onResume()
                              ↓ (user switches away)
                         onPause()
                              ↓ (becomes not visible)
                         onStop()
                              ↓ (back pressed / finish())
                         onDestroy()
```

Key callbacks:
- `onCreate()` — one-time setup, inflate layout/set content, observe ViewModel
- `onStart()` / `onStop()` — visibility events; start/stop animations
- `onResume()` / `onPause()` — focus events; pause/resume camera, sensors
- `onDestroy()` — cleanup; called on rotation (configuration change)

**Configuration changes** (rotation, locale, font size) destroy and recreate the Activity. **ViewModel** survives this — it is scoped to the Activity's lifecycle but not to the Activity instance.

## MVVM Architecture (Google's Recommended)

```
UI Layer         ViewModel Layer      Data Layer
─────────────────────────────────────────────────
Composables  →   ViewModel        →   Repository
(observe         (holds UI state,     (single source
 StateFlow)       calls repo)          of truth)
                                          ↓         ↓
                                       Room    Retrofit
                                      (local) (remote)
```

### Separation of Concerns

- **UI Layer**: purely reactive — observes StateFlow, sends events to ViewModel, no business logic
- **ViewModel**: survives configuration changes, holds and exposes UI state as StateFlow, orchestrates data operations
- **Repository**: hides data source details; decides when to use cache vs network
- **Data Sources**: Room for local persistence, Retrofit for REST API

### ViewModel

```kotlin
class TaskViewModel(private val repository: TaskRepository) : ViewModel() {
    private val _tasks = MutableStateFlow<List<Task>>(emptyList())
    val tasks: StateFlow<List<Task>> = _tasks.asStateFlow()

    init { loadTasks() }

    fun loadTasks() {
        viewModelScope.launch {
            _tasks.value = repository.getAllTasks()
        }
    }
}
```

`viewModelScope` is a coroutine scope tied to the ViewModel's lifecycle — cancelled automatically when ViewModel is cleared. `StateFlow` is a hot, state-holding Flow that always has a current value.

## Jetpack Compose

Compose is Android's modern **declarative UI toolkit** (stable since 2021). Instead of XML layouts and imperative view mutations, UI is described as a function of state.

### Core Concepts

**Composable functions**: annotated with `@Composable`, return Unit, describe UI.

```kotlin
@Composable
fun Greeting(name: String) {
    Text(text = "Hello, $name!")
}
```

**Recomposition**: when state changes, Compose re-executes only the composable functions that read that state. Compose tracks state reads and invalidates only affected subtrees.

**remember**: caches a value across recompositions.

```kotlin
var count by remember { mutableStateOf(0) }
```

### State Hoisting

Move state **up** to the lowest common ancestor that needs it. Pass state down as parameters and event callbacks up via lambdas. This pattern makes composables **stateless and reusable**.

```kotlin
// Stateless (reusable, testable)
@Composable
fun Counter(count: Int, onIncrement: () -> Unit) {
    Button(onClick = onIncrement) { Text("Count: $count") }
}

// Stateful parent (owns the state)
@Composable
fun CounterScreen() {
    var count by remember { mutableStateOf(0) }
    Counter(count = count, onIncrement = { count++ })
}
```

### Key Composables

- `Column`, `Row`, `Box` — layout containers
- `LazyColumn`, `LazyRow` — RecyclerView equivalents
- `Scaffold` — material design layout with top bar, FAB, bottom bar
- `Text`, `Button`, `TextField`, `Image` — basic UI elements
- `NavHost` — navigation container

## Room Database

Room is a SQLite abstraction with compile-time query verification.

### Three Components

**Entity**: a data class annotated with `@Entity`. Each instance = one row.

```kotlin
@Entity(tableName = "tasks")
data class Task(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val title: String,
    val isDone: Boolean = false
)
```

**DAO (Data Access Object)**: an interface with query annotations.

```kotlin
@Dao
interface TaskDao {
    @Query("SELECT * FROM tasks") fun getAll(): Flow<List<Task>>
    @Insert suspend fun insert(task: Task)
    @Delete suspend fun delete(task: Task)
}
```

**RoomDatabase**: abstract class annotated with `@Database`. Singleton.

```kotlin
@Database(entities = [Task::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun taskDao(): TaskDao
}
```

Returning `Flow<List<Task>>` from a DAO means Room automatically emits a new list whenever the database changes — reactive data.

## Navigation

Jetpack Navigation Compose uses `NavController` and `NavHost`:

```kotlin
NavHost(navController, startDestination = "list") {
    composable("list") { TaskListScreen(navController) }
    composable("detail/{taskId}") { backStackEntry ->
        TaskDetailScreen(backStackEntry.arguments?.getString("taskId"))
    }
}
```

Navigation is state-driven — the back stack is modelled as application state, not a side-effect of Activity launches.

## See Also

- [[kotlin-coroutines]] — Kotlin language, coroutines, Flow, Hilt, Retrofit, WorkManager
- [[oop-four-pillars]] — OOP relationships applied: Repository (Facade), ViewModel (Observer)
- [[solid-and-design-patterns]] — MVVM is an architectural application of SOLID principles
- [[INF2007-mobile-app-development]] — source course
