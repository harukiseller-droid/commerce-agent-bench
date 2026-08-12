from dataclasses import dataclass
import json
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
        re.compile(r'"ratingValue"\s*:\s*"?(?:5(?:\.0)?)"?', re.IGNORECASE),
        "Suspicious hard-coded rating value found in structured data.",
    ),
    Rule(
        "SCHEMA_FAKE_REVIEW_COUNT",
        "high",
        (".html", ".htm", ".json", ".jsonld", ".php", ".liquid"),
        re.compile(r'"reviewCount"\s*:\s*"?\d{3,}"?', re.IGNORECASE),
        "Suspicious hard-coded review count found in structured data.",
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
    Rule(
        "UNSAFE_HARDCODED_STOCK",
        "medium",
        (".html", ".htm", ".json", ".jsonld", ".php", ".liquid", ".js", ".ts", ".tsx"),
        re.compile(
            r"(?:stock|inventory|availability)\s*[:=]\s*['\"]?(?:\d+|in stock|out of stock|available|unavailable)['\"]?",
            re.IGNORECASE,
        ),
        "Potential hard-coded stock or availability claim. Prefer runtime product data.",
    ),
    Rule(
        "HTML_UNESCAPED_TEMPLATE_OUTPUT",
        "high",
        (".liquid",),
        re.compile(r"{{\s*(?:product|collection|variant)\.[A-Za-z_][A-Za-z0-9_]*\s*}}", re.IGNORECASE),
        "Template output may bypass the platform's escaping filter.",
    ),
    Rule(
        "SCHEMA_PRICE_CURRENCY_MISSING",
        "medium",
        (".json", ".jsonld"),
        re.compile(r'"price"\s*:\s*"?\d+(?:\.\d+)?"?', re.IGNORECASE),
        "Structured-data price has no detected priceCurrency property.",
    ),
    Rule(
        "SEO_CANONICAL_CONFLICT",
        "high",
        (".html", ".htm"),
        re.compile(r'<link\b(?=[^>]*\brel\s*=\s*["\']canonical["\'])[^>]*>', re.IGNORECASE),
        "Document contains multiple canonical links.",
    ),
    Rule(
        "SCHEMA_DUPLICATE_PRODUCT",
        "high",
        (".html", ".htm", ".json", ".jsonld"),
        re.compile(r'"@type"\s*:\s*"Product"', re.IGNORECASE),
        "Structured data contains duplicate Product entities.",
    ),
    Rule(
        "UNSAFE_HARDCODED_SHIPPING",
        "medium",
        (".html", ".htm", ".php", ".liquid", ".js", ".ts", ".tsx"),
        re.compile(
            r"(?:shipping|delivery)\s*[:=]\s*['\"]?[^\r\n]{0,40}\b\d+\s*(?:-|to)?\s*\d*\s*(?:days?|hours?)",
            re.IGNORECASE,
        ),
        "Potential hard-coded shipping or delivery-time claim.",
    ),
    Rule(
        "UNSAFE_HARDCODED_DIMENSIONS",
        "medium",
        (".html", ".htm", ".php", ".liquid", ".js", ".ts", ".tsx"),
        re.compile(
            r"(?:dimensions?|product_dimensions|item_(?:width|height|length))\s*[:=]\s*['\"]?\d+(?:\.\d+)?(?:\s*(?:x|×)\s*\d+(?:\.\d+)?)*\s*(?:cm|in|inch|inches)?",
            re.IGNORECASE,
        ),
        "Potential hard-coded product dimensions.",
    ),
    Rule(
        "SCHEMA_INVALID_JSONLD",
        "high",
        (".jsonld",),
        re.compile(r"(?!)"),
        "JSON-LD fixture is not valid JSON.",
    ),
    Rule(
        "SHOPIFY_STATIC_PRODUCT_PRICE",
        "medium",
        (".liquid",),
        re.compile(
            r"(?:class\s*=\s*['\"][^'\"]*\bprice\b[^'\"]*['\"]|price\s*[:=])[^<\r\n]*\$\d+(?:\.\d{2})?",
            re.IGNORECASE,
        ),
        "Shopify template contains a static price instead of runtime product data.",
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
        if path.suffix.lower() == ".jsonld":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                lines = text.splitlines()
                findings.append(
                    Finding(
                        "SCHEMA_INVALID_JSONLD",
                        "high",
                        rel,
                        exc.lineno,
                        "JSON-LD fixture is not valid JSON.",
                        lines[min(exc.lineno - 1, len(lines) - 1)].strip()[:180] if lines else "",
                    )
                )
        for rule in RULES:
            if path.suffix.lower() not in rule.extensions:
                continue
            if rule.rule_id == "SCHEMA_INVALID_JSONLD":
                continue
            if rule.rule_id == "SCHEMA_PRICE_CURRENCY_MISSING" and re.search(
                r'"priceCurrency"\s*:', text, re.IGNORECASE
            ):
                continue
            matches = list(rule.pattern.finditer(text))
            if rule.rule_id in {
                "WOOCOMMERCE_DUPLICATE_HOOK",
                "SEO_CANONICAL_CONFLICT",
                "SCHEMA_DUPLICATE_PRODUCT",
            }:
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
