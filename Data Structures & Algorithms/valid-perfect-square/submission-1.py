class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num // 2 # For positive integers > 1, the root is always >= num / 2

        while left <= right:
            mid = left + ((right - left) // 2)
            if mid**2 == num:
                return True
            if mid**2 > num:
                right = mid - 1
            else:
                left = mid + 1

        return False