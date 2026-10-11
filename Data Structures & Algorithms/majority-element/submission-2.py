class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1 -> Counter object
        # Solution 2 -> Manual count
        # Solution 3 -> sort
        # Solution 4 -> math

        nums = sorted(nums)
        middle = len(nums) // 2
        return nums[middle]
        
