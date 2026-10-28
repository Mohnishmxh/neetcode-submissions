class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        
        removed_count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If the current interval starts before the previous one ends, it's an overlap
            if intervals[i][0] < prev_end:
                removed_count += 1
            else:
                # No overlap, update the end time to the current interval's end
                prev_end = intervals[i][1]
                
        return removed_count