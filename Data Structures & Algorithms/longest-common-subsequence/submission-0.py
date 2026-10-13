class Solution:
    def f(self,a,b,i,j,dp):
        
        if i >= len(a) or j >= len(b):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if a[i] == b[j]:
            dp[i][j] = 1+self.f(a,b,i+1,j+1,dp)
            return dp[i][j]
        else:
            amove = self.f(a,b,i+1,j,dp)
            bmove = self.f(a,b,i,j+1,dp)
            dp[i][j] = max(amove,bmove)

        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        a = self.f(text1,text2,0,0,dp)
        return a