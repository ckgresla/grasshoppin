class Solution(object):
        def strStr(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """

            # No Haystack Case
            if len(haystack) == 0:
                return 0 #no haystack to search for
            else:
                for i in haystack:
                    # Check if first needle val is found
                    if i == needle[0]:
                        for j in needle:







# Test Vars & Func Call
test_stack = "hello"
test_needle = "ll"

s = Solution()
print(s.strStr(test_stack, test_needle))


