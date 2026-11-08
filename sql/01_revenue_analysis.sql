
-- 1. Overall Delivered Revenue, Orders and Average Order Value

SELECT
    ROUND(SUM(oi.price)::numeric, 2) AS total_delivered_revenue,
    COUNT(DISTINCT o.order_id) AS total_delivered_orders,
    ROUND(
        (SUM(oi.price) / NULLIF(COUNT(DISTINCT o.order_id), 0))::numeric,
        2
    ) AS average_order_value
FROM ecommerce.orders o
JOIN ecommerce.order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered';


-- 2. Monthly Delivered Revenue Trend

SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
    ROUND(SUM(oi.price)::numeric, 2) AS monthly_revenue
FROM ecommerce.orders o
JOIN ecommerce.order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_TRUNC('month', o.order_purchase_timestamp)
ORDER BY month;


-- 3. Revenue by Customer State

SELECT
    c.customer_state,
    ROUND(SUM(oi.price)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM ecommerce.orders o
JOIN ecommerce.order_items oi
    ON o.order_id = oi.order_id
JOIN ecommerce.customers c
    ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_state
ORDER BY total_revenue DESC;
