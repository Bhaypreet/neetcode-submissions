class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi1 = 0
        maxi2 = 0
        ans = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                ans+=1
            else:
                maxi1 = max(maxi1,ans)
                ans = 1
        maxi1 = max(maxi1,ans)

        ans = 1

        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                ans+=1
            else:
                maxi2 = max(maxi2,ans)
                ans = 1
        maxi2 = max(maxi2,ans)

        return max(maxi1,maxi2)
        
        