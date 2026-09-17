import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Max-heap stores entries as (-dist_sq, x, y)
        max_heap = []
        
        for x, y in points:
            dist_sq = x * x + y * y
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist_sq, x, y))
            elif dist_sq < -max_heap[0][0]:
                heapq.heapreplace(max_heap, (-dist_sq, x, y))
                
        return [[x, y] for _, x, y in max_heap]