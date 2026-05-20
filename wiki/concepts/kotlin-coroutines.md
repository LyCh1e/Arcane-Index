---
type: concept
title: "Kotlin, Coroutines, and Android Async"
domain: mobile-development
course: INF2007
complexity: high
tags: [kotlin, coroutines, flow, stateflow, hilt, retrofit, workmanager, dependency-injection]
updated: 2026-05-11
status: established
created: 2026-05-11
address: c-000011
---

# Kotlin, Coroutines, and Android Async

This page covers Kotlin language features used in Android development, the coroutines framework for asynchronous programming, and the key libraries that build on it: Hilt for dependency injection, Retrofit for REST, and WorkManager for background tasks.

## Kotlin Language Essentials

### Variables

```kotlin
val name = "Alice"    // immutable (cannot reassign)
var count = 0         // mutable (can reassign)
```

Kotlin uses type inference — explicit types optional when clear from context.

### Null Safety

Kotlin's type system distinguishes nullable from non-nullable types at compile time, eliminating most NPEs.

```kotlin
val name: String = "Alice"     // cannot be null — compile error if assigned null
val nullable: String? = null   // explicitly nullable

nullable?.length               // safe call — returns null if nullable is null
nullable ?: "default"          // Elvis operator — returns "default" if null
nullable!!.length              // not-null assertion — throws NPE if null (use sparingly)
```

### Lambdas and Higher-Order Functions

```kotlin
val double: (Int) -> Int = { x -> x * 2 }

// Trailing lambda syntax (most common)
listOf(1, 2, 3).filter { it > 1 }.map { it * 2 }
```

### Extension Functions

Add methods to existing classes without inheritance or modification:

```kotlin
fun String.isPalindrome(): Boolean = this == this.reversed()
"racecar".isPalindrome()  // true
```

Android uses extension functions extensively (e.g., `View.isVisible`, `Context.toast()`).

### Data Classes

```kotlin
data class User(val id: Int, val name: String)
```

Compiler auto-generates: `equals()`, `hashCode()`, `toString()`, `copy()`, and `componentN()` functions (for destructuring). Ideal for DTOs, database entities, and UI state models.

### Sealed Classes

All subclasses must be in the same package/file. Enables exhaustive `when` expressions — compiler guarantees all cases handled.

```kotlin
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val message: String) : Result<Nothing>()
    object Loading : Result<Nothing>()
}

when (result) {
    is Result.Success -> showData(result.data)
    is Result.Error   -> showError(result.message)
    Result.Loading    -> showSpinner()
    // No else needed — compiler verifies exhaustiveness
}
```

## Coroutines

Coroutines are Kotlin's solution to asynchronous programming. They are **lightweight threads** — thousands can run concurrently without the overhead of OS threads. Coroutines avoid callback hell and produce sequential-looking async code.

### launch vs async

```kotlin
// launch — fire and forget; returns Job
val job = viewModelScope.launch {
    repository.syncData()  // runs asynchronously
}

// async — concurrent computation; returns Deferred<T>
val deferred: Deferred<Int> = viewModelScope.async {
    computeHeavyResult()
}
val result = deferred.await()  // suspends until result ready
```

### suspend Functions

A `suspend` function can be paused and resumed without blocking the calling thread. Can only be called from another coroutine or another suspend function.

```kotlin
suspend fun fetchUser(id: Int): User {
    return apiService.getUser(id)  // network call — doesn't block thread
}
```

Under the hood, the compiler transforms suspend functions into a state machine using continuations.

### Dispatchers

Coroutine dispatchers determine which thread(s) a coroutine runs on:

| Dispatcher | Thread pool | Use for |
|------------|------------|---------|
| `Dispatchers.Main` | Main/UI thread | UI updates, ViewModel operations |
| `Dispatchers.IO` | Expandable (up to 64 threads) | File I/O, network, database |
| `Dispatchers.Default` | CPU-bound (= CPU cores) | Heavy computation, sorting |
| `Dispatchers.Unconfined` | No specific thread | Testing, immediate start |

```kotlin
viewModelScope.launch {
    val data = withContext(Dispatchers.IO) {
        repository.fetchFromNetwork()  // runs on IO thread
    }
    _uiState.value = data  // back on Main thread
}
```

### Structured Concurrency

