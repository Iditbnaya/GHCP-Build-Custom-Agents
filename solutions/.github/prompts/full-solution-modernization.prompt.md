---
description: Full reusable modernization workflow for any solution: discover code, refactor plan, modernization options, ADR, security review, approved implementation, validation, and documentation.
agent: IT Modernization Architect
---

# Full-solution modernization

Target: ${input:path:File, folder, or repository to modernize}

Use this prompt when you want one reusable command to coordinate the agents already used in this workshop across any solution: HTML, JavaScript, Python, PowerShell, AS/400 RPG, scripts, runbooks, generated reports, and documentation.

## Stage 1 - Discover the solution from code

Inspect the target and nearby files before proposing changes. Do not rely on pre-written documentation as the source of truth. Classify:

- languages and file types
- UI screens or generated HTML artifacts
- scripts, automation, scheduled jobs, and reports
- inputs, outputs, side effects, and generated files
- business rules and operational workflows inferred from code
- tests, sample data, validation commands, and manual checks
- assumptions that need confirmation

## Stage 2 - Explain current behavior

Summarize the current solution in plain language:

- user or operator flow
- component responsibilities
- data and control flow
- business rules and edge cases inferred from source
- risks, hard-coded assumptions, and dependencies
- what is fact versus assumption

## Stage 3 - Suggest a safe refactor plan

Use `Legacy Script Refactorer` principles for automation and script code. Use HTML/JavaScript modernization guidance for UI code. The plan must:

- preserve current behavior unless a defect is explicitly named
- identify characterization checks before broad refactors
- propose small, reviewable steps
- include language-specific improvements for Python, PowerShell, HTML/JavaScript, SQL, batch, or legacy code when present
- when an HTML UI is present, include a visible UI modernization step that updates the user-facing page or creates an approved modernized page, not just backend/script/report hardening
- avoid broad rewrites unless justified by safety or maintainability risk

Do not edit files yet.

## Stage 4 - Create modernization options and ADR

Use the `architecture-decision` skill approach to create:

1. Two or three modernization options.
2. One recommended option.
3. A staged implementation plan.
4. ADR content for the recommended decision, including:
   - status
   - context
   - decision
   - options considered
   - consequences
   - validation gates
   - rollback or exit criteria

Prefer incremental modernization, wrappers, adapters, and strangler patterns over risky rewrites.
When the target contains an HTML UI, at least one option must explicitly modernize the visible interface with semantic HTML, responsive CSS, accessible controls, safer DOM handling, and a clearer operator experience while preserving the existing workflow.

## Stage 5 - Run security review

Apply the `Security Reviewer` rules to the current solution and proposed plan. Cover:

- secrets, credentials, connection strings, and tokens
- hard-coded paths, servers, users, shares, and environment assumptions
- least privilege, scopes, and permissions
- input validation and injection risks
- unsafe DOM updates, string-built HTML, and output encoding
- Python parsing, report generation, and file handling
- PowerShell remoting, credential handling, and destructive operations
- logging, auditability, and data exposure
- production-risk assumptions

Report findings by severity with concrete minimal fixes.

## Stage 6 - Approval checkpoint

Stop before implementation. Present concise choices:

- **Approve implementation** - implement only approved refactor, modernization, and security changes.
- **Revise plan** - update the refactor plan, modernization options, ADR, or security findings.
- **Run security review** - repeat or deepen security review.
- **Generate documentation** - document the current plan or final solution.

If handoff buttons are available, use them. If not, ask me to type one short choice.

## Stage 7 - Implement only after approval

After explicit approval:

1. Restate the approved scope in one or two bullets.
2. Apply only approved changes.
3. Preserve legacy behavior and keep legacy files when useful for comparison or rollback.
4. Avoid new external dependencies unless explicitly approved.
5. Keep documentation and generated artifacts separate from source when practical.
6. If the approved scope includes an HTML UI, implement the visible UI modernization in the HTML/CSS/JavaScript files or approved new modernized UI artifact. Do not stop after only Python, test, or report hardening when UI modernization was approved.

## Stage 8 - Validate

Run the smallest relevant validation for the solution:

- diagnostics for changed files
- Python scripts or tests when Python is present
- PowerShell syntax or safe dry-run checks when PowerShell is present
- browser render checks when HTML UI is present
- generated report checks when reports are produced
- searches for stale references after renames or deletions
- confirmation that required target-specific documentation files were created or updated after implementation
- manual checks for legacy systems that cannot run locally

If validation fails, diagnose the root cause and fix only issues related to the approved change.

## Stage 9 - Document the modernized solution

This stage is mandatory after approved implementation. Do not consider the workflow complete until target-specific documentation exists for the modernized solution.

Use the `architecture-diagram` skill approach and `Architecture Documenter` rules to create or update documentation under `docs/`:

- `docs/architecture-target-slug.md` with current and modernized architecture, where `target-slug` is derived from the target file or folder name.
- `docs/modernization-plan-target-slug.md` with refactor plan, modernization options, ADR, security findings, approved implementation scope, validation gates, rollout notes, rollback notes, and residual risks.
- `docs/architecture-target-slug.drawio` as an editable Draw.io architecture design when available.

Include Mermaid diagrams for component structure, runtime flow, data/report flow, security boundaries, and before/after architecture when useful.

For HTML UI modernization, the documentation must describe the modernized user experience, the files changed or created, accessibility and responsive-design choices, JavaScript/DOM safety improvements, and manual browser validation evidence.

If implementation is complete but these docs are missing, create them before the final response.

## Final response

End with:

1. What changed
2. Why it is safer or clearer
3. How it was validated
4. Remaining risks or manual checks
5. Which target-specific documentation and architecture design files were created or updated

Do not modify source code unless I explicitly approve the implementation plan and security fixes.