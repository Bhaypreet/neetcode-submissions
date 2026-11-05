class Solution:
    def f(self,grid,i,j,vis):
        ans = 1
        rows = [1,0,-1,0,1,1,-1,-1]
        cols = [0,1,0,-1,1,-1,1,-1]
        from collections import deque
        q = deque()
        q.append((i,j,1))
        vis[i][j] = True

        while q:

            r,c,dis = q.popleft()

            if r == len(grid)-1 and c == len(grid[0])-1:
                return dis

            for k in range(8):

                nr = r + rows[k]
                nc = c + cols[k]

                if (nr >= 0 and nr < len(grid) and
                    nc >= 0 and nc < len(grid[0]) and
                    vis[nr][nc] is False and grid[nr][nc] == 0):

                    vis[nr][nc] = True
                    q.append((nr,nc,dis+1))

        return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        vis = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] ==1 :
            return -1
        return self.f(grid,0,0,vis)