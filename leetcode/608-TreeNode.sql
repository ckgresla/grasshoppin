-- Question Link- https://leetcode.com/problems/tree-node/




-- 3 Cases: Parent, Leaf or Root 
SELECT id, 
	CASE WHEN p_id IS NULL THEN 'Root' 
		 WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
		 ELSE "Leaf"
	END AS type --name of new column, built from above statements
FROM Tree 


-- Much Faster Version
SELECT id, "Root" AS TYPE 
FROM Tree 
WHERE p_id IS NULL 

UNION

SELECT id, "Inner" as type 
FROM Tree 
WHERE id IN (SELECT p_id FROM Tree WHERE  p_id IS NOT NULL) 
	AND p_id IS NOT NULL 

UNION 

SELECT id, "Leaf" AS type 
FROM Tree
WHERE id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) 
	AND p_id IS NOT NULL 





