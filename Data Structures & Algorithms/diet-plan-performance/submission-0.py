class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0

        count = 0
        left = 0
        for right in range(len(calories)):
            count += calories[right]

            if right - left + 1 == k:
                if count > upper: score += 1
                if count < lower: score -= 1

                count -= calories[left]
                left += 1

        return score
