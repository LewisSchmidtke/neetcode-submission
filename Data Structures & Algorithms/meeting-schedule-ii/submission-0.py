"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        sorted_start_values = sorted([i.start for i in intervals])
        sorted_end_values = sorted([i.end for i in intervals])
        
        max_nr_of_rooms = 0
        current_rooms = 0

        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(sorted_start_values):
            if sorted_start_values[start_pointer] < sorted_end_values[end_pointer]:
                start_pointer += 1
                current_rooms += 1
            else:
                end_pointer += 1
                current_rooms -= 1

            max_nr_of_rooms = max(max_nr_of_rooms, current_rooms)

        return max_nr_of_rooms
    

