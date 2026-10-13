class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxp = 0
        i = 0
        j = 1
        
        
        while(j < len(nums)):
            profit = nums[j]-nums[i]
            maxp = max(maxp,profit)
            if nums[j]<nums[i]:
                i = j
            j+=1
        
        return maxp
            
