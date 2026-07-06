"""Legacy ticket automation bot.

Reads the ticketing UI HTML, scrapes the request table, and writes a simple operations
handoff report.
"""

import re
from datetime import datetime

INPUT_FILE = "legacy-app.html"
OUTPUT_FILE = "handoff-report.html"
CRITICAL_WORDS = ["payroll", "finance", "portal", "down"]
TEAM_EMAILS = {
    "Business Apps": "business-apps@example.local",
    "Networking": "networking@example.local",
    "Identity": "identity@example.local",
    "Desktop": "desktop@example.local",
}


def load_html():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        return file.read()


def get_ticket_rows(html):
    body_match = re.search(r"<tbody id=\"rows\">(.*?)</tbody>", html, re.S)
    if not body_match:
        print("Could not find ticket table")
        return []

    rows = []
    for row_html in re.findall(r"<tr>(.*?)</tr>", body_match.group(1), re.S):
        cells = re.findall(r"<td>(.*?)</td>", row_html, re.S)
        if len(cells) == 5:
            rows.append({
                "id": cells[0],
                "title": re.sub(r"<.*?>", "", cells[1]),
                "team": re.sub(r"<.*?>", "", cells[2]),
                "impact": re.sub(r"<.*?>", "", cells[3]),
                "status": re.sub(r"<.*?>", "", cells[4]),
            })
    return rows


def route_ticket(ticket):
    title = ticket["title"].lower()
    if any(word in title for word in CRITICAL_WORDS):
        ticket["impact"] = "Critical"
        ticket["team"] = "Business Apps"
    if "vpn" in title:
        ticket["team"] = "Networking"
    if "password" in title or "access" in title:
        ticket["team"] = "Identity"
    ticket["owner"] = TEAM_EMAILS.get(ticket["team"], "helpdesk@example.local")
    return ticket


def build_report(tickets):
    critical_count = len([ticket for ticket in tickets if ticket["impact"] == "Critical"])
    rows = ""
    for ticket in tickets:
        rows += (
            "<tr>"
            f"<td>{ticket['id']}</td>"
            f"<td>{ticket['title']}</td>"
            f"<td>{ticket['team']}</td>"
            f"<td>{ticket['impact']}</td>"
            f"<td>{ticket['owner']}</td>"
            "</tr>"
        )

    return f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Ops handoff report</title></head>
<body>
  <h1>Ops handoff report</h1>
  <p>Generated: {datetime.now()}</p>
  <p>Critical tickets: {critical_count}</p>
  <table border="1">
    <tr><th>ID</th><th>Title</th><th>Team</th><th>Impact</th><th>Owner</th></tr>
    {rows}
  </table>
</body>
</html>"""


def main():
    html = load_html()
    tickets = [route_ticket(ticket) for ticket in get_ticket_rows(html)]
    report = build_report(tickets)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(report)
    print("Wrote " + OUTPUT_FILE + " with " + str(len(tickets)) + " tickets")


if __name__ == "__main__":
    main()
