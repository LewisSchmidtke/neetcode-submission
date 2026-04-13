class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.numbers = nums
        self.result = []
        self.backtrack(index=0, subset=[])
        return self.result
    
    def backtrack(self, index, subset):
        # Define our base case
        if index >= len(self.numbers):
            self.result.append(subset[:])
            return
        
        # Decision 1: add current number
        subset.append(self.numbers[index])
        self.backtrack(index + 1, subset)
        subset.pop()

        # Decision 2: dont add current number
        self.backtrack(index + 1, subset)
