---
name: woocommerce-code-review
description: Review WooCommerce hooks, product data, template overrides, escaping, and regression risks.
---
# WooCommerce Code Review

## Purpose

Review WooCommerce hooks, product data, template overrides, escaping, and regression risks.

## When to use

Use for `functions.php`, plugins, snippets, template overrides, or WooCommerce-specific frontend behavior.

## Inputs

- changed PHP, template, or plugin source;
- existing hook registrations and callback context;
- runtime product data source when buyer-facing values are involved.

## Required checks
- Search existing `add_action` / `add_filter` registrations before adding another.
- Verify callback priorities and removal/replacement behavior.
- Prefer `$product` / WooCommerce APIs for price, SKU, stock, dimensions, and attributes.
- Escape output and sanitize input appropriately.
- Avoid global behavior when the requested change is product/category-specific.
- Identify duplicate legacy snippets before merging new code.
- Report mobile/desktop markup impact when the change is frontend-facing.

## Output contract

Use the `PROTOCOL.md` finding contract and include hook names, callback names, priorities, and exact evidence.

## Failure conditions

- Do not add a callback before checking for duplicate registrations.
- Missing runtime product data means price, stock, SKU, dimensions, and attributes are `UNKNOWN`.
- Do not certify escaping or checkout behavior without the relevant source or runtime evidence.

## Verification

Run focused PHP/eval tests where available, inspect all matching hook registrations, and report unverified platform behavior.
