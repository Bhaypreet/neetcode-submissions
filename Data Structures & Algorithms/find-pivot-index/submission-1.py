class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):

            if i == 0 :
                if sum(nums[1:]) == 0 :
                    return 0
            elif i == len(nums)-1 :
                if sum(nums)-nums[-1] == 0:
                    return i

            elif sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1