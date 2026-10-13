
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        m = len(grid)
        n = len(grid[0])

        q = deque()
        row = [1, 0, -1, 0]
        cols = [0, 1, 0, -1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr = r + row[i]
                nc = c + cols[i]

                if (nr >= 0 and nr < m and
                    nc >= 0 and nc < n and
                    grid[nr][nc] == 2147483647):

                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
