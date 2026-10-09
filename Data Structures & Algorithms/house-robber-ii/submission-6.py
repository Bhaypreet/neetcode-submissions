class Solution:
    def f(self,nums,i,j,dp):
        if i >= j:
            return 0
        if dp[i] != -1:
            return dp[i]
        pick = self.f(nums,i+2,j,dp)+nums[i]
        notpick = self.f(nums,i+1,j,dp)

        dp[i] = max(pick,notpick)
        return dp[i]


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp1 = [-1 for _ in range(len(nums))]
        dp2 = [-1 for _ in range(len(nums))]
        return max(self.f(nums,0,n-1,dp1),self.f(nums,1,n,dp2))