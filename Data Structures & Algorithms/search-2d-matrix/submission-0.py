class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_lower = 0
        row_upper = len(matrix) - 1

        while row_lower <= row_upper:
            row_mid = row_lower + ((row_upper - row_lower) // 2)
            if matrix[row_mid][0] <= target <= matrix[row_mid][-1]:
                left = 0
                right = len(matrix[row_mid]) - 1

                while left <= right:
                    col_mid = left + ((right - left) // 2)
                    if matrix[row_mid][col_mid] < target:
                        left = col_mid + 1
                    elif matrix[row_mid][col_mid] > target:
                        right = col_mid - 1
                    else:
                        return True

                return False
                
            elif matrix[row_mid][0] > target:
                row_upper = row_mid - 1

            elif matrix[row_mid][-1] < target:
                row_lower = row_mid + 1
        return False
