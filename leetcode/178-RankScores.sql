-- Question Link- https://leetcode.com/problems/rank-scores/




-- Using 'DENSE_RANK' Function- https://www.mysqltutorial.org/mysql-window-functions/mysql-dense_rank-function/
SELECT score, 
    DENSE_RANK() OVER(ORDER BY score DESC) AS "rank"
FROM Scores


