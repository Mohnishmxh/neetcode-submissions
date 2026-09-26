class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # Initialize each node as its own parent
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            # Path compression
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            if root_i != root_j:
                parent[root_i] = root_j
                return 1  # Successfully merged two separate components
            return 0      # Already in the same component
            
        components = n
        for a, b in edges:
            # For every successful union, reduce the component count by 1
            components -= union(a, b)
            
        return components