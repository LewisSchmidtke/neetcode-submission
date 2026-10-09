class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter

        # return [val[0] for val in Counter(nums).most_common(k)]

        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        return [j[0] for j in sorted(counts.items(), key=lambda x: x[1], reverse=True)][:k]
