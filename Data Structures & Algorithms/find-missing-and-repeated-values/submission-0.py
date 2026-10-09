class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        sol = [0, 0] # Repeating | Missing
        bounds = len(grid)
        n = bounds ** 2
        seen = set()
        running_sum = 0
        ref_sum = int((n * (n + 1)) / 2) # (n * (n + 1)) / 2

        for row in range(bounds):
            for col in range(bounds):
                if grid[row][col] in seen:
                    sol[0] = grid[row][col]
                else:
                    seen.add(grid[row][col])
                    running_sum += grid[row][col]

        sol[1] = ref_sum - running_sum


        return sol
        