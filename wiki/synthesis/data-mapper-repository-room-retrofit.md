---
type: synthesis
title: "Data Mapper & Repository: Bridging ICT2112 Patterns and Android's Room + Retrofit"
domains: [software-engineering, mobile-development]
courses: [ICT2112, INF2007]
complexity: high
tags: [data-mapper, repository, room, retrofit, active-record, table-data-gateway, android, architecture, persistence]
updated: 2026-05-12
maturity: established
---

# Data Mapper & Repository: Bridging ICT2112 Patterns and Android's Room + Retrofit

ICT2112 identifies four data source layer patterns — Table Data Gateway, Row Data Gateway, Active Record, and Data Mapper — as abstract solutions to the problem of keeping domain objects and database infrastructure decoupled. INF2007's Android stack (Room + Retrofit + Repository) is a concrete instantiation of the same ideas. Mapping one to the other removes the gap between "pattern theory" and "Android code."

---

## The Problem Both Worlds Solve

The fundamental tension in any data-driven system is:

- **Domain objects** must be clean, testable, and free to evolve with business logic
- **Database schema** (or API contract) evolves independently, driven by storage or network concerns
- **Naive coupling** — where the domain object is also the database record — makes each side hostage to the other

This is the ICT2112 coupling problem at the data layer. The patterns below represent progressively stronger separations.

---

## Pattern Mapping: ICT2112 → Android

### Active Record ↔ Room Entity (naïve usage)

The **Active Record** pattern (ICT2112) collapses domain object and database record into one class. The object *is* the row — it carries both data and persistence behaviour.

In Android, using a Room `@Entity` directly as the domain model is the Active Record approach:

```kotlin
// Android Active Record style — Entity IS the domain object
@Entity(tableName = "tasks")
data class Task(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val title: String,
    val isDone: Boolean = false
    // Fields driven by BOTH business logic AND database schema
)

@Dao
interface TaskDao {
    @Query("SELECT * FROM tasks")
    fun getAll(): Flow<List<Task>>   // returns the Entity directly
    @Insert suspend fun insert(task: Task)
}
```

The ViewModel receives `Task` objects from the DAO and uses them directly. The schema and domain model are the same thing.

**When this is fine:** CRUD-heavy apps with simple domain logic (to-do lists, note apps). The simplicity is genuine; complexity is not being avoided, it simply does not exist.

**When this breaks down:** Business logic accumulates on `Task`. The schema adds a `blob` column for caching. A new API returns `TaskDto` with different field names. Each change collides with the others — Active Record's coupling tax is due.

---

### Table Data Gateway ↔ Room DAO

The **Table Data Gateway** (ICT2112) is an object that manages all rows of one database table through CRUD methods. One instance; returns raw data (DataTable/DataRow in .NET).

Room's `@Dao` interface is a direct implementation of this pattern:

```kotlin
// Room DAO = Table Data Gateway
@Dao
interface TaskDao {
    @Query("SELECT * FROM tasks") fun getAll(): Flow<List<TaskEntity>>
    @Query("SELECT * FROM tasks WHERE id = :id") suspend fun findById(id: Int): TaskEntity?
    @Insert(onConflict = OnConflictStrategy.REPLACE) suspend fun insert(task: TaskEntity)
    @Update suspend fun update(task: TaskEntity)
    @Delete suspend fun delete(task: TaskEntity)
}
```

| ICT2112 TDG | Room DAO |
|-------------|----------|
| `FindAll()` | `@Query("SELECT * FROM tasks")` |
| `FindById(id)` | `@Query("SELECT * FROM tasks WHERE id = :id")` |
| `Insert(...)` | `@Insert` |
| `Update(...)` | `@Update` |
| `Delete(...)` | `@Delete` |
| Returns raw data | Returns `@Entity` or primitive |

The critical observation: the DAO returns `TaskEntity` objects (shaped by the schema), not `Task` domain objects. Something above the DAO must perform the mapping.

---

### Data Mapper ↔ Repository + Mapper functions

The **Data Mapper** (ICT2112) is a layer that moves data between domain objects and the database while keeping them completely independent. Domain objects know nothing about the database; the database schema need not match the object structure.

In Android, the **Repository** class is the Data Mapper. It sits between the ViewModel (domain layer) and the DAO/API (data source layer) and owns the translation:

```kotlin
// Separate domain model (no Room annotations)
data class Task(
    val id: Int,
    val title: String,
    val isCompleted: Boolean
)

// Database entity (schema-shaped)
@Entity(tableName = "tasks")
data class TaskEntity(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val title: String,
    val is_done: Int  // SQLite has no Boolean; stored as 0/1
)

// Network DTO (API-shaped)
data class TaskDto(
    val task_id: Int,
    val task_title: String,
    val completed: Boolean
)

// Data Mapper / Repository — owns all translations
class TaskRepositoryImpl @Inject constructor(
    private val dao: TaskDao,
    private val api: TaskApiService
) : TaskRepository {

    // Entity → Domain
    private fun TaskEntity.toDomain() = Task(id, title, is_done == 1)

    // Domain → Entity
    private fun Task.toEntity() = TaskEntity(id, title, if (isCompleted) 1 else 0)

    // DTO → Domain
    private fun TaskDto.toDomain() = Task(task_id, task_title, completed)

    override fun getAllTasks(): Flow<List<Task>> =
        dao.getAll().map { entities -> entities.map { it.toDomain() } }

    override suspend fun syncFromNetwork() {
        val dtos = api.getTasks()
        dao.insertAll(dtos.map { it.toEntity() })
    }
}
```

