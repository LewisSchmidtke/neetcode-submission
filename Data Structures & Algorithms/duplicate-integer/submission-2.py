class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = Counter(nums)
        
        if not freq_map:
            return False

        return True if max(freq_map.values()) > 1 else False