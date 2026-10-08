class Solution:
    def bfs(self,grid,i,j,vis):
        vis[i][j] = True
        from collections import deque
        q = deque()
        q.append((i,j))
        rows = [0,1,0,-1]
        cols = [1,0,-1,0]


        while(q):
            r,c = q.popleft()
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]
                
                if nr >=0 and nr <len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == "1" and vis[nr][nc] is False:
                    q.append((nr,nc))
                    vis[nr][nc] = True
        return 



    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        vis = [[False for _ in range(c)] for _ in range(r)]
        n = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    if vis[i][j] is False:
                        self.bfs(grid,i,j,vis)
                        n+=1

        return n
