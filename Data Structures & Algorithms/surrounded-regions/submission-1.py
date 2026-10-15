class Solution:
    def f(self,grid,i,j,vis):
        vis[i][j] = True
        from collections import deque
        q = deque()

        q.append((i,j))

        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        while(q):
            r,c = q.popleft()
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]

                if nr >=0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and vis[nr][nc] is False and grid[nr][nc] == "O":
                    q.append((nr,nc))
                    vis[nr][nc] = True
                    


    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        
        vis = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and not vis[i][j] and board[i][j] == "O":
                    self.f(board,i,j,vis)


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and vis[i][j] is False:
                    board[i][j] = "X"
        
