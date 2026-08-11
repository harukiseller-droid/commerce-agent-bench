# Open Source Program Application Draft

Replace bracketed fields with your real information. Do not inflate usage, stars, contributors, or adoption.

## Project URL

`https://github.com/harukiseller-droid/commerce-agent-bench`

## What is the project?

commerce-agent-bench is an open-source collection of reusable agent skills, evidence-first maintenance workflows, deterministic checks, and reproducible regression fixtures for AI coding agents working on ecommerce codebases. It currently covers product-page quality, WooCommerce hook regressions, technical SEO, structured data, accessibility, and unsafe hard-coded commerce values.

## Why does it matter?

Ecommerce repositories mix application code with product facts, SEO metadata, structured data, analytics, theme hooks, and buyer-facing claims. Generic coding agents can produce technically valid changes that still create commercial regressions or unsupported claims. This project makes those failure modes explicit and testable, while providing a tool-agnostic protocol that maintainers can use with Codex and other coding agents.

## How would Codex / API credits be used?

Credits would be used to evaluate coding agents against reproducible ecommerce regression fixtures, test pull-request review workflows, compare agent patches against deterministic expected findings, and expand coverage across WooCommerce and Shopify maintenance tasks. Results and fixtures would remain open source so other maintainers can reproduce and improve them.

## Maintainer role

I am the primary maintainer. I design the fixtures, agent protocol, deterministic checks, and review workflows, and I maintain the public repository and contribution process.

## Current evidence

- Public repository: `https://github.com/harukiseller-droid/commerce-agent-bench`
- Release: [`v0.1.0`](https://github.com/harukiseller-droid/commerce-agent-bench/releases/tag/v0.1.0)
- CI workflow: [`CI`](https://github.com/harukiseller-droid/commerce-agent-bench/actions/workflows/ci.yml)
- Maintainer PR history: [PR #6](https://github.com/harukiseller-droid/commerce-agent-bench/pull/6) and [PR #7](https://github.com/harukiseller-droid/commerce-agent-bench/pull/7)
- Deterministic benchmark report: [`docs/benchmarks/`](docs/benchmarks/)
- Public roadmap: [GitHub Issues](https://github.com/harukiseller-droid/commerce-agent-bench/issues)
- External usage, stars, forks, and third-party contributions: `UNKNOWN`; do not represent them as adoption evidence without verified data.
