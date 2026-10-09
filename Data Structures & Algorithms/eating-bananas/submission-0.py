class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_ber = right

        while left <= right:
            ber = left + ((right - left) // 2)

            needed_hours = 0
            for pile in piles:
                tracker = pile
                while tracker > 0:
                    tracker -= ber
                    needed_hours += 1
            
            if needed_hours > h:
                left = ber + 1
            else:
                right = ber - 1
                min_ber = min(min_ber, ber)

        return min_ber