class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]] = 1

        lis = []
        for key,value in dic.items():
            if value > n/3 :
                lis.append(key)
            
        return lis