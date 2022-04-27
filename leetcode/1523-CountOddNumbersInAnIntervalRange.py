# Question Link- https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
	def countOdds(self, low, high):
		# Shoutout to- https://www.goodtecher.com/leetcode-1523-count-odd-numbers-in-an-interval-range/ (much faster solution than my base)
		# 3 Scenario Method (low is odd, high is odd, etc.)
		if low % 2 != 0:
			if high %2 != 0:
				return (high-low) // 2 + 1
			else:
				return (high-low) // 2 + 1
		else:
			if high % 2 != 0:
				return (high-low) // 2 + 1
			else:
				return (high-low) // 2 





# Driver Code
low, high = 8, 10

s = Solution()
output = s.countOdds(low, high)

print(output)
