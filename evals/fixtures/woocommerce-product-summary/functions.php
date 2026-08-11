<?php
function cab_first_product_note() { echo '<p>Product note one.</p>'; }
function cab_second_product_note() { echo '<p>Product note two.</p>'; }

add_action('woocommerce_single_product_summary', 'cab_first_product_note', 25);
add_action('woocommerce_single_product_summary', 'cab_second_product_note', 30);
