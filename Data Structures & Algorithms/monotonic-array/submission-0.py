class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = nums[0] < nums[-1]

        left = 0
        for right in range(1, len(nums)):
            if increasing:
                if nums[left] > nums[right]:
                    return False
            else:
                if nums[left] < nums[right]:
                    return False
            left += 1

        return True