/*Original Problem- https://leetcode.com/problems/group-sold-products-by-the-date/ */ 

SELECT sell_date, count(DISTINCT product) as num_sold, group_concat(DISTINCT product) as products
FROM Activities
GROUP BY sell_date 
ORDER BY sell_date

