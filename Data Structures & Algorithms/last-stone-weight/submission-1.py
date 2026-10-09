class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq # Only supports min heap so we have to swap values

        stones = [-s for s in stones]

        heapq.heapify(stones)
        while len(stones) > 1:
            max_stone = heapq.heappop(stones)
            second_max_stone = heapq.heappop(stones)

            if second_max_stone > max_stone:
                heapq.heappush(stones, second_max_stone - max_stone)

        if stones:
            return abs(stones[0])

        return 0