class Solution:
    def f(self,triangle,i,j,dp):
        if i >= len(triangle):
            return 0
        
        if dp[i][j] != -10001:
            return dp[i][j]
        
        a = self.f(triangle,i+1,j+1,dp)+triangle[i][j]
        b = self.f(triangle,i+1,j,dp)+triangle[i][j]
        dp[i][j] = min(a,b)
        return dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-10001 for _ in range(len(triangle[-1]))] for _ in range(len(triangle)+1)]
        return self.f(triangle,0,0,dp)