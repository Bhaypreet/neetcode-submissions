class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            nums[0],nums[1] = nums[1] ,nums[0]
            return nums
        lis1 = []
        lis2 = []

        a = 1
        b = 1
        for i in range(len(nums)):
            a = a*nums[i]
            lis1.append(a)
        for i in range(len(nums)-1,-1,-1):
            b = b*nums[i]
            lis2.append(b)
        lis2.reverse()

        flis = [0]*(len(nums))
        flis[0] = lis2[1]
        flis[len(nums)-1] = lis1[len(nums)-2]
        for i in range(1,len(nums)-1):
            flis[i] = lis1[i-1]*lis2[i+1]

        return flis