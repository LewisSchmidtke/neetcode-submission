class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: 
        ROWS = len(matrix)
        COLS = len(matrix[0])
        replaced = set()

        def replace_row(r):
            for x in range(COLS):
                matrix[r][x] = 0
                replaced.add((r,x))

        def replace_col(c):
            for x in range(ROWS):
                matrix[x][c] = 0
                replaced.add((x,c))

        row = 0
        col = 0

        while row < ROWS and col < COLS:
            print(matrix)
            if matrix[row][col] == 0 and (row,col) not in replaced:
                replace_row(row)
                replace_col(col)
                row += 1
                col = 0
            else:
                col += 1
                if col == COLS - 1:
                    col = 0
                    row += 1        

        