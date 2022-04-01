class Solution(object):

    # CKG Defined Func to get CPs for 2 strs
    def commonPrefixes(self, s1, s2):
        
        result = ""
        n1 = len(s1)
        n2 = len(s2)

        # Compare the two iteratively
        i = 0
        j = 0
        while i <= n1-1 and j <= n2-1:
            if (s1[i] != s2[j]):
                break
            
            result += s1[i]
            i += 1
            j += 1

        return (result)


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        This is a slower algorithm (many checks and loops) but is memory efficient? 
        """

        prefix = strs[0]

        for i in range(1, len(strs)):
            prefix = Solution.commonPrefixes(self, prefix, strs[i])
        return (prefix)
    
    




# Test Var & Function Call
strings_to_eval = ["flower", "flow", "flight"]

s = Solution()
s.longestCommonPrefix(strings_to_eval)




# Testing the util function
print(s.longestCommonPrefix(strings_to_eval))
# print(s.commonPrefixes(strings_to_eval[0], strings_to_eval[2]))

