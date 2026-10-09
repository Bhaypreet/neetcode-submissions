class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    ans = [i,j]
                    
        return ans 