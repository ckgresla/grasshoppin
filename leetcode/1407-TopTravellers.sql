-- Question Link- https://leetcode.com/problems/top-travellers/




-- Really slow, make faster?
SELECT U.name, COALESCE(SUM(R.distance), 0) AS travelled_distance
FROM Users U LEFT OUTER JOIN Rides R 
    ON (U.id=R.user_id)
GROUP BY R.user_id
ORDER BY travelled_distance DESC, U.name ASC



