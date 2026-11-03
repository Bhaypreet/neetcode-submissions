class Solution:
    def f(self,coins,amount,i,dp):
        if amount == 0:
            return 0
        if i >= len(coins) or amount < 0:
            return float('inf')
        
        if dp[i][amount] != -1:
            return dp[i][amount]
        
        a = 1+self.f(coins,amount-coins[i],i,dp)
        b = self.f(coins,amount,i+1,dp)
        
        dp[i][amount] = min(a,b)
  
        return dp[i][amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        a = self.f(coins,amount,0,dp)
        if a != float('inf'):
            return a
        return -1