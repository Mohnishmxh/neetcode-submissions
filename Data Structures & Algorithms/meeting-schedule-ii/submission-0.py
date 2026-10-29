"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Sort the intervals by their start times
        intervals.sort(key=lambda x: x.start)
        
        # Initialize a min-heap to track the end times of ongoing meetings
        rooms = []
        
        for interval in intervals:
            # If the room due to free up the earliest is free by the current meeting's start time,
            # we can reuse that room.
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)
            
            # Allocate a room by pushing the current meeting's end time
            heapq.heappush(rooms, interval.end)
            
        # The size of the heap is the maximum number of rooms required concurrently
        return len(rooms)