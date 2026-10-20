# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self,root,target):
        if root is None:
            return None

        root.left = self.f(root.left,target)
        root.right = self.f(root.right,target)

        if root.left is None and root.right is None:
            if root.val == target:
                return None
  

        

        return root 

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.f(root,target)