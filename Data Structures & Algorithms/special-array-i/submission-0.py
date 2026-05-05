class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for right in range(1, len(nums)):
            right_even = nums[right] % 2 == 0
            left_even = nums[right - 1] % 2 == 0

            if right_even and left_even:
                return False
            if not right_even and not left_even:
                return False

        return True
