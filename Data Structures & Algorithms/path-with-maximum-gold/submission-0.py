class Solution:
    def f(self,grid,i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 :
            return 0

        gold= grid[i][j] 
        grid[i][j] = 0
        
        best = 0
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        for k in range(4):
            r = i+rows[k]
            c = j+cols[k]
            best = max(best,self.f(grid,r,c))

        grid[i][j] = gold
        return best+gold
        
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    maxi = max(maxi, self.f(grid, i, j))

        return maxi