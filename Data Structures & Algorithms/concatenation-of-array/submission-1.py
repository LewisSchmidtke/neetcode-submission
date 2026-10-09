class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # result: length 2 * n with n length of nums
        n = len(nums)
        result_array = [0] * (2 * n)
        for idx, value in enumerate(nums):
            result_array[idx] = value
            result_array[idx + n] = value
        return result_array