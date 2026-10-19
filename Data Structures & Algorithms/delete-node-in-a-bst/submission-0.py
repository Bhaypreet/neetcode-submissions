# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self,root):
        while(root.left):
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key :
            if root.left:
                root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            if root.right :
                root.right = self.deleteNode(root.right,key)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            else:
                temp = self.f(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)

        return root