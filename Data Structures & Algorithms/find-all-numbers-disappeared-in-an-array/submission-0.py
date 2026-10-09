class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        should = set(range(1, len(nums) + 1))

        actual = set()

        for num in nums:
            actual.add(num)

        return list(should - actual)