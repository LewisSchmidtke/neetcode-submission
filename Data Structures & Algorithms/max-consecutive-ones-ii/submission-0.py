class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        consec_length = 0
        flip_c = 0

        max_consec_length = 0

        while right < len(nums):
            if nums[right] == 1:
                consec_length += 1
                right += 1
                max_consec_length = max(max_consec_length, consec_length)
                continue

            if nums[right] == 0 and flip_c < 1:
                flip_c += 1
                consec_length += 1
                max_consec_length = max(max_consec_length, consec_length)
                right += 1
                continue

            while flip_c >= 1:
                consec_length -= 1
                if nums[left] == 0:
                    flip_c -= 1
                left += 1

        max_consec_length = max(max_consec_length, consec_length)

        return max_consec_length


