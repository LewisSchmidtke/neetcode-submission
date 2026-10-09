class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_mut = 0
        has_zero = False

        for num in nums:
            if num != 0:
                if total_mut == 0:
                    total_mut = num
                else:
                    total_mut = total_mut * num
            else:
                has_zero = True

        for i in range(len(nums)):
            temp = nums[i]
            if temp == 0:
                nums[i] = total_mut
            else:
                if has_zero:
                    nums[i] = 0
                else:
                    nums[i] = int(total_mut / temp)

        return nums