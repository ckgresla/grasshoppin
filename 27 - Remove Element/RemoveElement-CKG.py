class Solution(object):
        def removeElement(self, nums, val):
            """
            :type nums: List[int]
            :type val: int
            :rtype: int
            """

            nums = [x for x in nums if x is not val]
            return len(nums), nums





# Test Case
test_nums = [3,2,2,3]
test_val = 3

#test_nums = [0,1,2,2,3,0,4,2]
#test_val = 2

s = Solution()
print(s.removeElement(test_nums, test_val))





