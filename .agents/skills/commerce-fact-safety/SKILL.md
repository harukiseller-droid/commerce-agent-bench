---
name: commerce-fact-safety
description: Classify ecommerce claims as FACT, INFERENCE, or UNKNOWN using traceable evidence.
---
# Commerce Fact Safety

## Purpose

Prevent unsupported buyer-facing or structured-data claims from entering ecommerce code, content, or reviews.

## When to use

Use for any change or review involving product facts, offers, schema, copy, metadata, or generated content.

## Inputs

- the changed source, diff, or generated content;
- repository and runtime data sources;
- user-provided verified facts, if any.

## Required checks

Inspect claims involving price, sale price, stock, inventory, rating, review count, shipping time, returns, dimensions, materials, compatibility, SKU, availability, and Product schema facts.

- Trace each claim to repository, runtime, or user-provided verified data.
- Classify directly supported values as `FACT`.
- Classify reasoned but unproven conclusions as `INFERENCE`.
- Classify unavailable or untraceable values as `UNKNOWN`.
- Prefer runtime platform data over hard-coded commerce values.

## Output contract

Return one JSON object per material claim:

```json
{
  "status": "FACT|INFERENCE|UNKNOWN",
  "severity": "low|medium|high|critical",
  "fact": "",
  "source": "",
  "reason": "",
  "recommended_action": ""
}
```

`source` must identify a file/path, runtime response, or user-supplied verified source for `FACT`.

## Failure conditions

- Never invent product specs, prices, materials, stock, shipping times, returns, ratings, reviews, certifications, guarantees, or compatibility.
- Do not upgrade an `UNKNOWN` value because it would make copy or schema look complete.
- Do not call a schema-only value verified without a visible or runtime-backed source.

## Verification

Review the complete diff, rerun relevant deterministic checks, and sample every emitted claim against its cited source.
