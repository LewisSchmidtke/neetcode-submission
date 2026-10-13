class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        place = k
        left = 0

        while left < len(nums):
            if place >= len(nums):
                place = place - len(nums)

            if isinstance(nums[left], int):
                new = nums[left]
            
            elif isinstance(nums[left], tuple):
                new = nums[left][1]

            keep = nums[place]
            nums[place] = (new, keep)
            
            place += 1
            left += 1

        for i in range(len(nums)):
            if not isinstance(nums[i], tuple):
                continue
            x = nums[i]
            nums[i] = x[0]

        
