class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        traverse = 0
        place = 0
        count = 1

        while traverse < len(nums):
            while traverse < len(nums) and nums[place] == nums[traverse]:
                traverse += 1
            place += 1
            if place >= len(nums) or traverse >= len(nums):
                break
            count += 1
            nums[place] = nums[traverse]
        
        return count