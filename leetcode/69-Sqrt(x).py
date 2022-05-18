# Question Link- https://leetcode.com/problems/sqrtx/




# Binary Tree Solution, not the fastest but kinda cool 
class Solution:
	def mySqrt(x): #x is always an + int -- should return an int (even if answer is decimal, truncate it)
		
		# Edge Case First
		if x==0 or x==1:
			return x #square root of 0 is undefined and sqrt(1)=1
		
		# Fun Stuff w Binary Tree style search
		left = 0
		right = x #upper bounds on a square root operation, definitely will be smaller 
		
		while left <= right:
			mid = (left+right)//2
			if mid**2 == x:
				return int(mid)

			# When Current Mid not the sqrt
			elif mid**2 < x:
				left = mid+1 
			else:
				right = mid-1
		return int(right) #will settle to sqrt(x)
					 	  #returns int with decimals sliced off (doesn't round up, what question wants)


