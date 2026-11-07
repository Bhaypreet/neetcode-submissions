class Solution:
    def f(self,n,k,target,dp):
        if target == 0 and n == 0:
            return 1
        if target < 0 or n == 0 :
            return 0
        
        if dp[n][target] != -1:
            return dp[n][target]

        ans = 0
        
        for i in range(1,k+1):
            ans+=self.f(n-1,k,target-i,dp)
            dp[n][target] = ans%1000000007
        
        return dp[n][target]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n*k < target:
            return 0
        if n*k == target:
            return 1
        dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
        
        return self.f(n,k,target,dp)

