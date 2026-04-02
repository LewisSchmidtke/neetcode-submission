class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = nums

        self.counter = defaultdict(int)
        self.init_count()

        self.pointer = 0
        self.move_pointer()

    def init_count(self):
        for c in self.q:
            self.counter[c] += 1

    def move_pointer(self):
        while self.pointer < len(self.q) and self.counter[self.q[self.pointer]] > 1:
            self.pointer += 1


    def showFirstUnique(self) -> int:
        if self.pointer >= len(self.q):
            return -1

        return self.q[self.pointer]
        

    def add(self, value: int) -> None:
        self.q.append(value)
        self.counter[value] += 1

        if value == self.showFirstUnique():
            self.move_pointer()


        

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
