class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        adjusted_k = len(nums) - k % len(nums)
        left = 0
        right = adjusted_k

        while right < len(nums):
            left_val = nums[left]
            nums[left] = nums[right]
            nums[right] = left_val
            left += 1
            right += 1