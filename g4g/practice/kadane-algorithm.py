# Kadane's Algorithm (Dynamic Programming)- https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1/?page=1&sortBy=submissions


# Sample Solution- https://favtutor.com/blogs/kadanes-algorithm-python
# Better Solution- https://martin-thoma.com/maximum-subarray-sum/




class Solution:
    # Will not run, issue with tabs & spaces (underlying algos are good, can run in browser)
    #Function to find the sum of contiguous subarray with maximum sum.

    def SubOptimal_maxSubArraySum(self,arr,N):
		#despite being suboptimal, this solution does not use built-in Python Functions (and is a more generalizable?)

		global_max = arr[0] #max sub-array for all seen thus far (need specify as effectively negative inf, if all nums in array are neg then algorithm will not return the best sum (will just return the first element which may be sub-optimal if using "arr[0]" as init for `global_max`)
		max_ending = 0 #for tracking sub-optimal sub-array's & updating global max

		# Iter through range of array (need find the index position?)
		for i in range(0, N):
			max_ending = max_ending + arr[i] #sub-array sums

			if max_ending < 0:
				max_ending = 0 #sub-optimal array? reset if max falls below negative value!
			elif (global_max < max_ending):
				global_max = max_ending #reassign global max if the current(global) one is sub-optimal (as compared to current max_ending)
		return global_max

    def maxSubArraySum(self,arr,N): #better version, follow 2nd link's idea
		global_max = float("-inf") #handles all negatives case! (1st one gets caught on best val being last negative in list of all negatives)	
		current_sum = 0 #initial val
		
		for num in arr:
			current_sum = max(num, current_sum+num) #if negative sum
			global_max = max(current_sum, global_max)
		return global_max



#  Driver Code Starts
import math
 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# End Driver Code

