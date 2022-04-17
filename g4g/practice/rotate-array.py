# Question Link- https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/?page=3&sortBy=submissions


class Solution:

	
	# Temp Array Method -- not really space or time efficient for this but good to keep in mind 
	def tempRotate(self, A, D, N):
		temp_array = []
		i = 0
		
		while (i < D):
			temp_array.append(A[i]) #append D items from beginning of A to temporary array
			i = i + 1
		
		i = 0
		while (D < N):
			A[i] = A[D]
			i = i + 1
			D += 1 
		A[:] = A[:i] + temp_array #full array is equal to the temp plus shifted original (slice out elements 'i' and on)
		return A 


	# Elegant Solution -- not time efficient! (would likely use in a real-world scenario though)
	def rotateElegant(self, A, D, N):

		# Len of Array shorter than rotate distance
		if D > N:
			R = D % N #result to shift array by
			A[:] = A[R:N] + A[0:R]

		else:
			A[:] = A[D:N] + A[0:D]
		return A


	# Fancy Juggling Method
	def rotateArr(self, A, D, N):
	
		for i in range(gcd(D, N)):
			# Move i-th Number of Blocks
			temp = A[i]
			j = i
	
			while 1:
				k = j + D
				if k >= N:
					k = k - N
				if k == i:
					break
				A[j] = A[k]
				j = k
			A[j] = temp

		return A

#GCD helper Func for Fancy Juggling Method
def gcd(a, b):
	if b == 0:
		return a;
	else:
		return gcd(b, a%b)




# Driver Code
s = Solution()

A = [1, 2, 3, 4, 5]
D = 3
N = len(A) #num of elements in array

rotated = s.rotateArr(A, D, N)
#rotated = s.tempRotate(A, D, N)
print(rotated)

