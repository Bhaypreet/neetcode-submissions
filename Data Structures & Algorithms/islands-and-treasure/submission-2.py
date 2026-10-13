class Solution:
   def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        q = deque()
        m = len(grid)
        n = len(grid[0])


        vis = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 :
                    q.append((i,j))

        
        row = [1,0,-1,0]
        cols = [0,1,0,-1]
        
        while(q):
            r,c = q.popleft()
            for i in range(4):
                nr = r+row[i]
                nc = c+cols[i]

                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and vis[nr][nc] is False and grid[nr][nc] == 2147483647 :
                    q.append((nr,nc))
                    vis[nr][nc] = True
                    grid[nr][nc] = grid[r][c]+1


