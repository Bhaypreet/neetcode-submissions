class Solution:
    def f(self,n,k,target,dp):
        if target == 0 and n == 0:
            return 1
        if n == 0 :
            return 0

        if dp[n][target] != -1:
            return dp[n][target]
        a = 0
        for i in range(1,k+1):
            a+=self.f(n-1,k,target-i,dp)
            dp[n][target] = a
        
        return dp[n][target]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n > target or n*k < target:
            return 0

        dp = [[-1 for _ in range(1001)] for _ in range(31)]
        return self.f(n,k,target,dp)%(1000000007)