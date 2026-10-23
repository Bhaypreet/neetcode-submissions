class Solution:
    def f(self,grid,i,j,s,color):
        grid[i][j] = color

        from collections import deque
        q = deque()
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        q.append((i,j))
        while(q):
            r,c = q.popleft()
            for i in range(4):
                nr = r+rows[i]
                nc = c+cols[i]

                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == s:
                    q.append((nr,nc))
                    grid[nr][nc] = color

        return grid              

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        s = image[sr][sc]
        if color == s:
            return image

        return self.f(image,sr,sc,s,color)