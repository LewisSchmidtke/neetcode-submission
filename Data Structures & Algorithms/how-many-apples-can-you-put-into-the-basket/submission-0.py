class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        basket = 0
        count = 0
        max_weight = 5000

        min_heap = weight
        heapq.heapify(min_heap)

        while min_heap:
            lightest_apple = heapq.heappop(min_heap)
            if basket + lightest_apple > max_weight:
                return count
            basket += lightest_apple
            count += 1
        
        return count
