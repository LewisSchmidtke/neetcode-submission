class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        self.ROWS = len(grid)
        self.COLS = len(grid[0])


        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    visited = self.iterative_traversal(r, c, visited, grid)

        return islands
    
    def iterative_traversal(self, r, c, visited, grid):
        stack = [(r,c)]
        while stack:
            for _ in range(len(stack)):
                rr, cc = stack.pop()

                if min(rr, cc) < 0 or rr == self.ROWS or cc == self.COLS:
                    continue

                if grid[rr][cc] != "1" or (rr, cc) in visited:
                    continue

                visited.add((rr, cc))

                stack.append((rr + 1, cc))
                stack.append((rr, cc + 1))
                stack.append((rr - 1, cc))
                stack.append((rr, cc - 1))
        
        return visited
