class Solution:
    def f(self,nums,lis,i,ans):
        if i >= len(nums):
            ans.append(lis[:])
            return 
        
        lis.append(nums[i])
        self.f(nums,lis,i+1,ans)
        lis.pop()
        self.f(nums,lis,i+1,ans)
        
        return ans


    def subsets(self, nums: List[int]) -> List[List[int]]:
        lis = []
        return self.f(nums,lis,0,[])
