class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        left = 0
        right = len(nums) - 1

        for num in nums:
            if num % 2 == 0:
                res[left] = num
                left += 1
            else:
                res[right] = num
                right -= 1

        return res

