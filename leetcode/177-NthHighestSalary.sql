-- Question Link- https://leetcode.com/problems/nth-highest-salary/
-- Explanation- https://thecodingbot.com/leetcode-177-nth-highest-salary/




-- Sample Solution (need write an SQL Function)
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT 
BEGIN 
	DECLARE M INT; 

	SET M = N - 1;
	RETURN ( 
	SELECT DISTINCT(salary) 
	FROM Employee
	ORDER BY Salary DESC 
		LIMIT 1 OFFSET M 
	); 
END 




