---
name: product-page-audit
description: Evidence-first review of ecommerce product pages without inventing merchant or product facts.
---
# Product Page Audit

## Purpose

Review product-page correctness and buyer-risk regressions using repository and runtime evidence.

## When to use

Use when reviewing a product template, product-page implementation, or buyer-facing product detail surface.

## Inputs

- product-page source, template, or fixture;
- runtime data source if one is available;
- visible page or test evidence for buyer-facing behavior.

## Required checks
- Identify runtime sources for title, price, variants, inventory, images, and product metadata.
- Check primary heading, image alt text, add-to-cart control, variant state, price/availability consistency, and mobile-safe markup.
- Check whether shipping/returns/specifications are verified data or generic hard-coded claims.
- Check Product structured data against visible/runtime facts.
- Mark unavailable merchant facts `UNKNOWN`.

## Output contract

Use the finding contract from `PROTOCOL.md`. Never convert a plausible product detail into a fact.

## Failure conditions

- Missing runtime or verified merchant data means the affected claim is `UNKNOWN`.
- Do not certify checkout, inventory, price, shipping, or returns behavior from static markup alone.
- Do not report a schema value as valid when it is not visible or runtime-backed.

## Verification

Run focused tests/evals, inspect the rendered route when available, and identify any unverified browser or platform behavior.
