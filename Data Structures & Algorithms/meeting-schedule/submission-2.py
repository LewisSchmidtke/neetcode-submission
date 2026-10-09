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
            if sorted_intervals[index - 1].end > sorted_intervals[index].start:
                return False
        
        return True