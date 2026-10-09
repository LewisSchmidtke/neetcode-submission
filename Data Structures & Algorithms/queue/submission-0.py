class Deque:
    
    def __init__(self):
        self.left = []
        self.right = []
        self.left_point = 0
        self.right_point = 0


    def isEmpty(self) -> bool:
        return not self.left and not self.right
        
    def append(self, value: int) -> None:
        self.right.append(value)
        self.right_point += 1

    def appendleft(self, value: int) -> None:
        self.left.append(value)
        self.left_point += 1

    def pop(self) -> int:
        if self.right:
            return self.right.pop()
        
        if self.left and self.left_point < len(self.left):
            val = self.left[self.left_point]
            self.left_point -= 1
            return val

        return -1

    def popleft(self) -> int:
        if self.left:
            return self.left.pop()
        
        if self.right and self.right_point < len(self.right):
            val = self.right[self.right_point]
            self.right_point -= 1
            return val

        return -1
