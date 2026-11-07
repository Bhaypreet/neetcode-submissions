class Solution:
    def f(self,grid,i,j,dp):
        if i == len(grid) :
            return 0

        if dp[i][j] != -10001:
            return dp[i][j]

        p1,p3 = 10001,10001
        if j-1 >=0:
            p1 = grid[i][j] + self.f(grid,i+1,j-1,dp)
        p2 = grid[i][j]+self.f(grid,i+1,j,dp)
        if j+1 < len(grid[0]):
            p3 = grid[i][j] + self.f(grid,i+1,j+1,dp)
        
        dp[i][j] = min(p1,p2,p3)

        return dp[i][j]


    def minFallingPathSum(self, matrix: List[List[int]]) -> int:


        dp = [[-10001 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        mini = float('inf')
        for i in range(len(matrix[0])):
            mini = min(mini,self.f(matrix,0,i,dp))
        return mini