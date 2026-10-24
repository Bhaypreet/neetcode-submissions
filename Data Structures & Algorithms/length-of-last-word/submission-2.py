class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)-1
        while(s[l] == " "):
            l-=1

        for i in range(l,-1,-1):
            if s[i] == " ":
                return l-i

        return l+1