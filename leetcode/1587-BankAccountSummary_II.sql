-- Question Link- https://leetcode.com/problems/bank-account-summary-ii/




-- Join on account number, group by the name and return rows that have more than min required balance
SELECT U.name, SUM(T.amount) AS balance
FROM Users U, Transactions T
WHERE U.account = T.account
GROUP BY U.name
HAVING SUM(T.amount) > 10000

