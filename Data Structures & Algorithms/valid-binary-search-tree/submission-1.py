# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,a,b):
        if root is None:
            return True
        if a < root.val < b :
            left = self.f(root.left,a,root.val)
            right = self.f(root.right,root.val,b)

            return left and right
        else:
            return False   
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.f(root,float("-inf"),float("inf"))