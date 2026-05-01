class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        decreasing = 1
        increasing = 1

        res = 0
        
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                increasing += 1
                res = max(res, decreasing)
                decreasing = 1
            
            elif nums[r] < nums[r - 1]:
                decreasing += 1
                res = max(res, increasing)
                increasing = 1
            
            else:
                res = max(res, increasing, decreasing)
                increasing = decreasing = 1

        res = max(res, increasing, decreasing)
        return res

