# Agent Instructions

Use this file as the thin adapter for Codex, Claude Code, Cursor, Gemini CLI, and other coding agents.

Read `PROTOCOL.md` before reviewing or changing ecommerce code. Then load only the relevant skill under `skills/`.

## Non-negotiable rules

- Never invent product specs, prices, materials, stock, shipping times, returns, ratings, review counts, certifications, or guarantees.
- Classify every material claim as `FACT`, `INFERENCE`, or `UNKNOWN`.
- For `FACT`, provide file/path evidence or point to user-supplied verified data.
- Prefer runtime platform data over hard-coded commerce values.
- Do not change unrelated layout, copy, business logic, or tracking code.
- For WooCommerce hooks, check for duplicate registrations before adding new callbacks.
- For schema, only emit claims that exist visibly on-page or in verified merchant data.
- Run the smallest relevant tests/evals after a patch.
- If evidence is missing, say `UNKNOWN` instead of guessing.

## Recommended workflow

1. Identify platform and files in scope.
2. Read the relevant skill.
3. Gather evidence before proposing fixes.
4. Produce findings using the output contract in `PROTOCOL.md`.
5. Patch only verified issues.
6. Run deterministic checks: `python scripts/run_evals.py` and project-native tests where available.
7. Report what was verified and what remains unknown.
