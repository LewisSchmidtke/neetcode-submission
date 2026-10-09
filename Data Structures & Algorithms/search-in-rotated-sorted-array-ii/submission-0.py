class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            mv = nums[mid] #mv: mid value

            if mv == target:
                return True
            
            if target < mv:
                if target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
            else: # target > mv
                if target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False
