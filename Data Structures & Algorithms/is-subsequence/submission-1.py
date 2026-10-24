class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        l = 0
        r = 0
        while(r < len(t)):
            if s[l] == t[r]:
                l+=1
                r+=1
            else:
                r+=1
            if l == len(s):
                return True
        return False