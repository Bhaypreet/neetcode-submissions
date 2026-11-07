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
        lis.append(root)
        self.f(root.right,lis)




    def recoverTree(self, root: Optional[TreeNode]) -> None:
        lis = []
        l = []
        self.f(root,lis)

        for item in lis:
            l.append(item.val)
        l.sort()

        for i in range(len(lis)):
            lis[i].val = l[i]

        return root
        