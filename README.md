# commerce-agent-bench

Open-source skills, workflows, and reproducible evals for AI coding agents maintaining ecommerce codebases.

`commerce-agent-bench` gives coding agents a shared protocol for reviewing WooCommerce, Shopify, and static ecommerce projects without inventing product facts or silently turning assumptions into claims. It combines portable agent instructions with deterministic regression fixtures that can run locally and in CI.

## Why this exists

AI agents are useful at code review, migrations, SEO fixes, schema work, and ecommerce maintenance, but commerce code has failure modes that generic coding benchmarks rarely cover:

- hard-coded prices, reviews, or inventory claims;
- duplicate WooCommerce hooks and theme overrides;
- broken product-page accessibility;
- missing SEO metadata and structured-data regressions;
- fabricated product facts in generated copy;
- platform-specific fixes that ignore runtime product data.

This repository turns those problems into reusable skills, review recipes, and small eval fixtures.

## What is included

- **Portable agent skills** in `skills/` for product-page review, technical SEO, schema, WooCommerce, accessibility, and Pinterest content generation.
- **Deterministic scanner** in `src/commerce_agent_bench/` for fast regression checks.
- **Reproducible evals** in `evals/` with intentionally broken fixtures and expected rule IDs.
- **Safe examples** for WooCommerce, Shopify Liquid, and static storefronts.
- **GitHub Actions CI** to run tests and evals on every pull request.
- **Agent protocol** in `AGENTS.md` so Codex, Claude Code, Cursor, Gemini CLI, and similar tools can follow the same evidence-first workflow.

## Quick start

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/commerce-agent-bench.git
cd commerce-agent-bench
python -m venv .venv
source .venv/bin/activate
pip install -e .
commerce-agent-bench evals/fixtures/broken-product-page --format text
python scripts/run_evals.py
```

Expected eval summary:

```text
PASS product-page-basics
PASS schema-integrity
PASS woocommerce-hook-regression
PASS accessibility-regression
PASS seo-regression

5/5 eval cases passed
```

## Use with a coding agent

Point the agent at `AGENTS.md`, then ask it to run one of the workflows:

```text
Audit this WooCommerce product template using the product-page-audit and
woocommerce-code-review skills. Separate FACT, INFERENCE, and UNKNOWN.
Do not invent product facts. Include file paths and line evidence.
```

The core contract is tool-agnostic. Agent-specific files should stay thin and refer back to the shared protocol instead of duplicating it.

## Output contract

Agent findings should use this shape:

```text
status: FACT | INFERENCE | UNKNOWN
severity: low | medium | high | critical
category: seo | schema | accessibility | commerce-data | platform | content
location: path:line
finding: concise description
evidence: exact code or observed behavior
risk: why it matters
recommended_patch: smallest safe fix
verification: how to prove the fix worked
```

## Current deterministic rules

| Rule | Severity | Purpose |
|---|---:|---|
| `HTML_IMG_ALT_MISSING` | medium | Detect image tags without `alt` |
| `HTML_BUTTON_NAME_MISSING` | medium | Detect empty unnamed buttons |
| `SEO_TITLE_MISSING` | high | Detect HTML documents without `<title>` |
| `SEO_META_DESCRIPTION_MISSING` | medium | Detect missing meta descriptions |
| `SCHEMA_FAKE_RATING` | high | Flag suspicious hard-coded rating/review values |
| `WOOCOMMERCE_DUPLICATE_HOOK` | high | Flag duplicate product-summary hook registration |
| `UNSAFE_HARDCODED_PRICE` | medium | Flag likely hard-coded commerce prices |

These checks are intentionally small and explainable. They are not a replacement for platform linters, browser tests, or human review.

## Repository layout

```text
commerce-agent-bench/
├── AGENTS.md
├── PROTOCOL.md
├── README.md
├── APPLICATION.md
├── skills/
├── recipes/
├── src/commerce_agent_bench/
├── tests/
├── evals/
│   ├── fixtures/
│   ├── expected/
│   └── manifest.json
├── examples/
├── scripts/
├── docs/
└── .github/
```

## Design principles

1. **Evidence before conclusions.** Agents must cite code, rendered behavior, or supplied product data.
2. **No fabricated commerce facts.** Unknown shipping, price, material, inventory, dimensions, review counts, or guarantees remain `UNKNOWN`.
3. **Runtime data over hard-coded copy.** Product-specific values should come from the platform or verified source data.
4. **Small, reproducible fixtures.** Every benchmark should isolate one failure mode and have explicit expected findings.
5. **Tool-agnostic core.** Codex, Claude Code, Cursor, and other agents should consume the same protocol.
6. **Safe patches over broad rewrites.** Prefer the smallest change that fixes a verified issue.

## Roadmap

- More WooCommerce and Shopify fixtures
- JSON-LD graph validation
- Lighthouse/axe adapters
- Playwright storefront fixtures
- Agent-output scoring and rubric-based evals
- Pull-request review examples using Codex and other coding agents
- Community-submitted commerce regression cases

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New fixtures should be minimal, deterministic, documented, and free of private merchant data.

## Security

Do not submit API keys, customer data, order exports, private themes, or merchant credentials. See [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
