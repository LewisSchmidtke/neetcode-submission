class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.distinct = set()
        self.grid = grid
        self.ref = None

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] == 1:
                    island_set = set()
                    self.dfs(row, col, (row, col), island_set)

                    if island_set:
                        self.distinct.add(frozenset(island_set))

        return len(self.distinct)


    def dfs(self, r, c, reference, isl_set):
        if min(r, c) < 0 or r == self.ROWS or c == self.COLS:
            return

        if self.grid[r][c] != 1:
            return

        self.grid[r][c] = 2

        rel_h, rel_w = reference[0] - r, reference[1] - c
        isl_set.add((rel_h, rel_w))

        self.dfs(r, c + 1, reference, isl_set)
        self.dfs(r + 1, c, reference, isl_set)
        self.dfs(r, c - 1, reference, isl_set)
        self.dfs(r - 1, c, reference, isl_set)



