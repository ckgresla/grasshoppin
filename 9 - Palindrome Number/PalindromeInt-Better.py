class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool -- true or false depending on if int is a palindrome

        Referenced this post- https://redquark.org/leetcode/0009-palindrome-number/

        """

        # If x less than zero, not Palindrome due to negative sign!
        if x < 0:
            return False


        num = x #will check reverse of x by transforming num
        reverse = 0 #also need store reverse of val

        while num:
            reverse = reverse * 10 + num % 10 #actually gangster as fuck
            num //= 10 #floor division, returns an int with the remaining float values stripped off (less accurate but needed here)
        return x == reverse


# Call Function for Example Solution
x = 121



s = Solution()
print(s.isPalindrome(x))



