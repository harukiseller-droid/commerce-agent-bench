---
name: woocommerce-code-review
description: Review WooCommerce hooks, product data, template overrides, escaping, and regression risks.
---
# WooCommerce Code Review

Use for `functions.php`, plugins, snippets, template overrides, or WooCommerce-specific frontend behavior.

## Required checks
- Search existing `add_action` / `add_filter` registrations before adding another.
- Verify callback priorities and removal/replacement behavior.
- Prefer `$product` / WooCommerce APIs for price, SKU, stock, dimensions, and attributes.
- Escape output and sanitize input appropriately.
- Avoid global behavior when the requested change is product/category-specific.
- Identify duplicate legacy snippets before merging new code.
- Report mobile/desktop markup impact when the change is frontend-facing.
