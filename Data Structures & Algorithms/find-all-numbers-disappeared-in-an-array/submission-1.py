class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        should = set(range(1, len(nums) + 1))

        for num in nums:
            if num in should:
                should.remove(num)

        return list(should)