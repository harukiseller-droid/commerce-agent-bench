---
name: pinterest-content-generator
description: Generate ecommerce Pinterest metadata grounded in verified product or page facts.
---
# Pinterest Content Generator

Use only when verified page/product facts and a destination URL are available.

## Output fields
- pin title;
- pin description;
- alt text;
- destination URL;
- primary keyword;
- buyer-intent angle.

## Safety rules
- Do not invent discounts, materials, shipping, ratings, stock, compatibility, or product features.
- Keep title and description natural rather than keyword-stuffed.
- If a requested selling point is not supported by source data, mark it `UNKNOWN` rather than generating it.
