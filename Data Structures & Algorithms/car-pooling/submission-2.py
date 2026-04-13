class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        print(trips)
        min_end_heap = []
        current_passengers = 0

        for trip in trips:
            passengers, start, end = trip
            current_passengers += passengers

            heapq.heappush(min_end_heap, (end, passengers))

            while min_end_heap:
                ending, occupants = heapq.heappop(min_end_heap)
                if ending <= start:
                    current_passengers -= occupants
                else:
                    heapq.heappush(min_end_heap, (ending, occupants))
                    break

            if current_passengers > capacity:
                return False

        return True
