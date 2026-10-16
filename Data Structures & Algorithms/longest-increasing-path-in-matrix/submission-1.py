from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        in_degree = [[0] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Step 1: Compute in-degrees for each cell
        # An in-degree counts how many neighbors are strictly smaller than the current cell.
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
                        in_degree[r][c] += 1
                        
        # Step 2: Add all cells with 0 in-degree (local minima) to a queue
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if in_degree[r][c] == 0:
                    queue.append((r, c))
                    
        # Step 3: BFS level-by-level (each level represents a step in the increasing path)
        path_len = 0
        while queue:
            path_len += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Move to neighbors that are strictly greater
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        in_degree[nr][nc] -= 1
                        if in_degree[nr][nc] == 0:
                            queue.append((nr, nc))
                            
        return path_len