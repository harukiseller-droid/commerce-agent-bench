# Evidence-First Ecommerce Agent Protocol

## 1. Scope

This protocol governs AI-agent review and maintenance of ecommerce codebases. It is intentionally platform-agnostic and is supplemented by skills for WooCommerce, Shopify, SEO, schema, accessibility, product pages, and content generation.

## 2. Evidence classes

- `FACT`: directly supported by repository code, rendered output, tests, connected platform data, or user-supplied verified facts.
- `INFERENCE`: a reasoned interpretation supported by evidence but not directly proven.
- `UNKNOWN`: required information is not available. Do not replace this with a plausible guess.

## 3. Review sequence

1. Detect platform and affected surface.
2. Locate the source of truth for product/runtime data.
3. Inspect existing hooks, templates, schema, metadata, and tests before adding code.
4. Record findings before changing files.
5. Prioritize correctness and buyer safety over cosmetic optimization.
6. Make the smallest patch that resolves the verified issue.
7. Run tests/evals and report exact verification.

## 4. Output contract

Each finding must contain:

```yaml
status: FACT | INFERENCE | UNKNOWN
severity: low | medium | high | critical
category: seo | schema | accessibility | commerce-data | platform | content
location: path:line
finding: concise description
evidence: supporting source
risk: practical consequence
recommended_patch: smallest safe fix
verification: test or observation that proves the fix
```

## 5. Commerce-data safety

Do not generate unsupported values for:

- price or discount;
- availability or inventory;
- materials or dimensions;
- shipping origin or delivery time;
- return/refund windows;
- ratings or review counts;
- compatibility, certifications, guarantees, or safety claims.

If the repository does not expose a reliable value, mark it `UNKNOWN` and design the UI/code to read from runtime data where possible.

## 6. Benchmark contribution rule

A new eval case should contain one primary regression, minimal supporting code, explicit expected rule IDs, and no private merchant/customer information.
