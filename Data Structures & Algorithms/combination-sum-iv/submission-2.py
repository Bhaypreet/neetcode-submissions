class Solution:
    def f(self,nums,target,dp):
        if target == 0:
            return 1
        if target < 0 :
            return 0
        if dp[target] != -1:
            return dp[target] 
        
        ways = 0

        for i in range(len(nums)):
            ways+=self.f(nums,target-nums[i],dp)
        dp[target] = ways
        return dp[target]



    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1 for _ in range(target+1)]
        return self.f(nums,target,dp)