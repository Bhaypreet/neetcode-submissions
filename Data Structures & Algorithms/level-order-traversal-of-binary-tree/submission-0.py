# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def f(self,root,ans):
        from collections import deque
        q = deque()
        q.append(root)


        while(q):
            lis = []
            for i in range(len(q)):
                r = q.popleft()
                lis.append(r.val)
                if r.left:
                    q.append(r.left)
                if r.right :
                    q.append(r.right)    
            ans.append(lis)
        
        return ans        
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        return self.f(root,[])