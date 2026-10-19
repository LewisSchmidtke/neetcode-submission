class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        store = set(range(1, n**2 + 1))
        duplicate = 0

        for row in grid:
            for val in row:
                if val in store:
                    store.remove(val)
                else:
                    duplicate = val

        return [duplicate, store.pop()]

