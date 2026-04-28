class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        islands = 0

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] != "1":
                    continue
                
                # call island traversal function
                self.traverse_island(row, col, grid)

                islands += 1
        
        return islands

    def traverse_island(self, r, c, matrix):
        if min(r, c) < 0 or r == self.ROWS or c == self.COLS: # Out of bounds conditions
            return None
        
        if matrix[r][c] != "1": # Wrong value condition
            return None

        matrix[r][c] = "2" # visited state

        self.traverse_island(r + 1, c, matrix) # down
        self.traverse_island(r, c + 1, matrix) # right
        self.traverse_island(r - 1, c, matrix) # up
        self.traverse_island(r, c - 1, matrix) # left


        

