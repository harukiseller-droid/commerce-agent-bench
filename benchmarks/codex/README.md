# Codex benchmark scenarios

These scenarios are prompt-and-fixture packages for a real Codex execution. They are not deterministic scanner evals and must not be marked as passed from static inspection.

Each scenario contains:

- `task.md`: the agent task;
- `README.md`: scope, expected behavior, and current status;
- `fixture/`: synthetic ecommerce source with no private merchant data;
- `expected.json`: required findings and forbidden behaviors.

After a real Codex run, add `codex-output.md`, `patch.diff`, and `result.json` to that scenario. Until then, the status is `NOT RUN` and no result artifact should exist.

Validate the package structure with:

```bash
python scripts/validate_benchmarks.py
```

`Codex benchmark execution: NOT RUN` is the current repository-wide status until an actual Codex runtime produces evidence.

The optional GitHub workflow is `.github/workflows/codex-review.yml`. It is manual, disabled unless explicitly opted into, and `NOT VERIFIED`; normal CI never requires an API secret.
