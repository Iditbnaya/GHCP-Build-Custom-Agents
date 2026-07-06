from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from ticket_triage.triage import Ticket, format_report, load_tickets, triage_ticket, triage_tickets


class TicketTriageTests(unittest.TestCase):
    def test_business_critical_outage_is_critical(self) -> None:
        ticket = Ticket(
            ticket_id="T-1",
            title="Payroll outage",
            description="The payroll portal is unavailable for approvers.",
            service="payroll",
            requester="finance@example.com",
            vip=False,
        )

        result = triage_ticket(ticket)

        self.assertEqual("critical", result.severity)
        self.assertEqual("Business Applications", result.owner_team)

    def test_intermitent_network_issue_is_medium(self) -> None:
        ticket = Ticket(
            ticket_id="T-2",
            title="VPN intermittent",
            description="Connection drops every few minutes.",
            service="network",
            requester="tech@example.com",
            vip=False,
        )

        result = triage_ticket(ticket)

        self.assertEqual("medium", result.severity)
        self.assertEqual("Network Operations", result.owner_team)

    def test_unknown_service_goes_to_service_desk(self) -> None:
        ticket = Ticket(
            ticket_id="T-3",
            title="Office chair request",
            description="Need a replacement chair.",
            service="facilities",
            requester="employee@example.com",
            vip=False,
        )

        result = triage_ticket(ticket)

        self.assertEqual("low", result.severity)
        self.assertEqual("Service Desk", result.owner_team)

    def test_loads_sample_tickets(self) -> None:
        tickets = load_tickets(PROJECT_ROOT / "data" / "tickets.csv")

        self.assertEqual(5, len(tickets))
        self.assertTrue(tickets[0].vip)

    def test_report_contains_ticket_summary(self) -> None:
        tickets = load_tickets(PROJECT_ROOT / "data" / "tickets.csv")
        results = triage_tickets(tickets)

        report = format_report(results)

        self.assertIn("IT Ticket Triage Report", report)
        self.assertIn("#1001 [CRITICAL]", report)
        self.assertIn("Business Applications", report)


if __name__ == "__main__":
    unittest.main()
