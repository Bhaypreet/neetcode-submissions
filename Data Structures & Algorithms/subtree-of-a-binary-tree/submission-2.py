class Solution:
    def f(self, root, subroot):
        if root is None and subroot is None:
            return True

        if root is None or subroot is None:
            return False

        if root.val != subroot.val:
            return False

        return (self.f(root.left, subroot.left) and
                self.f(root.right, subroot.right))
    def findroot(self, root, subroot):
        if root is None:
            return False

        if root.val == subroot.val:
            if self.f(root, subroot):
                return True

        return (self.findroot(root.left, subroot) or
                self.findroot(root.right, subroot))

    

    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        return self.findroot(root, subRoot)