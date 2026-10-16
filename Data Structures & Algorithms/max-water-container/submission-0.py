class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        maxi = 0
        curr = 0

        while(l<r):
            curr = min(nums[l],nums[r])*(r-l)
            maxi = max(maxi,curr)
            if nums[r]>nums[l]:
                l+=1
            else:
                r-=1
            
        return maxi