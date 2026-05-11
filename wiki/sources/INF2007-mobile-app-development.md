---
type: source-index
title: "INF2007 Mobile Application Development"
course: INF2007
institution: SIT
raw: "raw/INF2007 Mobile Application Development Notes.md"
domain: mobile-development
topics: [kotlin, android, jetpack-compose, mvvm, coroutines, hilt, retrofit]
ingested: 2026-05-11
---

# INF2007 — Mobile Application Development

MAD covers professional Android application development using the modern toolchain: Kotlin, Jetpack Compose, MVVM architecture, and the Jetpack suite of libraries. By the end students can build a production-quality Android app with persistent storage, REST API integration, dependency injection, and background work — all following Google's recommended architecture.

## Course Overview

The course layers knowledge intentionally: Kotlin language → Android platform fundamentals → UI with Jetpack Compose → architecture (MVVM) → data layer (Room/Retrofit) → dependency injection (Hilt) → async/concurrency (coroutines/Flow) → background work (WorkManager).

## Key Topics

### Kotlin Language

Kotlin is concise, null-safe, and fully interoperable with Java. Key features:
- `val` (immutable) vs `var` (mutable)
- Null safety: `?`, `!!`, `?.`, `?:` (Elvis)
- Lambdas and higher-order functions
- Extension functions — add methods to existing classes without inheritance
- Data classes (auto-generated `equals`, `hashCode`, `copy`, `toString`)
- Sealed classes for exhaustive `when` expressions

See [[kotlin-coroutines]] for coroutines, Flow, and Hilt.

### Android Platform

The Android OS stack: Linux kernel → HAL → Android Runtime (ART) → Framework APIs → Apps. The four **app components**:
1. **Activity** — a single screen with a UI
2. **Service** — background work with no UI
3. **BroadcastReceiver** — responds to system-wide broadcasts
4. **ContentProvider** — structured data sharing across apps

**Intents** are the messaging objects that activate components (explicit = specific component, implicit = action-based).

The **Activity Lifecycle**: `onCreate → onStart → onResume → [running] → onPause → onStop → onDestroy`. Configuration changes (rotation) restart the Activity by default — ViewModel survives this.

### Jetpack Compose

Compose is Android's modern **declarative UI** toolkit. Instead of inflating XML layouts and mutating views imperatively, you write `@Composable` functions that describe UI as a function of state. When state changes, Compose **recomposes** only the affected subtree.

Key concepts: `remember {}`, `mutableStateOf`, **state hoisting** (lift state up to the lowest common ancestor that needs it), `LazyColumn`, `Scaffold`, `NavHost`.

### MVVM Architecture

See [[android-architecture]] for the full stack. The pattern: **UI Layer** (Composables observe StateFlow) → **ViewModel** (holds UI state, exposes StateFlow, calls repository) → **Repository** (single source of truth, abstracts Room and Retrofit) → **Data Sources** (Room DB or Retrofit service).

### Room Database

Room is a SQLite abstraction. Three components:
- `@Entity` — a data class mapping to a table
- `@Dao` — interface with `@Query`, `@Insert`, `@Update`, `@Delete`
- `@Database` — abstract class, singleton, migration management

### Retrofit

Retrofit turns an interface annotated with HTTP annotations into a type-safe REST client. Uses `GsonConverterFactory` or `MoshiConverterFactory` for JSON serialisation. Supports coroutines with `suspend` functions.

### Navigation

Jetpack Navigation with Compose: `NavController`, `NavHost`, composable destinations, `navigate()`. Navigation is state-driven — back stack is managed automatically.

## Concept Pages

| Concept | Description |
|---------|-------------|
| [[android-architecture]] | Platform, components, lifecycle, MVVM, Room, Compose |
| [[kotlin-coroutines]] | Kotlin basics, coroutines, Flow, Hilt, Retrofit, WorkManager |

## Related Courses

- [[INF1009-object-oriented-programming]] — Kotlin is OOP; patterns like Repository/Singleton apply directly
- [[INF1008-data-structures-algorithms]] — Collections and algorithm choice matter in mobile performance
- [[INF2002-human-computer-interaction]] — UI/UX principles apply to Compose screen design
