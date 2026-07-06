---
description: Run modernization planning and security review together in one safe workflow.
agent: IT Modernization Architect
---

# Modernize, then security-review

Target: ${input:path:File, folder, or repo to modernize}

Use this prompt when you want one command to coordinate modernization planning and security review without manually switching agents.

1. Inspect the target and nearby documentation first.
2. Use the `IT Modernization Architect` approach to document the current state, business rules, constraints, dependencies, and modernization risks.
3. Create two or three modernization options and recommend one option.
4. Include a clearly marked **implementation option** section with staged steps, validation gates, rollback notes, and any assumptions.
5. Do **not** implement code yet. Wait for explicit approval before any file edits.
6. After the modernization plan is complete, immediately hand off to the `Security Reviewer` agent, or apply the `Security Reviewer` rules if handoff is not available in the current chat mode.
7. The security review must cover secrets, hard-coded paths, least privilege, input validation, data exposure, logging, auditability, unsafe defaults, and production-risk assumptions.
8. End with:
   - modernization recommendation
   - security findings by severity
   - approval conditions before implementation
   - validation plan
   - remaining risks and manual checks

Do not modify source code unless I explicitly approve the implementation plan and any security fixes.
