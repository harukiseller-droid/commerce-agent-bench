---
name: ecommerce-pr-review
description: Review ecommerce pull requests in a fixed evidence-first order.
---
# Ecommerce PR Review

## Purpose

Review ecommerce pull requests for buyer risk, runtime regressions, unsupported facts, and missing verification.

## When to use

Use for any pull request or proposed patch that touches ecommerce code, templates, content, schema, integrations, or agent workflows.

## Inputs

- the pull request diff and base revision;
- repository protocol and relevant core skills;
- tests, evals, runtime evidence, and verified merchant data when available.

## Required checks

Review in this order:

1. Commerce fact safety
2. Runtime regression
3. Checkout/cart risk
4. Product data integrity
5. Schema
6. WooCommerce/Shopify integration
7. Accessibility
8. SEO
9. Security
10. Test coverage

Use exact file and line evidence. Check callers and data sources before concluding that a behavior is broken.

## Output contract

For each finding, return:

```text
[SEVERITY] rule-id
File: path:line
Evidence: exact source or observed behavior
Risk: practical consequence
Fix: smallest verified fix
```

Mark unsupported conclusions as `UNKNOWN` or `INFERENCE`; never present speculation as a confirmed issue.

## Failure conditions

- Do not approve a commerce claim without traceable evidence.
- Do not certify runtime, checkout, or platform behavior from static code alone.
- Do not widen the review into unrelated layout, copy, business logic, or tracking changes.

## Verification

Inspect the final diff, run `pytest -q` and `python scripts/run_evals.py`, and report remaining unverified runtime or platform risks.
