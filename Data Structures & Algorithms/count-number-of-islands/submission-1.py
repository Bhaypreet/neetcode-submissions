class Solution:
    def dfs(self,grid,i,j,vis):
        vis[i][j] = True
        rows = [0,1,0,-1]
        cols = [1,0,-1,0]

        for k in range(4):
            nr = i+rows[k]
            nc = j+cols[k]
                
            if nr >=0 and nr <len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == "1" and vis[nr][nc] is False:
                self.dfs(grid,nr,nc,vis)
        return 



    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        vis = [[False for _ in range(c)] for _ in range(r)]
        n = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    if vis[i][j] is False:
                        self.dfs(grid,i,j,vis)
                        n+=1

        return n
