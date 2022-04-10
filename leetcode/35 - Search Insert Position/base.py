"""
This one uses binary search -- a first for me
"""


class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		
		# Binary Search Params
		left = 0 #1st element in array
		right = len(nums) - 1 #up to last element in array (if beyond right side, then return the last element in array)
		
		while left <= right:
			mid = (left + right) // 2 #mid is the middle of the array (rounds down division, for array of len 7, mid will be 3)
			
			# Success Case for finding target
			if nums[mid] == target:
				return mid #index of target if it is in the array
			
			# Left Window Adjustment 
			elif nums[mid] < target:
				left = mid + 1 #reassigned left window to mid plus 1 (has to be greater than current target)
			
			# Right Window Adjustment:
			else: 
				right = mid -1 #cut right hand down, target has to be less than current max value

		# If Target Value is not in array (left is greater than right window)
		return left 



# Driver Code
test_target = 5
test_nums = [1, 2, 3, 4, 5, 6, 7]

sol = Solution()
answer = sol.searchInsert(test_nums, test_target) 

print(answer)
