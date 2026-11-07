class Solution:
    def f(self,grid,q):
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        while q:
            r,c = q.popleft()
            for k in range(4):
                nr = r+rows[k]
                nc = c+cols[k]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 0:
                    q.append((nr,nc))
                    grid[nr][nc] = 1
        return grid

    def n(self,grid,vis,q):
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        while q:
            r,c = q.popleft()
            for k in range(4):
                nr = r+rows[k]
                nc = c+cols[k]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 0 and vis[nr][nc] is False:
                    q.append((nr,nc))
                    vis[nr][nc] =True
        


    def closedIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1) and grid[i][j] == 0:
                    grid[i][j] = 1
                    q.append((i,j))
        self.f(grid,q)

        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and vis[i][j] is False:
                    d = deque()
                    d.append((i,j))
                    vis[i][j] = True
                    ans+=1
                    self.n(grid,vis,d)

        return ans












