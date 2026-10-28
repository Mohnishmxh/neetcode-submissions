class Solution:
    def canAttendMeetings(self, intervals): 
        intervals.sort(key = lambda i : i.start)
        
        for i in range(1, len(intervals)): 
            i1 = intervals[i - 1] 
            i2 = intervals[i] 
            if i2.start < i1.end: 
                return False
        return True