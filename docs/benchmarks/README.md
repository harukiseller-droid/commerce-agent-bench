# Deterministic benchmark report

This report covers the seven cases currently registered in `evals/manifest.json`. It measures exact rule-ID agreement between each fixture's expected findings and the scanner output.

Run command:

```bash
python scripts/run_benchmarks.py
```

The recorded run used source commit `80d50ec` on 2026-08-12.

| Metric | Result |
|---|---:|
| Fixture cases | 7 |
| Expected findings | 10 |
| Detected findings | 10 |
| Missed findings | 0 |
| Unexpected findings | 0 |
| False positives against the manifest | 0 |

This is deterministic repository evidence, not evidence of external adoption or production recall. A case passes only when the detected rule-ID set exactly matches the manifest's expected set. The machine-readable case-level output is in [`results.json`](results.json).

Platform-specific reports:

- [`shopify-product-card.md`](shopify-product-card.md)
- [`woocommerce-product-summary.md`](woocommerce-product-summary.md)
