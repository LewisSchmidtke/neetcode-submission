class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = k - 1

        min_delta = 100000

        while right < len(nums):
            min_delta = min(min_delta, nums[right] - nums[left])

            right += 1
            left += 1
        
        return min_delta
