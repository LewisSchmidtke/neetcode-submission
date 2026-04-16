class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nr_of_fruits = 0
        time = 0

        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    nr_of_fruits += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and nr_of_fruits > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for inc_r, inc_c in DIRECTIONS:
                    new_r, new_c = r + inc_r, c + inc_c
                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2 # Convert current fruit to rotting fruit
                        q.append((new_r, new_c))
                        nr_of_fruits -= 1

            time += 1

        return time if nr_of_fruits == 0 else -1





