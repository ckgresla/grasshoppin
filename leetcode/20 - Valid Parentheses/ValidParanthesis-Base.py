class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Using "pop" method in below, this removes an item in list (here just the most current value)
        """
        
        leftSymbols = [] #to hold valid opening characters

        # One Loop for all characters in s
        for c in s:
            if c in ["[", "{", "("]: #check against all possible opening chars
                leftSymbols.append(c) 
            elif c == ")" and len(leftSymbols) != 0 and leftSymbols[-1] == "(":
                leftSymbols.pop()
            elif c == "]" and len(leftSymbols) != 0 and leftSymbols[-1] == "[":
                leftSymbols.pop()
            elif c == "}" and len(leftSymbols) != 0 and leftSymbols[-1] == "{":
                leftSymbols.pop()
            
            else:
                return False

        return leftSymbols == [] #or true in other words & completed


testString = "[]{}"

sol = Solution().isValid(s=testString)
print(sol)