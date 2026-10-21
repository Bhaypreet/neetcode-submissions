
class Solution:
    def f(self, grid, i, j, dp):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        a = b = c = d = 0

        if i + 1 < len(grid) and grid[i+1][j] > grid[i][j]:
            a = self.f(grid, i+1, j, dp)+1

        if j + 1 < len(grid[0]) and grid[i][j+1] > grid[i][j]:
            b = self.f(grid, i, j+1, dp)+1

        if i - 1 >= 0 and grid[i-1][j] > grid[i][j]:
            c = self.f(grid, i-1, j, dp)+1

        if j - 1 >= 0 and grid[i][j-1] > grid[i][j]:
            d = self.f(grid, i, j-1, dp)+1

        dp[i][j] =  max(a, b, c, d)
        return dp[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        maxi = 0

        for i in range(m):
            for j in range(n):
                maxi = max(maxi, self.f(matrix, i, j, dp))

        return maxi+1
