class Solution:
    def f(self,nums,target,dp):

        if target == 0:
            return 1
        if target < 0 :
            return 0
        
        if dp[target] != -1:
            return dp[target]
        
        ans = 0
        for j in range(len(nums)):
            ans+=self.f(nums,target-nums[j],dp)
            dp[target] = ans
        return dp[target]
                
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1 for _ in range(target+1)]
        return self.f(nums,target,dp)