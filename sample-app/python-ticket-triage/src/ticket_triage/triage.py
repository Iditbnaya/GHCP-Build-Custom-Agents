"""Core ticket triage rules for the IT helpdesk sample app."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


CRITICAL_TERMS = ("outage", "unavailable", "blocked", "failed", "data loss", "breach")
HIGH_TERMS = ("cannot", "error", "failing", "down")
MEDIUM_TERMS = ("slow", "intermittent", "degraded")

TEAM_BY_SERVICE = {
    "backup": "Backup Operations",
    "email": "Collaboration Services",
    "identity": "Identity and Access Management",
    "laptop": "Desktop Support",
    "network": "Network Operations",
    "payroll": "Business Applications",
}

BUSINESS_CRITICAL_SERVICES = {"backup", "identity", "payroll"}


@dataclass(frozen=True)
class Ticket:
    """A helpdesk ticket loaded from CSV input."""

    ticket_id: str
    title: str
    description: str
    service: str
    requester: str
    vip: bool = False


@dataclass(frozen=True)
class TriageResult:
    """The assigned severity and owner for a ticket."""

    ticket: Ticket
    severity: str
    owner_team: str
    reason: str


def load_tickets(csv_path: str | Path) -> list[Ticket]:
    """Load tickets from a CSV file.

    The CSV is expected to contain these headers: ticket_id, title, description,
    service, requester, and vip. Unknown columns are ignored so workshop
    participants can extend the sample data safely.
    """

    path = Path(csv_path)
    with path.open(newline="", encoding="utf-8-sig") as ticket_file:
        reader = csv.DictReader(ticket_file)
        return [_ticket_from_row(row) for row in reader]


def triage_tickets(tickets: list[Ticket]) -> list[TriageResult]:
    """Triage all tickets in input order."""

    return [triage_ticket(ticket) for ticket in tickets]


def triage_ticket(ticket: Ticket) -> TriageResult:
    """Assign severity and owner team for one ticket."""

    service = ticket.service.strip().lower()
    text = f"{ticket.title} {ticket.description}".lower()
    owner_team = TEAM_BY_SERVICE.get(service, "Service Desk")

    if _contains_any(text, CRITICAL_TERMS) and service in BUSINESS_CRITICAL_SERVICES:
        return TriageResult(ticket, "critical", owner_team, "business-critical service impact")

    if ticket.vip and (_contains_any(text, HIGH_TERMS) or service in BUSINESS_CRITICAL_SERVICES):
        return TriageResult(ticket, "high", owner_team, "VIP requester or critical service")

    if _contains_any(text, HIGH_TERMS):
        return TriageResult(ticket, "high", owner_team, "service access or error keywords")

    if _contains_any(text, MEDIUM_TERMS):
        return TriageResult(ticket, "medium", owner_team, "degraded service keywords")

    return TriageResult(ticket, "low", owner_team, "standard service request")


def format_report(results: list[TriageResult]) -> str:
    """Format triage results as a plain-text operations report."""

    lines = ["IT Ticket Triage Report", "=======================", ""]
    for result in results:
        ticket = result.ticket
        lines.append(
            f"#{ticket.ticket_id} [{result.severity.upper()}] "
            f"{ticket.title} -> {result.owner_team} ({result.reason})"
        )
    return "\n".join(lines)


def _ticket_from_row(row: dict[str, str]) -> Ticket:
    return Ticket(
        ticket_id=row.get("ticket_id", "").strip(),
        title=row.get("title", "").strip(),
        description=row.get("description", "").strip(),
        service=row.get("service", "").strip(),
        requester=row.get("requester", "").strip(),
        vip=row.get("vip", "").strip().lower() in {"1", "true", "yes", "y"},
    )


def _contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)
