class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool -- true or false depending on if int is a palindrome

        Because the question only asks about a number, we need not care about capitalization of String values!
          if this was a word based version, it could be problematic as the capitalization technically changes the word!
        """
        # Leverage Python's built in String Inverse func
        x = str(x)

        # Check if Palindrome
        if x[::-1] == x:
            return True
        else:
            return False



# Call Function for Example Solution
x = "Madam"



s = Solution()
print(s.isPalindrome(x))



