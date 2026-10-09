class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0

        max_size = 0
        curr_size = 0
        flips = 0

        while right < len(nums):
            if nums[right] == 0:
                flips += 1

            while flips > k and left <= right:
                removed_val = nums[left]
                if removed_val == 0:
                    flips -= 1

                curr_size -= 1
                left += 1
            
            right += 1
            
            curr_size += 1
            max_size = max(max_size, curr_size)

        return max_size