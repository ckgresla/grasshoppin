class Solution(object):
        def removeElement(self, nums, val):
            """
            :type nums: List[int]
            :type val: int
            :rtype: int
            """

            count = 0

            # Using a Counter (to filter the list effectively)
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[count] = nums[i]
                    count +=1 #add 1 index pos for new list, swapping out vals in place if not the VAL?

            return count




# Test Case
test_nums = [3,2,2,3]
test_val = 3

test_nums = [0,1,2,2,3,0,4,2]
test_val = 2

s = Solution()
print(s.removeElement(test_nums, test_val))





