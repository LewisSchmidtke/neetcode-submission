"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        for index in range(1, len(intervals)):
            does_overlap = intervals[index - 1].end > intervals[index].start
            if does_overlap:
                return False
        
        return True