**What the ViewModel sees:** a `Flow<List<Task>>` — pure domain objects, no `@PrimaryKey`, no `is_done`, no `task_id`. The ViewModel and all UI code above it are completely isolated from Room and Retrofit.

---

### Retrofit Service ↔ Remote Data Gateway

Retrofit's annotated interface (INF2007) is not explicitly named in ICT2112's taxonomy, but it maps cleanly to a **Remote Data Gateway** — a Table Data Gateway whose "table" is a REST endpoint:

```kotlin
// Remote Data Gateway via Retrofit
interface TaskApiService {
    @GET("tasks")          suspend fun getTasks(): List<TaskDto>
    @POST("tasks")         suspend fun createTask(@Body task: TaskDto): TaskDto
    @DELETE("tasks/{id}")  suspend fun deleteTask(@Path("id") id: Int)
}
```

| TDG concept | Retrofit equivalent |
|-------------|-------------------|
| `FindAll()` | `@GET("tasks")` |
| `Insert(data)` | `@POST("tasks")` |
| `Delete(id)` | `@DELETE("tasks/{id}")` |
| Returns raw data | Returns DTO |

The Repository consumes both Room DAO and Retrofit service and hides both behind the `TaskRepository` interface — acting as a **Facade** (see [[concepts/software-architecture-patterns]]) over the two data gateways.

---

## The Full Stack, Named by Pattern

```
UI Layer (Jetpack Compose)
    │  observes Flow<Task>       ← pure domain objects
    ▼
ViewModel
    │  calls TaskRepository (interface — DIP)
    ▼
Repository  ←────────────── Data Mapper (maps Entity↔Domain, DTO↔Domain)
    │              │          Facade (hides whether local or remote)
    ▼              ▼
Room DAO       Retrofit Service
(Table Data    (Remote Data
 Gateway)       Gateway)
    │              │
    ▼              ▼
SQLite DB     REST API
```

---

## When to Use Active Record vs Data Mapper in Android

| Criterion | Active Record (Entity = Domain) | Data Mapper (Separate models) |
|-----------|--------------------------------|-------------------------------|
| Domain logic | Simple, mostly CRUD | Complex, involves calculations, rules |
| Schema stability | Stable; schema == domain | Schema evolves independently of domain |
| API integration | Local DB only | Remote API with different field names |
| Testability | Harder (domain tied to Room) | Easy (domain objects are plain classes) |
| Code volume | Less (one class) | More (Entity + Domain + mapper functions) |
| Team size | Solo or small | Larger teams; separate DB and business owners |

**Practical guideline:** Start with Active Record (Entity as domain). Introduce the Data Mapper split *when* you first find yourself putting business logic into the Entity, or when your API response shape diverges from your local storage shape.

---

## Design Smell: Leaky Abstraction

A common mistake is using `@Entity` classes directly in the ViewModel:

```kotlin
// ❌ Leaky — ViewModel knows about Room schema
class TaskViewModel @Inject constructor(
    private val dao: TaskDao  // DAO, not Repository
) : ViewModel() {
    val tasks: Flow<List<TaskEntity>> = dao.getAll()  // Entity in UI layer
}
```

This violates the **Layered Architecture** rule (upper layers should not know the implementation of lower layers — [[concepts/software-architecture-patterns]]). `@PrimaryKey`, `@ColumnInfo`, and schema-specific field names appear in the ViewModel. When the schema changes, the ViewModel must change too.

The fix is always the same: insert a Repository that owns the mapping.

---

## Connection to ICT2112 Quality Attributes

| ICT2112 Quality Attribute | How Data Mapper + Repository Satisfies It |
|---------------------------|------------------------------------------|
| **Maintainability** | Schema changes are contained in Entity + mapper functions; domain and ViewModel are unaffected |
| **Testability** | Domain objects are plain Kotlin data classes; testable without Room or a real database |
| **Reusability** | `TaskRepository` interface can be implemented differently for tests, for a different backend, or for an offline-first vs. always-online strategy |
| **Conceptual Integrity** | Each layer has a single responsibility; the boundary between layers is clear and explicit |

---

## Summary

| ICT2112 Pattern | Android Equivalent | Role |
|-----------------|-------------------|------|
| Table Data Gateway | Room `@Dao` | CRUD operations on local SQLite table |
| Remote Data Gateway | Retrofit `interface` | CRUD operations on remote REST endpoint |
| Active Record | `@Entity` used directly as domain model | Acceptable for simple CRUD; couples domain to schema |
| Data Mapper | `Repository` + mapper extension functions | Translates Entity↔Domain↔DTO; keeps layers independent |
| Facade | `Repository` hiding both DAO and Retrofit | Single interface to multiple data sources |

The Android Repository is not one ICT2112 pattern — it is three at once: **Data Mapper** (translation), **Facade** (simplification), and the boundary that makes **DIP** possible (see [[synthesis/dip-hilt-dependency-injection]]). Recognising this makes both the ICT2112 theory and the INF2007 practice considerably clearer.

---

## See Also

- [[concepts/software-architecture-patterns]] — Data Mapper, Active Record, TDG, Facade, Layered Architecture
- [[concepts/solid-and-design-patterns]] — Facade, DIP, and the Singleton used for `AppDatabase`
- [[concepts/android-architecture]] — Room, ViewModel, MVVM full detail
- [[concepts/kotlin-coroutines]] — Retrofit, Hilt modules, `@Inject constructor`
- [[synthesis/dip-hilt-dependency-injection]] — complementary synthesis: how DIP + Hilt enables the Repository interface to be injected
