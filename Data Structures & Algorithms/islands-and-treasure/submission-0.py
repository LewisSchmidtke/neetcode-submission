class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = deque()
        distance = 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))

        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for inc_r, inc_c in DIRECTIONS:
                    new_r, new_c = r + inc_r, c + inc_c
                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 2147483647:
                        grid[new_r][new_c] = distance
                        queue.append((new_r, new_c))

            distance += 1



