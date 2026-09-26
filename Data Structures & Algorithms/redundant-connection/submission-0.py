class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        # Since nodes are labeled from 1 to n, size the parent array to n + 1
        parent = list(range(n + 1))
        
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
                return True
            return False  
        
        redundant_edge = []
        for u, v in edges:
            # If u and v already share the same root, adding this edge creates a cycle
            if not union(u, v):
                redundant_edge = [u, v]
                
        return redundant_edge