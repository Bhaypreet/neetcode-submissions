class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def f(i, buy):
            if i >= n:
                return 0

            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy:
                # Buy or skip
                take = -prices[i] + f(i + 1, 0)
                not_take = f(i + 1, 1)
                dp[i][buy] = max(take, not_take)

            else:
                # Sell and skip one day, or keep holding
                take = prices[i] + f(i + 2, 1)
                not_take = f(i + 1, 0)
                dp[i][buy] = max(take, not_take)

            return dp[i][buy]

        return f(0, 1)