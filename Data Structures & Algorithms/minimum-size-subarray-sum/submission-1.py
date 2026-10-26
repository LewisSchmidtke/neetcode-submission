class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = len(nums)
        solution = False

        l = 0
        total = 0
        
        for r in range(minSize):
            total += nums[r]
            while total >= target and l <= r:
                solution = True
                minSize = min(minSize, (r - l + 1))
                total -= nums[l]
                l += 1

        return minSize if solution else 0

