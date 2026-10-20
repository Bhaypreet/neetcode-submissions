class Solution:
    def f(self, root, dp):
        if root is None:
            return 0

        if root in dp:
            return dp[root]

        # Take the current house
        take = root.val

        if root.left:
            take += self.f(root.left.left, dp)
            take += self.f(root.left.right, dp)

        if root.right:
            take += self.f(root.right.left, dp)
            take += self.f(root.right.right, dp)

        # Do not take the current house
        nottake = self.f(root.left, dp) + self.f(root.right, dp)

        dp[root] = max(take, nottake)
        return dp[root]

    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        return self.f(root, dp)