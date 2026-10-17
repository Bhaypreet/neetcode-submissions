class Solution:
    def bfs(self,grid,i,j,vis,ans):
        vis[i][j] = True
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]
        from collections import deque
        q = deque()
        ans = 0

        q.append((i,j))

        while(q):
            r,c = q.popleft()
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]
                if not( nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1):
                    ans+=1
                elif not vis[nr][nc]:
                    q.append((nr,nc))
                    vis[nr][nc] = True                    

        return ans

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.bfs(grid,i,j,vis,1)