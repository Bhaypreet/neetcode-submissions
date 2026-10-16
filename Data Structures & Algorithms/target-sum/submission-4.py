class Solution:
    def f(self,nums,target,i,ans,dp):
        if i == len(nums):
            if ans == target:
                return 1
            else:
                return 0
        if dp[i][ans] != -1:
            return dp[i][ans]

        plus = self.f(nums,target,i+1,ans+nums[i],dp)
        minus = self.f(nums,target,i+1,ans-nums[i],dp)
        dp[i][ans] = plus+minus
        return dp[i][ans]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[-1 for _ in range(2*sum(nums)+1)] for _ in range(len(nums))]
        return self.f(nums,target,0,0,dp)