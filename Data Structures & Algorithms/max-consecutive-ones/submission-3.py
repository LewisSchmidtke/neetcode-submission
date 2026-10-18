class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0

        right = 0
        count = 0

        while right < len(nums):
            if nums[right] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

            right += 1

        max_count = max(max_count, count)
        return max_count
            