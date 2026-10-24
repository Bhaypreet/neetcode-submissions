class Solution:
    def f(self,nums,l,r):
        if l > r :
            return None

        mid = (l+r)//2
        root = TreeNode(nums[mid])

        root.left = self.f(nums,l,mid-1)
        root.right = self.f(nums,mid+1,r)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
        return self.f(nums,0,len(nums)-1)