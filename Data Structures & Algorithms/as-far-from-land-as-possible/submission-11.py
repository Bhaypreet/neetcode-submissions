class Solution:
    def f(self,grid,q):
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]
        ans = -1

        while(q):
            for _ in range(len(q)):
                r,c = q.popleft()
                for k in range(4):
                    nr = r+rows[k]
                    nc = c+cols[k]
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 0 :
                        q.append((nr,nc))
                        grid[nr][nc] = 1
            ans+=1

        return ans



    def maxDistance(self, grid: List[List[int]]) -> int:
        land = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                land+=grid[i][j]

        if land == len(grid)*len(grid[0]) or land == 0:
            return -1

        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        from collections import deque
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))
        return self.f(grid,q)