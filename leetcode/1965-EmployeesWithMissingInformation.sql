-- Question Link- https://leetcode.com/problems/employees-with-missing-information/




-- Solved using a Union SubQuery, returns  
SELECT employee_id 
FROM (SELECT employee_id FROM Employees 
     UNION ALL
     SELECT employee_id FROM Salaries) temp
GROUP BY 1 
HAVING COUNT(*) = 1
ORDER BY 1 


-- Solved with "Set Theory" (not as fast as above, makes multiple subqueries)
SELECT employee_id FROM Employees
WHERE employee_id NOT IN 
	(SELECT employee_id FROM Salaries)
UNION 
SELECT employee_id FROM Salaries
WHERE employee_id NOT IN 
	(SELECT employee_id FROM Employees)
ORDER BY employee_id ASC 



