class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_values = set()
        for number in nums:
            if number in seen_values:
                return True
            
            seen_values.add(number)
        
        return False