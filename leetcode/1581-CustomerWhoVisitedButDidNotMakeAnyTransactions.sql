-- Question Link- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/




-- Base
SELECT DISTINCT customer_id, count(*) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id 


