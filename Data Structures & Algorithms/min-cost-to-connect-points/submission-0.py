class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        
        # min_dist[i] stores the minimum Manhattan distance from node i
        # to any node currently included in the MST.
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        
        visited = [False] * n
        total_cost = 0
        
        for _ in range(n):
            # Step 1: Find the unvisited node with the smallest distance to the MST
            curr = -1
            curr_dist = float('inf')
            for i in range(n):
                if not visited[i] and min_dist[i] < curr_dist:
                    curr_dist = min_dist[i]
                    curr = i
            
            # Step 2: Include this node into the MST
            visited[curr] = True
            total_cost += curr_dist
            curr_x, curr_y = points[curr]
            
            # Step 3: Update the distance to MST for all remaining unvisited nodes
            for nxt in range(n):
                if not visited[nxt]:
                    nxt_x, nxt_y = points[nxt]
                    dist = abs(curr_x - nxt_x) + abs(curr_y - nxt_y)
                    if dist < min_dist[nxt]:
                        min_dist[nxt] = dist
                        
        return total_cost