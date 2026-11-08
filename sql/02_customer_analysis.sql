
-- 1. Total Customers by State

SELECT
    customer_state,
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM ecommerce.customers
GROUP BY customer_state
ORDER BY total_customers DESC;


-- 2. Top 10 Cities by Customer Count

SELECT
    customer_city,
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM ecommerce.customers
GROUP BY customer_city
ORDER BY total_customers DESC
LIMIT 10;


-- 3. Customer Order Frequency

SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM ecommerce.customers c
JOIN ecommerce.orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_unique_id
ORDER BY total_orders DESC;


-- 4. Repeat vs One-Time Customers

WITH customer_orders AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM ecommerce.customers c
    JOIN ecommerce.orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)
SELECT
    CASE
        WHEN total_orders = 1 THEN 'One-Time Customer'
        ELSE 'Repeat Customer'
    END AS customer_type,
    COUNT(*) AS total_customers
FROM customer_orders
GROUP BY customer_type;
