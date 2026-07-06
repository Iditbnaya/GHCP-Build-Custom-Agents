---
description: Produce an end-to-end plain-English explanation of a system from its repository structure and flows.
---

# Explain the system

Target: ${input:path:Repo, folder, or entry point to explain}

Walk the repository structure and key flows, then explain, in plain English:

- What the system does and who uses it.
- The main components and how they interact.
- The important runtime flows (happy path and key edge cases).
- External dependencies and integration points.
- Anything that looks risky, unclear, or undocumented.

Use existing repository files, not assumptions. Cite the files you relied on.
