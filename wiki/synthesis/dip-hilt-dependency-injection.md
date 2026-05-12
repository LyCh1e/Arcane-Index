---
type: synthesis
title: "DIP in Practice: How Hilt Implements the Dependency Inversion Principle"
domains: [software-engineering, mobile-development]
courses: [ICT2112, INF2007]
complexity: high
tags: [solid, dip, dependency-injection, hilt, dagger, android, testing, inversion-of-control]
updated: 2026-05-12
maturity: established
---

# DIP in Practice: How Hilt Implements the Dependency Inversion Principle

The **Dependency Inversion Principle** (ICT2112) and **Hilt** (INF2007) are the same idea at different altitudes — one is an abstract design principle, the other is a concrete framework that enforces it. Understanding this connection turns Hilt from a "magic annotation tool" into a principled architectural decision.

---

## The Principle (ICT2112)

From [[concepts/solid-and-design-patterns]]:

> **High-level modules should not depend on low-level modules. Both should depend on abstractions.**  
> Abstractions should not depend on details. Details should depend on abstractions.

The canonical violation is a high-level module directly instantiating a low-level module:

```csharp
// ICT2112 violation example (C#)
public class OrderService {
    private MySQLRepository _repo = new MySQLRepository();  // high-level depends on low-level
}
```

If the database changes to PostgreSQL, `OrderService` must be edited — the two are tightly coupled at the Content level (see [[concepts/software-design-process]] coupling scale).

The DIP fix: introduce an abstraction.

```csharp
// DIP-compliant (C#)
public class OrderService {
    private readonly IOrderRepository _repo;

    public OrderService(IOrderRepository repo) {  // depends on abstraction
        _repo = repo;
    }
}
// The concrete MySQLRepository implements IOrderRepository
// Something external (a DI container) supplies the concrete instance
```

`OrderService` no longer knows which database it talks to. The *caller* is responsible for supplying the concrete implementation — this is **Inversion of Control (IoC)**.

---

## The Framework (INF2007)

Hilt is Google's DI framework for Android, built on Dagger 2. It automates the IoC pattern: instead of writing manual factory code to wire dependencies, annotations tell Hilt what to inject and where to obtain it.

### The Same Structure, in Kotlin

```kotlin
// INF2007 — DIP in Android (Kotlin/Hilt)

// Abstraction (the interface both sides depend on)
interface TaskRepository {
    suspend fun getAllTasks(): List<Task>
    suspend fun insert(task: Task)
}

// Low-level module: concrete implementation
class TaskRepositoryImpl @Inject constructor(
    private val dao: TaskDao,
    private val api: TaskApiService
) : TaskRepository {
    override suspend fun getAllTasks() = dao.getAll()
    override suspend fun insert(task: Task) = dao.insert(task)
}

// High-level module: depends only on the abstraction
@HiltViewModel
class TaskViewModel @Inject constructor(
    private val repository: TaskRepository  // ← interface, not impl
) : ViewModel() {
    val tasks = repository.getAllTasks()
}
```

`TaskViewModel` never mentions `TaskRepositoryImpl`, `TaskDao`, or `Room`. It cannot be affected by a switch from Room to another persistence library — as long as the new library's adapter implements `TaskRepository`.

---

## The Mapping: DIP Concept → Hilt Mechanism

| DIP Concept | Hilt Mechanism |
|-------------|---------------|
| Abstraction | Interface / abstract class |
| High-level module | ViewModel (or any class with `@Inject constructor`) |
| Low-level module | `TaskRepositoryImpl`, `AppDatabase`, `Retrofit` service |
| IoC container | Hilt component hierarchy (`SingletonComponent`, `ViewModelComponent` …) |
| Binding (what implements what) | `@Binds` in a `@Module` |
| Provision (how to create) | `@Provides` in a `@Module` |
| Lifetime / scope | `@Singleton` → one instance per app; `@ViewModelScoped` → one per ViewModel |

### @Binds — Wiring the Abstraction

```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    @Singleton
    abstract fun bindTaskRepository(
        impl: TaskRepositoryImpl  // Hilt builds this
    ): TaskRepository             // and supplies it wherever TaskRepository is needed
}
```

`@Binds` tells Hilt: "when anyone asks for `TaskRepository`, give them `TaskRepositoryImpl`." The ViewModel never knows.

### @Provides — Creating Infrastructure Dependencies

