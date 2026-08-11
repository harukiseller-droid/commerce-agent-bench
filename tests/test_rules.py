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
    assert "SCHEMA_FAKE_RATING" in ids("schema-conflict")


def test_duplicate_hooks():
    assert "WOOCOMMERCE_DUPLICATE_HOOK" in ids("duplicate-hooks")


def test_accessibility_regression():
    found = ids("accessibility-regression")
    assert "HTML_BUTTON_NAME_MISSING" in found
    assert "HTML_IMG_ALT_MISSING" in found


def test_seo_regression():
    found = ids("seo-regression")
    assert "SEO_TITLE_MISSING" in found
