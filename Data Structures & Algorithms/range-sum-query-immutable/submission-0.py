class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        sum_val = 0
        self.pref = []
        for num in nums:
            sum_val += num
            self.pref.append(sum_val)

    def sumRange(self, left: int, right: int) -> int:
        if left >= 1:
            val = self.pref[left - 1]
        else:
            val = 0

        return self.pref[right] - val


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)