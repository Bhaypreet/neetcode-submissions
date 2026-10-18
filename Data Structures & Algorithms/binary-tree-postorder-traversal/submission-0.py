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
        self.f(root.right,lis)

        lis.append(root.val)
        
        return lis


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.f(root,[])