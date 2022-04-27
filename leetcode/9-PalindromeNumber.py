class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool -- true or false depending on if int is a palindrome

        Referenced this post- https://redquark.org/leetcode/0009-palindrome-number/

        The below algorithm is half the time of the other "Better" solution, it also uses a constant space complexity?
        """

        # If x is a negative number, not a palindrome (due to sign!)
        # If x % 10 = 0, the first digit needs to also be zero (not feasible for how Ningen write numbers)
        if x < 0 or (x % 10 == 0):
            return False

        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return True if (x == reverse or x == reverse // 10) else False









# Call Function for Example Solution
x = 121



s = Solution()
print(s.isPalindrome(x))



