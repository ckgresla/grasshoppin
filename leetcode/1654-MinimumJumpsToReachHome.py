# Question Link- https://leetcode.com/problems/minimum-jumps-to-reach-home/




# 
from collections import deque #not needed in leetcode but referencing for func call below

class Solution:
	def minimumJumps(self, forbidden, a, b, x):
		visited = set()
		q = deque(([0, 0])) #effectively a list wherein you can add or remove (pop) values from the left or right "side" of array
		forbidden = set(forbidden) #get atomic list of vals in case dupes
		furthest = max(x, max(forbidden)) + a + b #for edge cases?

		res = 0 #item to return, number of steps to reach home for Bug

		while q: 
			n = len(q)
			for _ in range(n):
				p, is_back = q.popleft()
				
				# 
				if p in forbidden or (p, is_back) in visited or p<0 or p>furthest:
					continue
				# Made it Home Case 
				if p == x:
					return res 

				# if not home, document journey
				visited.add((p, is_back))
				q.append((p+a, 0))
				if not is_back:
					q.append((p-b, 1))

			res += 1 #add one step to return item if made additional jump
		return -1 # if getting home not feasible (loop terminates) 



