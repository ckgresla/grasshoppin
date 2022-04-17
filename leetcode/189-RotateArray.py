# Question Link- https://leetcode.com/problems/rotate-array/



class Solution:

	# Passing Solution
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        i = 0
        count = 0
        while count < n:
            pos = (i + k) % len(nums)
            curr = nums[pos]
            nums[pos] = nums[i]
            count += 1
            j = pos
            while j != i and count < n:
                pos = (j + k) % len(nums)
                nums[pos], curr = curr, nums[pos]
                j = pos
                count += 1
            i += 1

	# Clean Solution, not time efficient (only python as well)
    def elegantRotate(self, a, k):
        a[:] = a[k:] + a[:k]





# Driver Code
array = [1, 2, 3, 4, 5, 6, 7, 8]
k = 2

s = Solution()
#s.elegantRotate(array, k)
s.rotate(array, k)

print(array)
