class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_ordered = [(x[1], x[2], x[0]) for x in trips]
        trips_ordered.sort(key=lambda x: x[0])
        
        min_start_heap = trips_ordered
        min_end_heap = []
        current_passengers = 0

        while len(min_start_heap) > 0:
            start, end, passengers = heapq.heappop(min_start_heap)
            current_passengers += passengers

            heapq.heappush(min_end_heap, (end, passengers))

            while len(min_end_heap) > 0:
                ending, occupants = heapq.heappop(min_end_heap)
                if ending <= start:
                    current_passengers -= occupants
                else:
                    heapq.heappush(min_end_heap, (ending, occupants))
                    break
            
            if current_passengers > capacity:
                return False

        return True
