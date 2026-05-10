class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0

        for num in nums:
            if num != 0:
                total *= num
            else:
                zeros += 1

        if zeros == len(nums):
            return nums

        for index in range(len(nums)):
            if nums[index] == 0:
                if zeros > 1:
                    nums[index] = 0
                else:
                    nums[index] = total
            else:
                if zeros > 0:
                    nums[index] = 0
                else:
                    temp = nums[index]
                    nums[index] = int(total / temp)

        return nums