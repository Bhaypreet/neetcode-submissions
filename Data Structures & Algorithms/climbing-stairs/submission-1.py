class Solution:
    # def f(self,n,dp,i):
    #     if i == n-2:
    #         dp[i] == 1
    #         return 

        






    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        if n == 1:
            return 1
        dp[0] = 1
        dp[1] = 2

        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n-1] 