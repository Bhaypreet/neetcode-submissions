class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = (l+r)//2
        nums.sort()

        while(l<=r):
            num = nums[m]
            if num > target:
                r = m-1
                m = (l+r)//2
            elif num < target:
                l = m+1
                m = (l+r)//2
            else:
                return m
        return -1

