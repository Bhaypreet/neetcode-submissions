class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        l = 0
        sum = 0

        for r in range(len(nums)):
            sum +=nums[r]
            while(sum >= target):
                sum-=nums[l]
                mini = min(mini,r-l+1)
                l+=1
            

        if mini == float('inf'):
            return 0
        return mini