class Solution:
    def f(self,grid,q):
        ans = 1
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        while(q):
            for _ in range(len(q)):
                r,c = q.popleft()
                for i in range(4):
                    nr = r+rows[i]
                    nc = c+cols[i]
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 2147483647 :
                        q.append((nr,nc))
                        grid[nr][nc] = ans
            ans+=1



    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        self.f(grid,q)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 2147483647:
        #             grid[i][j] = 1
        


        