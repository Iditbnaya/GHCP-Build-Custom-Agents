# GitHub Copilot Agents for IT Modernization - Participant Guide

Welcome! In this hands-on workshop you'll learn to build and use your **own GitHub Copilot
customizations** to modernize legacy IT code **safely** - and you'll do it **without hand-writing
configuration files**. You describe what you want, and Copilot builds it.

> New to this? Don't worry. Every exercise gives you the exact prompt to paste. If you get
> stuck, the completed **reference solutions** are already in this repo (see the last section).

---

## What you'll learn

- What a Copilot **agent** is, the **agent types** (Local, Copilot CLI, Cloud), and when to use each.
- How to create **custom agents, prompt files, skills, and instructions** - by *describing* them, not hand-writing Markdown.
- How to use them to **refactor fragile automation**, **review security risks**, and **modernize full polyglot solutions** safely.

## Before you start (5 minutes)

1. **VS Code**, updated (`Help → Check for Updates`). Recent versions include **GitHub Copilot built-in** - no extension to install.
2. Sign in: click the **Copilot icon** in the status bar → **Use AI Features** → sign in with GitHub (a **free tier** is available).
3. Open the **Chat** view and select **Agent** mode.
4. Set the permission level to **Request approval** so you review changes before they happen.
5. Open **this folder** in VS Code (`File → Open Folder`).

## What's in this repo

```text
├── .github/                              # starter customizations used during the workshop
│   ├── agents/legacy-script-refactorer.agent.md
│   └── prompts/refactor-legacy-script.prompt.md
├── legacy-as400/order_pricing.rpgle      # legacy RPG business logic
├── legacy-scripts/                       # fragile IT automation scripts for refactoring exercises
│   ├── user_export.ps1
│   ├── disk_space_report.ps1
│   ├── new_employee_setup.ps1
│   └── test.ps1
├── sample-app/ops-request-portal/        # legacy HTML ticketing UI + Python automation script
├── solutions/.github/                    # completed reference solutions for participants who get stuck
├── image.png                             # screenshot used by the workshop guide
└── README.md                             # this participant guide
```

The starter `.github/` folder intentionally contains only the refactor agent and refactor prompt.
Most agents, prompts, instructions, and skills are created during the exercises. If something does
not work during the workshop, compare with or copy from `solutions/.github/`.

## The agent types (quick reference)

Three decide **where** the agent runs; the fourth decides **which engine**.

| Type | Where it runs | Best for |
| --- | --- | --- |
| **Local** | In VS Code, on your open files | Interactive refactoring - you see & approve each change |
| **Copilot CLI** | In your terminal | Ops, pipelines, `git` / `kubectl` / `terraform`, over SSH |
| **Cloud** | In the background on GitHub | Delegated, well-scoped work → returns a pull request |

## Hands-on exercises

> The big idea: **you don't hand-write these files.** You describe what you want and Copilot builds them.
> Paste each prompt into **Chat (Agent mode)**.

## Exercise 1 - Create the repository instruction file

**Goal:** create the house rules first so every later exercise follows the same safe workflow.

```text
Create a .github/copilot-instructions.md for this repo: always plan -> approve -> implement
-> validate -> summarize; preserve legacy behavior unless a defect is named; never hard-code
paths, servers or secrets; least-privilege; ignore the solutions/ folder and all of its content
unless I explicitly ask to use it; end every answer with what changed, why safer, how validated,
and remaining risks. Show me the file.
```

**You should see:** Copilot creates or updates `.github/copilot-instructions.md` and shows the
rules it will follow for the rest of the workshop.

**Success:** the repo has clear safety guardrails before any modernization work starts.

## Exercise 2 - Add Awesome Copilot memory-bank instructions

**Goal:** use Awesome Copilot as a source of reusable customization ideas, then add a memory-bank
instruction so agents can preserve important project context between tasks.

```text
Use Awesome Copilot to find a memory-bank instruction that fits this repo.
Add it under .github/instructions/ so Copilot records concise project learnings, decisions,
and reusable context without storing secrets. Show me the file and explain when it applies.
```

**You should see:** a new instruction file under `.github/instructions/` that tells Copilot how
to capture useful memory-bank notes safely.

**Success:** future agents have a repeatable place to remember project decisions and lessons learned.

## Exercise 3 - Refactor a fragile script *(Local agent)*

**Goal:** learn the difference between choosing an agent and giving it a precise workflow.

