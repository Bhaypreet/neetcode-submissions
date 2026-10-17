# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,lis):
        if root is None:
            return 

        self.f(root.left,lis)
        lis.append(root.val)
        self.f(root.right,lis)

        return lis

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = self.f(root,[])
        
        return a[k-1]