class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res # XOR: '^' -->  a ^ a = 0 and a ^ 0 = a
            print(res, num)
        return res