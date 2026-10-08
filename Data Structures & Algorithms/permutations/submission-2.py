class Solution:
    def f(self,nums,ans,lis):
        if len(lis) == len(nums):
            ans.append(lis.copy())
            return
        
        for i in range(len(nums)):
            if nums[i] not in lis:
                lis.append(nums[i])
                self.f(nums,ans,lis)
                lis.pop()
        
        return ans



    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.f(nums,[],[])
        