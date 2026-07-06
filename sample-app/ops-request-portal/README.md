# Ops Request Portal sample

This sample contains a small legacy IT request portal and a Python automation script that reads
the portal HTML and generates an operations handoff report.

## Files

- `legacy-app.html` — the ticketing UI used by the operations team.
- `legacy_ticket_bot.py` — the Python automation script that reads the ticketing UI and writes a handoff report.

## Run locally

1. Open `legacy-app.html` in a browser.
2. From this folder, run `python legacy_ticket_bot.py`.
3. Open the generated `handoff-report.html` in a browser.
