class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        has_zero = False

        for num in nums:
            if num != 0:
                total *= num
            else:
                has_zero = True

        for index in range(len(nums)):
            if nums[index] == 0:
                nums[index] = total
            else:
                if has_zero:
                    nums[index] = 0
                else:
                    temp = nums[index]
                    nums[index] = int(total / temp)

        return nums