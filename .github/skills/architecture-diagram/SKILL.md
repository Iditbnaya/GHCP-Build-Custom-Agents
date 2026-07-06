---
name: architecture-diagram
description: Produce high-quality architecture documentation with Mermaid diagrams. Use when documenting, mapping, or explaining a codebase.
argument-hint: "[file, folder, or repository to document]"
---

# Architecture Diagram skill

Use this skill to turn source code into clear architecture documentation with valid Mermaid diagrams.

## Choose the right diagram per view

- `flowchart` — component / module structure and dependencies
- `sequenceDiagram` — key runtime flows (request handling, jobs, integrations)
- `erDiagram` — data models and relationships
- `classDiagram` — object models

Keep every diagram **valid** (correct Mermaid syntax) and **readable** (group related nodes, label edges, avoid overcrowding — split into multiple diagrams if needed).

## Procedure

1. Inspect the target and identify components, responsibilities, and boundaries.
2. Trace the main data and control flows and the external dependencies.
3. Generate the diagrams above that apply to this code.
4. Write the document following [architecture-template.md](./architecture-template.md).
5. Explain the code in plain language — assume the reader is new to it.

## Output quality bar

- Explain **both** the code and the architecture.
- Separate facts from assumptions; note anything you could not determine.
- Do not modify source code.
- End with assumptions, risks, and next steps.
