-- URI Online Judge 2620

SELECT c.name, o.id
FROM customers c
    JOIN orders o ON c.id = o.id_customers
WHERE o.orders_date < DATE('2016-07-01')

