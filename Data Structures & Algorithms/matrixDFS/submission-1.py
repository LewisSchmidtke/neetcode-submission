class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.HEIGHT = len(grid)
        self.WIDTH = len(grid[0])
        self.count = 0
        self.seen = set()
        self.dfs(0, 0, grid)
        return self.count

    def dfs(self, r, c, grid):
        if min(r, c) < 0 or r >= self.HEIGHT or c >= self.WIDTH:
            return
            
        if grid[r][c] > 0:
            return

        if (r, c) in self.seen:
            return

        if r == self.HEIGHT - 1 and c == self.WIDTH - 1:
            self.count += 1
            return

        self.seen.add((r, c))

        self.dfs(r + 1, c, grid)
        self.dfs(r, c + 1, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r, c - 1, grid)

        self.seen.remove((r, c))