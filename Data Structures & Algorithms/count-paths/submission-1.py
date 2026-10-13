class Solution:
    def f(self,m,n,i,j,dp):
        if i < 0 or j < 0 :
            return 0
        if i == 0 and j == 0 :
            return 1

        if dp[i][j] != -1:
            return dp[i][j]
        
        left = self.f(m,n,i,j-1,dp)
        up = self.f(m,n,i-1,j,dp)
        dp[i][j] = left+up
        return dp[i][j]    

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n ==1 :
            return 1


        dp = [[-1 for _ in range(n)] for _ in range(m)]

        self.f(m,n,m-1,n-1,dp)

        return dp[m-1][n-1]