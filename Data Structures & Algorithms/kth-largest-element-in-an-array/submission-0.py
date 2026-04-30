class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = nums
        heapq.heapify_max(max_heap)
        for _ in range(k - 1):
            heapq.heappop_max(max_heap)

        return heapq.heappop_max(max_heap)