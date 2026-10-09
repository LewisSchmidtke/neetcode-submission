class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)

        return True if max(freq_map.values()) > 1 else False