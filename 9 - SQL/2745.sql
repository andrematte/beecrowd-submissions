-- URI Online Judge 2745

SELECT name, round(people.salary * 0.1, 2) AS "tax"
FROM people
WHERE salary > 3000
