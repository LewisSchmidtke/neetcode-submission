class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        new_mat = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                new_mat[c][r] = matrix[r][c]

        return new_mat