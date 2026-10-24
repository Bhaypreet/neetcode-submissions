class Solution:
    def f(self,grid,i,j):
        # vis[i][j] = True
        ans = grid[i][j]
        grid[i][j] = 0

        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        from collections import deque
        q = deque()
        q.append((i,j))

        while q :
            r,c = q.popleft()
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] > 0:
                    q.append((nr,nc))
                    ans+=grid[nr][nc]
                    grid[nr][nc] = 0

        return ans


    def findMaxFish(self, grid: List[List[int]]) -> int:

        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    maxi = max(maxi,self.f(grid,i,j))


        return maxi

