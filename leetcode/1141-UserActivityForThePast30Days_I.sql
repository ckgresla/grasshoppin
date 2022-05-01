-- Question Link- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/




-- 
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
GROUP BY day
	HAVING day > (SELECT SUBDATE("2019-07-27", INTERVAL 30 DAY))

