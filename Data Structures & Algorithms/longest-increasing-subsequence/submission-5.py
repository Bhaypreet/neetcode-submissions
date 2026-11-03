class Solution:
    def f(self,nums,prev,i,dp):
        if i == len(nums):
            return 0

        if dp[i][prev] != -1:
            return dp[i][prev]
        
        if nums[i] > prev:
            a = self.f(nums,nums[i],i+1,dp)+1
            b = self.f(nums,prev,i+1,dp)
            dp[i][prev] = max(a,b)
            return dp[i][prev]
        else:
            dp[i][prev] = self.f(nums,prev,i+1,dp)
            return dp[i][prev]

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for _ in range(2002)]for _ in range(len(nums))]
        return self.f(nums,-1001,0,dp)