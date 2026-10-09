class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_vals = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window_vals.remove(nums[left])
                left += 1
            if nums[right] in window_vals:
                return True

            window_vals.add(nums[right])

        return False



        
        