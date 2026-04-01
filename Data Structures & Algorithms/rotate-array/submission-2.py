class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        j = k % length
        if j == 0:
            return

        left = 0

        while left < len(nums):
            place = left + j - len(nums) if left + j >= len(nums) else left + j


            if isinstance(nums[left], tuple):
                plc_num, new = nums[left]
                nums[left] = new
            else:
                plc_num = nums[left]

            if place < j:
                nums[place] = plc_num
            else:
                temp = nums[place]
                nums[place] = (temp, plc_num)

            left += 1
        



