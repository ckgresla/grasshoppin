class Solution(object):
        def strStr(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """

            #If the needle is in the haystack, return its index
            if needle in haystack:
                return haystack.index(needle)

            #If not, return -1
            if needle not in haystack:
                return -1

            #If there is no needle (len == 0), return 0
            if len(needle) == 0:
                return 0





# Test Vars & Func Call
test_stack = "hello"
test_needle = "ll"

s = Solution()
print(s.strStr(test_stack, test_needle))


