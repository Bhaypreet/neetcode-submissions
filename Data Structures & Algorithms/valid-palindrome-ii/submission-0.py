class Solution:
    def f(self,s):
        l = 0
        r = len(s)-1
        while(l<=r):
            if s[l] != s[r] :
                return False
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:

        if len(s) == 1 or self.f(s):
            return True
        
        for i in range(len(s)):
            a = s[:i] + s[i+1:]
            if self.f(a):
                return True

        return False