<?php
/** Safe example: render a product-specific note from runtime data. */
add_action('woocommerce_single_product_summary', function () {
    global $product;
    if (!$product) return;
    $sku = $product->get_sku();
    if ($sku) {
        echo '<p class="product-sku">SKU: ' . esc_html($sku) . '</p>';
    }
}, 35);
