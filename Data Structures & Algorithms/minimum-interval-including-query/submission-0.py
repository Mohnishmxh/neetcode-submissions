class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        
        # Sort intervals by start point
        intervals.sort()
        
        # Sort queries while keeping original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        # Min-heap: (interval_length, right_endpoint)
        heap = []
        result = [0] * len(queries)
        i = 0
        n = len(intervals)
        
        for original_idx, query in sorted_queries:
            # Add all intervals that start at or before this query point
            while i < n and intervals[i][0] <= query:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1
            
            # Remove intervals that end before this query point
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            # Result is the length of the shortest valid interval
            result[original_idx] = heap[0][0] if heap else -1
        
        return result