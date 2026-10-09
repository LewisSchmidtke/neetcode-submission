class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq # Only supports min heap so we have to swap values

        stones = [-s for s in stones]

        heapq.heapify(stones)
        while len(stones) > 1:
            max_stone = heapq.heappop(stones)
            second_max_stone = heapq.heappop(stones)
            print(max_stone, second_max_stone)

            if abs(max_stone - second_max_stone) > 0:
                heapq.heappush(stones, abs(max_stone - second_max_stone))

        if stones:
            return stones[0]

        return 0