class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = defaultdict(int)

        for num in arr1:
            freq[num] += 1
        
        res = []

        for num in arr2:
            number_list = [num] * freq[num]
            res.extend(number_list)
            freq.pop(num)

        last = []
        sort_num = sorted([k for k, v in freq.items()])
        for n in sort_num:
            last.extend([n] * freq[n])

        res.extend(last)
        return res