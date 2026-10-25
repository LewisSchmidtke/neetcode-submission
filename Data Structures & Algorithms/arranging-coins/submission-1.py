class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        
        max_rows = n - 1
        min_rows = 1

        rows = 0

        while min_rows <= max_rows:
            mid = (min_rows + max_rows) // 2
            coins_needed = int(mid * mid) - int((mid * (mid - 1)) / 2)
            if n == coins_needed:
                return mid
            elif n > coins_needed:
                rows = max(rows, mid)
                min_rows = mid + 1
            else:
                max_rows = mid - 1

        return rows
