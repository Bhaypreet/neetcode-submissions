# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self,root,ans,target):
        if root is None:
            return False

        ans += root.val

        if root.left is None and root.right is None:
            return ans == target

        left = self.f(root.left,ans,target)
        right = self.f(root.right,ans,target)

        return left or right

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.f(root,0,targetSum)
            