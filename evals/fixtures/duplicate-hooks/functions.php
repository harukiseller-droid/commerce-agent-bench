<?php
function cab_shipping_note() { echo '<p>Ships from runtime settings.</p>'; }
function cab_fit_note() { echo '<p>Read product dimensions.</p>'; }
add_action('woocommerce_single_product_summary', 'cab_shipping_note', 25);
add_action('woocommerce_single_product_summary', 'cab_fit_note', 30);
