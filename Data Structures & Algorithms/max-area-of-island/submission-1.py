class Solution:
    def bfs(self,grid,vis,i,j,ans):
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]
        sumi = 0
        from collections import deque
        q = deque()
        q.append((i,j))
        vis[i][j] = True

        while(q):
            r,c = q.popleft()
            sumi+=1
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]

                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and vis[nr][nc] is False and grid[nr][nc] == 1:
                    q.append((nr,nc))
                    vis[nr][nc] = True
                    
                    
        return sumi

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and vis[i][j] is False:
                    a = self.bfs(grid,vis,i,j,0)
                    maxi = max(maxi,a)
        return maxi