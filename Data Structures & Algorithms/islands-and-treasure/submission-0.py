from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647
        
        # Step 1: Add all treasure chests (0) to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        # Step 2: Perform Multi-Source BFS
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if the neighbor is an INF land cell
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))