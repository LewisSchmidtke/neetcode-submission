from collections import Counter

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = nums

        self.counter = Counter(nums)

        self.pointer = 0
        self._move_pointer()

    def _move_pointer(self):
        while self.pointer < len(self.q) and self.counter[self.q[self.pointer]] > 1:
            self.pointer += 1


    def showFirstUnique(self) -> int:
        if self.pointer >= len(self.q):
            return -1

        return self.q[self.pointer]
        

    def add(self, value: int) -> None:
        self.q.append(value)
        self.counter[value] += 1

        if self.pointer < len(self.q) and self.q[self.pointer] == value and self.counter[value] > 1:
            self._move_pointer()


        

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
