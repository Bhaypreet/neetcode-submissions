# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,lis):
        from collections import deque
        q = deque()

        q.append(root)

        while(q):
            for i in range(len(q)):
                r = q.popleft()
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            lis.append(r.val)

        return lis



    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.f(root,[])