from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    path: str
    line: int
    message: str
    evidence: str


@dataclass(frozen=True)
class Rule:
    rule_id: str
    severity: str
    extensions: tuple[str, ...]
    pattern: re.Pattern[str]
    message: str


RULES: tuple[Rule, ...] = (
    Rule(
        "HTML_IMG_ALT_MISSING",
        "medium",
        (".html", ".htm", ".liquid", ".php"),
        re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*>", re.IGNORECASE),
        "Image element is missing an alt attribute.",
    ),
    Rule(
        "HTML_BUTTON_NAME_MISSING",
        "medium",
        (".html", ".htm", ".liquid", ".php"),
        re.compile(r"<button\b[^>]*>\s*</button>", re.IGNORECASE),
        "Button has no accessible name.",
    ),
    Rule(
        "SEO_TITLE_MISSING",
        "high",
        (".html", ".htm"),
        re.compile(r"<head>(?:(?!<title\b).)*</head>", re.IGNORECASE | re.DOTALL),
        "Document head does not contain a title element.",
    ),
    Rule(
        "SEO_META_DESCRIPTION_MISSING",
        "medium",
        (".html", ".htm"),
        re.compile(r"<head>(?:(?!name=[\"']description[\"']).)*</head>", re.IGNORECASE | re.DOTALL),
        "Document head does not contain a meta description.",
    ),
    Rule(
        "SCHEMA_FAKE_RATING",
        "high",
        (".html", ".htm", ".json", ".jsonld", ".php", ".liquid"),
        re.compile(r'"(?:ratingValue|reviewCount)"\s*:\s*"?(?:5(?:\.0)?|9999)"?', re.IGNORECASE),
        "Suspicious hard-coded rating/review value found in structured data.",
    ),
    Rule(
        "WOOCOMMERCE_DUPLICATE_HOOK",
        "high",
        (".php",),
        re.compile(r"add_action\(\s*['\"]woocommerce_single_product_summary['\"]", re.IGNORECASE),
        "WooCommerce product-summary hook registered; duplicate registrations are checked per file.",
    ),
    Rule(
        "UNSAFE_HARDCODED_PRICE",
        "medium",
        (".php", ".liquid", ".js", ".ts", ".tsx"),
        re.compile(r"(?:price|amount)\s*[:=]\s*['\"]?\$?\d+(?:\.\d{2})?['\"]?", re.IGNORECASE),
        "Potential hard-coded commerce price. Prefer runtime product data.",
    ),
)


def iter_source_files(root: Path) -> Iterable[Path]:
    ignored = {".git", ".venv", "venv", "node_modules", "dist", "build"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored for part in path.parts):
            continue
        yield path


def _line_number(text: str, start: int) -> int:
    return text.count("\n", 0, start) + 1


def scan_path(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_source_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        rel = str(path.relative_to(root))
        for rule in RULES:
            if path.suffix.lower() not in rule.extensions:
                continue
            matches = list(rule.pattern.finditer(text))
            if rule.rule_id == "WOOCOMMERCE_DUPLICATE_HOOK":
                if len(matches) <= 1:
                    continue
                matches = matches[1:]
            for match in matches:
                evidence = match.group(0).strip().replace("\n", " ")[:180]
                findings.append(
                    Finding(
                        rule.rule_id,
                        rule.severity,
                        rel,
                        _line_number(text, match.start()),
                        rule.message,
                        evidence,
                    )
                )
    return sorted(findings, key=lambda x: (x.path, x.line, x.rule_id))
