class Solution:
    def f(self,coins,target,x,i,dp):
        if x == target:
            return 1
        if i >= len(coins) or x > target:
            return 0
        if dp[i][x] != -1:
            return dp[i][x] 
        take = self.f(coins,target,x+coins[i],i,dp)
        nottake = self.f(coins,target,x,i+1,dp)
        dp[i][x] = take+nottake
        return dp[i][x] 

    def change(self, amount: int, coins: List[int]) -> int:


        dp = [[-1 for _ in range(amount)] for _ in range(len(coins))]

        a = self.f(coins,amount,0,0,dp)
        return a