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

        lis.append(root.val)
        self.f(root.left,lis)
        self.f(root.right,lis)
        
        return lis




    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.f(root,[])