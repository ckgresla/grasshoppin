-- Question Link- https://leetcode.com/problems/market-analysis-i/




-- Pretty slow, but today I am exhausted
SELECT A.user_id AS buyer_id, A.join_date, IFNULL(B.orders_in_2019, 0) AS orders_in_2019
FROM (
    SELECT user_id, join_date
    FROM Users
    ) AS A

LEFT JOIN (
    SELECT buyer_id, COUNT(order_id) AS orders_in_2019
    FROM Orders
    WHERE YEAR(order_date) = 2019
    GROUP BY 1
    ) AS B
    
ON A.user_id = B.buyer_id
