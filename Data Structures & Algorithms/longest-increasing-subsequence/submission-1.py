class Solution:
    def f(self,nums,i,maxi,dp):
        if i == len(nums):
            return 0
        if dp[i][maxi] != -1:
            return dp[i][maxi] 
        if nums[i] > maxi:
            take = self.f(nums,i+1,nums[i],dp) + 1
            nottake = self.f(nums,i+1,maxi,dp)
            

        else:
            take = 0
            nottake = self.f(nums,i+1,maxi,dp)
            
        dp[i][maxi] = max(take,nottake)   
        return max(take,nottake)


    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for _ in range(2002)] for _ in range(len(nums))]
        return self.f(nums,0,-1001,dp)