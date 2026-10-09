class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_map = {}

        for index, num in enumerate(nums):
            if target - num in value_map:
                return [value_map[target - num], index]
            else:
                value_map[num] = index