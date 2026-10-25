class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            if square > num:
                right = mid - 1
            else:
                left = mid + 1

        return False 