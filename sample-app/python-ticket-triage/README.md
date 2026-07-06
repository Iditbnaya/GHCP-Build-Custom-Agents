# Python ticket triage sample

This sample app is a small Python package for IT operations workshops. It reads helpdesk tickets from CSV, assigns a severity and owning team, and prints a concise triage report.

It is designed for three workshop activities:

1. **Modernization/refactoring** — improve rule configuration, reporting, and packaging while preserving behavior.
2. **Security review** — inspect CSV input handling, data exposure in reports, and operational logging assumptions.
3. **Architecture documentation** — document the flow from ticket data to triage decisions and CLI output.

## What it does

- Loads tickets from `data/tickets.csv`.
- Assigns severity: `critical`, `high`, `medium`, or `low`.
- Assigns an owning IT team based on service area.
- Produces a human-readable report.
- Includes unit tests using only the Python standard library.

## Run the report

From this folder:

```powershell
$env:PYTHONPATH = "src"
python -m ticket_triage.cli --input data/tickets.csv
```

## Run tests

From this folder:

```powershell
python -m unittest discover -s tests
```

The tests add `src` to the Python import path automatically, so no package install is required.

## Workshop prompts to try

- Ask the modernization agent to make assignment rules configurable without changing current behavior.
- Ask the security reviewer to identify any input, logging, or data exposure risks.
- Ask the architecture documenter to create Mermaid and Draw.io diagrams for the ticket triage flow.
