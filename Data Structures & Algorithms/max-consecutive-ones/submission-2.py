class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        curr = 0

        for j in nums:
            if j == 0:
                max1 = max(max1, curr)
                curr = 0
            else:
                curr += 1
                
        max1 = max(max1, curr)
        return max1
