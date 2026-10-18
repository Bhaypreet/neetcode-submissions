# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self,root,val):
        
        if val > root.val:
            if root.right:
                self.f(root.right,val)
            else:
                root.right = TreeNode(val)
                return root
        else:
            if root.left:
                self.f(root.left,val)
            else:
                root.left = TreeNode(val)
                return root

        return root






    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return TreeNode(val)

        return self.f(root,val)