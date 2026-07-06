---
description: Plan and apply a safe refactor of a legacy IT automation script while preserving behavior.
agent: Legacy Script Refactorer
---

# Refactor a legacy script

Target: ${input:path:Path to the script to refactor}

1. Inspect the target script and nearby files first.
2. Identify behavior, inputs, outputs, side effects, and risks.
3. Propose a low-risk refactor plan and **wait for my approval** before editing.
4. After approval, apply: parameters, structured output, error handling, logging, and idempotency.
5. Run the smallest relevant validation available in the workspace.

End with: what changed, why it is safer, how it was validated, and remaining risks.
