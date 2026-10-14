class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        l = 0
        mpp = {}
        ans = 0

        for r in range(len(s)):
            if s[r] in mpp:
                mpp[s[r]] += 1
            else:
                mpp[s[r]] = 1
            
            maxi = max(mpp.values())


            while r-l+1 - maxi > k :
                mpp[s[l]] -=1
                if mpp[s[l]] == 0:
                    del mpp[s[l]]
                l+=1
                maxi = max(mpp.values())

            ans = max(ans,r-l+1)

        return ans
