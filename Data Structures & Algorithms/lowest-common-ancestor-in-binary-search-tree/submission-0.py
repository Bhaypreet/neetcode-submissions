# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,p,q):
        if root is None:
            return None
        if root == p or root == q :
            return root
        
        left = self.f(root.left,p,q)
        right = self.f(root.right,p,q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        else:
            return None
        


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.f(root,p,q)