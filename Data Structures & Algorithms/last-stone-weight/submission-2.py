import heapq # Only supports min heap so we have to swap values
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            max_stone = heapq.heappop(stones)
            second_max_stone = heapq.heappop(stones)

            if second_max_stone > max_stone:
                heapq.heappush(stones, max_stone - second_max_stone)

        stones.append(0)
        return abs(stones[0])