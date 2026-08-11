# Adding an eval

1. Create a minimal directory under `evals/fixtures/<case-name>/`.
2. Add only the code required to reproduce the regression.
3. Add expected rule IDs to `evals/manifest.json`.
4. Add or update a pytest test when introducing a new scanner rule.
5. Run `pytest -q` and `python scripts/run_evals.py`.
6. In the pull request, explain the practical ecommerce failure mode.
