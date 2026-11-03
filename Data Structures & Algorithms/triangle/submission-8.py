class Solution:
    def f(self,triangle,i,j,dp):
        if i >= len(triangle):
            return 0

        if dp[i][j] != -10001:
            return dp[i][j]

        down = self.f(triangle,i+1,j,dp)+triangle[i][j]
        diag = self.f(triangle,i+1,j+1,dp)+triangle[i][j]
        dp[i][j] = min(down,diag)

        return dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [[-10001 for _ in range(n)] for _ in range(len(triangle))]
        
        return self.f(triangle,0,0,dp)