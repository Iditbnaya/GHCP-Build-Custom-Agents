---
name: Legacy code modernization standards
description: Rules for assessing and modernizing legacy AS/400, RPG, COBOL, batch, and operational code by inferring behavior from source first.
applyTo: "legacy-as400/**/*"
---

# Legacy code modernization standards

- Infer business rules from source code first; do not rely on external notes unless the code supports them.
- Separate facts, assumptions, and recommendations clearly.
- Preserve calculations, thresholds, status codes, file layouts, and operational side effects unless the user confirms a change.
- Prefer characterization tests, wrappers, adapters, and strangler patterns before full rewrites.
- Identify integration points such as files, queues, databases, reports, scheduled jobs, operators, and downstream systems.
- Document migration options with validation gates, rollback steps, and manual reconciliation checks.
- Flag ambiguous business rules for human review instead of silently simplifying them.