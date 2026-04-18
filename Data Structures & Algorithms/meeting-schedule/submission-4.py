"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        if not intervals:
            return True
        prev = intervals[0]

        for vals in intervals[1:]:
            s= vals.start
            e = vals.end
            if s<prev.end:
                return False
            prev.end = e

        return True


