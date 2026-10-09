class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == val:
                counter += 1
            else:
                nums[left] = nums[right]
                left += 1
            right += 1

        return len(nums) - counter

                
