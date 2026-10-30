class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            largest = heapq.heappop_max(stones)
            second_largest = heapq.heappop_max(stones)
            if largest == second_largest:
                continue
            
            heapq.heappush_max(stones, largest - second_largest)
        
        return 0 if not stones else stones[0]
