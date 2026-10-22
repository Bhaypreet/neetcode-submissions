class Solution:
    def f(self,word1,word2,l,r,dp):
        if l < 0:
            return r+1

        if r < 0 :
            return l+1

        if dp[l][r] != -1:
            return dp[l][r]

        
        if word1[l] != word2[r]:
            ins = self.f(word1,word2,l,r-1,dp)+1
            de = self.f(word1,word2,l-1,r,dp)+1
            rep = self.f(word1,word2,l-1,r-1,dp)+1

            dp[l][r] = min(ins,de,rep)
        else:
            dp[l][r] = self.f(word1,word2,l-1,r-1,dp)

        return dp[l][r]

    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        return self.f(word1,word2,len(word1)-1,len(word2)-1,dp)