class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        frequency_tuple_list = [(count, num) for num, count in freq.items()]
        heapq.heapify_max(frequency_tuple_list)

        res = []
        for _ in range(k):
            res.append(heapq.heappop_max(frequency_tuple_list)[1])
        
        return res
