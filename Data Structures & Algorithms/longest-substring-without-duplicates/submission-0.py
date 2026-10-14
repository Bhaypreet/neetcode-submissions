class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        maxi = 0
        l = 0
        r = 0

        st = ""

        while(r < len(s)):
            if s[r] not in st:
                st+=s[r]
                r+=1
                maxi = max(maxi,len(st))
            else:
                st= st[1:]
                l+=1
        return maxi