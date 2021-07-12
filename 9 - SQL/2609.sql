-- URI Online Judge 2609

SELECT 
    categories.name,
    SUM(products.amount) AS sum
FROM products
    JOIN categories ON categories.id = products.id_categories
GROUP BY categories.name