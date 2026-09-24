"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Dictionary to map original nodes to their corresponding clones
        visited = {}
        
        def dfs(curr):
            # If the node is already visited, return its clone
            if curr in visited:
                return visited[curr]
            
            # Create a clone for the current node
            clone_node = Node(curr.val)
            visited[curr] = clone_node
            
            # Recursively clone all neighbors and add them to the clone's list
            for neighbor in curr.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
                
            return clone_node
        
        return dfs(node)