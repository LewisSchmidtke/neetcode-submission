class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort(reverse=True)
        current_number = nums[0]
        count = 1

        for number in nums[1:]:
            if number != current_number:
                if count == 1:
                    return current_number
                current_number = number
                count = 1
            else:
                count += 1

        if count == 1:
            return current_number
            
        return -1
            
            
