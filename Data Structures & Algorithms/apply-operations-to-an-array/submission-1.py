class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0

        place = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            
            nums[place] = nums[i]
            if place != i:
                nums[i] = 0
            place += 1

        return nums
            

