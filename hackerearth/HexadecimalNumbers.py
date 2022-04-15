"""
Question Link- https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/yet-another-easy-problem-1f3273a0/

"""



# Write your code here
import math 

def convertHexDec(n): 
    total = 0
    for i in hex(n).lstrip("0x").rstrip("L"):
        total += int(i, 16) #base 16 for hexadecimal nums

    return total

T = int(input()) #read `T` input

for _ in range(T):
    L, R = input().split()
    count = 0 

    # Read Specified range of vals
    for i in range(int(L), int(R)+1): 
        # Find num of ints (count of them) such that (follows math constraint in question)
        if math.gcd(i, convertHexDec(i)) > 1:
            count+=1 
    print(count) #write to standard out



