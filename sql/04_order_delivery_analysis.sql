
-- 1. Order Status Distribution

SELECT
    order_status,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(
        COUNT(DISTINCT order_id) * 100.0 /
        SUM(COUNT(DISTINCT order_id)) OVER (),
        2
    ) AS percentage
FROM ecommerce.orders
GROUP BY order_status
ORDER BY total_orders DESC;


-- 2. Average Delivery Time

SELECT
    ROUND(
        AVG(
            EXTRACT(EPOCH FROM (
                order_delivered_customer_date -
                order_purchase_timestamp
            )) / 86400
        )::numeric,
        2
    ) AS average_delivery_days
FROM ecommerce.orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_purchase_timestamp IS NOT NULL;


-- 3. Monthly Average Delivery Time

SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    ROUND(
        AVG(
            EXTRACT(EPOCH FROM (
                order_delivered_customer_date -
                order_purchase_timestamp
            )) / 86400
        )::numeric,
        2
    ) AS average_delivery_days
FROM ecommerce.orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_purchase_timestamp IS NOT NULL
GROUP BY DATE_TRUNC('month', order_purchase_timestamp)
ORDER BY month;


-- 4. Orders Delivered Later Than Estimated Date

SELECT
    COUNT(*) AS delayed_orders
FROM ecommerce.orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date >
      order_estimated_delivery_date;
