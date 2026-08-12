---
name: schema-validator
description: Validate ecommerce JSON-LD and structured data against visible or verified runtime facts.
---
# Schema Validator

## Purpose

Validate structured data against visible page content and verified runtime or merchant data.

## When to use

Use when reviewing Product, Offer, AggregateRating, BreadcrumbList, Organization, WebSite, or related structured data.

## Inputs

- JSON-LD, HTML, or template source;
- visible page values and runtime data when available;
- the expected schema type and route scope.

## Required checks
- Trace every commercial value to runtime or verified merchant data.
- Do not synthesize ratings, review counts, prices, stock, GTINs, SKUs, materials, or shipping details.
- Check duplicate Product graphs and conflicting offers.
- Treat a value that only exists in schema, but not in a verified source, as unsupported.
- Prefer removal of unsupported properties over invented completion.

## Output contract

Report each issue using the `PROTOCOL.md` finding contract and identify the exact property and evidence path.

## Failure conditions

- Missing source or runtime evidence: mark the property `UNKNOWN` or unsupported.
- Never invent ratings, review counts, prices, stock, GTINs, SKUs, materials, or shipping details.
- Do not call a graph valid solely because it parses as JSON.

## Verification

Run schema fixtures and deterministic evals; compare emitted properties with visible or verified values.
