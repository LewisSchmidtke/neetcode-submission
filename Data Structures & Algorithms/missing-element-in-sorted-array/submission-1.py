class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = right - (right - left) // 2
            if (nums[mid] - nums[0]) - mid < k: # All values up until mid complete
                left = mid
            else:
                right = mid - 1

        return nums[0] + left + k