class Solution:
    def f(self,s,t,i,j,dp):
        if j >= len(t):
            return 1
        if i >= len(s):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] != t[j]:
            dp[i][j] = self.f(s,t,i+1,j,dp)
        else:
            a = self.f(s,t,i+1,j,dp)
            b = self.f(s,t,i+1,j+1,dp)
            dp[i][j] = a+b
        
        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]
        return self.f(s,t,0,0,dp)