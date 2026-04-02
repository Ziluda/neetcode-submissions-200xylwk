class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # populate each hashmap first
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # check if each hashmap has the same key and counts
        for x in countS:
            if countS[x] != countT.get(x, 0):
                return False
        
        return True

        

