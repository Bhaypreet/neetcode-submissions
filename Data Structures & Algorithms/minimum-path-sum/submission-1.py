class Solution:
    def f(self,grid,i,j,dp):
        if i == len(grid)-1 and j == len(grid[0])-1:
            return grid[i][j]
        if i >= len(grid) or j >= len(grid[0]):
            return float('inf')
        
        if dp[i][j] != -1:
            return dp[i][j]

        right = grid[i][j]+self.f(grid,i,j+1,dp)
        down = grid[i][j]+self.f(grid,i+1,j,dp)
        dp[i][j] = min(right,down)

        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:

        dp = [[-1 for _ in range(len(grid[0]))]for _ in range(len(grid))]

        return self.f(grid,0,0,dp)