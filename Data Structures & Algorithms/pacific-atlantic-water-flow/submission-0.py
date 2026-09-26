from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        def bfs(sources):
            reachable = set(sources)
            queue = deque(sources)
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    # Check bounds, whether it's visited, and if water can flow 'uphill' backwards
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reachable:
                        if heights[nr][nc] >= heights[r][c]:
                            reachable.add((nr, nc))
                            queue.append((nr, nc))
            return reachable

        # Define initial border sources
        pacific_sources = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_sources = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        
        # Find all cells reachable from each ocean
        pacific_reachable = bfs(pacific_sources)
        atlantic_reachable = bfs(atlantic_sources)
        
        # Return cells that can reach both oceans
        return [[r, c] for r, c in pacific_reachable.intersection(atlantic_reachable)]