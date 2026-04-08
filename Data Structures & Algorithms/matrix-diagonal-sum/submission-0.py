class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0

        sec_diag = len(mat) - 1

        for j in range(len(mat)):
            total += mat[j][j]
            if j != sec_diag:
                total += mat[sec_diag][j]

            sec_diag -= 1

        return total

        