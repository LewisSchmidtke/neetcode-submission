class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        dim = len(matrix)
        size = dim - 1

        for row in range(dim):
            for col in range(dim):
                entry = matrix[row][col]
                if isinstance(entry, tuple):
                    entry = entry[1]

                new_row, new_col = col, size - row
                target_entry = matrix[new_row][new_col]
                matrix[new_row][new_col] = (entry, target_entry)
                
        for row in range(dim):
            for col in range(dim):
                tup = matrix[row][col]
                matrix[row][col] = tup[0]
        


