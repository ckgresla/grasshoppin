class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        StackExchange Example- https://codereview.stackexchange.com/questions/216403/in-place-solution-to-remove-duplicates-from-a-sorted-list
        """

        # Base Case
        if len(nums) < 2: return(len(nums))

        # Iteration Case
        i = 0 #slow pointer?
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j] #overwrite?

        return i + 1





# Test Case
test_input = [1, 1, 2]

s = Solution()
print(s.removeDuplicates(test_input))