When constructor injection is impossible (e.g., third-party classes like `Room.databaseBuilder`), `@Provides` is used:

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {
    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext ctx: Context): AppDatabase =
        Room.databaseBuilder(ctx, AppDatabase::class.java, "tasks.db").build()

    @Provides
    fun provideTaskDao(db: AppDatabase): TaskDao = db.taskDao()
}
```

Hilt resolves the full dependency graph: `TaskViewModel` needs `TaskRepository` → Hilt provides `TaskRepositoryImpl` → which needs `TaskDao` → Hilt provides it from `AppDatabase` → which needs `Context` → Hilt provides `@ApplicationContext`.

---

## Why This Matters: Testability

The most concrete benefit of DIP + Hilt is **unit testability without an Android device**.

**Without DIP** — the ViewModel creates its own repository:
```kotlin
class TaskViewModel : ViewModel() {
    private val repo = TaskRepositoryImpl(/* needs Room, needs Context */)
    // Untestable without a real database and Android environment
}
```

**With DIP + Hilt** — the ViewModel receives the repository:
```kotlin
// In tests: supply a fake
val fakeRepo = FakeTaskRepository(listOf(Task("Buy milk"), Task("Walk dog")))
val viewModel = TaskViewModel(fakeRepo)
// Test the ViewModel in pure JUnit, no Android, no Room, no network
```

This directly satisfies the **Testability** quality attribute from [[concepts/software-design-process]].

---

## The Singleton Connection

`@Singleton` in Hilt and the **Singleton GoF pattern** from [[concepts/solid-and-design-patterns]] serve the same purpose — ensuring exactly one instance exists — but Hilt does it transparently:

| GoF Singleton | Hilt @Singleton |
|---------------|----------------|
| Class manages its own instance (`private static _instance`) | Hilt's `SingletonComponent` manages the instance |
| Global state is hard to replace in tests | Hilt test modules can swap the singleton |
| Thread safety requires explicit locking | Hilt handles creation safely |

Hilt's managed singleton is strictly superior for testability: you can swap the singleton out in tests by providing a different `@TestInstallIn` module. The GoF Singleton pattern's key weakness — untestability due to global state — is eliminated.

---

## Component Hierarchy = Scope Hierarchy

The DIP principle says nothing about lifetime — Hilt adds this with its component hierarchy. Each component is tied to an Android lifecycle; a dependency scoped to a component lives as long as that component:

```
SingletonComponent       → @Singleton     → app lifetime
  ActivityRetainedComponent → @ActivityRetainedScoped → survives rotation
    ViewModelComponent       → @ViewModelScoped        → ViewModel lifetime
    ActivityComponent        → @ActivityScoped         → Activity lifetime
      FragmentComponent      → @FragmentScoped         → Fragment lifetime
```

**Rule of thumb:**
- Database and repositories → `@Singleton` (shared, expensive to create, stateless)
- ViewModel-specific helpers → `@ViewModelScoped`
- UI-specific adapters → `@ActivityScoped` or `@FragmentScoped`

---

## Design Smell Diagnosis

When reviewing Android code for DIP violations, look for these design smells (from [[concepts/software-design-process]]):

| Symptom | Smell | Fix |
|---------|-------|-----|
| ViewModel contains `= SomeClass()` or `= SomeClass.getInstance()` | **Rigidity** — changing the class forces ViewModel edits | Inject via constructor |
| Class is impossible to unit test without a real database | **Fragility** — test environment bleeds into prod code | Extract interface; inject fake in tests |
| Repository implementation details leak into the ViewModel | **Opacity** — ViewModel code is hard to reason about | Depend on interface only |
| Multiple classes each create their own database connection | **Needless Repetition** — violates DRY | `@Singleton` database in Hilt module |

---

## Summary

```
ICT2112 DIP Principle
    "Depend on abstractions, not concretions."
            │
            ▼
    Define interfaces for all cross-layer dependencies
            │
            ▼
    Inject concrete implementations from outside the class
            │
            ▼
INF2007 Hilt Framework automates this:
    @Inject constructor  → declares what you need (abstraction)
    @Binds / @Provides   → declares how to build it (concretion)
    @Singleton / scopes  → declares how long it lives
    Component hierarchy  → tied to Android lifecycle
```

Hilt is not magic — it is DIP made automatic. Every `@Inject constructor` is a DIP-compliant dependency declaration. Every `@Module` is the IoC container that resolves those declarations.

---

## See Also

- [[concepts/solid-and-design-patterns]] — DIP definition, all SOLID principles, GoF Singleton
- [[concepts/software-design-process]] — coupling scale; testability quality attribute; design smells
- [[concepts/kotlin-coroutines]] — Hilt annotations and component hierarchy in full detail
- [[concepts/android-architecture]] — MVVM architecture that DIP + Hilt makes testable
- [[synthesis/data-mapper-repository-room-retrofit]] — the complementary synthesis: how the Repository pattern bridges Data Mapper (ICT2112) and Room + Retrofit (INF2007)
