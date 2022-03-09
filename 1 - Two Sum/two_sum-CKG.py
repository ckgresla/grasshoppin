# Two Sum -- https://leetcode.com/problems/two-sum/
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            sub_targets = []
            sol = []

            for val_ind in range(0, len(nums)):
                #print(f"Index-{val_ind} Value-{nums[val_ind]}")
                val = nums[val_ind]

                # if val is already larger than target, skip current iter of loop
                if val >= target:
                   continue
                #if val is possible candidate, append to list of lists with mappings to iter through
                elif val < target:
                    sub_targets.append([val, val_ind])

            # Check sub_targets for possible solution
            for lst in sub_targets:
                val_1 = lst[0]
                for lst2 in sub_targets:
                    val_2 = lst2[0]
                    if val_1 == val_2:
                        break
                    elif val_1 + val_2 == target:
                        sol.append([lst[1], lst2[1]])
                        print("Possible Solutions are:", sol)
                        break






# test case
test_list = [2,7,11,15]
test_target = 9


# Run Above
if __name__ == '__main__':
    Solution.twoSum(Solution, nums=test_list, target=test_target)


