# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def f(self,root,p,q):
        if root is None:
            return None

        if root == p or root == q:
            return root
        

        a = self.f(root.left,p,q)
        b = self.f(root.right,p,q)

        if a is None and b is None:
            return None

        elif a is None :
            return b
        elif b is None:
            return a
        else:
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.f(root,p,q)