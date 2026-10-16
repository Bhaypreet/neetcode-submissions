# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,cnt,maxi):
        if root is None:
            return cnt
        if root.val >= maxi :
            cnt+=1

        maxi = max(maxi,root.val)
        cnt = self.f(root.left,cnt,maxi)
        cnt = self.f(root.right,cnt,maxi)

        
        return cnt

    def goodNodes(self, root: TreeNode) -> int:
        return self.f(root,0,float("-inf"))