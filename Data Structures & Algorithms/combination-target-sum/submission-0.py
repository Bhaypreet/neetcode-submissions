class Solution:
    def f(self,nums,target,ans,lis,i):
        if i >= len(nums) or sum(lis) > target:
            return
        if sum(lis) == target :
            ans.append(lis.copy())
            return
        
        lis.append(nums[i])
        self.f(nums,target,ans,lis,i)
        lis.pop()
        self.f(nums,target,ans,lis,i+1)

        return ans

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.f(nums,target,[],[],0)