First, use the custom agent directly with a very short instruction:

```text
Use the Legacy Script Refactorer agent.
Refactor legacy-scripts/user_export.ps1
```

**Notice:** even when an agent is designed for safe refactoring, a short request may not express
the full workflow you want. The agent might start changing code before it has clearly inspected,
planned, and waited for approval.

Now run the reusable prompt file instead. The prompt calls the same agent, but also tells it the
exact sequence to follow: inspect first, identify behavior and risks, propose a plan, **wait for
approval**, then implement only after approval.

```text
/refactor-legacy-script legacy-scripts/new_employee_setup.ps1
```

**You should see:** inspect → behavior/risk summary → refactor plan → approval checkpoint → edits
only after approval → validation → summary.

## Exercise 4 - Build and test modernization and security agents

**Goal:** create a custom `it-modernization-architect` agent and a `security-reviewer` agent,
then create one prompt that runs modernization planning and security review together before implementation.

### Create the modernization architect agent

```text
Create a custom agent at .github/agents/it-modernization-architect.agent.md: an "IT
Modernization Architect" that assesses legacy code and proposes safe modernization paths.
Read-only planning first; prefer strangler/wrapper/adapter patterns and characterization tests.
Show me the file.
```

### Create the security reviewer agent

```text
Create a custom agent at .github/agents/security-reviewer.agent.md: a "Security Reviewer"
that reviews scripts, infrastructure, and modernization plans for secrets, hard-coded paths,
least privilege, input validation, unsafe defaults, logging gaps, and auditability.
It should be read-only by default, produce prioritized findings, and recommend safe fixes
without changing code unless I explicitly approve. Show me the file.
```

### Create one prompt that chains both agents

```text
Create a prompt file .github/prompts/modernize-then-secure.prompt.md invocable as
/modernize-then-secure. It should use the IT Modernization Architect agent to analyze the target,
create modernization options, recommend one option, and include a clearly marked implementation
option. Then it should immediately run a Security Reviewer pass on that modernization plan for
secrets, least privilege, data exposure, input validation, logging, auditability, and risky
assumptions. Do not implement code unless I explicitly approve. Show me the file.
```

### Test the chained prompt

Paste one command instead of switching agents manually:

```text
/modernize-then-secure legacy-as400/order_pricing.rpgle
```

**You should see:** one prompt creates a modernization plan and implementation option, then adds
security findings and approval conditions before any implementation work.

**Success:** you have a reusable prompt that coordinates modernization and security review in a
single safe, reviewable workflow.

## Exercise 5 - Build a documentation agent

**Goal:** create a documentation agent that explains code and produces architecture docs with
Mermaid diagrams and Draw.io architecture diagrams.

First, install the Awesome Copilot Draw.io skill so the documentation agent can create editable
Draw.io artifacts in addition to Markdown diagrams:

```text
gh skills install github/awesome-copilot drawio
```

```text
Create a custom agent + skill + prompt that turn code into architecture docs with Mermaid
diagrams and Draw.io architecture diagrams. The prompt /document-architecture should generate
a target-specific Markdown file under docs/, such as docs/architecture-order-pricing.md for
legacy-as400/order_pricing.rpgle or docs/architecture-ops-request-portal.md for
sample-app/ops-request-portal/. It should include a plain-English explanation, a component
flowchart, a sequence diagram, and a linked target-specific .drawio file such as
docs/architecture-order-pricing.drawio. Do not use a generic name like ARCHITECTURE.md when
the target is a specific file or folder. Do not modify code.
```

Then run it:

```text
/document-architecture legacy-as400/order_pricing.rpgle
```

**You should see:** a generated architecture document with a target-specific filename, such as
`docs/architecture-order-pricing.md`, that explains the current system, includes Mermaid diagrams,
and links to a matching editable Draw.io diagram.

**Success:** the team can understand the current code before deciding what to modernize.

## Exercise 6 - Run the full-solution modernization workflow

**Goal:** use everything you built on any solution folder or file: scripts, HTML, Python,
PowerShell, legacy RPG, generated reports, and docs. One short prompt should inspect the code,
infer behavior, suggest a refactor, create a modernization plan with ADR content, run a security
review, wait for approval, optionally implement approved changes, validate them, and create full
documentation with diagrams.

