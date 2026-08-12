<?php
function cab_first_summary_note() { echo '<p>First synthetic note.</p>'; }
function cab_second_summary_note() { echo '<p>Second synthetic note.</p>'; }

add_action('woocommerce_single_product_summary', 'cab_first_summary_note', 25);
add_action('woocommerce_single_product_summary', 'cab_second_summary_note', 30);
