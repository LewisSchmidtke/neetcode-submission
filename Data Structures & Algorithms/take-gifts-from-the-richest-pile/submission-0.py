import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        for _ in range(k):
            max_gifts = heapq.heappop_max(gifts)
            new_gifts = math.floor(math.sqrt(max_gifts))
            heapq.heappush_max(gifts, new_gifts)

        return sum(gifts)