Coroutines follow a **parent-child hierarchy**: a child coroutine inherits the scope of its parent. If the parent is cancelled, all children are cancelled. If a child throws an uncaught exception, the parent and siblings are cancelled.

```
viewModelScope (CoroutineScope)
├── launch (Job A)
│   └── async (Deferred B) ← child of A
└── launch (Job C)
```

`viewModelScope` is automatically cancelled when the ViewModel is cleared — preventing memory leaks from dangling coroutines.

## Flow, StateFlow, and collectAsState

### Flow

A cold, asynchronous stream of values. Produces values only when collected. Built on coroutines.

```kotlin
fun numberStream(): Flow<Int> = flow {
    for (i in 1..5) {
        delay(100)
        emit(i)
    }
}

// Collect in a coroutine
numberStream()
    .filter { it % 2 == 0 }
    .map { it * 10 }
    .collect { println(it) }  // 20, 40
```

Room DAOs return `Flow<List<T>>` — the flow re-emits whenever the underlying data changes.

### StateFlow

A **hot**, state-holding flow with a current value. Always has a value; new collectors immediately receive the latest. Used in ViewModels to expose UI state.

```kotlin
private val _uiState = MutableStateFlow(UiState())
val uiState: StateFlow<UiState> = _uiState.asStateFlow()

// Update state
_uiState.update { it.copy(isLoading = true) }
```

### collectAsState in Compose

```kotlin
val uiState by viewModel.uiState.collectAsState()
// uiState is now a Compose State — recomposition triggered on change
```

`collectAsState` bridges the Flow/StateFlow world and Compose's state system.

## Hilt — Dependency Injection

Hilt is Google's DI framework for Android, built on Dagger 2. It implements the Dependency Inversion Principle from [[solid-and-design-patterns]].

### Core Annotations

```kotlin
// Mark class as injectable with its dependencies
@HiltViewModel
class TaskViewModel @Inject constructor(
    private val repository: TaskRepository
) : ViewModel()

// Provide dependencies (when constructor injection isn't possible)
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {
    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): AppDatabase =
        Room.databaseBuilder(context, AppDatabase::class.java, "app.db").build()
}
```

### Component Hierarchy

Hilt components are tied to Android lifecycles:
- `SingletonComponent` — app lifetime
- `ActivityRetainedComponent` — survives configuration changes
- `ViewModelComponent` — ViewModel lifetime
- `ActivityComponent` — Activity lifetime
- `FragmentComponent` — Fragment lifetime

`@Singleton` scopes a dependency to one instance per `SingletonComponent` — the standard scope for database and repository.

## Retrofit — REST API Client

Retrofit turns an annotated Kotlin interface into a type-safe HTTP client.

```kotlin
interface TaskApiService {
    @GET("tasks")
    suspend fun getTasks(): List<TaskDto>

    @POST("tasks")
    suspend fun createTask(@Body task: TaskDto): TaskDto

    @DELETE("tasks/{id}")
    suspend fun deleteTask(@Path("id") id: Int)
}

// Build once, inject everywhere (via Hilt Module)
val retrofit = Retrofit.Builder()
    .baseUrl("https://api.example.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val apiService = retrofit.create(TaskApiService::class.java)
```

`suspend` functions in the interface mean Retrofit handles threading automatically — no callbacks needed.

## WorkManager — Background Work

WorkManager is the Jetpack solution for **deferrable, guaranteed background work**. Unlike background Services, WorkManager survives process death, app restarts, and device reboots.

```kotlin
class SyncWorker(context: Context, params: WorkerParameters) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        return try {
            repository.syncWithServer()
            Result.success()
        } catch (e: Exception) {
            Result.retry()
        }
    }
}

// Enqueue
val request = PeriodicWorkRequestBuilder<SyncWorker>(15, TimeUnit.MINUTES)
    .setConstraints(Constraints(requiresNetwork = true))
    .build()

WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "sync", ExistingPeriodicWorkPolicy.KEEP, request
)
```

`CoroutineWorker` provides a suspend `doWork()` that runs on `Dispatchers.Default`. Return `Result.success()`, `Result.failure()`, or `Result.retry()`.

## See Also

- [[android-architecture]] — MVVM, Room, Compose, Activity lifecycle
- [[solid-and-design-patterns]] — DIP implemented by Hilt; Singleton pattern for app-wide instances
- [[INF2007-mobile-app-development]] — source course
