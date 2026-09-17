import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Negate values to simulate a max-heap using Python's min-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # Heaviest stone
            x = -heapq.heappop(max_heap)  # Second heaviest stone

            if y > x:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0