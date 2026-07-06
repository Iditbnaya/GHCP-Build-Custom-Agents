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
- How to use them to **refactor a fragile script**, **review security risks**, and to **understand and document legacy code** safely.

## Before you start (5 minutes)

1. **VS Code**, updated (`Help → Check for Updates`). Recent versions include **GitHub Copilot built-in** - no extension to install.
2. Sign in: click the **Copilot icon** in the status bar → **Use AI Features** → sign in with GitHub (a **free tier** is available).
3. Open the **Chat** view and select **Agent** mode.
4. Set the permission level to **Request approval** so you review changes before they happen.
5. Open **this folder** in VS Code (`File → Open Folder`).

## What's in this repo

```text
├── legacy-scripts/user_export.ps1      # a fragile PowerShell script (you'll refactor it)
├── legacy-scripts/disk_space_report.ps1 # another script for reusing your refactor prompt
├── legacy-as400/order_pricing.rpgle    # legacy RPG business logic (you'll understand it)
├── sample-app/docs/legacy-order-flow.md
├── .github/                            # REFERENCE SOLUTIONS (agents, prompts, skills, instructions)
└── README.md                           # this guide
```

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
paths, servers or secrets; least-privilege; end every answer with what changed, why safer,
how validated, and remaining risks. Show me the file.
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
/refactor-legacy-script legacy-scriptsnew_employee_setup.ps1
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
docs/ARCHITECTURE.md with a plain-English explanation, a component flowchart, a sequence diagram,
and a linked docs/ARCHITECTURE.drawio file for an editable architecture view. Do not modify code.
```

Then run it:

```text
/document-architecture sample-app/
```

**You should see:** a generated architecture document that explains the current system, includes
Mermaid diagrams, and links to an editable Draw.io diagram.

**Success:** the team can understand the current code before deciding what to modernize.

## Exercise 6 - Build a chained modernization prompt

**Goal:** create one prompt that runs the documentation, modernization, and security review agents
one after another: first document the current state, then modernize, then run security review,
then document the modernization result.

```text
Create a prompt file .github/prompts/document-modernize-document.prompt.md invocable as
/document-modernize-document. It should:
1. Run the documentation workflow first to document the current system.
2. Hand off to the it-modernization-architect agent to create a modernization plan and wait for approval.
3. After approval, implement only the approved modernization changes.
4. Hand off to the Security Reviewer agent to review the implemented changes for secrets,
   least privilege, input validation, logging, and auditability. Wait for approval before applying
   any security fixes.
5. Apply only approved security fixes, if any.
6. Run the documentation workflow again and write docs/MODERNIZED-ARCHITECTURE.md describing
   what changed, including security-review results.
7. End with files changed, validation results, security review findings, and remaining risks.

Show me the prompt file.
```

Then test the chained prompt:

```text
/document-modernize-document sample-app/
```

**You should see:** current-state documentation, a modernization plan, an approval checkpoint,
approved implementation work, security review findings, optional approved security fixes, and a
new modernization document.

**Success:** one reusable command coordinates documentation, modernization, and security agents in
a safe, reviewable sequence.

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
- Not sure how to phrase something? Peek at the **reference solutions** in `.github/`.

## Reference solutions

The `.github/` folder already contains **completed versions** of every agent, prompt, skill, and
the instructions file. **Try building your own first** — then compare with these, or reuse them.

## Keep going after today

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)** — ready-made agents, prompts and skills to adopt.
- **Reuse your agents everywhere:** save an agent at **User scope** (in the Agent Customizations editor: `Chat: Open Customizations` → choose **User**) and it appears in **all** your repos. To share with your team, commit it to a repo and push.
- **VS Code docs:** *Agent customization* → custom agents, prompt files, skills, and instructions.

---

*Facilitators: see `WORKSHOP-RUNBOOK.md` for the 60-minute timing and delivery notes.*
