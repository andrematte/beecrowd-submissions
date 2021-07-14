-- URI Online Judge 2737 

(

SELECT name, customers_number
FROM lawyers
WHERE customers_number = (SELECT MAX(customers_number) FROM lawyers)
   OR customers_number = (SELECT MIN(customers_number) FROM lawyers)
ORDER BY customers_number DESC

)
UNION ALL
(

SELECT 
  'Average' AS name, 
  ROUND(AVG(customers_number), 0) AS customers_number
FROM lawyers

)