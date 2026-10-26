class Solution:
    def f(self,grid,i,j,dp):
        if  i>=len(grid)  or j >= len(grid[0]) :
            return 0
        if grid[i][j] == "0":
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        right = self.f(grid,i,j+1,dp)
        down = self.f(grid,i+1,j,dp)
        diag = self.f(grid,i+1,j+1,dp)
        dp[i][j] = 1+min(right,down,diag)

        return dp[i][j]


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        maxi =0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    a = self.f(matrix,i,j,dp)
                    maxi = max(maxi,a*a)

        return maxi