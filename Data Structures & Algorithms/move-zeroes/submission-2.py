class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        trav = 0
        place = 0

        while trav < len(nums):
            while place < len(nums) and nums[place] != 0:
                place += 1
                trav += 1
            
            while trav < len(nums) and nums[trav] == 0:
                trav += 1
            
            if trav >= len(nums) or place >= len(nums):
                break
            
            nums[place] = nums[trav]
            nums[trav] = 0
            trav += 1
            place += 1


        