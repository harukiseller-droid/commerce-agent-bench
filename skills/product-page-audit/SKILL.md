---
name: product-page-audit
description: Evidence-first review of ecommerce product pages without inventing merchant or product facts.
---
# Product Page Audit

Use when reviewing a product template, product-page implementation, or buyer-facing product detail surface.

## Required checks
- Identify runtime sources for title, price, variants, inventory, images, and product metadata.
- Check primary heading, image alt text, add-to-cart control, variant state, price/availability consistency, and mobile-safe markup.
- Check whether shipping/returns/specifications are verified data or generic hard-coded claims.
- Check Product structured data against visible/runtime facts.
- Mark unavailable merchant facts `UNKNOWN`.

## Output
Use the finding contract from `PROTOCOL.md`. Never convert a plausible product detail into a fact.
