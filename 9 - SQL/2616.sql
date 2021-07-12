-- URI Online Judge 2616

SELECT
	c.id,
	c.name
FROM customers c
WHERE c.id NOT IN (
	SELECT id_customers FROM locations
)