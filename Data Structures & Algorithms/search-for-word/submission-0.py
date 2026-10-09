class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        DIRECTIONS = [(1,0), (0,1), (-1, 0), (0, -1)]
        start_letter = word[0]

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == start_letter:
                    visited = set()
                    queue = deque()
                    queue.append((row, col))
                    index = 0
                    while queue:
                        r, c = queue.popleft()

                        if board[r][c] != word[index]:
                            continue
                        visited.add((r,c))

                        if index == len(word) - 1:
                            return True
                        
                        for dirs in DIRECTIONS:
                            new_r = r + dirs[0]
                            new_c = c + dirs[1]

                            if (new_r, new_c) in visited:
                                continue
                            if min(new_r, new_c) < 0 or new_r >= ROWS or new_c >= COLS:
                                continue

                            queue.append((new_r, new_c))
                        index += 1

        return False

                        

                        