#!/usr/bin/env python3
"""Produce a machine-readable summary of the deterministic eval manifest."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from commerce_agent_bench.rules import scan_path  # noqa: E402


def main() -> int:
    manifest_path = ROOT / "evals" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cases = []
    expected_findings = 0
    detected_findings = 0
    missed_findings = 0
    unexpected_findings = 0

    for case in manifest["cases"]:
        fixture = ROOT / "evals" / "fixtures" / case["fixture"]
        expected = set(case["expected_rule_ids"])
        actual = {finding.rule_id for finding in scan_path(fixture)}
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        expected_findings += len(expected)
        detected_findings += len(expected & actual)
        missed_findings += len(missing)
        unexpected_findings += len(unexpected)
        cases.append(
            {
                "id": case["id"],
                "fixture": case["fixture"],
                "expected_rule_ids": sorted(expected),
                "detected_rule_ids": sorted(actual),
                "missing_rule_ids": missing,
                "unexpected_rule_ids": unexpected,
                "status": "PASS" if not missing and not unexpected else "FAIL",
            }
        )

    report = {
        "benchmark": "deterministic-evals",
        "fixture_count": len(cases),
        "expected_findings": expected_findings,
        "detected_findings": detected_findings,
        "missed_findings": missed_findings,
        "unexpected_findings": unexpected_findings,
        "false_positives": unexpected_findings,
        "cases": cases,
    }
    print(json.dumps(report, indent=2))
    return 1 if missed_findings or unexpected_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
