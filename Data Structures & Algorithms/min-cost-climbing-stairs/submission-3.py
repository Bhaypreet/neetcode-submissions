class Solution:
    def f(self,cost,i,dp):
        if i >= len(cost):
            return 0
        if i == len(cost)-1:
            return cost[i]

        if dp[i] != -1:
            return dp[i]

        take = self.f(cost,i+1,dp)+cost[i]
        takee = self.f(cost,i+2,dp)+cost[i]

        dp[i] = min(take,takee)

        return dp[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = [-1 for _ in range(len(cost))]
        dp2 = [-1 for _ in range(len(cost))]
        return min(self.f(cost,0,dp1),self.f(cost,1,dp2))