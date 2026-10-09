class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        res = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            # Coins needed for number of rows to try and build
            coins = (mid * (mid + 1)) // 2
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                res = max(res, mid)

        return res
