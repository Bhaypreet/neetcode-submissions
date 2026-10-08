# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,depth):
        if root is None:
            return depth
        l = self.f(root.left,depth+1)
        r = self.f(root.right,depth+1)
        return max(l,r)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.f(root,0)