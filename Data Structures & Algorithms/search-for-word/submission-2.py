class Solution:
    def f(self,grid,i,j,idx,word):
        if idx == len(word):
            return True
        
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[idx]:
            return False
        
        ch = grid[i][j] 
        grid[i][j] = "#"

        found = self.f(grid,i+1,j,idx+1,word) or self.f(grid,i,j+1,idx+1,word) or self.f(grid,i,j-1,idx+1,word) or self.f(grid,i-1,j,idx+1,word)

        grid[i][j] = ch
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.f(board,i,j,0,word):
                        return True


        return False