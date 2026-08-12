---
name: pinterest-content-generator
description: Generate ecommerce Pinterest metadata grounded in verified product or page facts.
status: experimental
---
# Pinterest Content Generator

## Purpose

Generate Pinterest metadata from verified product or page facts. This is an experimental, non-core workflow.

## When to use

Use only when verified page/product facts and a destination URL are available.

## Inputs

- verified page or product facts;
- destination URL;
- primary keyword and buyer-intent context when supplied.

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

## Output contract

Return the requested output fields and label unsupported claims `UNKNOWN`. Do not imply that this experimental workflow is part of the core ecommerce review path.

## Failure conditions

- Missing verified facts or destination URL: stop and report `UNKNOWN`.
- Never invent discounts, materials, shipping, ratings, stock, compatibility, or product features.
- Do not claim publication, traffic, or engagement without verified platform evidence.

## Verification

Check every generated field against the supplied source facts and verify the destination URL format.
