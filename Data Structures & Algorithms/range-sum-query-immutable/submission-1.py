class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prep = self.prepare_array()

    def sumRange(self, left: int, right: int) -> int:
        print(self.prep)
        top_range = self.prep[right]
        if left - 1 >= 0:
            bottom_range = self.prep[left - 1]
            return top_range - bottom_range
        else:
            return top_range


    def prepare_array(self):
        res = []
        count = 0
        for val in self.nums:
            count += val
            res.append(count)
        
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)