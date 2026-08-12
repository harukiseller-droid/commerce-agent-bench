---
name: accessibility-audit
description: Review ecommerce UI code for practical accessibility regressions in buyer flows.
---
# Accessibility Audit

## Purpose

Review ecommerce UI code for practical accessibility regressions without claiming conformance that was not tested.

## When to use

Use for product cards, product pages, cart, filters, navigation, dialogs, and checkout-adjacent UI.

## Inputs

- the changed UI source and nearby components;
- route, template, or fixture scope;
- browser evidence when interactive behavior is part of the claim.

## Required checks
- meaningful image alternatives;
- accessible names for buttons/links/inputs;
- label/control association;
- keyboard reachability and focus behavior when code is available;
- semantic headings and landmarks;
- state communication for variants, filters, errors, and disabled actions;
- avoid relying on color alone.

## Output contract

Use the finding contract from `PROTOCOL.md`: status, severity, category, location, finding, evidence, risk, recommended patch, and verification.

## Failure conditions

- Required source or rendered evidence is missing: mark the conclusion `UNKNOWN`.
- Do not claim WCAG conformance from static code inspection alone.
- Do not treat a passing static check as proof of keyboard or screen-reader behavior.

## Verification

Run the smallest relevant project tests/evals and state whether browser or assistive-technology testing was performed.
