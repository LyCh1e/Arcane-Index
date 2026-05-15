---
type: area
title: "Mobile Development"
domain: mobile-development
sources: [[[sources/INF2007-mobile-app-development]], [[sources/INF1009-object-oriented-programming]]]
updated: 2026-05-15
tags: [area, mobile-development]
---

# Mobile Development

**Sources**: INF2007 — Mobile Application Development (Android) and INF1009 — Object-Oriented Programming, SIT.

---

## What I Know

Android application development using Kotlin and the Jetpack library stack. INF1009 establishes OOP foundations in Java/Kotlin. INF2007 builds on these with MVVM architecture, Jetpack Compose, Room, Retrofit, coroutines, and navigation. Together they cover the full lifecycle of a production Android app.

---

## Concept Pages

| Page | Source | What It Covers |
|------|--------|---------------|
| [[concepts/oop-four-pillars\|OOP: Four Pillars]] | INF1009 | Encapsulation, inheritance, polymorphism, abstraction; Java/Kotlin class syntax; interfaces; access modifiers |
| [[concepts/android-architecture\|Android Architecture & Jetpack]] | INF2007 | MVVM (Model-View-ViewModel), LiveData, ViewModel lifecycle, Jetpack Compose composables and state, Room (Entity/DAO/Database), Retrofit + OkHttp REST client, Hilt dependency injection, Navigation component |
| [[concepts/kotlin-coroutines\|Kotlin Coroutines & Async]] | INF2007 | Coroutines vs threads, suspend functions, CoroutineScope and lifecycle-aware scopes (viewModelScope/lifecycleScope), Dispatchers (Main/IO/Default), Flow (cold stream), StateFlow/SharedFlow (hot), structured concurrency |

---

## Key Ideas

- **MVVM separates concerns**: View (Compose UI) observes ViewModel state; ViewModel holds business logic and survives configuration changes; Model (Room/Retrofit) is the data layer — each layer depends only on the layer below
- **Compose is declarative**: UI is a function of state (`@Composable fun Screen(state: UiState)`). Recomposition fires automatically when state changes; understanding what triggers recomposition prevents performance issues
- **Coroutines replace callbacks**: `suspend fun` functions can be called sequentially in a coroutine; structured concurrency via scope means cancellation propagates automatically to child coroutines
- **Room enforces compile-time SQL**: `@Query` annotations are validated at compile time; Entities map directly to SQL tables; DAOs are the only access point to the database
- **Hilt wires the dependency graph**: `@HiltViewModel` + `@Inject constructor` means Android creates the ViewModel via Hilt; no manual factory boilerplate needed
- **Retrofit + coroutines**: `suspend fun getUser(): Response<User>` in a Retrofit interface switches to Dispatchers.IO automatically via OkHttp; exceptions from network errors vs HTTP errors must be handled separately

---

## Cross-Domain Connections

- [[synthesis/dip-hilt-dependency-injection|DI in Practice]] — how Hilt implements the Dependency Inversion Principle from ICT2112 Software Design
- [[synthesis/data-mapper-repository-room-retrofit|Repository Pattern]] — bridges ICT2112's Data Mapper pattern to Room + Retrofit
- [[synthesis/rest-api-cross-stack|REST Cross-Stack]] — the full HTTP lifecycle from Retrofit on Android through Express on the backend
- [[concepts/software-architecture-patterns|Software Architecture Patterns]] — MVVM is one of the architectural patterns covered in ICT2112
- [[concepts/server-side-web-development|Server-Side Web Dev]] — Retrofit consumes the same REST APIs built with Express/Node.js in INF1005
