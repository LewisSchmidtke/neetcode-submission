class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lows = []
        highs = []
        max_dist = 0

        for index, arr in enumerate(arrays):
            lows.append((arr[0], index))
            highs.append((arr[-1], index))
        
        lows.sort()
        highs.sort(reverse=True)

        if lows[0][1] != highs[0][1]: # Check if the smalles and largest value come from the same array
            return abs(lows[0][0] - highs[0][0]) 
        
        # If they are from the same array, check largest and second smallest and second largest and smallest distances
        dist_a = abs(highs[0][0] - lows[1][0]) # largest and second smallest
        dist_b = abs(highs[1][0] - lows[0][0]) # second largest and smallest

        return max(dist_a, dist_b)