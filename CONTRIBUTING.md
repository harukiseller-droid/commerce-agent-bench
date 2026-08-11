# Contributing

Thanks for helping improve ecommerce-agent reliability.

## Good contributions

- Minimal regression fixtures from WooCommerce, Shopify, or static storefront patterns
- New deterministic checks with tests
- Better agent workflows with clear evidence requirements
- False-positive reductions
- Documentation and cross-platform examples

## Fixture requirements

A fixture must:

1. isolate a small failure mode;
2. contain no private merchant/customer data;
3. document the expected rule IDs in `evals/manifest.json`;
4. include a test when adding a new scanner rule;
5. avoid trademarked storefront copies unless necessary for interoperability discussion.

## Local checks

```bash
pip install -e . pytest
pytest -q
python scripts/run_evals.py
```

## Pull requests

Explain the regression being modeled, why the expected result is correct, and how false positives were considered.
