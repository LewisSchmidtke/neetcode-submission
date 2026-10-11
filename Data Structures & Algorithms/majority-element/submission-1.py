class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1 -> Counter object
        # Solution 2 -> Manual count
        # Solution 3 -> sort
        # Solution 4 -> math

        # First check first, middle and last element, if middle and first or middle and last are the same we found the element, if not move left and right by half

        nums = sorted(nums)
        middle = len(nums) // 2
        reference = nums[middle]
        left = 0
        right = len(nums) - 1

        for i in range(2):
            if reference == nums[left] or reference == nums[right]:
                return reference
            left = middle // 2
            right = (middle + right) // 2
        
