-- Question Link- https://leetcode.com/problems/duplicate-emails/




-- Window Partition Method
WITH DupeEmails AS (
    SELECT DISTINCT email, COUNT(email) OVER (PARTITION BY email) AS duplicate_count
    FROM Person)

SELECT email 
FROM DupeEmails
WHERE duplicate_count > 1 

