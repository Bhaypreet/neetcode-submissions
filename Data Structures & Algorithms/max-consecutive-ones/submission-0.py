class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = 0
            else:
                ans+=1
                maxi = max(maxi,ans)

        return maxi