import heapq # Only supports min heap so we have to swap values
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while len(stones) > 1:
            max_s = heapq.heappop_max(stones)
            second_max_s = heapq.heappop_max(stones)
            if max_s - second_max_s > 0:
                heapq.heappush_max(stones, max_s - second_max_s)
        
        return stones[0] if stones else 0

        