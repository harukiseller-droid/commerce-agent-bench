# WooCommerce product-summary benchmark

## Scope

The `woocommerce-product-summary` PHP fixture registers the same WooCommerce product-summary hook twice. It uses neutral demo callbacks and contains no merchant or customer data.

## Expected result

- Fixture: `evals/fixtures/woocommerce-product-summary`
- Expected rule: `WOOCOMMERCE_DUPLICATE_HOOK`
- Detected rule: `WOOCOMMERCE_DUPLICATE_HOOK`
- Status: `PASS`

Reproduce with:

```bash
python -m commerce_agent_bench.cli evals/fixtures/woocommerce-product-summary --format json
```
