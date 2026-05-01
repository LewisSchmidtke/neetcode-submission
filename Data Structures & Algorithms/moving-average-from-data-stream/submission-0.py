class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = [0] * self.size

        self.total = 0
        self.entries = 0
        self.index = 0

    def next(self, val: int) -> float:
        temp = self.arr[self.index]
        self.arr[self.index] = val
        self.total -= temp
        self.total += val

        self.index += 1
        self.index %= self.size

        if self.entries < self.size:
            self.entries += 1

        return self.total / self.entries
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
