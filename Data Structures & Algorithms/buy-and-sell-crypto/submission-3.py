
class Solution:
    def f(self, nums, i, a, dp):
        if i >= len(nums):
            return 0

        if dp[i][a] != -1:
            return dp[i][a]

        if a == 0:
            buy = self.f(nums, i + 1, 1, dp) - nums[i]
            buyn = self.f(nums, i + 1, 0, dp)
            dp[i][a] = max(buy, buyn)
        else:
            sell = nums[i]
            nsell = self.f(nums, i + 1, 1, dp)
            dp[i][a] = max(sell, nsell)

        return dp[i][a]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 2 for _ in range(len(prices))]
        return self.f(prices, 0, 0, dp)
