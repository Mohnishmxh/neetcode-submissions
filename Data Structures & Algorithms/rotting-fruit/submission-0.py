from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Initialize queue with all rotten fruits and count fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # If there are no fresh fruits to begin with, 0 minutes are needed
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Perform BFS level by level (each level = 1 minute)
        while queue and fresh_count > 0:
            minutes += 1
            # Process all currently rotten fruits in this wave
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is a fresh fruit, rot it and add to queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        # Step 3: Check if all fresh fruits were successfully rotted
        return minutes if fresh_count == 0 else -1