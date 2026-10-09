class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()

        right = len(nums) - 1
        prev = None
        dupe = False

        while right >= 0:
            if prev is not None and nums[right] != prev and dupe is False:
                return prev
            if prev is not None and nums[right] == prev:
                dupe = True
            else:
                dupe = False
            prev = nums[right]
            right -= 1

        return -1