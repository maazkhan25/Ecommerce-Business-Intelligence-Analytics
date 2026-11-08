
-- 1. Top 10 Product Categories by Revenue

SELECT
    COALESCE(ct.product_category_name_english, 'Unknown') AS product_category,
    ROUND(SUM(oi.price)::numeric, 2) AS total_revenue
FROM ecommerce.order_items oi
JOIN ecommerce.orders o
    ON oi.order_id = o.order_id
JOIN ecommerce.products p
    ON oi.product_id = p.product_id
LEFT JOIN ecommerce.category_translation ct
    ON p.product_category_name = ct.product_category_name
WHERE o.order_status = 'delivered'
GROUP BY ct.product_category_name_english
ORDER BY total_revenue DESC
LIMIT 10;


-- 2. Top 10 Best-Selling Product Categories

SELECT
    COALESCE(ct.product_category_name_english, 'Unknown') AS product_category,
    COUNT(*) AS total_items_sold
FROM ecommerce.order_items oi
JOIN ecommerce.orders o
    ON oi.order_id = o.order_id
JOIN ecommerce.products p
    ON oi.product_id = p.product_id
LEFT JOIN ecommerce.category_translation ct
    ON p.product_category_name = ct.product_category_name
WHERE o.order_status = 'delivered'
GROUP BY ct.product_category_name_english
ORDER BY total_items_sold DESC
LIMIT 10;


-- 3. Average Product Price by Category

SELECT
    COALESCE(ct.product_category_name_english, 'Unknown') AS product_category,
    ROUND(AVG(oi.price)::numeric, 2) AS average_price
FROM ecommerce.order_items oi
JOIN ecommerce.products p
    ON oi.product_id = p.product_id
LEFT JOIN ecommerce.category_translation ct
    ON p.product_category_name = ct.product_category_name
GROUP BY ct.product_category_name_english
ORDER BY average_price DESC;


-- 4. Top 10 Sellers by Delivered Revenue

SELECT
    oi.seller_id,
    ROUND(SUM(oi.price)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT oi.order_id) AS total_orders
FROM ecommerce.order_items oi
JOIN ecommerce.orders o
    ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY oi.seller_id
ORDER BY total_revenue DESC
LIMIT 10;
