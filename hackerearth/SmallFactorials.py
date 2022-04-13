'''
Question Link– https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/small-factorials/


# Problem
You are asked to calculate factorials of some small positive integers.

# Input
An integer T, denoting the number of testcases, followed by T lines, each containing a single integer N.

# Output
For each integer N given at input, output a single line the value of N!


# Input Constraint

1 <= T <= 100
1 <= N <= 100
'''

# Write your code here -- 1st attemp 
# T = int(input())

# for j in range(T):
#     N = int(T())
#     res = 1
#     for i in range(1, N+1):
#         res *= i



# Solution Provided
Ts = int(input())
for t in range(Ts):
    N = int(input())
    factorial = 1 #init
    for i in range(1, N+1): #N+1 to make inclusive of last element in factorial chain
        factorial *= i
    print(factorial)
