class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = 0
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1] :
                ans+=nums[i]
            else:
                maxi = max(maxi,ans)
                ans = nums[i]

        return max(maxi,ans)