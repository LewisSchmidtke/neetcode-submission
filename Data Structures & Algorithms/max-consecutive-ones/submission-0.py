class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_one_count = 0
        max_one_count = 0

        for num in nums:
            if num == 1:
                curr_one_count += 1
            else:
                max_one_count = max(max_one_count, curr_one_count)
                curr_one_count = 0
        
        max_one_count = max(max_one_count, curr_one_count)
        return max_one_count
        