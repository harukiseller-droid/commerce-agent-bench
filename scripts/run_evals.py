#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from commerce_agent_bench.rules import scan_path  # noqa: E402


def main() -> int:
    manifest_path = ROOT / "evals" / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    failures = []

    for case in manifest["cases"]:
        fixture = ROOT / "evals" / "fixtures" / case["fixture"]
        actual = {f.rule_id for f in scan_path(fixture)}
        expected = set(case["expected_rule_ids"])
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        status = "PASS" if not missing and not unexpected else "FAIL"
        print(f"{status:4} {case['id']}")
        if missing:
            print("     missing:", ", ".join(missing))
        if unexpected:
            print("     unexpected:", ", ".join(unexpected))
        if missing or unexpected:
            failures.append(case["id"])

    print(f"\n{len(manifest['cases']) - len(failures)}/{len(manifest['cases'])} eval cases passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
