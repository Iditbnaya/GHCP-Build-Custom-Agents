---
name: architecture-decision
description: Create architecture decision records and modernization architecture options. Use when selecting target architecture, documenting tradeoffs, or preparing a migration proposal.
argument-hint: "[decision topic or modernization scenario]"
---

# Architecture Decision skill

Use this skill when the task requires architecture tradeoffs, target-state design, migration planning, or an Architecture Decision Record.

## Procedure

1. Capture current state from the repository, scripts, and documentation.
2. Identify constraints: security, operations, data, compliance, integration, cost, and delivery time.
3. Generate two or three realistic options.
4. Compare options by complexity, risk, reversibility, operational impact, and hackathon feasibility.
5. Recommend one option.
6. Produce an ADR using [adr-template.md](./adr-template.md).

## Output quality bar

- Make assumptions explicit.
- Separate facts from recommendations.
- Include validation gates.
- Include rollback or exit criteria.
- Prefer incremental modernization over risky rewrites.
