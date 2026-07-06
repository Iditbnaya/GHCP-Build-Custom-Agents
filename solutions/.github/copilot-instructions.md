# Copilot instructions — IT Modernization Workshop

These repository-wide instructions apply to every Copilot interaction in this repo.

**Audience:** infrastructure and IT operations engineers modernizing legacy automation safely.
This is a demo-friendly workshop repo, so every change must be small, explainable, and reviewable.

## Working sequence
- Always follow: **plan → get approval → implement → validate → summarize**.
- Do not edit files before showing a short plan for broad, sensitive, or production-related work.

## Legacy safety
- Preserve existing behavior unless you name and explain a defect.
- Prefer parameters, structured output, error handling, idempotency, and characterization tests.
- Favor strangler / wrapper / adapter patterns over full rewrites.

## Security & governance
- Never hard-code paths, servers, or secrets. Keep secrets out of code.
- Use least-privilege tokens and permissions. Add logging where useful.
- Flag anything that touches production.

## Scope discipline
- Change only the files required for the task. Do not reformat unrelated code.

## Output contract
End every response with:
1. What changed
2. Why it is safer or clearer
3. How it was validated
4. Remaining risks or manual checks
