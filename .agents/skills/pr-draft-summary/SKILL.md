---
name: pr-draft-summary
description: Produce a factual pull-request summary from verified changes and checks.
---
# PR Draft Summary

## Purpose

Turn verified implementation evidence into a concise reviewer-facing pull-request description.

## When to use

Use before opening or updating a pull request after implementation and verification.

## Inputs

- final diff and changed files;
- issue or task scope;
- commands actually run and their outputs;
- known limitations and reviewer risks.

## Required checks

Confirm the summary covers:

- What changed
- Why
- Tests run
- Eval results
- Known limitations
- Risk
- Reviewer focus

Separate repository facts from assumptions and link exact evidence where possible.

## Output contract

Return these headings in this order:

```text
## What changed
## Why
## Tests run
## Eval results
## Known limitations
## Risk
## Reviewer focus
```

Use plain factual language. Include `Codex benchmark execution: NOT RUN` unless a real Codex execution artifact exists.

## Failure conditions

- Do not use marketing language or inflate adoption, usage, stars, contributors, or performance.
- Do not report guessed test results.
- Do not create `codex-output.md`, `patch.diff`, or `result.json` without an actual execution.

## Verification

Compare every statement with the final diff, command output, and repository state before publishing the summary.
