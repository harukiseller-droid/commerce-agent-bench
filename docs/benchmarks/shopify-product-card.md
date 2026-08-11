# Shopify product-card benchmark

## Scope

The `shopify-product-card` Liquid fixture models a product card whose image has no `alt` attribute. Product title and price are read from Liquid runtime variables; no merchant data is included.

## Expected result

- Fixture: `evals/fixtures/shopify-product-card`
- Expected rule: `HTML_IMG_ALT_MISSING`
- Detected rule: `HTML_IMG_ALT_MISSING`
- Status: `PASS`

Reproduce with:

```bash
python -m commerce_agent_bench.cli evals/fixtures/shopify-product-card --format json
```
