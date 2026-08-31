---
type: learning
status: established
title: "dotnet build fails with MSB3021/MSB3027 — output exe locked by a running process"
updated: 2026-08-31
tags: [learning, dotnet, csharp, msbuild, windows, build-errors]
---

# `dotnet build` MSB3021 / MSB3027 — output exe locked

## Symptom
`dotnet build` on a console project fails (not a compile error):

```
error MSB3027: Could not copy "...\obj\Debug\net10.0\apphost.exe" to "bin\Debug\net10.0\<App>.exe".
              Exceeded retry count of 10. Failed. The file is locked by: "<App> (27176)"
error MSB3021: Unable to copy file ... The process cannot access the file ... because it is being
              used by another process.
```

MSBuild helpfully names the locking process and PID.

## Cause
A previous `dotnet run` of the app is still alive — on Windows, most often sitting at a
`Console.ReadLine()` prompt in another terminal. Windows locks the running `.exe`, so the next build
cannot overwrite `bin\...\<App>.exe`.

## Fix
```
taskkill /IM <App>.exe /F
# or PowerShell:
Get-Process <App> | Stop-Process -Force
```
Then rebuild. Or just `Ctrl+C` / close the terminal running the stuck app.

## Prevention
- Design console apps to finish and exit (answer all prompts); don't leave them hanging.
- `dotnet test` never emits a locked `.exe`, so it is unaffected — use it freely.
- Encountered in [[examples/ict3112-lab1-nunit-tdd-calculator]] (ICT3112 Lab 1).
