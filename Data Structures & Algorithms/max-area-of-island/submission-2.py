class Solution:
    def f(self,grid,i,j,vis):
        vis[i][j] = True
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]
        ans = 1

        from collections import deque
        q = deque()
        q.append((i,j))
        while q:
            r,c = q.popleft()
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and vis[nr][nc] is False and grid[nr][nc] == 1:
                    q.append((nr,nc))
                    ans += 1
                    vis[nr][nc] = True
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[i][j] is False and grid[i][j] == 1:
                    maxi = max(maxi,self.f(grid,i,j,vis))
        return maxi