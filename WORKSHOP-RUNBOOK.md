# GitHub Copilot Agents for IT Modernization


### Demo 1: plan first
```text
Use the Legacy Script Refactorer agent.
Inspect legacy-scripts/user_export.ps1 and propose a low-risk refactor plan.
Do not edit files until I approve the plan.
```

### Demo 1: implement after approval
```text
Apply the approved refactor.
Preserve behavior, parameterize environment-specific values, use structured CSV export,
add safer error handling, and run the smallest relevant validation command.
```

### Demo 2: explain legacy logic
```text
Use the IT Modernization Architect agent.
Analyze legacy-as400/order_pricing.rpgle and sample-app/docs/legacy-order-flow.md.
Extract the business rules, identify modernization seams, and recommend one safe hackathon-sized path.
```

### Demo 2: generate an ADR
```text
/generate-adr for modernizing the order pricing logic into a tested service with an API wrapper
```

## Token-saving prompt pattern

```text
Goal: [specific outcome]
Scope: [files/folders/components]
Constraints: preserve behavior, no unrelated formatting, no broad rewrites
Process: inspect -> plan -> ask if risky -> implement -> validate
Output: changed files, validation, risks, next step
```

## Recommended agent ideas for IT teams

| Agent | Best use |
| --- | --- |
| Legacy Script Refactorer | Modernize PowerShell, Bash, Python, SQL, or batch automation. |
| AS/400 Modernizer | Explain RPG/COBOL logic and identify modernization seams. |
| Runbook Generator | Turn a repo or script folder into an operations guide. |
| Architecture Documenter | Map code into architecture docs with Mermaid diagrams. |
| Architecture Coach | Produce target architecture, tradeoffs, and ADRs. |
| Security Reviewer | Check secrets, least privilege, input validation, and auditability. |
| Test Builder | Add characterization tests before refactoring. |
| Cloud Migration Analyst | Map current components to Azure modernization options. |
