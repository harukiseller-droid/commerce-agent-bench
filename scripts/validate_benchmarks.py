#!/usr/bin/env python3
"""Validate Codex benchmark package structure without fabricating run results."""

import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_ROOT = ROOT / "benchmarks" / "codex"
EXPECTED_SCENARIOS = {
    "001-hardcoded-price",
    "002-fake-rating",
    "003-duplicate-wc-hook",
    "004-shopify-runtime-data",
    "005-fabricated-product-fact",
}
REQUIRED_FILES = ("task.md", "README.md", "expected.json")


def validate() -> list[str]:
    errors: list[str] = []
    if not BENCHMARK_ROOT.is_dir():
        return [f"missing benchmark root: {BENCHMARK_ROOT.relative_to(ROOT)}"]

    scenarios = {path.name for path in BENCHMARK_ROOT.iterdir() if path.is_dir()}
    for missing in sorted(EXPECTED_SCENARIOS - scenarios):
        errors.append(f"missing scenario directory: {missing}")
    for unexpected in sorted(scenarios - EXPECTED_SCENARIOS):
        errors.append(f"unexpected scenario directory: {unexpected}")

    seen_scenario_names: set[str] = set()
    for scenario_dir in sorted(BENCHMARK_ROOT.iterdir()):
        if not scenario_dir.is_dir() or scenario_dir.name not in EXPECTED_SCENARIOS:
            continue
        for filename in REQUIRED_FILES:
            if not (scenario_dir / filename).is_file():
                errors.append(f"{scenario_dir.name}: missing {filename}")
        fixture_dir = scenario_dir / "fixture"
        if not fixture_dir.is_dir() or not any(fixture_dir.iterdir()):
            errors.append(f"{scenario_dir.name}: fixture directory is missing or empty")

        expected_path = scenario_dir / "expected.json"
        if not expected_path.is_file():
            continue
        try:
            expected = json.loads(expected_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{scenario_dir.name}: invalid expected.json ({exc})")
            continue
        if not isinstance(expected, dict):
            errors.append(f"{scenario_dir.name}: expected.json must contain an object")
            continue
        scenario_name = expected.get("scenario")
        if not isinstance(scenario_name, str) or not scenario_name.strip():
            errors.append(f"{scenario_dir.name}: scenario name is empty")
        elif scenario_name in seen_scenario_names:
            errors.append(f"duplicate scenario name: {scenario_name}")
        else:
            seen_scenario_names.add(scenario_name)
        required_findings = expected.get("required_findings")
        if not isinstance(required_findings, list) or not required_findings or not all(
            isinstance(item, str) and item.strip() for item in required_findings
        ):
            errors.append(f"{scenario_dir.name}: required_findings must be a non-empty string list")

        result_path = scenario_dir / "result.json"
        codex_output_path = scenario_dir / "codex-output.md"
        patch_path = scenario_dir / "patch.diff"
        readme_path = scenario_dir / "README.md"
        artifacts = (result_path, codex_output_path, patch_path)
        present = [path.exists() for path in artifacts]
        if any(present) and not all(present):
            errors.append(
                f"{scenario_dir.name}: result artifacts must include result.json, codex-output.md, and patch.diff together"
            )
        if readme_path.is_file():
            readme = readme_path.read_text(encoding="utf-8")
            marked_pass = re.search(r"(?im)^\s*-\s*Status:\s*`?PASS\b", readme)
            if marked_pass and not all(present):
                errors.append(f"{scenario_dir.name}: PASS status requires complete result artifacts")
        if result_path.is_file():
            try:
                result = json.loads(result_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{scenario_dir.name}: invalid result.json ({exc})")
                continue
            if not isinstance(result, dict):
                errors.append(f"{scenario_dir.name}: result.json must contain an object")
                continue
            if result.get("scenario") != scenario_name:
                errors.append(f"{scenario_dir.name}: result scenario does not match expected.json")
            if result.get("agent") != "codex":
                errors.append(f"{scenario_dir.name}: result agent must be codex")
            if result.get("result") not in {"pass", "fail"}:
                errors.append(f"{scenario_dir.name}: result must be pass or fail")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("FAIL benchmark-artifact-validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS benchmark-artifact-validation")
    print(f"scenarios: {len(EXPECTED_SCENARIOS)}")
    print("Codex benchmark execution: NOT RUN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
