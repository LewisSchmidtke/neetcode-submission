class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        DESCENDING = "descending"
        ASCENDING = "ascending"

        prior = None
        state = None

        for num in nums:
            if prior is None:
                prior = num
                continue

            if num > prior:
                if state is not None and state != ASCENDING:
                    return False
                state = ASCENDING
            elif num < prior:
                if state is not None and state != DESCENDING:
                    return False
                state = DESCENDING

            prior = num
        
        return True

            