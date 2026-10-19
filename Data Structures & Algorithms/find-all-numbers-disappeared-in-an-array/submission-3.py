class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        number_set = set(range(1, len(nums) + 1))
        
        for num in nums:
            if num in number_set:
                number_set.remove(num)

        return list(number_set)