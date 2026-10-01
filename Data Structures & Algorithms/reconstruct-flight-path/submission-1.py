from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Step 1: Group tickets by source in O(E)
        adj_raw = defaultdict(list)
        for u, v in tickets:
            adj_raw[u].append(v)

        # Step 2: Bucket sort each adjacency list in O(len(list) + 26^3)
        # Or convert airport codes to 0..17575 integers.
        # Since tickets <= 300 in typical constraints, Radix Sort gives strictly O(E).
        graph = {}
        for src, dests in adj_raw.items():
            # Counting/bucket sort on 3-letter strings: O(k) where k = len(dests)
            # Sorting in descending order for O(1) pop from the end
            counts = defaultdict(int)
            for d in dests:
                counts[d] += 1
            
            sorted_dests = []
            # Iterate through all unique destinations in descending lexical order
            for d in sorted(counts.keys(), reverse=True):
                sorted_dests.extend([d] * counts[d])
            graph[src] = sorted_dests

        # Step 3: Hierholzer's DFS traversal in O(E)
        itinerary = []
        stack = ["JFK"]
        
        while stack:
            curr = stack[-1]
            if curr in graph and graph[curr]:
                stack.append(graph[curr].pop())
            else:
                itinerary.append(stack.pop())

        return itinerary[::-1]