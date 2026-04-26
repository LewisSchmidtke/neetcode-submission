class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.grid = board
        self.word = word

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == word[0]:
                    found = self._dfs(row, col, set(), 0)
                    if found:
                        return True
        
        return False

    def _dfs(self, r, c, visited, i):
        if i == len(self.word):
            return True

        if min(r,c) < 0 or r >= self.ROWS or c >= self.COLS:
            return False

        if (r, c) in visited or self.grid[r][c] != self.word[i]:
            return False

        visited.add((r, c))
        
        res = (
            self._dfs(r + 1, c, visited, i + 1) or 
            self._dfs(r, c + 1, visited, i + 1) or
            self._dfs(r - 1, c, visited, i + 1) or
            self._dfs(r, c - 1, visited, i + 1)
            )
        visited.remove((r,c))

        return res
            
            

                        

                        