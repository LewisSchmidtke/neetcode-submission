class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS = len(heights)
        self.COLS = len(heights[0])
        self.res = []
        self.grid = heights

        for r in range(self.ROWS):
            for c in range(self.COLS):
                p, a = self.traverse(r, c, set(), heights[r][c])

                if p and a:
                    self.res.append([r, c])

        return self.res

        

    def traverse(self, r, c, visited, height):
        if (r, c) in visited: # Already seen
            return False, False

        pacific = r < 0 or c < 0
        atlantic = r >= self.ROWS or c >= self.COLS

        if min(r, c) < 0 or r >= self.ROWS or c >= self.COLS: # Out of bounds
            return pacific, atlantic

        if self.grid[r][c] > height: # Cant keep flowing
            return False, False

        visited.add((r, c)) # Keep track of current location

        p, a = self.traverse(r + 1, c, visited, height=self.grid[r][c]) # Down
        pacific = pacific or p
        atlantic = atlantic or a

        p, a = self.traverse(r, c + 1, visited, height=self.grid[r][c]) # right
        pacific = pacific or p
        atlantic = atlantic or a

        p, a = self.traverse(r - 1, c, visited, height=self.grid[r][c]) # up
        pacific = pacific or p
        atlantic = atlantic or a

        p, a = self.traverse(r, c - 1, visited, height=self.grid[r][c]) # left
        pacific = pacific or p
        atlantic = atlantic or a
    

        return pacific, atlantic

        
        

