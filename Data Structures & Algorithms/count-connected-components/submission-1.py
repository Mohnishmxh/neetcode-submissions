from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        components = 0
        
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
                
        return components