import argparse
import json
from pathlib import Path
from .rules import scan_path


def _serialize(findings):
    return [f.__dict__ for f in findings]


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="commerce-agent-bench",
        description="Run deterministic ecommerce code checks used by agent eval fixtures.",
    )
    parser.add_argument("path", nargs="?", default=".", help="Repository or fixture directory")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--fail-on", choices=("none", "medium", "high"), default="high")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    findings = scan_path(root)

    if args.format == "json":
        print(json.dumps(_serialize(findings), indent=2))
    else:
        if not findings:
            print("PASS: no findings")
        for f in findings:
            print(f"{f.severity.upper():6} {f.rule_id:32} {f.path}:{f.line} {f.message}")

    levels = {"medium": 1, "high": 2}
    threshold = levels.get(args.fail_on, 99)
    return 1 if any(levels.get(f.severity, 0) >= threshold for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
