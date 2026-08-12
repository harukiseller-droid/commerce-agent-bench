---
name: technical-seo-audit
description: Review ecommerce templates for indexation, metadata, canonical, heading, internal-link, and duplicate-page regressions.
---
# Technical SEO Audit

## Purpose

Review ecommerce templates for indexation and metadata regressions using source evidence.

## When to use

Use for product, collection, category, blog, or template-level SEO review.

## Inputs

- HTML or template source;
- route and canonical context;
- runtime or crawl evidence when indexability is part of the request.

## Required checks
- title and meta description source;
- canonical behavior;
- robots/indexability;
- one meaningful H1;
- crawlable internal links;
- pagination/filter parameter behavior where visible in code;
- duplicate template outputs;
- structured data consistency.

## Output contract

Use the `PROTOCOL.md` finding contract and distinguish code evidence from SEO strategy inference.

## Failure conditions

- Do not claim rankings, traffic, search volume, or indexing status without external verified data.
- If canonical, robots, or parameter behavior cannot be observed, report `UNKNOWN`.
- Do not treat metadata presence alone as proof of search performance.

## Verification

Run relevant HTML/eval checks and, when available, inspect the rendered route and response headers.
