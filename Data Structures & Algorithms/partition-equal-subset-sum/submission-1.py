class Solution:
    def f(self,i,nums,ans,target,dp):
        if ans == target:
            return True

        if i == len(nums):
            return False

        if dp[i][ans] != -1:
            return dp[i][ans]
        
        take = self.f(i+1,nums,ans+nums[i],target,dp)     
        nottake = self.f(i+1,nums,ans,target,dp)

        dp[i][ans] = take or nottake

        return dp[i][ans]

    def canPartition(self, nums: List[int]) -> bool:

        dp = [[-1 for _ in range(sum(nums))] for _ in range(len(nums))]

        a = sum(nums)
        if a%2 ==1 :
            return False
        target = a//2

        return self.f(0,nums,0,target,dp)
