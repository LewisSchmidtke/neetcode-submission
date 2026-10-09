class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ###################### NON-OPTIMAL SOLUTION ###################
        # runs in O(M log M) and needs O(M) space
        # lows = []
        # highs = []
        # max_dist = 0

        # for index, arr in enumerate(arrays):
        #     lows.append((arr[0], index))
        #     highs.append((arr[-1], index))
        
        # lows.sort()
        # highs.sort(reverse=True)

        # if lows[0][1] != highs[0][1]: # Check if the smalles and largest value come from the same array
        #     return abs(lows[0][0] - highs[0][0]) 
        
        # # If they are from the same array, check largest and second smallest and second largest and smallest distances
        # dist_a = abs(highs[0][0] - lows[1][0]) # largest and second smallest
        # dist_b = abs(highs[1][0] - lows[0][0]) # second largest and smallest

        # return max(dist_a, dist_b)


        ###################### OPTIMAL SOLUTION ###################
        res = 0
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            
            # here we calculate with the cur_min and cur_max to avoid using min and max from same array
            res = max(res, abs(arrays[i][-1] - cur_min), abs(cur_max - arrays[i][0])) 

            # update
            cur_min = min(cur_min, arrays[i][0])
            cur_max = max(cur_max, arrays[i][-1])
            
        return res