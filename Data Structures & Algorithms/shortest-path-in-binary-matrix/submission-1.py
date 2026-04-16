class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

        q = deque()
        visited = set((0, 0))
        if grid[0][0] == 0:
            q.append((0, 0))

        path_length = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS -1:
                    return path_length

                for r_increment, c_increment in DIRECTIONS:
                    new_r, new_c = r + r_increment, c + c_increment

                    if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS:
                        continue

                    if (new_r, new_c) in visited:
                        continue

                    if grid[new_r][new_c] == 1:
                        continue

                    visited.add((new_r, new_c))
                    q.append((new_r, new_c))
            
            path_length += 1

        return -1

