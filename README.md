# GitHub Copilot Agents for IT Modernization — Participant Guide

Welcome! In this hands-on workshop you'll learn to build and use your **own GitHub Copilot
customizations** to modernize legacy IT code **safely** - and you'll do it **without hand-writing
configuration files**. You describe what you want, and Copilot builds it.

> New to this? Don't worry. Every exercise gives you the exact prompt to paste. If you get
> stuck, the completed **reference solutions** are already in this repo (see the last section).

---

## What you'll learn

- What a Copilot **agent** is, the **agent types** (Local, Copilot CLI, Cloud), and when to use each.
- How to create **custom agents, prompt files, skills, and instructions** - by *describing* them, not hand-writing Markdown.
- How to use them to **refactor a fragile script** and to **understand and document legacy code** safely.

## Before you start (5 minutes)

1. **VS Code**, updated (`Help → Check for Updates`). Recent versions include **GitHub Copilot built-in** - no extension to install.
2. Sign in: click the **Copilot icon** in the status bar → **Use AI Features** → sign in with GitHub (a **free tier** is available).
3. Open the **Chat** view and select **Agent** mode.
4. Set the permission level to **Request approval** so you review changes before they happen.
5. Open **this folder** in VS Code (`File → Open Folder`).

## What's in this repo

```
├── legacy-scripts/user_export.ps1      # a fragile PowerShell script (you'll refactor it)
├── legacy-as400/order_pricing.rpgle    # legacy RPG business logic (you'll understand it)
├── sample-app/docs/legacy-order-flow.md
├── .github/                            # REFERENCE SOLUTIONS (agents, prompts, skills, instructions)
└── README.md                           # this guide
```

## The four agent types (quick reference)

Three decide **where** the agent runs; the fourth decides **which engine**.

| Type | Where it runs | Best for |
|---|---|---|
| **Local** | In VS Code, on your open files | Interactive refactoring - you see & approve each change |
| **Copilot CLI** | In your terminal | Ops, pipelines, `git` / `kubectl` / `terraform`, over SSH |
| **Cloud** | In the background on GitHub | Delegated, well-scoped work → returns a pull request |


# Hands-on exercises

> The big idea: **you don't hand-write these files.** You describe what you want and Copilot builds them.
> Paste each prompt into **Chat (Agent mode)**.

## Exercise 1 - Refactor a fragile script *(Local agent)*

**Goal:** safely modernize `legacy-scripts/user_export.ps1` while preserving its behavior.

1. Ask Copilot to plan first (it should **not** edit yet):
   ```
   Inspect legacy-scripts/user_export.ps1 and propose a low-risk refactor plan
   (parameters, structured CSV, error handling, logging, and filter before load).
   Do not edit until I approve.
   ```
2. Read the plan, then approve:
   ```
   Apply the approved refactor. Preserve behavior, parameterize the server and output path,
   use a structured CSV export, add error handling, and run the smallest validation you can.
   ```

**You should see:** a plan → your approval → edits → a short summary of what changed and why.
**Success:** the script now takes parameters, has no hard-coded paths, and handles errors.

## Exercise 2 — Build your own customizations *(no hand-writing MD)*

Create each one by **describing it** — Copilot writes the file.

**a) House rules (instructions):**
```
Create a .github/copilot-instructions.md for this repo: always plan -> approve -> implement
-> validate -> summarize; preserve legacy behavior unless a defect is named; never hard-code
paths, servers or secrets; least-privilege; end every answer with what changed, why safer,
how validated, and remaining risks. Show me the file.
```

**b) A custom agent:**
```
Create a custom agent at .github/agents/it-modernization-architect.agent.md: an "IT
Modernization Architect" that assesses legacy code and proposes safe modernization paths.
Read-only planning first; prefer strangler/wrapper/adapter patterns and characterization tests.
Show me the file.
```

**c) A reusable command (prompt file):**
```
Create a prompt file .github/prompts/refactor-legacy-script.prompt.md invocable as
/refactor-legacy-script that plans a safe refactor, waits for approval, then applies it and
validates. Show me the file.
```

**You should see:** each new file created — and the **custom agent appears in the agent picker**.

## Exercise 3 - Understand legacy code before changing it *(IT Modernization Architect)*

**Goal:** extract the business rules from RPG code — understanding first, not code changes.
```
Analyze legacy-as400/order_pricing.rpgle and sample-app/docs/legacy-order-flow.md.
Extract the business rules in plain English and create examples that prove current behavior.
Do not modernize yet.
```
**Success:** you can explain the discount rules (item A → 15%, tier G → 10%, else → 5%) in your own words.

## Exercise 4 — *(Stretch)* Code → architecture with diagrams

Build a documentation agent **and** use it, then open the result in **Preview** to see the diagrams.
```
Create a custom agent + skill + prompt that turn code into architecture docs with Mermaid
diagrams. The prompt /document-architecture should generate docs/ARCHITECTURE.md with a
plain-English explanation plus a component flowchart and a sequence diagram. Do not modify code.
```
Then:
```
/document-architecture sample-app/
```

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
