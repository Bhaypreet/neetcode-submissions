class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]] = 1

        for key,value in dic.items():
            if value > 1:
                return key