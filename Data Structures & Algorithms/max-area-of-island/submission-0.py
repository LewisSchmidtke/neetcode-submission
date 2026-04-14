class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        self.grid = grid

        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 1:
                    area = self.traverse(r, c)
                    self.max_area = max(self.max_area, area)
        
        return self.max_area

    def traverse(self, r, c):
        if min(r, c) < 0 or r == len(self.grid) or c == len(self.grid[0]):
            return 0
        
        if self.grid[r][c] != 1:
            return 0

        area = 1
        self.grid[r][c] = 2 # Mark as visited

        area += self.traverse(r - 1, c)
        area += self.traverse(r, c + 1)
        area += self.traverse(r + 1, c)
        area += self.traverse(r, c - 1)

        return area