class Solution:
    def f(self,grid,q,a,fresh):
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        if fresh == 0:
            return 0

        while(q and fresh > 0):
            for i in range(len(q)):
                r,c = q.popleft()
                rotten = False
                for i in range(4):
                    nr = r+rows[i]
                    nc = c+cols[i]
                    if nr >= 0 and nr < len(grid) and nc >=0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh-=1
                
            a+=1
        if fresh == 0:
            return a

        return -1


    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1


        return self.f(grid,q,0,fresh)
        