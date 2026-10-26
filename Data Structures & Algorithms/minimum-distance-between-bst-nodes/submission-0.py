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
        lis.append(root.val)
        self.f(root.right,lis)

        return lis


    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lis = self.f(root,[])
        mini = float('inf')
        for i in range(1,len(lis)):
            mini = min(mini,lis[i]-lis[i-1])

        return mini