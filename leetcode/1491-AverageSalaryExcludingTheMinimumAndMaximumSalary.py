# Question Link- https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/


class Solution:
	def average(self, salary):
		
		# First LeetCode w/o needing to lookup an answer! Maybe we aren't COMPLETELY brain dead!
		n, s, mi, ma = 0, 0, min(salary), max(salary)
		
		for i in salary:
			if i == mi:
				continue
			elif i == ma:
				continue
			else:
				n += 1
				s += i

		return s/n 





# Driver Code


	
