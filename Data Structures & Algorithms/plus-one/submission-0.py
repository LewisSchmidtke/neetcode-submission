class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        length = len(digits)
        right = length - 1

        while right >= 0 and digits[right] == 9:
            digits[right] = 0
            right -= 1

        if right >= 0:
            digits[right] += 1
            return digits
        else:
            new_digits = [0] * length
            new_digits[0] = 1
            new_digits[1: length + 1] = digits
            return new_digits
