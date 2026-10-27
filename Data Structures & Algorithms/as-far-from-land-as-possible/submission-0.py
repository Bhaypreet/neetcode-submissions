from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()

        # Add all land cells to the queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))

        # All land or all water
        if len(q) == 0 or len(q) == n * m:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < n and
                        0 <= nc < m and
                        grid[nr][nc] == 0):

                        grid[nr][nc] = 1
                        q.append((nr, nc))

            dist += 1

        return dist