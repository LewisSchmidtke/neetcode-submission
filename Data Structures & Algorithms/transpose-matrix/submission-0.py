import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        new_mat = np.zeros((cols, rows), dtype=int)

        for r in range(rows):
            for c in range(cols):
                new_mat[c][r] = matrix[r][c]

        return list(new_mat)