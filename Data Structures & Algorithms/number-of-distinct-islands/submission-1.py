class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.distinct = set()
        self.grid = grid
        self.count = 0

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] == 1:
                    island_set = set()
                    self.dfs(row, col, island_set, (row, col))
                    self.distinct.add(frozenset(island_set))
                    self.count += 1
        return len(self.distinct)


    def dfs(self, r, c, isl_set, reference):
        if min(r, c) < 0 or r == self.ROWS or c == self.COLS:
            return

        if self.grid[r][c] != 1:
            return

        self.grid[r][c] = 2
        rel_h, rel_w = reference[0] - r, reference[1] - c
        isl_set.add((rel_h, rel_w))

        self.dfs(r, c + 1, isl_set, (r, c))
        self.dfs(r + 1, c, isl_set, (r, c))
        self.dfs(r, c - 1, isl_set, (r, c))
        self.dfs(r - 1, c, isl_set, (r, c))



