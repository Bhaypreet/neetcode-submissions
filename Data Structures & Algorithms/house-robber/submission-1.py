class Solution:
    def f(self,nums,i,dp):
        if i >= len(nums):
            return 0
        if dp[i] != -1:
            return dp[i]
        pick = self.f(nums,i+2,dp)+nums[i]
        
        notpick = self.f(nums,i+1,dp)

        dp[i] = max(pick,notpick)

        return dp[i]

    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        return self.f(nums,0,dp)