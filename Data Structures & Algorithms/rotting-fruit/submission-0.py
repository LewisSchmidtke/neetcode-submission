class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotting_fruit = None
        nr_of_fruits = 0
        time_length = 0

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    nr_of_fruits += 1
                if grid[r][c] == 2:
                    rotting_fruit = (r, c)

        q = deque()

        if rotting_fruit is not None:
            q.append(rotting_fruit)

        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == 1:
                    nr_of_fruits -= 1

                grid[r][c] = 2 # Convert current fruit to rotting fruit

                if nr_of_fruits == 0:
                    return time_length

                for inc_r, inc_c in DIRECTIONS:
                    new_r, new_c = r + inc_r, c + inc_c
                    
                    if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS:
                        continue

                    if grid[new_r][new_c] != 1:
                        continue

                    q.append((new_r, new_c))
            time_length += 1

        return -1





