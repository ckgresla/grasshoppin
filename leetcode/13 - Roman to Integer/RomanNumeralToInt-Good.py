class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        This method loops through the input roman numeral string in reverse, the idea behind this
        being that any value that comes AFTER a value in the REVERSED string needs to be larger than 5 in ans
        (min count interval & current answer) or it is representing a subtraction operation
        """
        # Variables
        roman_nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0

        for i in range(len(s)-1, -1, -1):
            num = roman_nums[s[i]] #iterate through x in reverse, lookup current value in dict
            if 4 * num < ans: ans -= num #if we are doing an "IV" like op (4 in roman nums), subtract!
                                         #above line checks if next val is less than 5 (min increment other than 1) & if so it subtracts next value
            else: ans += num
        return ans




# Test Variable & Func Output
s = "DXXIV"
sol = Solution()
#print(sol.romanToInt(s))
print(s, "in Roman Numerals is:", sol.romanToInt(s))
