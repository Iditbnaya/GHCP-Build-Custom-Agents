"""Command-line interface for the ticket triage sample app."""

from __future__ import annotations

import argparse
from pathlib import Path

from .triage import format_report, load_tickets, triage_tickets


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an IT ticket triage report from CSV input.")
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to a CSV file containing helpdesk tickets.",
    )
    args = parser.parse_args()

    tickets = load_tickets(args.input)
    results = triage_tickets(tickets)
    print(format_report(results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
