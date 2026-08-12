# Agent Instructions

Use this file as the thin routing layer for Codex, Claude Code, Cursor, Gemini CLI, and other coding agents.

Read `PROTOCOL.md` before reviewing or changing ecommerce code. Load only the relevant core skill from `.agents/skills/`. Experimental workflows under `extras/` are not core routing targets.

## Mandatory skill routing

- Any ecommerce PR: use `.agents/skills/ecommerce-pr-review`.
- Any product fact change: use `.agents/skills/commerce-fact-safety`.
- Any WooCommerce hook or template change: use `.agents/skills/woocommerce-code-review`.
- Any schema modification: use `.agents/skills/schema-validator`.
- Any source-code modification: use `.agents/skills/code-change-verification`.
- Before completing a substantial PR: use `.agents/skills/pr-draft-summary`.
- For product-page behavior: also use `.agents/skills/product-page-audit`.
- For SEO behavior: also use `.agents/skills/technical-seo-audit`.
- For accessibility behavior: also use `.agents/skills/accessibility-audit`.

## Non-negotiable rules

- Never invent product specs, prices, materials, stock, shipping times, returns, ratings, review counts, certifications, or guarantees.
- Classify every material claim as `FACT`, `INFERENCE`, or `UNKNOWN`.
- For `FACT`, provide file/path evidence or point to user-supplied verified data.
- Prefer runtime platform data over hard-coded commerce values.
- Do not change unrelated layout, copy, business logic, or tracking code.
- For WooCommerce hooks, check for duplicate registrations before adding callbacks.
- For schema, emit only claims visible on-page or present in verified merchant/runtime data.
- Do not commit secrets or claim Codex execution without a real Codex run.

## Required workflow

1. Read the task and identify the exact scope.
2. Inspect the repository and current implementation.
3. Select and read the mandatory skills.
4. Collect evidence before proposing or applying a change.
5. Make the smallest valid change.
6. Run `pytest -q`.
7. Run `python scripts/run_evals.py`.
8. Run any relevant benchmark or validator command.
9. Review the diff, unexpected files, dependencies, generated artifacts, and secrets.
10. Report verified results, limitations, and remaining risk.

Never bypass deterministic checks because an LLM believes the patch is correct.
