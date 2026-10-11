from collections import deque

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total = len(nums)
        occurrences = 0
        index_queue = deque()

        for idx, number in enumerate(nums):
            if number == val:
                occurrences += 1
                index_queue.append(idx)
                continue
            
            if index_queue:
                nums[index_queue.popleft()] = number
                index_queue.append(idx)
            
        return total - occurrences
        

            