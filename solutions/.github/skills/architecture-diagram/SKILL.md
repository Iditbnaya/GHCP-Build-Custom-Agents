---
name: architecture-diagram
description: Produce high-quality architecture documentation with Mermaid and Draw.io diagrams. Use when documenting, mapping, or explaining a codebase.
argument-hint: "[file, folder, or repository to document]"
---

# Architecture Diagram skill

Use this skill to turn source code into clear architecture documentation with valid Mermaid diagrams and editable Draw.io architecture artifacts.

## Choose the right diagram per view

- `flowchart` — component / module structure and dependencies
- `sequenceDiagram` — key runtime flows (request handling, jobs, integrations)
- `erDiagram` — data models and relationships
- `classDiagram` — object models
- `.drawio` — editable architecture view for collaborative review, modernization planning, and presentation-ready diagrams

Keep every diagram **valid** (correct Mermaid syntax or Draw.io XML) and **readable** (group related nodes, label edges, avoid overcrowding — split into multiple diagrams if needed).

## Procedure

1. Inspect the target and identify components, responsibilities, and boundaries.
2. Trace the main data and control flows and the external dependencies.
3. Generate the Mermaid diagrams above that apply to this code.
4. Generate a companion target-specific `.drawio` file under `docs/` when the Draw.io skill is installed, such as `docs/architecture-order-pricing.drawio`.
5. Write the document following [architecture-template.md](./architecture-template.md), including a link to the Draw.io artifact.
6. Explain the code in plain language — assume the reader is new to it.

## Output quality bar

- Explain **both** the code and the architecture.
- Include both Markdown-friendly Mermaid diagrams and an editable Draw.io diagram when available.
- Separate facts from assumptions; note anything you could not determine.
- Do not modify source code.
- End with assumptions, risks, and next steps.
