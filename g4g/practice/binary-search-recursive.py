
"""
Original Post- https://www.geeksforgeeks.org/binary-search/
Practice Page- https://practice.geeksforgeeks.org/problems/binary-search/1

This is a recursive implementation of Binary Search, akin to the LeetCode Find Index problem (did an iterative version for that)
"""


def binarysearch_recursive(array, left, right, target):
	if right >= left:
		mid = left + (right - left) // 2 
		
		if array[mid] == target:
			return mid

		elif array[mid] > target: 
			return binarysearch_recursive(array, left, mid-1, target)

		else: 
			return binarysearch_recursive(array, mid+1, right, target)

	else:
		return -1 #if element is not in the array



# Driver Code
a = [1, 3, 5, 6, 12, 16, 25]
x = 12

answer = binarysearch_recursive(a, 0, len(a)-1, x)

if answer != -1:
	print(answer)
else:
	print("item not in array")
