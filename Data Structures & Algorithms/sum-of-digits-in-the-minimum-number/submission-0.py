class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minimum = str(min(nums))
        
        res = 0
        for digit in minimum:
            res += int(digit)
        
        return 1 if res % 2 == 0 else 0

