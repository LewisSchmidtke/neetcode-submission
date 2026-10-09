class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 2:
            return False

        if k >= len(nums):
            k = len(nums)

        left = 0
        right = 1
        while left < len(nums):
            if nums[left] == nums[right]:
                return True

            if right - left < k and right < len(nums):
                right += 1
            else:
                left += 1
        
        return False



        
        