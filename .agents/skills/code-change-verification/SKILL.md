---
name: code-change-verification
description: Verify a source change, its tests, its diff boundaries, and remaining risk.
---
# Code Change Verification

## Purpose

Provide a repeatable final gate for source changes before merge or release.

## When to use

Use for every source-code modification and before completing a substantial pull request.

## Inputs

- the working-tree diff and base revision;
- project test and eval commands;
- dependency, generated-artifact, and runtime context.

## Required checks

- Inspect the full diff and changed file list.
- Run project tests.
- Run deterministic evals.
- Check changed behavior against the requested contract.
- Check for unexpected files.
- Check dependency changes.
- Check generated artifacts and secrets.
- Summarize remaining risk and unverified behavior.

## Output contract

Return exactly one top-level status:

```text
PASS
PASS WITH WARNINGS
FAIL
```

Include commands, exact results, changed scope, warnings, and remaining risk below the status.

## Failure conditions

- `FAIL` if a required test/eval fails, the diff contains an unrelated change, or a secret is detected.
- `PASS WITH WARNINGS` when deterministic checks pass but required runtime or external-platform evidence is unavailable.
- Never claim a test ran when it did not run.

## Verification

Run the final commands from the repository contract, review `git diff --check`, inspect status, and repeat any invalidated gate after the last change.
