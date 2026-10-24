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

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        lis = []
        self.f(root,lis)

        ans = 0
        for i in range(len(lis)):
            if low <= lis[i] <= high :
                ans+=lis[i]

        return ans