class Solution:
    def f(self,prices,i,sts,dp):
        if i >= len(prices):
            return 0

        if dp[i][sts] != -1:
            return dp[i][sts]

        if sts == 0:
            take = self.f(prices,i+1,1,dp)-prices[i]
            nottake = self.f(prices,i+1,0,dp)
            dp[i][sts] = max(take,nottake)
            return dp[i][sts]
        
        else:

            s = self.f(prices,i+1,0,dp)+prices[i]
            ns = self.f(prices,i+1,1,dp)
            dp[i][sts] = max(s,ns)
            return dp[i][sts]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for _ in range(len(prices))]
        return self.f(prices,0,0,dp)