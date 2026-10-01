import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Min-heap stores: (max_elevation_so_far, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            t, r, c = heapq.heappop(heap)
            
            # Reached destination: because we use a min-heap,
            # the first time we pop (n - 1, n - 1), t is guaranteed minimal.
            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # Cost to move into the neighbor is the max of
                    # the current path's bottleneck and the neighbor's elevation
                    next_t = max(t, grid[nr][nc])
                    heapq.heappush(heap, (next_t, nr, nc))
                    
        return -1