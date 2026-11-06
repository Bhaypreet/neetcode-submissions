class Solution:
    def f(self,nums,i,j,dp):
        if i >= j:
            return 0

        if dp[i] != -1:
            return dp[i]

        take = self.f(nums,i+2,j,dp)+nums[i]
        nottake = self.f(nums,i+1,j,dp)
        dp[i] = max(take,nottake)

        return dp[i]


    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        l = len(nums)
        dp1 = [-1 for _ in range(l)]
        dp2 = [-1 for _ in range(l)]
        
        return max(self.f(nums,0,l-1,dp1),self.f(nums,1,l,dp2))