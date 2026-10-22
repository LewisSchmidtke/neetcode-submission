class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = [0] * 201
        offset = 100

        for n in nums:
            freq[n + offset] += 1
        
        relevant = [(idx - offset, val) for idx, val in enumerate(freq) if val != 0]
        relevant.sort(key=lambda x: (x[1], -x[0]))
        
        res = []
        for num, count in relevant:
            res.extend([num] * count)

        return res

        
        