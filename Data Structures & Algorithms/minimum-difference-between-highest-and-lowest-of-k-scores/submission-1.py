class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        minDiff = 100001
        left = 0
        for right in range(len(nums)):
            if right - left + 1 < k:
                continue
            
            minDiff = min(minDiff, (nums[right] - nums[left]))
            left += 1
        
        return minDiff
            