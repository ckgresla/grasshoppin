# Two Sum -- https://leetcode.com/problems/two-sum/
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


This solution (as explained in this YouTube video- https://www.youtube.com/watch?v=KLlXCFG5TnA&t=418s&ab_channel=NeetCode) goes over a one-pass solution for the two_sum problem, the one-pass is feasible for this as we just need to find one solution (not all possible sets of solutions) for the target value.

We accomplish this with a hash map of each value that we see (in the one pass) wherein each value is stored like this
value : index
We then will check each new value in the "nums" list to see what the difference is from our target variable to it (we just need add the difference to our current value to get the target!) if the difference is stored as a value in our hash map, then we just return the index for the difference value along with the index of the current value that we are checking!

"""

class Solution(object):
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            h_map = {} #value : index -- what we will be iteratively adding to

            for i, n in enumerate(nums): #elegant way of iter-ing through our input list & easily getting indexes
                difference = target - n

                # If Difference in Hash Map
                if difference in h_map:
                    return [i, h_map[difference]]

                # If Difference not in the Hash Map -- Update the current value to it!
                h_map[n] = i



num = [2,7,11,15]
target = 9

s = Solution()
print(s.twoSum(num,target))




