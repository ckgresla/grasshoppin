-- Question Link- https://leetcode.com/problems/second-highest-salary/
-- Great Explanation- https://thecodingbot.com/leetcode-176-second-highest-salary/




-- Offset & Limit Approach (get all salaries, order them and select 2nd item from column)
SELECT (SELECT DISTINCT(Salary) 
		FROM Employee 
		ORDER BY Salary DESC 
		LIMIT 1 OFFSET 1) --skip first entry and cutoff all remaining entries
AS SecondHighestSalary


-- Ignore Highest and Return Max (not as fast as above)
SELECT MAX(Salary) as SecondHighestSalary 
FROM Employee
WHERE Salary <> (SELECT MAX(Salary) as Salary FROM Employee) --get actual max and return where not equal to that value (2nd max)


