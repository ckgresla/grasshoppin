-- Question Link- https://leetcode.com/problems/game-play-analysis-i/




-- Using MIN of dates for first item, group by eliminates multi-login IDs when combined w Aggregate
SELECT player_id, MIN(event_date) AS first_login
FROM Activity 
GROUP BY player_id


