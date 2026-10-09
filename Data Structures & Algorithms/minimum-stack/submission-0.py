class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_values = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.stack_values:
            self.stack_values[val] += 1
        else:
            self.stack_values[val] = 1
        
    def pop(self) -> None:
        val = self.stack.pop(-1)
        self.stack_values[val] -= 1
        if self.stack_values[val] == 0:
            del self.stack_values[val]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack_values)
        
