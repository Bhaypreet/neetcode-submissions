# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,i,lis):
        if root is None:
            return 
        
        if root.right:
            if i+1 > len(lis):
                lis.append(root.right.val)
            self.f(root.right,i+1,lis)
        if root.left:
            if i+1 > len(lis):
                lis.append(root.left.val)
            self.f(root.left,i+1,lis)

        return lis
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        a = self.f(root,0,[])
        a = a[::-1]
        a.append(root.val)
        a = a[::-1]
        return a