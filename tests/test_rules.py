from pathlib import Path
from commerce_agent_bench.rules import scan_path

ROOT = Path(__file__).parents[1]


def ids(fixture: str) -> set[str]:
    return {f.rule_id for f in scan_path(ROOT / "evals" / "fixtures" / fixture)}


def test_broken_product_page():
    found = ids("broken-product-page")
    assert "HTML_IMG_ALT_MISSING" in found
    assert "SEO_TITLE_MISSING" in found
    assert "SEO_META_DESCRIPTION_MISSING" in found


def test_schema_conflict():
    found = ids("schema-conflict")
    assert "SCHEMA_FAKE_RATING" in found
    assert "SCHEMA_FAKE_REVIEW_COUNT" in found


def test_duplicate_hooks():
    assert "WOOCOMMERCE_DUPLICATE_HOOK" in ids("duplicate-hooks")


def test_accessibility_regression():
    found = ids("accessibility-regression")
    assert "HTML_BUTTON_NAME_MISSING" in found
    assert "HTML_IMG_ALT_MISSING" in found


def test_seo_regression():
    found = ids("seo-regression")
    assert "SEO_TITLE_MISSING" in found


def test_extended_regressions():
    expected = {
        "hardcoded-price": "UNSAFE_HARDCODED_PRICE",
        "fake-review-count": "SCHEMA_FAKE_REVIEW_COUNT",
        "fake-stock": "UNSAFE_HARDCODED_STOCK",
        "unsafe-template-escaping": "HTML_UNESCAPED_TEMPLATE_OUTPUT",
        "missing-price-currency": "SCHEMA_PRICE_CURRENCY_MISSING",
        "canonical-conflict": "SEO_CANONICAL_CONFLICT",
        "duplicate-product-schema": "SCHEMA_DUPLICATE_PRODUCT",
        "fabricated-shipping": "UNSAFE_HARDCODED_SHIPPING",
        "fabricated-dimensions": "UNSAFE_HARDCODED_DIMENSIONS",
        "invalid-product-jsonld": "SCHEMA_INVALID_JSONLD",
        "shopify-static-price": "SHOPIFY_STATIC_PRODUCT_PRICE",
        "empty-cta": "HTML_BUTTON_NAME_MISSING",
    }
    for fixture, rule_id in expected.items():
        assert rule_id in ids(fixture)
