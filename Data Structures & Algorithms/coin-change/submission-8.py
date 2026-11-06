class Solution:
    def f(self,coins,target,i,dp):
        if target == 0:
            return 0
        if target < 0 or i >= len(coins):
            return float('inf')
        
        if dp[i][target] != -1:
            return dp[i][target]
        
        take = self.f(coins,target-coins[i],i,dp) + 1
        nottake = self.f(coins,target,i+1,dp)
        dp[i][target] = min(take,nottake) 

        return dp[i][target]  

    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
        
        a = self.f(coins,amount,0,dp)
        if a == float('inf'):
            return -1
        return a



