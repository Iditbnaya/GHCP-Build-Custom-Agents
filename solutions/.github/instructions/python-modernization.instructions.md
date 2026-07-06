---
name: Python modernization standards
description: Rules for safely refactoring and modernizing Python automation, parsing, reporting, and utility scripts.
applyTo: "**/*.py"
---

# Python modernization standards

- Infer current behavior from code before proposing changes.
- Preserve inputs, outputs, file names, generated artifacts, and exit behavior unless a defect is explicitly named.
- Prefer small functions with clear responsibilities for parsing, routing, transformation, rendering, and I/O.
- Use `argparse` or explicit parameters when turning hard-coded values into configurable inputs.
- Use safe file handling with `encoding="utf-8"` and clear errors for missing or malformed files.
- Escape generated HTML or text reports when data can come from user-controlled input.
- Add type hints where they clarify boundaries without making the script harder to teach.
- Prefer standard-library solutions unless an external dependency is explicitly justified and approved.
- Add characterization tests or sample-run validation before changing parsing or report-generation behavior.