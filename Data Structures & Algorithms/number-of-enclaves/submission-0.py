class Solution:
    def f(self,grid,q):
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        while q:
            r,c = q.popleft()
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                    q.append((nr,nc))
                    grid[nr][nc] = 0

    def numEnclaves(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1) and grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append((i,j))


        self.f(grid,q)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans+=1

        return ans
        