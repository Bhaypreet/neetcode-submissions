class Solution:
    def f(self,i,target,dp):
        if target == 0:
            return 1
        if target < 0 or i > target:
            return 0

        if dp[i][target] != -1:
            return dp[i][target]

        take = self.f(i,target-i,dp)*i
        notake = self.f(i+1,target,dp)
        dp[i][target] = max(take,notake)

        return dp[i][target]


    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.f(1,n,dp)