---
name: HTML and JavaScript modernization standards
description: Rules for safely refactoring and modernizing HTML, CSS, JavaScript, forms, browser UI, and generated web artifacts.
applyTo: "**/*.{html,js,css}"
---

# HTML and JavaScript modernization standards

- Infer visible behavior and user flows from the markup and scripts before changing UI code.
- Preserve the core scenario unless a behavior defect is explicitly named.
- Prefer semantic HTML, labels, keyboard-friendly controls, and clear focus states.
- Validate form input near the user action and provide accessible feedback.
- Prefer safe DOM APIs such as `textContent`, `createElement`, and event listeners over string-built HTML and inline event handlers in modernized output.
- Keep generated or static HTML reports readable, printable, and safe for untrusted text.
- Use responsive layouts that remain usable on narrow screens.
- Avoid adding external JavaScript or CSS dependencies unless approved.
- When creating self-contained HTML artifacts, keep styles local and document any generated-output assumptions.