class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.distinct = set()
        self.grid = grid
        self.count = 0

        for row in range(self.ROWS):
            for col in range(self.ROWS):
                if self.grid[row][col] == 1:
                    island_set = set()
                    self.dfs(row, col, island_set, (row, col))
                    print(row, col)
                    self.distinct.add(frozenset(island_set))
                    self.count += 1

        return len(self.distinct)


    def dfs(self, row, col, isl_set, reference):
        if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
            return

        if self.grid[row][col] != 1:
            return

        self.grid[row][col] = 2
        rel_h, rel_w = reference[0] - row, reference[1] - col
        print(rel_h, rel_w, isl_set)
        isl_set.add((rel_h, rel_w))

        self.dfs(row, col + 1, isl_set, (row, col))
        self.dfs(row + 1, col, isl_set, (row, col))
        self.dfs(row, col - 1, isl_set, (row, col))
        self.dfs(row - 1, col, isl_set, (row, col))