class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity
        self.count = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # print(self.array, self.count, n, self.capacity)
        if self.count >= self.capacity:
            self.resize()
        # print(self.array, self.count, n, self.capacity)
        self.array[self.count] = n
        print('Pushback', self.array)
        self.count += 1

    def popback(self) -> int:
        self.count -= 1
        pop = self.array[self.count]
        self.array[self.count] = None
        return pop
        

    def resize(self) -> None:
        self.capacity *= 2
        addition = [None] * self.capacity
        temp = self.array
        self.array = addition
        self.array[:self.count] = temp

    def getSize(self) -> int:
        return self.count
        
    
    def getCapacity(self) -> int:
        return self.capacity
