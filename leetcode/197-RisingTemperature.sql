-- Question Link- https://leetcode.com/problems/rising-temperature/




-- Comparision of Two Tables to create notion of "yesterday", then compare yest against today- https://youtu.be/09wjf87VRs0
SELECT w2.id 
FROM Weather w1 JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = -1
WHERE w2.temperature > w1.temperature

