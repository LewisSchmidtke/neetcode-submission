class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_map = {}

        for idx, number in enumerate(nums):
            if number in res_map:
                return [res_map[number], idx]
            
            res_map[target - number] = idx
        