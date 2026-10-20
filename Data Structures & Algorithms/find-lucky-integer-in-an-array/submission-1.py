class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_map = defaultdict(int)

        for val in arr:
            freq_map[val] += 1


        val_counts = [val for val, count in freq_map.items() if val == count]

        return max(val_counts) if val_counts else -1