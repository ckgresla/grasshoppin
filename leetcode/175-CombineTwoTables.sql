-- Question Link: https://leetcode.com/problems/combine-two-tables/



-- 1st Attempt
SELECT firstName, lastName, city, state 
FROM Person as p

LEFT JOIN Address as a

ON p.personId=a.personId



-- 2nd Method
SELECT P.firstName, P.lastName, P.city, P.state
FROM Person AS P LEFT OUTER JOIN Address as A
	ON (P.personID=A.personID)


