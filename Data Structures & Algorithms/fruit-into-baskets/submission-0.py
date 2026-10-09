class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0

        from collections import defaultdict
        counts = defaultdict(int)

        for fruit in fruits:
            counts[fruit] += 1

        res = sorted(list(counts.items()), key=lambda x: x[1])
        
        try:
            return res[-1][1] + res[-2][1]
        except KeyError:
            return res[-1][1]