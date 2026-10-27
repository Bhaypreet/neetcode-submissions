class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(1,len(nums)+1):
            if i not in nums:
                nums.append(i)
                j+=1

        return nums[len(nums)-j:]