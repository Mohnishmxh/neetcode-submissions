class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            max_len = 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
            
            memo[(r, c)] = max_len
            return max_len
        
        return max(dfs(r, c) for r in range(rows) for c in range(cols))