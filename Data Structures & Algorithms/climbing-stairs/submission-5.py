class Solution:
    def f(self,n,dp,i):
        if n <= 2:
            return n
        if dp[i] == -1:
            dp[i] = self.f(n,dp,i-1)+ self.f(n,dp,i-2)
        return dp[i]        


    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n)]
        if n == 1:
            return 1
        dp[0] = 1
        dp[1] = 2
        
        self.f(n,dp,n-1) 
        return dp[n-1]