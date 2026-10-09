class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen_numbers = set()

        for number in nums:
            if number in seen_numbers:
                return True
            else:
                seen_numbers.add(number)

        return False