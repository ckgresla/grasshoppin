-- Question Link- https://leetcode.com/problems/find-total-time-spent-by-each-employee/




-- 
SELECT DISTINCT event_day AS DAY, emp_id, SUM(out_time) - SUM(in_time) AS total_time
FROM Employees
GROUP BY day, emp_id



