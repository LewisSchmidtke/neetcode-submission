class StringIterator:

    def __init__(self, compressedString: str):
        self.stack = []

        right = len(compressedString) - 1

        while right > 0:
            number = compressedString[right]
            right -= 1
            letter = compressedString[right]

            for _ in range(int(number)):
                self.stack.append(letter)
            
            right -= 1

    def next(self) -> str:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
