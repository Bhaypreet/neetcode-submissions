class Solution:
    def f(self,nums,lis,ans,i):
        if i >= len(nums):
            a = lis[:]
            a.sort()
            if a not in ans:
                ans.append(a.copy())
            return
        
        lis.append(nums[i])
        self.f(nums,lis,ans,i+1)
        lis.pop()
        self.f(nums,lis,ans,i+1)

        return ans

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.f(nums,[],[],0)