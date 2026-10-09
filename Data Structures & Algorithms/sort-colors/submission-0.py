class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for num in nums:
            counts[num] += 1

        left = 0
        for k in range(len(counts)):
            for _ in range(counts[k]):
                nums[left] = k
                left += 1
        