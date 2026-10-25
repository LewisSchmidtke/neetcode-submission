class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        res = 0 

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x:
                return mid
            if square > x:
                high = mid - 1
            else:
                res = max(res, mid)
                low = mid + 1
        
        return res