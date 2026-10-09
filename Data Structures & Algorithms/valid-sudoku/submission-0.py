from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue

                if val in rows[row] or val in cols[col] or val in grids[(row // 3, col //3)]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                grids[(row // 3, col // 3)].add(val)

        return True

