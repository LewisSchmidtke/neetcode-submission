class Solution:
    def countOdds(self, low: int, high: int) -> int:

        numbers_in_range = high - low + 1
        total_odd = numbers_in_range // 2

        if high % 2 != 0 and low % 2 != 0:
            return total_odd + 1

        return total_odd