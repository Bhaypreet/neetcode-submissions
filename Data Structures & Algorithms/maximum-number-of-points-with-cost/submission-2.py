class Solution:
    def f(self,grid,i,j,dp):
        if i >= len(grid):
            return 0
        ans = 0
        if dp[i][j] != -1:
            return dp[i][j]

        for k in range(len(grid[0])):
            ans = max(ans,grid[i][j]+self.f(grid,i+1,k,dp)-abs(j-k))
            dp[i][j] = ans
        return dp[i][j]




    def maxPoints(self, points: List[List[int]]) -> int:

        dp = [[-1 for _ in range(len(points[0]))] for _ in range(len(points))]


        maxi = 0
        for i in range(len(points)):
            for j in range(len(points[0])):
                maxi = max(maxi,self.f(points,i,j,dp))

        return maxi