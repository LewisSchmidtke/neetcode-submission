class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = [0] * len(nums)


        left = 0
        right = 0
        place = 0

        while right < len(nums):
            right += 2
            left += 1

        mid = left

        if a >=0:
            right = mid - 1
            while right >= 0:
                res[place] = a * nums[right]**2 + nums[right] * b + c
                right -= 1
                place += 1
            left = mid
            while left < len(nums):
                res[place] = a * nums[left]**2 + nums[left] * b + c
                left += 1
                place += 1
                
        else:
            left = 0
            while left < mid:
                res[place] = a * nums[left]**2 + nums[left] * b + c
                left += 1
                place += 1
            right = len(nums) - 1
            while right >= mid:
                res[place] = a * nums[right]**2 + nums[right] * b + c
                right -= 1
                place += 1

        return res

            

