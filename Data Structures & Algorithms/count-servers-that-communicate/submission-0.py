class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        self.count = 0
        row_map = defaultdict(int)
        col_map = defaultdict(int)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row_map[r] += 1
                    col_map[c] += 1
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and max(row_map[r], col_map[c]) > 1:
                    self.count += 1

        return self.count

                
