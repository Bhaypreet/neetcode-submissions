class Solution:
    def f(self,coins,amt,target,i,dp):
        if amt == target:
            return 0
        if amt > target or i >= len(coins):
            return float("inf")
        
        if dp[i][amt] != -1:
            return dp[i][amt]

        take = self.f(coins,amt+coins[i],target,i,dp)+1
        nottake = self.f(coins,amt,target,i+1,dp)
        dp[i][amt] = min(take,nottake)
        return dp[i][amt]

    def coinChange(self, coins: List[int], amount: int) -> int:

        maxa = sum(coins)

        dp = [[-1 for _ in range(amount)] for _ in range(len(coins)+1)]


        a =  self.f(coins,0,amount,0,dp)
        if a!= float("inf"):
            return a
        return -1