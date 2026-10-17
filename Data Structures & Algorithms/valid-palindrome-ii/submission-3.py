class Solution:
    def check(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        if len(s) == 1 :
            return True

        while(l<=r):
            if s[l] != s[r]:
                return (self.check(s,l+1,r) or self.check(s,l,r-1))

            l+=1
            r-=1
        return True
         