You can use `sample-app/ops-request-portal/` as a visible demo input. Open
`sample-app/ops-request-portal/legacy-app.html` in a browser, then run `python legacy_ticket_bot.py`
from that folder and open the generated `handoff-report.html`. This gives everyone a visible UI
and a concrete automation flow, but the workflow is reusable for any target.

For this sample, the approved implementation should include a **visible modernization of the HTML UI**,
not only Python or report hardening. The modernized result should make the portal clearly look and
feel newer while preserving the ticket workflow.

Do not create the modernized solution by hand. It should come from the reusable prompt only after
the agents produce a plan, ADR, and security review.

First improve the reusable agents you created earlier and create the final prompt:

```text
Update the existing Legacy Script Refactorer, IT Modernization Architect, Security Reviewer,
and Architecture Documenter agents so they support full solutions across HTML, Python,
PowerShell, legacy RPG, generated reports, and docs. Add language-specific instructions for
Python, HTML/JavaScript, PowerShell, and legacy code. Create .github/prompts/full-solution-modernization.prompt.md
invocable as /full-solution-modernization. It should coordinate discovery from code, refactor
suggestion, modernization plan, ADR, security review, approval checkpoint, approved implementation,
validation, and mandatory final documentation for any target path. The workflow is not complete
until it creates target-specific docs for the modernized solution, including an architecture design
with Mermaid diagrams and an editable Draw.io diagram when available. When the target includes an HTML UI,
the modernization options and approved implementation must include visible UI modernization
using semantic HTML, responsive CSS, accessible controls, and safer JavaScript/DOM handling,
while preserving current behavior. Show me the changed files.If the HTML UI still looks materially the same after implementation, treat the task as incomplete and continue improving the visible UI until the modernization is apparent to a reviewer opening the page in a browser.
```

Then run the reusable command against any target:

```text
/full-solution-modernization sample-app/ops-request-portal/
```

After the plan is complete, approve the option that includes **visible HTML UI modernization**.
If the first implementation only updates Python or tests, ask it to continue with the approved UI modernization phase.
If it does not create target-specific documentation and architecture design for the modernized app,
ask it to continue with the final documentation phase before considering the workflow complete.

Try it on other targets too:

```text
/full-solution-modernization legacy-scripts/
```

```text
/full-solution-modernization legacy-as400/order_pricing.rpgle
```

**You should see:** a current-state summary, a low-risk refactor suggestion, two or three
modernization options, ADR content, security findings, and a clear approval checkpoint before any
source code changes are made. For `sample-app/ops-request-portal/`, after approval you should also
see a visibly modernized HTML portal, not only Python/report changes, plus target-specific docs such as
`docs/architecture-ops-request-portal.md`, `docs/modernization-plan-ops-request-portal.md`, and a matching
`.drawio` architecture design when supported.

When supported by your VS Code/Copilot version, use handoff or approval actions such as
**Approve implementation**, **Revise plan**, **Run security review**, and **Generate documentation**.
If buttons do not appear, type one of those short choices.

**Success:** one reusable command coordinates refactor planning, modernization, ADR, security,
implementation approval, validation, and architecture documentation for whatever solution the
participant brings. For the HTML sample, success requires both a visibly modernized app and docs
that explain the modernized architecture and validation evidence.

---

## Your challenge (10 minutes)

Create **one reusable customization** for a real scenario from your own team:

1. Pick a scenario (a legacy script, a runbook, a security review, an architecture question).
2. Create a **custom agent** for it (persona, allowed tools, safety rules) — by describing it.
3. Add **one** prompt file or skill.
4. Run it on a sample file — the agent must **plan, act, validate, and summarize**.
5. Be ready to share what you built and why it's safer.

## If you get stuck

- New agent not showing? Run **`Developer: Reload Window`**.
- Agent editing without asking? Switch to **Plan** or **Request approval**.
- Not sure how to phrase something? Peek at the **reference solutions** in `solutions/.github/`.

## Reference solutions

The `solutions/.github/` folder contains **completed versions** of the agents, prompts, skills, and
instruction files participants create during the workshop. **Try building your own first** — then
compare with these, or copy a file into `.github/` if something is not working.

## Keep going after today

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** — ready-made agents, prompts and skills to adopt.
- **Reuse your agents everywhere:** save an agent at **User scope** (in the Agent Customizations editor: `Chat: Open Customizations` → choose **User**) and it appears in **all** your repos. To share with your team, commit it to a repo and push.
- **VS Code docs:** *Agent customization* → custom agents, prompt files, skills, and instructions.

---
