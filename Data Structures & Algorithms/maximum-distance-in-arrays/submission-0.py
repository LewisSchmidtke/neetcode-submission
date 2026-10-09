class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        low = 100000
        high = 0
        max_dist = 0

        for arr in arrays:
            low = min(arr[0], low)
            high = max(arr[-1], high)
            max_dist = max(abs(low - high), max_dist)

        return max_dist