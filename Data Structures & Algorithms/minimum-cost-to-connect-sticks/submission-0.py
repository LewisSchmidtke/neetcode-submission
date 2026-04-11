import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            smallest = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            stick_cost = smallest + second
            cost += stick_cost
            heapq.heappush(sticks, stick_cost)

        return cost