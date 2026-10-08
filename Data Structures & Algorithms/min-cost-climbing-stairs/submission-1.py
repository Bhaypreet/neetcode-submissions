class Solution:
    def f(self,cost,dp,i):
        if i > len(cost)-1:
            return 0
        if dp[i] == -1 :
            dp[i] = cost[i]+min(self.f(cost,dp,i+1),self.f(cost,dp,i+2))
        return dp[i]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp= [-1 for _ in range(len(cost))]
        return min(self.f(cost,dp,0),self.f(cost,dp,1))