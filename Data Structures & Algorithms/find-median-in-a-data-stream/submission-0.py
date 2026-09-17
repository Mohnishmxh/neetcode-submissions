import heapq

class MedianFinder:

    def __init__(self):
        # small is a max-heap (invert values to simulate with Python's min-heap)
        self.small = []
        # large is a min-heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap (invert sign for max-heap behavior)
        heapq.heappush(self.small, -num)
        
        # Step 2: Ensure all elements in `small` are <= elements in `large`
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Step 3: Maintain size balance (len(small) == len(large) or len(small) == len(large) + 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0