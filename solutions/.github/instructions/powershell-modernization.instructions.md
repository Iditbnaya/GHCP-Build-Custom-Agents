---
name: PowerShell modernization standards
description: Rules for refactoring PowerShell automation scripts.
applyTo: "**/*.ps1"
---

# PowerShell modernization standards

- Use `[CmdletBinding()]` and explicit `param(...)` blocks for scripts that accept inputs.
- Avoid hard-coded paths, servers, and environment-specific values.
- Prefer structured objects and `Export-Csv` over manual CSV string concatenation.
- Use `Write-Verbose`, `Write-Warning`, and terminating errors consistently.
- Validate inputs with parameter attributes where practical.
- Preserve behavior first; optimize only after behavior is clear.
- Add a small usage example or testable command line when changing script interfaces.
