---
description: Generate full architecture documentation with Mermaid diagrams for the given code.
agent: Architecture Documenter
---

# Document architecture

Target: ${input:path:File, folder, or repo to document}

Using the `architecture-diagram` skill, analyze the target and generate `docs/ARCHITECTURE.md` containing:

- A plain-English explanation of what the code does.
- A full architecture section with multiple Mermaid diagrams: a component `flowchart`, at least one `sequenceDiagram`, and a data/class diagram when relevant.
- Dependencies and integrations.
- Assumptions and risks.

Do **not** modify source code.
