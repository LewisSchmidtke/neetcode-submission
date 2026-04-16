class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # 0's are traversable, 1's are blockades
        # Find shortest path from (0,0) to (len(grid) - 1, len(grid[0]) - 1)

        ROWS = len(grid)
        COLS = len(grid[0])

        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Increments of row and column | right, down, left, up

        q = deque()
        q.append((0, 0))
        visited = set((0, 0))

        path_length = 0 # Keep track of length from start

        while q:
            for _ in range(len(q)):
                curr_r, curr_c = q.popleft()

                if curr_r == ROWS - 1 and curr_c == COLS - 1: # We reached goal
                    return path_length

                for increment_r, increment_c in DIRECTIONS:
                    new_r, new_c = curr_r + increment_r, curr_c + increment_c

                    if min(new_r, new_c) < 0: # Out of lower bounds
                        continue

                    if new_r == ROWS or new_c == COLS: # Out of upper bounds
                        continue

                    if grid[new_r][new_c] == 1: # Rock value, cannot traverse
                        continue

                    if (new_r, new_c) in visited: # Already traversed
                        continue

                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))

            path_length += 1 # New bfs level

        return - 1

                


