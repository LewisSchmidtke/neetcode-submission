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

        low_p = 0
        high_p = 0

        while low_p < len(lows) and high_p < len(highs):
            if lows[low_p][1] != highs[high_p][1]:
                return abs(lows[low_p][0] - highs[high_p][0])
            
            left += 1
            right += 1
        