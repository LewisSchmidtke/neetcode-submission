import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[:]

        index_min_heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(index_min_heap)

        for _ in range(k):
            num, index = heapq.heappop(index_min_heap)
            new_val = num * multiplier
            res[index] = new_val
            heapq.heappush(index_min_heap, (new_val, index))

        return res