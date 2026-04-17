class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        trapped_landmass = 0
        visited = set()

        for r in range(1, self.ROWS - 1): # Exclude outer loop
            for c in range(1, self.COLS - 1):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area, valid = self.dfs(r, c, visited, True, grid, 0)
                    print(area, valid)
                    trapped_landmass += area

        return trapped_landmass

    def dfs(self, row, col, visited, valid, grid, area):
        if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
            return 0, False

        if grid[row][col] == 1 and (min(row,col) == 0 or row == self.ROWS - 1 or col == self.COLS - 1):
            return 0, False

        if (row, col) in visited or grid[row][col] == 0:
            return area, True

        visited.add((row, col))

        area, val = self.dfs(row, col + 1, visited, valid, grid, area)
        valid = val and valid
        area, val = self.dfs(row + 1, col, visited, valid, grid, area)
        valid = val and valid
        area, val = self.dfs(row, col - 1, visited, valid, grid, area)
        valid = val and valid
        area, val = self.dfs(row - 1, col, visited, valid, grid,area)
        valid = val and valid

        return (area + 1, valid) if valid else (0, False)