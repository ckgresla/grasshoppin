-- Question Link- https://leetcode.com/problems/find-followers-count/




-- Wrote from scratch, feels good to not remain an absolute nincompoop
SELECT DISTINCT user_id as user_id, COUNT(DISTINCT(follower_id)) AS followers_count
FROM Followers
GROUP BY user_id 

