class Solution(object):
        def strStr(self, haystack, needle):
            """
            :type haystack: str
            :type needle: str
            :rtype: int
            """

            # Init Vars
            i = 0
            j = 0
            m = len(needle)
            n = len(haystack)

            # No Needle Case
            if m == 0:
                return 0 #nothing to search for

            while i<n and n-i+1>=m:
                if haystack[i] == needle[j]:
                    temp = i #need iter to check haystack for needle

                    while j<m and i<n and needle[j] == haystack[i]:
                        i += 1
                        j += 1
                    if j == m:
                        return temp
                    i = temp + 1
                    j = 0
                else:
                    i += 1
            return -1




# Test Vars & Func Call
test_stack = "hello"
test_needle = "ll"

s = Solution()
print(s.strStr(test_stack, test_needle))


