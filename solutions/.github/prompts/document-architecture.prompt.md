---
description: Generate full architecture documentation with Mermaid and Draw.io diagrams for the given code.
agent: Architecture Documenter
---

# Document architecture

Target: ${input:path:File, folder, or repo to document}

Using the `architecture-diagram` skill and the installed Draw.io skill, analyze the target and generate:

- A target-specific Markdown file under `docs/`, named from the target path, such as `docs/architecture-order-pricing.md` for `legacy-as400/order_pricing.rpgle` or `docs/architecture-ops-request-portal.md` for `sample-app/ops-request-portal/`, containing:
	- A plain-English explanation of what the code does.
	- A full architecture section with multiple Mermaid diagrams: a component `flowchart`, at least one `sequenceDiagram`, and a data/class diagram when relevant.
	- A link to the matching target-specific `.drawio` file.
	- Dependencies and integrations.
	- Assumptions and risks.
- A matching target-specific `.drawio` file under `docs/`, such as `docs/architecture-order-pricing.drawio`, containing an editable architecture diagram suitable for reviews and modernization planning.

Do not use a generic filename like `docs/ARCHITECTURE.md` or `docs/ARCHITECTURE.drawio` when the target is a specific file or folder.

Do **not** modify source code.
