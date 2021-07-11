-- URI Online Judge 2622

SELECT customers.name
FROM customers
RIGHT JOIN legal_person
ON customers.id = legal_person.id_customers