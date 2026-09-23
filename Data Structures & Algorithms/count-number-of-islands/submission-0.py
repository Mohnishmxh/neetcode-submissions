class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Check boundaries and if the current cell is water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current cell as visited by turning it into '0'
            grid[r][c] = '0'
            
            # Recursively visit all adjacent directions (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c) # This will sink the entire island
                    
        return island_count