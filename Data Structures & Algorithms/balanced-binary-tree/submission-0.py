# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,maxi):
        if root is None:
            return 0
        
        l = 1+self.f(root.left,maxi)
        r = 1+ self.f(root.right,maxi)

        maxi[0] = max(maxi[0],abs(l-r))
        return max(l,r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxi = [0]
        self.f(root,maxi)

        if maxi[0] > 1 :
            return False
        return True