class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def traverse(row, col):
            if row >= len(triangle):
                return 0
            
            if cache[row][col] != "inf":
                return cache[row][col]
            
            cache[row][col] = triangle[row][col] + min(traverse(row + 1, col), traverse(row + 1, col + 1))

            return cache[row][col]

        cache = [["inf"] * len(triangle[row]) for row in range(len(triangle))]
        return traverse(0, 0)