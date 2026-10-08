class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in range(len(s)):
            if s[i].isalnum():
                ans+=s[i]

        ans = ans.lower()
        
        l = 0
        r = len(ans)-1
        while(l<=r):
            if ans[l] != ans[r] :
                return False
            l+=1
            r-=1
        return True