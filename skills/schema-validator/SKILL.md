---
name: schema-validator
description: Validate ecommerce JSON-LD and structured data against visible or verified runtime facts.
---
# Schema Validator

Use when reviewing Product, Offer, AggregateRating, BreadcrumbList, Organization, WebSite, or related structured data.

## Rules
- Trace every commercial value to runtime or verified merchant data.
- Do not synthesize ratings, review counts, prices, stock, GTINs, SKUs, materials, or shipping details.
- Check duplicate Product graphs and conflicting offers.
- Treat a value that only exists in schema, but not in a verified source, as unsupported.
- Prefer removal of unsupported properties over invented completion.
