"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        # res, count =0,0
        # s,e=0,0

        # while s < len(intervals):

        #     if start[s] < end[e]:
        #         s+=1
        #         count+=1
        #     else:
        #         e+=1
        #         count-=1
        #     res= max(res, count)
        # return res       

        maps =defaultdict(int)
        for i in intervals:
            maps[i.start]+=1
            maps[i.end]-=1

        res, cnt =0,0
        for i in sorted(maps):
            cnt+=maps[i]
            res= max(res, cnt)
        return res
        