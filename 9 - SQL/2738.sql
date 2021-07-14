-- URI Online Judge 2738

SELECT 
    candidate.name,
	ROUND(((2.0*math) + (3.0*specific) + (5.0*project_plan))/10 ,2) AS avg 
FROM candidate
    JOIN score ON  candidate.id = score.candidate_id
ORDER BY avg DESC