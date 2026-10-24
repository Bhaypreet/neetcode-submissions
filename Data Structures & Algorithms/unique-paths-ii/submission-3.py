class Solution:
    def f(self,grid,i,j,dp):
        if i == len(grid)-1 and j == len(grid[0])-1 :
            return 1
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 :
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        right = 0
        down = 0
        if j < len(grid[0])-1 and grid[i][j+1] == 0:
            right = self.f(grid,i,j+1,dp)

        if i < len(grid)-1 and grid[i+1][j] == 0:
            down = self.f(grid,i+1,j,dp)

        dp[i][j] = right+down

        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        return self.f(obstacleGrid,0,0,dp)