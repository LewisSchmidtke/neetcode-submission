class StringIterator:

    def __init__(self, compressedString: str):
        self.stack = []
        self.raw = compressedString

        right = len(self.raw) - 1

        while right > 0:
            left = right 
            while self.raw[left].isnumeric():
                left -= 1
            count = int(self.raw[left + 1: right + 1])

            right = left

            letter = self.raw[right]
            
            self.stack.append([letter, count])
            right -= 1

    def next(self) -> str:
        if not self.hasNext:
            return " "
        
        letter, count = self.stack.pop()
        count -= 1
        if count > 0:
            self.stack.append([letter, count])
        
        return letter
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
