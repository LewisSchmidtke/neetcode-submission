class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        for _, values in freq_map.items():
            if values % 2 != 0:
                return False

        return True


