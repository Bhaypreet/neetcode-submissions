class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        maxi = 0
        cnt = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                cnt+=1
            elif nums[i+1] == nums[i]:
                continue
            else:
                maxi = max(maxi,cnt)
                cnt = 1
        maxi = max(maxi,cnt)
        return maxi