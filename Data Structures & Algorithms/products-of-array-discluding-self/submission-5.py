class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        nr_of_zeros = 0

        for number in nums:
            if number == 0:
                nr_of_zeros += 1
            else:
                result *= number
        
        for idx, number in enumerate(nums):
            if number != 0:
                if nr_of_zeros > 0:
                    nums[idx] = 0
                else:
                    nums[idx] = int(result / number)
            else:
                if nr_of_zeros > 1:
                    nums[idx] = 0
                else:
                    nums[idx] = result

        return nums
            
