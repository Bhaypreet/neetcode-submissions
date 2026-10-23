class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0
        r = 0
        while(l < len(s)):
            if r == len(t):
                return 0

            if s[l] == t[r] :
                l+=1
                r+=1
            else:
                l+=1

        return len(t)-r
