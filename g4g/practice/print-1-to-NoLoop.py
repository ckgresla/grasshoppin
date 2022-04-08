"""
This is an interesting one, to print each value from 1 to N (without a for loop) we recursively call the funciton with decreasing values of N (n-1 per recursive call) to work our way back to 0, printing values of each recursive call all the way back up to 'N' 
"""



class Solution:
	def printN(self, N):
		if N > 0:
			Solution().printN(N-1)
			print(N, end=" ")




Solution().printN(N=10)
