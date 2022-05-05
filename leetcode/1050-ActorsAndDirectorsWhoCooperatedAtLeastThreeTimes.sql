-- Question Link- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/




-- Reasonably Fast solution, count instances of grouped rows 
SELECT actor_id, director_id 
FROM ActorDirector
GROUP BY actor_id, director_id 
	HAVING COUNT(*) > 2 



